# Práctica 1 - ALUMNO: FRANCISCO SÁNCHEZ VÁSQUEZ

Práctica sobre representación de imágenes e interpolación bilineal.

## Iniciando

Asegurense de tener instalado OpenCV y opencv-python.

### Prerequisitos

* [OpenCV](https://opencv.org/)
* [opencv-python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows)

Les recomiendo instalarlo en un ambiente virtual: 

```
python3 -mvenv .env
```

Una vez creado, lancenlo e installen opencv-python:

```
pip install opencv-python
```

## Calificación

El script de calificación calcula el [MAE](https://en.wikipedia.org/wiki/Mean_absolute_error) entre los valores en el archivo final que se obtiene al ejecutar

```
python __init__.py 
```

desde la carpeta **practica01**. Se compara su resultado contra mi propia implementación, que sirve como *ground truth*. ***Asegurense de que resultado.txt no sea una imagen vacía antes de subir los cambios.***

