# -*- coding: utf-8 -*-
#
# LOS CAMBIOS SE IMPLEMENTAN AQUI.
#
# LLENEN LAS FUNCIONES Y LLAMEN __init__.py
# 
# PARA FACILITAR EL TRABAJO, ESTAN LOS RETURNS

import numpy as np
from unidecode import unidecode
import itertools

def convertir_a_ascii(texto_de_entrada):
    try:
        mensaje_en_ascii = unidecode(unicode(texto_de_entrada, encoding = "utf-8"))
    except:
        mensaje_en_ascii = unidecode(str(texto_de_entrada))
    return mensaje_en_ascii

def decodificar_mensaje(imagen, mascara):
	matriz_nueva = np.zeros(imagen.shape, dtype="int32")
	matriz_nueva = ([x @ y for x, y in zip(imagen,mascara)])
	texto_del_mensaje = ''
	for x in matriz_nueva:
		if x > 0:
			texto_del_mensaje += str(chr(x))
	return texto_del_mensaje

def codificar_mensaje(mensaje, imagen_original):
    mascara = np.zeros(imagen_original.shape)
    imagen_modificada = imagen_original.copy()
    codificado = []
    for pos in mensaje:
        codificado.append(ord(pos))    
    arr_mensaje = np.array(codificado)
    arr_mensaje = np.reshape(arr_mensaje, (-1, 1)) 
    arr_dif = []
    for f, m in itertools.zip_longest(imagen_modificada, arr_mensaje, fillvalue=0):
        arr_dif.append(f-m)
    arr_dif = np.array(arr_dif)
    arr_dif = np.reshape(arr_dif, imagen_original.shape)
    i = 0
    for f, c in zip(arr_dif, arr_mensaje):
    	cols = int(c)
    	rows = i
    	try:
    		mascara[rows][cols] = '1'
    		imagen_modificada[rows][cols] = c
    	except ValueError as msg:
    		return msg
    	i+=1
    return mascara.astype("uint8"), imagen_modificada.astype("uint8")