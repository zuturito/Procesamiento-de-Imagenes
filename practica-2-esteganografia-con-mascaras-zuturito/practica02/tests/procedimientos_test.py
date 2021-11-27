import procedimientos
import numpy as np
import random
import pytest

pytest.total = 100

def img_message_str():
    message = [n for n in range(48, 123)]
    message_str = "".join([chr(v) for v in message])
    
    img = np.zeros((len(message_str), 256))
    for i in range(len(message_str)): 
        for j in range(256):
            img[i,j] = j

    img = img.astype("uint8")
    return img, message, message_str

def test_convertir_a_ascii():
    try:
        procedimientos.convertir_a_ascii("áéíóú¿ñ").encode("ascii")
    except Exception as e:
        pytest.total -= 20
        print("Falla convertir a ascii: -20%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)

def test_codificar_mensaje():
    img, message, message_str = img_message_str()
    
    try:
        mask, _ = procedimientos.codificar_mensaje(message_str, img)

        for i in range(len(message_str)):
            j = message.pop(0)
            assert mask[i, j] == 1
            assert mask.sum() == len(message_str)
    except Exception as e:
        pytest.total -= 30
        print("Falla codificar mensaje: -30%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)

def test_decodificar_mensaje():
    img, message, message_str = img_message_str()
    try:
        mask, _ = procedimientos.codificar_mensaje(message_str, img)
        assert message_str == procedimientos.decodificar_mensaje(img, mask)
    except Exception as e:
        pytest.total -= 50
        print("Falla decodificar mensaje: -50%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)
