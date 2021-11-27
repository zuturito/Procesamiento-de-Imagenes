import numpy as np
from auxiliar import ventana_rodante

def filtro_min(imagen, n):
    assert n % 2 == 1
    # TODO: Implementar filtro min
    parches_imagen = ventana_rodante(imagen, n)
    minimo_val = np.vectorize(lambda x: np.sort(x).min(), signature="(n)->()")
    result = minimo_val(parches_imagen).reshape(imagen.shape)
    return result.astype("uint8")

def filtro_mediana(imagen, n):
    assert n % 2 == 1
    # TODO: Implementar filtro mediana
    imagen_filtro_med = np.copy(imagen)
    ventana = ventana_rodante(imagen, n)
    x = 0
    i = 0
    for fila in imagen:
        y = 0
        for intensidad in fila:
            ventana_ord = sorted(ventana[i])
            filtro_med = ventana_ord[int((n*n)/2) - 1]
            imagen_filtro_med[x, y] = filtro_med 
            y += 1
            i += 1
        x += 1
    return imagen_filtro_med.astype("uint8")
#----------------hasta aquí OK------------------
def kernel_promedio(n):
    assert n % 2 == 1
    # TODO: Regresa un kernel promedio de nxn
    result = np.ones((n, n)) * (1/(n*n))
    return result.astype("float32")

def kernel_gaussiano(n, K, sigma):
    assert n % 2 == 1
    # TODO: Regresa un kernel gaussiano de nxn, con desviacion sigma
    # y parametro K
    valor = int((n-1)/2)
    result = np.ones((n, n))
    for x in range(n):
        for y in range(n):
            diferencia = np.sqrt((x - valor) ** 2 + (y - valor) ** 2)
            result[x, y] = np.exp(-(diferencia**2)/(2 * sigma **2))
    return result.astype("float32")

def kernel_seis_sigma(K, sigma):
    #raise NotImplementedError("No implementado :(")
    # TODO: Regresa un kernel gaussiano de 6sigma x 6sigma, 
    # con desviacion sigma y parametro K.
    #
    # OJO: 6sigma + 1 si 6sigma es par
    if ((6 * sigma) % 2 == 0):
        n = 6 * sigma + 1
    else:
        n = 6 * sigma
    valor = int((n-1)/2)
    result = np.ones((n, n))
    for x in range(n):
        for y in range(n):
            diferencia = np.sqrt((x - valor) ** 2 + (y - valor) ** 2)
            result[x, y] = np.exp(-(diferencia**2)/(2 * sigma **2))
    return result.astype("float32")

def convolucion(imagen, kernel, return_type="float32"):
    #raise NotImplementedError("No implementado :(")
    # TODO: Hace la operacion de convolucion
    #
    # OJO: a veces return_type queremos forzarlo a uint8 pero
    # no siempre, ya que operaciones como la derivada daran
    # valores negativos (en uint8 se pierden)
    imagen_conv = np.zeros(np.shape(imagen))
    n = kernel.shape[0]
    ventana = ventana_rodante(imagen, n)
    x = 0
    i = 0
    for fila in imagen:
        y = 0
        for intensidad in fila:
            s = 0 
            arr = np.reshape(ventana[i], kernel.shape)
            g = arr * kernel 
            i += 1
            if return_type == "uint8":
                imagen_conv[x, y] = round(g.sum())
            else:
                imagen_conv[x, y] = g.sum()
            y += 1
        x += 1
    return imagen_conv.astype(return_type)

def filtro_mascara_borrosa(imagen, imagen_suavizada, k):
    #raise NotImplementedError("No implementado :(")
    # TODO: Implementar filtro de mascara borrosa
    h = np.zeros(np.shape(imagen))
    resultado = np.zeros(np.shape(imagen))
    x = 0
    for fila in imagen:
        y = 0
        for var in fila:
            h[x, y] = int(imagen[x, y]) - int(imagen_suavizada[x, y])
            resultado[x, y] = imagen[x, y] + k * h[x, y]
            y += 1
        x += 1
    return resultado.astype("uint8")

def gradiente_sobel(imagen):
    #raise NotImplementedError("No implementado :(")
    # TODO: Implementar filtro de sobel
    # y regresar la imagen gradiente
    gx = np.array(([-1, -2, -1],[0, 0, 0],[1, 2, 1]),dtype="float64")
    gy = np.array(([-1, 0, 1],[-2, 0, 2],[-1, 0, 1]),dtype="float64")
    Imagen1 = convolucion(imagen,gx, "float64")
    Imagen2 = convolucion(imagen,gy, "float64")
    result = np.sqrt(np.square(Imagen1) + np.square(Imagen2))
    return result.astype("float32")

def laplaciano(imagen):
    #raise NotImplementedError("No implementado :(")
    # TODO: Implementar laplaciano
    kOperador = np.array(([1, 1, 1],[1, -8, 1],[1, 1, 1]),dtype="float64")
    result = convolucion(imagen,kOperador)
    return result.astype("float32")
