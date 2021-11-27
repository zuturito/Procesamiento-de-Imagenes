import numpy as np
import sys
from auxiliar import ventana_rodante, registrar_equivalencias, construir_tabla
import math
try:
    import cv2
except:
    pass

#-----------recicle de código----------------------------
def etiquetado_componentes_conexas(img, B):
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
#--------------------------------------------
def segmentacion_de_notas(img):
    kernel = np.array(([1, 1, 1],[1, -8, 1],[1, 1, 1]),dtype="uint8")
    B = np.array(([0, 1, 0],[1, 1, 1],[0, 1, 0]),dtype="uint8")
    dst = cv2.filter2D(img,-1,kernel)
    img_bw = cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,dst)[1]
    laplacian_img = cv2.Laplacian(img_bw,cv2.CV_64F)
    sobelx = cv2.Sobel(laplacian_img,cv2.CV_64F,1,0,ksize=5)
    erosion = cv2.dilate(sobelx ,B, iterations = 4) 
    image = cv2.erode(erosion, B, iterations = 10)
    img_bw_2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY)[1]
    img_bw_2 = np.array(img_bw_2) / 255
    return img_bw_2