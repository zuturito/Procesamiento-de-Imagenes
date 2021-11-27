from auxiliar import *
from procedimientos import *

import os
import sys

def main():

    # Asegura el directorio de trabajo para respetar rutas relativas
    if len(os.path.dirname(__file__)) > 0 :
        os.chdir(os.path.dirname(__file__))

    b_8N = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]], dtype="uint")

    nombre = "balleto_ponce"
    imagen = cargar_imagen("../resources/%s.png" % nombre)
    mostrar_imagen(imagen, "Original")
    
    imagen_segmentada = segmentacion_de_notas(imagen)
    mostrar_imagen(normalizar_255(imagen_segmentada), "Segmentacion")
    
    componentes = etiquetado_componentes_conexas(imagen_segmentada, b_8N)
    componentes_coloreados = colorear_componentes_conexas(componentes)
    mostrar_imagen(componentes_coloreados, "%d candidatos" % np.unique(componentes).size)

    np.savez_compressed('../solutions/notas_encontradas', solucion=componentes)
    
    guardar_imagen(componentes_coloreados, "../solutions/notas_encontradas.png")

    imagen_combinada = combinar_imagenes_color(imagen, componentes_coloreados)
    mostrar_imagen(imagen_combinada, "Traslape")
    guardar_imagen(imagen_combinada, "../solutions/traslape_notas_encontradas.png")

if __name__ == "__main__":
    main()
