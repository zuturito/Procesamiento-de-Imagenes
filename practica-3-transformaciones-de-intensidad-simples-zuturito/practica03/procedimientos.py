import math
import numpy as np
# AQUI VA EL CODIGO

def construir_tabla_t_inv():
    i = 0
    arreglo_inv = []
    while i < 256:
    	cuenta_inv = 255 - i
    	arreglo_inv.append(cuenta_inv)
    	i+=1
    return arreglo_inv

def construir_tabla_t_log(constante):
    arreglo_valor_log = []
    i = 0
    while i < 256:
    	cuenta_log = 255 * constante * math.log(1+i/255)
    	arreglo_valor_log.append(round(cuenta_log))
    	i+=1
    return arreglo_valor_log

def construir_tabla_t_gamma(v_gamma, constante):
    arreglo_valor = []
    i = 0
    while i < 256:
    	cuenta = 255 * constante * (i / 255) ** v_gamma
    	arreglo_valor.append(round(cuenta))
    	i+=1
    return arreglo_valor

def mapeo(imagen, tabla):
    imagen_mapeo = np.zeros(imagen.shape)
    i = 0
    for row in imagen:
        j = 0
        for col in row:
           l = tabla[col]
           imagen_mapeo[i, j] = l
           j += 1
        i += 1
    return imagen_mapeo.astype("uint8")

def comprimir(imagen):
    i = 0
    b = 0
    newImg = np.zeros(imagen.shape)
    for row in imagen:
        j = 0
        for col in row:
            b = "{0:08b}".format(int(col))
            b = list(b)
            b8 = (int(b[0]) * int(2**(8-1)))
            b7 = (int(b[1]) * int(2**(7-1)))
            b6 = (int(b[2]) * int(2**(6-1)))
            b5 = (int(b[3]) * int(2**(5-1)))             
            g = int(b8) + int(b7) + int(b6) + int(b5)
            newImg[i, j] = g
            j += 1
        i += 1
    return newImg.astype('uint8')
