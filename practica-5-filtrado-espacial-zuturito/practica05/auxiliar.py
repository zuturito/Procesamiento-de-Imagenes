try:
    import cv2
except:
    pass
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

# Método que genera una vecindad de nxn para cada pixel
def ventana_rodante(img, n):
    assert n % 2 == 1
    # Padding
    pad_value = int((n-1)/2)
    ext_img = np.pad(img, [pad_value, pad_value]).astype("uint8")

    complete_img = np.zeros((img.shape[0], img.shape[1], n*n), 
                            dtype="uint8")
    for i in range(n):
        for j in range(n):
            complete_img[::, ::, i*n + j] = ext_img[i:i + img.shape[0],
                                                    j:j + img.shape[1]]
    return complete_img.reshape(img.shape[0] * img.shape[1], n*n).astype("float32")

# Normalizacion ingenua
def normalizar_abs_255(img):
    return np.abs(255. * (img/img.max())).astype("uint8")

# Normalizacion correcta
def normalizar_255(img):
    return (255. * (img - img.min())/(img.max()-img.min())).astype("uint8")

# Añadir el resultado de la derivada a la imagen
def transformacion_derivada(img, img_derivada, c_value=-1):
    resultado = img + normalizar_255((c_value)*img_derivada).astype("float32")
    return normalizar_255(resultado)

# Ejemplo de filtro no lineal
def filtro_max(imagen, n):
    assert n % 2 == 1
    parches_imagen = ventana_rodante(imagen, n)
    max_op = np.vectorize(lambda x: np.sort(x).max(), signature="(n)->()")
    result = max_op(parches_imagen).reshape(imagen.shape)
    return result.astype("uint8")
