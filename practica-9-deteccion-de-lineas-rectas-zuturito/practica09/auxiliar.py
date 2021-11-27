try:
    import cv2
except:
    pass
from collections import Counter
import numpy as np
import random

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

# Método para señalar componentes conexas
def colorear_componentes_conexas(componentes_etiquetadas):
    img = np.zeros((componentes_etiquetadas.size, 3), dtype="uint8")
    flat_cc = componentes_etiquetadas.flatten()
    
    colors = {}
    for label in np.unique(flat_cc):
        r = random.randint(63, 255)
        g = random.randint(63, 255)
        b = random.randint(63, 255)
        colors[label] = [r,g,b]

    for i in range(flat_cc.size):
        if flat_cc[i] > 0:
            img[i] = colors[flat_cc[i]]
    return img.reshape(componentes_etiquetadas.shape[0],
                      componentes_etiquetadas.shape[1],
                      3)

# Metodo para hacer overlap entre la componente encontrada y una imagen de gris
def combinar_imagenes_color(img_gray, img_color):
    img_gray_three_channels = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
    img_gray_three_channels[img_color != 0] = img_color[img_color != 0]
    return img_gray_three_channels
    
# Método para guardar una imagen en un archivo (default png)
def guardar_imagen(arreglo_bidimensional, ruta_de_salida="../salida.png"):

    # Pasa encima de cualquier otro formato, xq si
    if not ruta_de_salida.endswith(".png"):
        ruta_de_salida += ".png"

    cv2.imwrite(ruta_de_salida, arreglo_bidimensional)
    return True

def ventana_rodante(img, n, border=0):
    assert n % 2 == 1
    # Padding
    pad_value = int((n-1)/2)
    ext_img = np.pad(img, 
                     [pad_value, pad_value],
                     constant_values=border).astype("uint8")

    complete_img = np.zeros((img.shape[0], img.shape[1], n*n), 
                            dtype="uint8")
    for i in range(n):
        for j in range(n):
            complete_img[::, ::, i*n + j] = ext_img[i:i + img.shape[0],
                                                    j:j + img.shape[1]]
    return complete_img.reshape(img.shape[0] * img.shape[1], n*n).astype("float32")

# Normalizacion ingenua
def normalizar_abs_255(img):
    if img.max() > 0:
        return np.abs(255. * (img/img.max())).astype("uint8")
    else:
        # Division by zero
        return img.astype("uint8")

# Normalizacion correcta
def normalizar_255(img):
    if img.max()-img.min() > 0:
        return (255. * (img - img.min())/(img.max()-img.min())).astype("uint8")
    else:
        # Division by zero
        return img.astype("uint8")

def transformacion_derivada(img, img_derivada, c_value=-1):
    resultado = img + normalizar_255((c_value)*img_derivada).astype("float32")
    return normalizar_255(resultado)

# Método para contar componentes conexas
def count_labels(labelled_img):
    return [(label, (labelled_img == label).sum()) for label in np.unique(labelled_img) if label != 0]

# Métodos auxiliares para registrar equivalencias (OPCIONAL)
def registrar_equivalencias(valores, equivalencias):
    valores = set(valores)
    found = []
    new_equivalencias = []
    for i in range(len(equivalencias)):
        grupo = equivalencias[i]
        for valor in list(valores):
            if valor in grupo:
                if i not in found:
                    found.append(i)
    if len(found) > 0:
        for i in range(len(equivalencias)):
            if i in found:
                valores = valores.union(equivalencias[i])
            else:
                new_equivalencias.append(equivalencias[i])
    else:
        new_equivalencias = equivalencias
    new_equivalencias.append(valores)
    return new_equivalencias

def construir_tabla(equivalencias):
    tabla = {}
    for group in equivalencias:
        clase_real = min(group)
        for value in list(group):
            tabla[value] = clase_real
    return tabla
