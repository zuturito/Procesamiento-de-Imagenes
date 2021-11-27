# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math as math
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

# Método donde se cargará el archivo txt
def cargar_imagen(ruta_imagen_txt):
    with open(ruta_imagen_txt, "r") as fp:
        img_contents = fp.readlines()
    # TODO: AQUÍ VA EL CODIGO
    x = int(img_contents[0])
    y = int(img_contents[1])
    img = np.array((x, y), dtype=np.float)
    lst = img_contents[2].split(" ")
    arreglo = []
    for i in (lst):
        pixel = math.floor(255 * float(i))
        arreglo.append(pixel)
    img = np.array(arreglo)
    img = np.reshape(img, (x,y), 'F')
    # regresa una matriz de enteros sin signo de 8 bits
    return img.astype('uint8')

# Método para agrandar la imágen
def agrandar_imagen(arreglo_bidimensional, tamanio):
    ''' tamaño será un número entero (en el caso del ejemplo, la función recibe un 3) '''  
    # esto crea una imagen en blanco
    #white_img = np.ones((no_filas, no_columnas)) * 255
    # TODO: AQUÍ VA EL CODIGO
    row, col = arreglo_bidimensional.shape
    p = tamanio - 1
    blank_image=cv2.resize(arreglo_bidimensional,(((col*tamanio)-p),(row*tamanio)-p),interpolation=cv2.INTER_LINEAR)
    return blank_image

# Método para guardar la imagen en un archivo de texto
def guardar_imagen(arreglo_bidimensional, ruta_de_salida="../resultado.txt"):
    ''' Formato: linea 1 no_filas, linea 2 no_columnas, linea 3 vector de intensidad normalizado 
    (concatenación de columnas verticales) '''
    # TODO: AQUÍ VA EL CODIGO
    row, col = arreglo_bidimensional.shape
    pixeles = arreglo_bidimensional/255
    arreglo_final = ' '.join(' '.join('%0.2f' %x for x in y) for y in pixeles)
    file = open(ruta_de_salida,"w")
    file.writelines([str(row), "\n"+str(col), "\n"+str(arreglo_final)])
    file.close()
    # aquí no vamos a guardar nada, la salida se escribe en disco
    raise NotImplementedError("No esta implementado")

