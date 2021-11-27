from procedimientos import *
from auxiliar import *

import os
import sys

def main():
    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))

    # Generacion de lookup tables
    gamma_dist_table = construir_tabla_t_gamma(2.5, 1)
    gamma_corr_table = construir_tabla_t_gamma(1/2.5, 1)
    inv_table = construir_tabla_t_inv()
    log_table = construir_tabla_t_log(1)

    # Cargar la imagen
    nombre_img = "casa_muerte_graciela_iturbide_1985"
    imagen = cargar_imagen("../resources/{0}.png".format(nombre_img))
    
    # Imagen inversa
    imagen_inv = mapeo(imagen, inv_table)
    
    # Imagen con distorsion log
    imagen_log = mapeo(imagen, log_table)
    
    # Imagen con distorsion gamma
    imagen_gamma_decode = mapeo(imagen, gamma_dist_table)
    
    # Correccion gamma
    imagen_gamma_corr = mapeo(imagen, gamma_corr_table)
   
    # Despliegue y guardado
    mostrar_imagen(imagen_inv, "Inversa")
    guardar_imagen(imagen_inv, 
                   "../solutions/{0}_inv.png".format(nombre_img))
    
    mostrar_imagen(imagen_log, "Logaritmica")
    guardar_imagen(imagen_log, 
                   "../solutions/{0}_log.png".format(nombre_img))
    
    mostrar_imagen(imagen_gamma_decode, "Decodificacion Gamma")
    guardar_imagen(imagen_gamma_decode, 
                   "../solutions/{0}_gamma_decode.png".format(nombre_img))
    
    mostrar_imagen(imagen_gamma_corr, "Correccion Gamma")
    guardar_imagen(imagen_gamma_corr, 
                   "../solutions/{0}_gamma_corr.png".format(nombre_img))
    
    # Compresion de la imagen corregida mediante cuatro planos de 8 bits
    imagen_comprimida = comprimir(imagen)
    mostrar_imagen(imagen_comprimida, "Comprimida")
    guardar_imagen(imagen_comprimida, 
                   "../solutions/{0}_comprimida.png".format(nombre_img))

if __name__ == "__main__":
    main()
