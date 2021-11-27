# -*- coding: utf-8 -*-

from procedimientos import *

def main():
    # Se carga la imagen reducida
    imagen = cargar_imagen("../resources/entierro_yalalag_lola_alvares_bravo_1946.txt")
    mostrar_imagen(imagen)
    
    # Se agranda la imagen reducida
    imagen_bilinear = agrandar_imagen(imagen, 3)
    mostrar_imagen(imagen_bilinear)
    
    # Se guarda la imagen interpolada
    guardar_imagen(imagen_bilinear)
    
    # Se carga la imagen interpolada guardada
    imagen_cargada = cargar_imagen("../resultado.txt")
    mostrar_imagen(imagen_cargada)

if __name__ == "__main__":
    main()
