from procedimientos import *
from auxiliar import *

import os
import sys

def main():
    
    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))

    nombre_img = "adixans_nahuiolin_1924"
    imagen = cargar_imagen("../resources/{0}.png".format(nombre_img))

    # Ecualizacion global de la imagen
    imagen_ecualizada = ecualizar(imagen)
    mostrar_imagen(imagen_ecualizada, "Ecualizada")
    guardar_imagen(imagen_ecualizada,
                   "../solutions/{0}_ecualizada.png".format(nombre_img))
    
    # Especificacion de histograma
    hist_norm_lognorm = generar_dist_lognorm()
    imagen_lognorm = especificar(imagen, hist_norm_lognorm)
    mostrar_imagen(imagen_lognorm, "Especificacion dist Lognorm")
    guardar_imagen(imagen_lognorm,
                   "../solutions/{0}_lognorm.png".format(nombre_img))
    
    hist_norm_laplace = generar_dist_laplace()
    imagen_laplace = especificar(imagen, hist_norm_laplace)
    mostrar_imagen(imagen_laplace, "Especificacion dist Laplace")
    guardar_imagen(imagen_laplace,
                   "../solutions/{0}_laplace.png".format(nombre_img))
    
    hist_norm_gamma = generar_dist_gamma()
    imagen_gamma = especificar(imagen, hist_norm_gamma)
    mostrar_imagen(imagen_gamma, "Especificacion dist gamma")
    guardar_imagen(imagen_gamma,
                   "../solutions/{0}_gamma.png".format(nombre_img))
   
    nombre_img = "local_patch_img"
    imagen = cargar_imagen("../resources/{0}.png".format(nombre_img))
    
    # Ecualizacion local
    imagen_ecualizada_ventana = ecualizar_local(imagen, 3)
    mostrar_imagen(imagen_ecualizada_ventana, "Ecualizacion local")
    guardar_imagen(imagen_ecualizada_ventana,
                   "../solutions/{0}_ecualizada.png".format(nombre_img))
    
if __name__ == "__main__":
    main()
