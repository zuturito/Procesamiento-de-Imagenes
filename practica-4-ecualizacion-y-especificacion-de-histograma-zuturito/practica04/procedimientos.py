import math
import numpy as np

def histograma_norm(imagen):
    # TODO: implementar histograma normalizado
    # Debe regresar arreglo resultado = [...] de 256
    # posiciones, con valores de 0 a 1 en cada posicion
    arreglo_frec = []
    arreglo = []
    m = int(imagen.shape[0])
    n = int(imagen.shape[1])
    i = 0
    valor = 0
    imagen = list(imagen)
    while i < 256:
    	for x in imagen[i]:
    		valor+=1
    	arreglo_frec.append(valor)
    	valor = 0
    	i+=1
    for x in arreglo_frec:
    	arreglo.append(x/(m*n))
    return arreglo

def cum_dist_func(hist_norm, v_intensidad):
    # TODO: implementar funcion de probabilidad acumulada
    # Debe regresar un valor entre 0 y 1 calculado
    # a partir de hist_norm; v_intensidad es un valor
    # entre 0 y 255
    acumulada = 0
    for n in range(0, int(v_intensidad) + 1):
        acumulada += hist_norm[n]
    return acumulada

def ecualizar(imagen):
    # TODO: implementar ecualizacion
    # Debe regresar la imagen ecualizada
    return np.abs(255 * (imagen/imagen.max())).astype("uint8")

def ecualizar_local(imagen, n):
    # TODO: implementar ecualizacion local con una ventana de nxn
    # Debe regresar la imagen ecualizada localmente
    # NOTA: ES UN FILTRO NO LINEAL, COMO EL FILTRO MEDIANA
    # EN LUGAR DE LA MEDIANA, SE CALCULA LA ECUALIZACION
    # PARA LOS VALORES DE LA VENTANA
    valores = [0]*256
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            valores[imagen[i,j]]+=1
    cdf = [0] * len(valores)
    cdf[0] = valores[0]
    for i in range(n*n, len(valores)):
        cdf[i]= cdf[i-1]+valores[i]
    cdf = [ele*255/cdf[-1] for ele in cdf]
    image_equalized = np.interp(imagen, range(0,256), cdf)
    return image_equalized.astype("uint8")

def especificar(imagen, hist_norm_especifico):
    # TODO: implementar especificacion de histograma
    # Debe regresar la imagen especificada.
    # La variable hist_norm_especifico es el histograma
    # normalizado calculado a partir del muestreo
    # de la distribución especifica.
    imagen_norm = np.zeros(imagen.shape)
    t_i= -1
    x = 0
    for fila in imagen:
        y = 0
        for intensidad in fila:
            cdf = cum_dist_func(hist_norm_especifico, int(intensidad))
            T = math.floor(255. * cdf)
            imagen_norm[x, y] = T
            y += 1
        x += 1
    resultado = imagen + ecualizar((t_i)*imagen_norm).astype("float32")
    return (255. * (imagen_norm - imagen_norm.min())/(imagen_norm.max()-imagen_norm.min())).astype("uint8")