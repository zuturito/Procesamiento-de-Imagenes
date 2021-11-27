# Práctica 4 - ALUMNO: FRANCISCO SÁNCHEZ VÁSQUEZ

Práctica sobre ecualización de histograma.

## Iniciando

Asegurense de tener instalado OpenCV y opencv-python.

### Prerequisitos

* [OpenCV](https://opencv.org/)
* [SciPy](https://www.scipy.org/)
* [opencv-python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows)
* [matplotlib](https://matplotlib.org/) (Opcional: para tests)

Les recomiendo instalarlo en un ambiente virtual: 

```
python3 -mvenv .env
```

Una vez creado, lancenlo e installen opencv-python, SciPy y matplotlib (para testing):

```
pip install opencv-python scipy matplotlib
```

## Calificación

El script de calificación revisa la implementación de las tres funciones que establece la práctica, las cuales tienen los valores siguientes: 

```
Calcular histograma: 10%
Calcular probabilidad acumulada: 10%
Ecualizar imagen (global): 20%
Ecualizar imagen (local): 30%
Especificacion de histograma: 30%
```

Estrictamente hablando, la práctica está aprobada con los ejercicios de ecualización (70/100). La especificación tradicionalmente les cuesta más trabajo, entonces la estoy calificando más laxamente (ver los tests).
