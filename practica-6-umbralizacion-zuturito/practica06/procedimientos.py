import numpy as np
from auxiliar import ventana_rodante
import math
from functools import partial
from collections import Counter

#recicle de código
def histograma_norm(imagen):
    M = imagen.shape[0]
    N = imagen.shape[1]
    result = []
    for n in range(0, 256):
        cantidad = np.sum(imagen == n)
        probabilidad = cantidad / (M * N)
        result.append(probabilidad)
    return result

def convolucion(imagen, kernel, return_type="float32"):
    imagen_conv = np.zeros(np.shape(imagen))
    n = kernel.shape[0]
    ventana = ventana_rodante(imagen, n)
    x = 0
    i = 0
    for fila in imagen:
        y = 0
        for intensidad in fila:
            s = 0 
            arr = np.reshape(ventana[i], kernel.shape)
            g = arr * kernel 
            i += 1
            if return_type == "uint8":
                imagen_conv[x, y] = round(g.sum())
            else:
                imagen_conv[x, y] = g.sum()
            y += 1
        x += 1
    return imagen_conv.astype(return_type)

def kernel_gaussiano(n, K, sigma):
    assert n % 2 == 1
    valor = int((n-1)/2)
    result = np.ones((n, n))
    for x in range(n):
        for y in range(n):
            diferencia = np.sqrt((x - valor) ** 2 + (y - valor) ** 2)
            result[x, y] = np.exp(-(diferencia**2)/(2 * sigma **2))
    return result.astype("float32")

def gradiente_sobel(imagen):
    gx = np.array(([-1, -2, -1],[0, 0, 0],[1, 2, 1]),dtype="float64")
    gy = np.array(([-1, 0, 1],[-2, 0, 2],[-1, 0, 1]),dtype="float64")
    Imagen1 = convolucion(imagen,gx, "float64")
    Imagen2 = convolucion(imagen,gy, "float64")
    result = np.sqrt(np.square(Imagen1) + np.square(Imagen2))
    return result.astype("float32")
#-----------------------------------------------------------------------
def umbralizacion_global(img, umbral):
    # Ojo: umbral puede estar fuera del rango [0, 255], para
    # poder umbralizar imagenes gradiente, etc
    result = np.zeros(img.shape)
    x = 0
    for fila in img:
        y = 0
        for intensidad in fila:
            if(intensidad > umbral):
            	valor = 1
            else:
            	valor = 0
            result[x, y] = valor
            y += 1
        x += 1
    return result.astype("uint8")

def promedio(valores):
	sumatoria=0
	for valor in valores:
		sumatoria+=valor
	cantidadValores = len(valores)
	return sumatoria/float(cantidadValores)

def metodo_otsu(imagen):
	#hist_normalizado
    his = histograma_norm(imagen)
    #plk
    pixel_number = imagen.shape[0] * imagen.shape[1]
    mean_weigth = 1.0/pixel_number
    bins = np.arange(0,257)
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]:
    	#probabilidad y promedio acumulado
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weigth
        Wf = pcf * mean_weigth
        #varianza gloabl
        mub = np.sum(intensity_arr[:t]*his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*his[t:]) / float(pcf)
        #mg
        value = Wb * Wf * (mub - muf) ** 2
        if value is None:
        	value = 0
        else:
        	value = value
        #ajustando a 0-255
        if value > final_value:
            final_thresh = t - 1
            final_value = value
    threshold = final_thresh
    eta = threshold / final_value
    return threshold, eta

def mascara_de_umbralizacion_gradiente(imagen, percentil):
    assert 0 <= percentil <= 100
    ImagenSobel = gradiente_sobel(imagen)
    T = np.percentile(ImagenSobel, percentil)
    result = umbralizacion_global(ImagenSobel,T)
    return result.astype("uint8")

def umbralizacion_adaptiva(imagen, n, sigma, C):
    assert n % 2 == 1
    w = kernel_gaussiano(n, 1, sigma)
    w_norm = w/w.sum()
    #convolucion
    convo = convolucion(imagen,w_norm,"float64")
    result = np.zeros(imagen.shape)
    x = 0
    for fila in imagen:
        y = 0
        for intensidad in fila:
        	convoVal = convo[x][y] - C
        	if(int(intensidad) > int(convoVal)):
        		valor = 1.0
        	else:
        		valor = 0.0
        	result[x, y] = valor
        	y += 1
        x += 1
    return result.astype("uint8")