# -*- coding: utf-8 -*-
# ESTE ARCHIVO CONTIENE METODOS AUXILIARES: NO MODIFICAR
# LOS CAMBIOS SE IMPLEMENTAN EN procedimientos.py

from auxiliar import *
from procedimientos import *

import os
import sys

def main():
    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))

    # Decodificar
    imagen_llave = cargar_imagen("../resources/imagen_llave.png")
    imagen_mascara_codigo = cargar_imagen("../resources/imagen_mascara_codigo.png")
    print("\nMensaje en imagen_llave:\n")
    print(decodificar_mensaje(imagen_llave,
                              imagen_mascara_codigo))

    # Codificar
    imagen_limpia = cargar_imagen("../resources/gran_calavera_electrica.png")
    # Se carga el mensaje a codificar
    if len(sys.argv) == 1:
        mensaje = convertir_a_ascii(input("\nEscribe tu mensaje: "))
    else:
        # Se le puede pasar un archivo de texto directamente
        with open(sys.argv[1], "r") as fp:
            mensaje = fp.read()
        mensaje = convertir_a_ascii(mensaje)
    
    # Se codifica el mensaje en la imagen gran calavera electrica
    mascara, imagen_modificada = codificar_mensaje(mensaje, 
                                                   imagen_limpia)

    # Se guardan las imgs
    guardar_imagen(imagen_modificada, "../gran_calavera_llave.png")
    guardar_imagen(mascara, "../gran_calavera_mascara_codigo.png")
    
    # Decodificar (prueba)
    print("\nEl mensaje guardado en gran_calavera_llave:\n")
    print(decodificar_mensaje(imagen_modificada,
                              mascara))

if __name__ == "__main__":
    main()
