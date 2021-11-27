from auxiliar import *
from procedimientos import *

import os
import sys

def main():

    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))
   
    nombre_imagen = "piedra_sol_original"
    ruta_recursos = "../resources/%s.png"
    ruta_soluciones = "../solutions/%s.png"
    
    imagen = cargar_imagen(ruta_recursos % nombre_imagen)
    mostrar_imagen(imagen, "Original")

    # Filtro max
    imagen_max = filtro_max(imagen, 3)
    mostrar_imagen(imagen_max, "Filtro max")
    guardar_imagen(imagen_max, ruta_soluciones % (nombre_imagen + "_max"))

    # Filtro min
    imagen_min = filtro_min(imagen, 3)
    mostrar_imagen(imagen_min, "Filtro min")
    guardar_imagen(imagen_min, ruta_soluciones % (nombre_imagen + "_min"))
    
    # Filtro mediana
    imagen_mediana = filtro_mediana(imagen, 7)
    mostrar_imagen(imagen_mediana, "Filtro mediana")
    guardar_imagen(imagen_mediana, ruta_soluciones % (nombre_imagen + "_mediana"))

    # Filtro promedio
    kernel_9_promedio = kernel_promedio(9)
    imagen_promedio = convolucion(imagen, 
                                  kernel_9_promedio,
                                  "uint8")
    mostrar_imagen(imagen_promedio, "Filtro promedio")
    guardar_imagen(imagen_promedio, ruta_soluciones % (nombre_imagen + "_promedio"))

    # Filtro gaussiano (5x5)
    kernel_5_gaussiano = kernel_gaussiano(5, 1, 1)
    kernel_5_gaussiano_norm = (1/kernel_5_gaussiano.sum()) *\
            kernel_5_gaussiano
    imagen_5_gauss = convolucion(imagen, 
                                 kernel_5_gaussiano_norm,
                                 "uint8")
    mostrar_imagen(imagen_5_gauss, "Filtro gaussiano (5x5)")
    guardar_imagen(imagen_5_gauss, ruta_soluciones % (nombre_imagen + "_gauss_55"))
    
    # Filtro gaussiano (7x7)
    kernel_7_gaussiano = kernel_gaussiano(7, 1, 1)
    kernel_7_gaussiano_norm = (1/kernel_7_gaussiano.sum()) *\
            kernel_7_gaussiano
    imagen_7_gauss = convolucion(imagen, 
                                 kernel_7_gaussiano_norm,
                                 "uint8")
    mostrar_imagen(imagen_7_gauss, "Filtro gaussiano (7x7)")
    guardar_imagen(imagen_7_gauss, ruta_soluciones % (nombre_imagen + "_gauss_77"))
    
    # Filtro gaussiano (sigma=7)
    kernel_sigma_7_gaussiano = kernel_seis_sigma(1, 7)
    kernel_sigma_7_gaussiano_norm = (1/kernel_sigma_7_gaussiano.sum()) *\
            kernel_sigma_7_gaussiano
    imagen_sigma_7_gauss = convolucion(imagen, 
                                       kernel_sigma_7_gaussiano_norm,
                                       "uint8")
    mostrar_imagen(imagen_sigma_7_gauss, "Filtro gaussiano (sigma=7)")
    guardar_imagen(imagen_sigma_7_gauss, ruta_soluciones % (nombre_imagen + "_gauss_sigma7"))

    # Filtro mascara borrosa
    imagen_m_borr_7_gauss = filtro_mascara_borrosa(imagen, 
                                                   imagen_7_gauss, 
                                                   1)
    mostrar_imagen(imagen_m_borr_7_gauss, "Filtro mascara borrosa (Gauss 7x7)")
    guardar_imagen(imagen_m_borr_7_gauss, ruta_soluciones % (nombre_imagen + "_mb_gauss_77"))
    
    imagen_m_borr_sigma_7 = filtro_mascara_borrosa(imagen, 
                                                   imagen_sigma_7_gauss, 
                                                   1)
    mostrar_imagen(imagen_m_borr_sigma_7, "Filtro mascara borrosa (Gauss sigma=7)")
    guardar_imagen(imagen_m_borr_sigma_7, ruta_soluciones % (nombre_imagen + "_mb_gauss_sigma7"))
    
    imagen_highboost_5_gauss = filtro_mascara_borrosa(imagen, 
                                                      imagen_5_gauss, 
                                                      2)
    mostrar_imagen(imagen_highboost_5_gauss, "Filtro high boost (k=2, Gauss 5x5)")
    guardar_imagen(imagen_highboost_5_gauss, ruta_soluciones % (nombre_imagen + "_hb_gauss_55"))
   
   # Filtros derivativos
    sobel = gradiente_sobel(imagen_7_gauss)
    imagen_sobel = normalizar_abs_255(sobel)
    mostrar_imagen(imagen_sobel,
                   "Gradiente de Sobel (Gauss 7x7)")
    guardar_imagen(imagen_sobel, ruta_soluciones % (nombre_imagen + "_sobel_gauss_77"))
    
    laplace = laplaciano(imagen_7_gauss)
    imagen_laplace = normalizar_abs_255(laplace)
    mostrar_imagen(imagen_laplace,
                   "Laplaciano (Gauss 7x7)")
    guardar_imagen(imagen_laplace, ruta_soluciones % (nombre_imagen + "_laplace_gauss_77"))
    
    # Transformacion Laplaciano
    imagen_t_laplaciano = transformacion_derivada(imagen,
                                                  laplace)
    mostrar_imagen(imagen_t_laplaciano, 
                   "Transformacion Laplaciano (Gauss 7x7)")
    guardar_imagen(imagen_t_laplaciano, ruta_soluciones % (nombre_imagen + "_t_laplace_gauss_77"))

if __name__ == "__main__":
    main()

