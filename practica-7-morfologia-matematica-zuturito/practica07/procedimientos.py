import numpy as np
import math
from auxiliar import ventana_rodante, registrar_equivalencias, construir_tabla
#-----------recicle de código----------------------------
def umbralizacion_global(img, umbral):
    result = np.zeros(img.shape)
    x = 0
    for fila in img:
        y = 0
        for intensidad in fila:
            if(intensidad > umbral):
            	valor = 0
            else:
            	valor = 1
            result[x, y] = valor
            y += 1
        x += 1
    return result.astype("uint8")
#---------------------------------------------------------
def erosion(img, B, borde=0):
    imagen = np.zeros(np.shape(img))
    centrar = ventana_rodante(img, B.shape[0], borde)
    x = 0
    i = 0
    for fila in img:
        y = 0
        for z in fila:
            ventana = centrar[i].reshape(np.shape(B))
            comparacion = ventana * B
            if (comparacion == B).all():
                imagen[x, y] = 1
            i += 1 
            y += 1
        x += 1
    return imagen.astype("uint8")

def dilatacion(img, B):
    imagen = np.zeros(np.shape(img))
    centrar = ventana_rodante(img, B.shape[0])
    x = 0
    i = 0
    for fila in img:
        y = 0
        for z in fila:
            ventana = centrar[i].reshape(np.shape(B))
            x2 = 0
            for row_v in ventana:
                y2 = 0
                for v in row_v:
                    if (B[x2, y2] == v) & (B[x2, y2] == 1):
                        imagen[x, y] = 1
                    y2 += 1
                x2 += 1
            i += 1 
            y += 1
        x += 1
    return imagen.astype("uint8")

def apertura(img, B):
	aper1 = erosion(img,B)
	aper2 = dilatacion(aper1,B)
	return aper2.astype("uint8")

def cerradura(img, B):
	cerra1 = dilatacion(img,B)
	cerra2 = erosion(cerra1,B,1)
	return cerra2.astype("uint8")

def etiquetado_componentes_conexas(img, B):
    # OJO: Las etiquetas pueden ser > 255, entonces el arreglo
    # tiene que ser al menos int32
    #
    # Los metodos registrar_equivalencias y construir_tabla
    # pueden auxiliarlos si lo desean (o pueden escribir el propio)
    #raise NotImplementedError("Implementar etiquetado de componentes conexas")
    result = np.zeros(np.shape(img))
    ventanas = ventana_rodante(img, B.shape[0])
    etiqueta = 1
    equivalencias = []
    x = 0
    i = 0
    #Primer_pase
    for fila in img:
        y = 0
        for intensidad in fila:
            if (intensidad == 1):
                ventana = ventanas[i].reshape(np.shape(B))
                vecindad = ventana * B
                #etiquetar_val
                ventanas_result = ventana_rodante(result, B.shape[0])
                ventana_result = ventanas_result[i].reshape(np.shape(B))
                ventana_temp = vecindad * ventana_result
                #¿existe?
                if (ventana_temp.sum() > 0):
                    mascara = np.ma.masked_equal(ventana_temp, 0, copy=False)
                    result[x, y] = mascara.min()
                    #Registros
                    valores = []
                    for var in ventana_temp[np.nonzero(ventana_temp)]:
                        valores.append(int(var))
                    equivalencias = registrar_equivalencias(valores, equivalencias)
                    tabla = construir_tabla(equivalencias)
                else:
                    result[x, y] = etiqueta
                    etiqueta += 1            
            i += 1
            y += 1
        x += 1
    #Segundo_pase
    x = 0
    for row in result:
        y = 0
        for etiqueta_2 in row:
            if (etiqueta_2 > 0):
                try:
                    result[x, y] = tabla[int(etiqueta_2)]
                except:
                    pass
            y += 1
        x += 1
    return np.array(result, dtype="int32")

def binarizar(img):
    # OJO: la binarizacion puede ser cualquier metodo de umbral,
    # solo asegurense que devuelva una imagen binaria en el rango
    # de [0, 1]
    result = umbralizacion_global(img, 91)
    return result.astype("uint8")
