# -*- coding: utf-8 -*-
# ESTE ARCHIVO CONTIENE METODOS AUXILIARES: NO MODIFICAR
import cv2

import numpy as np

# Método auxiliar para mostrar una imagen
def mostrar_imagen(arreglo_bidimensional, titulo_de_ventana=None):
    if not titulo_de_ventana:
        titulo_de_ventana = "%dx%d" % arreglo_bidimensional.shape[:2] 
   
    assert isinstance(titulo_de_ventana, str)

    arreglo_bidimensional = arreglo_bidimensional.astype('uint8')
    cv2.imshow(titulo_de_ventana, arreglo_bidimensional)
    
    while cv2.getWindowProperty(titulo_de_ventana, 
                                cv2.WND_PROP_VISIBLE) >= 1:
        if cv2.waitKeyEx(1000) == 27:
            cv2.destroyWindow(titulo_de_ventana)
            break

# Método que carga una imagen de gris
def cargar_imagen(ruta_imagen):
    
    imagen = cv2.imread(ruta_imagen)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return gris

# Método para guardar una imagen en un archivo (default png)
def guardar_imagen(arreglo_bidimensional, ruta_de_salida="../salida.png"):
    
    # Pasa encima de cualquier otro formato, xq si
    if not ruta_de_salida.endswith(".png"):
        ruta_de_salida += ".png"
    
    cv2.imwrite(ruta_de_salida, arreglo_bidimensional)
    return True
