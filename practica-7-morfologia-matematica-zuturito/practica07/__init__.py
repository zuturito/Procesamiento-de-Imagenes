from auxiliar import *
from procedimientos import *

import os
import sys

def main():

    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))

    selem_4N = np.array([[0,1,0],
                         [1,1,1],
                         [0,1,0]], dtype="uint8")

    selem_8N = np.array([[1,1,1],
                         [1,1,1],
                         [1,1,1]], dtype="uint8")
    
    nombre = "ponce"
    for i in range(3):
        imagen = cargar_imagen("../resources/%s%d.png" % (nombre, i))
        mostrar_imagen(imagen, "Original (%d)" % i)
        
        imagen_binaria = binarizar(imagen)
        mostrar_imagen(normalizar_255(imagen_binaria), "Binaria (%d)" % i)
        guardar_imagen(normalizar_255(imagen_binaria), 
                "../solutions/%s%d_bin.png" % (nombre, i))

        imagen_apertura = apertura(imagen_binaria, selem_4N)
        mostrar_imagen(normalizar_255(imagen_apertura), "Apertura (%d)" % i)
        guardar_imagen(normalizar_255(imagen_apertura),
                "../solutions/%s%d_opening.png" % (nombre, i))
        
        imagen_cerradura = cerradura(imagen_binaria, selem_4N)
        mostrar_imagen(normalizar_255(imagen_cerradura), "Cerradura (%d)" % i)
        guardar_imagen(normalizar_255(imagen_cerradura),
                "../solutions/%s%d_closing.png" % (nombre, i))
        
        img_cc_4N = etiquetado_componentes_conexas(imagen_binaria, selem_4N)
        no_cc_4N = np.unique(img_cc_4N).size
        img_cc_4N_color = colorear_componentes_conexas(img_cc_4N)
        mostrar_imagen(img_cc_4N_color, "Componentes conexas 4N (%d; %d componentes)" % (i, no_cc_4N))
        guardar_imagen(img_cc_4N_color,
                "../solutions/%s%d_cc4N.png" % (nombre, i))
        
        img_cc_8N = etiquetado_componentes_conexas(imagen_binaria, selem_8N)
        no_cc_8N = np.unique(img_cc_8N).size
        img_cc_8N_color = colorear_componentes_conexas(img_cc_8N)
        mostrar_imagen(img_cc_8N_color, "Componentes conexas 8N (%d; %d componentes)" % (i, no_cc_8N))
        guardar_imagen(img_cc_8N_color,
                "../solutions/%s%d_bin_cc8N.png" % (nombre, i))

if __name__ == "__main__":
    main()
