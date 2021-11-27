import math
import numpy as np

def separar_planos_color(imagen):
    #raise NotImplementedError("Implementar separacion de planos")
    A = imagen[:,:,0] #B
    B = imagen[:,:,1] #G
    C = imagen[:,:,2] #R
    return A, B, C

def integrar_planos_color(A, B, C):
    #raise NotImplementedError("Implementar composicion de planos")
    imagen_ABC = np.zeros((A.shape[0],A.shape[1],3), dtype="uint8")
    imagen_ABC[:,:,0] = A
    imagen_ABC[:,:,1] = B
    imagen_ABC[:,:,2] = C
    return imagen_ABC

def convertir_a_hsi(imagen_rgb):
	rgb = np.float32(imagen_rgb)/255
	red, green, blue = separar_planos_color(rgb)
	H = calc_hue(red, green, blue)
	S = calc_saturation(red, green, blue)
	I_no_normal = calc_intensity(red, green, blue)
	I = np.empty((I_no_normal.shape[0],I_no_normal.shape[1]))
	for i in range(len(I_no_normal)):
		for j in range(len(I_no_normal[i])):
			I[i][j]=round(I_no_normal[i][j]*255)
	#H = round(np.rad2deg(H.sum()))
	#S = round(S.sum())
	return H, S, I

def normalizar_I(I):
    I1=np.empty((I.shape[0],I.shape[1]))
    for i in range(len(I)):
        for j in range(len(I[i])):
            I1[i][j]=round(I[i][j]*255)
    return I1

def calc_intensity(red, green, blue):
	return np.true_divide(red + green + blue, 3)

def calc_saturation(red, green, blue):
	minimum = np.minimum(np.minimum(red, green), blue)
	saturation=np.empty((red.shape[0],red.shape[1]))
	for i in range(len(red)):
		for j in range(len(red[i])):
			if (red[i][j]==0) and (green[i][j]==0) and (blue[i][j]==0):
				saturation[i][j]=0
			else:
				saturation[i][j] = 1 - (3 / (red[i][j] + green[i][j] + blue[i][j]) * minimum[0][0])
	return saturation

def calc_hue(red, green, blue):
	h=np.empty((red.shape[0],red.shape[1]))
	for i in range(0, blue.shape[0]):
		for j in range(0, blue.shape[1]):
			if (red[i][j]==green[i][j]) and (green[i][j]==blue[i][j]):
				h[i][j]==90
			else:
				a=0.5*((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j]))
				b1=math.pow((red[i][j] - green[i][j]),2)+((red[i][j] - blue[i][j])*(green[i][j] - blue[i][j]))
				b=math.pow(b1, 0.5)
				if b==0:
					h[i][j]=0
				else:
					h[i][j]=np.true_divide(a, b)
					h[i][j] = math.acos(h[i][j])
			if blue[i][j] <= green[i][j]:
					h[i][j] = h[i][j]
			elif blue[i][j]>green[i][j]:
					h[i][j]=((360 * math.pi) / 180.0) - h[i][j]
	return h

def segmentar(componente_h):
    #raise NotImplementedError("Implementar segmentacion en H")
    h=np.round(componente_h)
    T_Otsu, eta = metodo_otsu(h)
    mascara_binaria=umbralizacion_doble(componente_h, T_Otsu+.7,T_Otsu+2.0)
    return mascara_binaria

def umbralizacion_doble(img, umbral,umbral2):
    for fil in range(img.shape[0]):
        for col in range(img.shape[1]):
            pixel=img[fil,col]
            if umbral<pixel and pixel<umbral2:
                img[fil,col]=1
            else:
                img[fil,col]=0
    return img.astype("uint8")

#---------------recicle de código----------------------
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

def histograma_norm(imagen):
    M = imagen.shape[0]
    N = imagen.shape[1]
    result = []
    for n in range(0, 256):
        cantidad = np.sum(imagen == n)
        probabilidad = cantidad / (M * N)
        result.append(probabilidad)
    return result