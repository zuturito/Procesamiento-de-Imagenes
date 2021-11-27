import procedimientos as pr
import numpy as np
import pytest

from auxiliar import count_labels

pytest.total = 100

def image_generator():
    '''Generates: 

    border_img: a squared image with center_value intensity pixels, 
    surrounded by a border of border_value intensity pixels. 
    
    ramp: a 255 intensity ramp.
    '''
    img_cross = np.array([[0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,1,0,0,0,0,0,1,0],
                          [0,0,0,0,1,0,0,0,0],
                          [0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,1,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,1,0,0,0,0,0,1,0],
                          [0,0,0,0,0,0,0,0,0]], dtype="uint8")
    
    img_one_cc = np.array([[0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,1,0,0,1,1,0,1,0],
                           [0,0,1,0,1,1,1,0,0],
                           [0,0,1,1,0,0,0,0,0],
                           [0,1,0,1,1,1,0,0,0],
                           [0,0,1,0,0,0,1,0,0],
                           [0,1,0,0,0,0,0,1,0],
                           [0,0,0,0,0,0,0,0,0]], dtype="uint8")
    
    selem_4N = np.array([[0,1,0],
                         [1,1,1],
                         [0,1,0]], dtype="uint8")

    selem_8N = np.array([[1,1,1],
                         [1,1,1],
                         [1,1,1]], dtype="uint8")
    
    return img_cross, img_one_cc, selem_4N, selem_8N

def test_erosion():
    try:
        img_cross, _, selem_4N, selem_8N = image_generator()
        expected_4N = np.array([[0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,1,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0]], dtype="uint8")
        expected_8N = np.zeros(img_cross.shape, dtype="uint8")
        assert False not in (expected_4N == pr.erosion(img_cross, selem_4N))
        assert False not in (expected_8N == pr.erosion(img_cross, selem_8N))
    except Exception as e:
        print("\n Erosion mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_dilatacion():
    try:
        img_cross, _, selem_4N, selem_8N = image_generator()
        expected_4N = np.array([[0,0,0,0,0,0,0,0,0],
                                [0,1,0,0,0,0,0,1,0],
                                [1,1,1,0,1,0,1,1,1],
                                [0,1,0,1,1,1,0,1,0],
                                [0,0,1,1,1,1,1,0,0],
                                [0,0,0,1,1,1,0,0,0],
                                [0,1,0,0,1,0,0,1,0],
                                [1,1,1,0,0,0,1,1,1],
                                [0,1,0,0,0,0,0,1,0]], dtype="uint8")

        expected_8N = np.array([[0,0,0,0,0,0,0,0,0],
                                [1,1,1,0,0,0,1,1,1],
                                [1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1],
                                [0,0,1,1,1,1,1,0,0],
                                [0,0,1,1,1,1,1,0,0],
                                [1,1,1,1,1,1,1,1,1],
                                [1,1,1,0,0,0,1,1,1],
                                [1,1,1,0,0,0,1,1,1]], dtype="uint8")

        assert False not in (expected_4N == pr.dilatacion(img_cross, selem_4N))
        assert False not in (expected_8N == pr.dilatacion(img_cross, selem_8N))
    except Exception as e:
        print("\n Dilatacion mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_apertura():
    try:
        img_cross, _, selem_4N, selem_8N = image_generator()
        expected_4N = np.array([[0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,1,0,0,0,0],
                                [0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,1,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0]], dtype="uint8")
        
        expected_8N = np.zeros(img_cross.shape, dtype="uint8")
        assert False not in (expected_4N == pr.apertura(img_cross, selem_4N))
        assert False not in (expected_8N == pr.apertura(img_cross, selem_8N))
    except Exception as e:
        print("\n Apertura mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_cerradura():
    try:
        img_cross, _, selem_4N, selem_8N = image_generator()
        expected_4N = np.copy(img_cross)
        expected_8N = np.array([[0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [1,1,0,0,0,0,0,1,1],
                                [0,0,0,1,1,1,0,0,0],
                                [0,0,0,1,1,1,0,0,0],
                                [0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [1,1,0,0,0,0,0,1,1],
                                [1,1,0,0,0,0,0,1,1]], dtype="uint8")
        assert False not in (expected_4N == pr.cerradura(img_cross, selem_4N))
        assert False not in (expected_8N == pr.cerradura(img_cross, selem_8N))
    except Exception as e:
        print("\n Cerradura mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_connected_component_labelling():
    try:
        _, img_cc, selem_4N, selem_8N = image_generator()
        
        labels_4N = count_labels(pr.etiquetado_componentes_conexas(img_cc, selem_4N))
        assert len(labels_4N) == 9
        
        labels_8N = count_labels(pr.etiquetado_componentes_conexas(img_cc, selem_8N))
        assert len(labels_8N) == 1
    except Exception as e:
        print("\n Etiquetado de componentes conexas mal implementado :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_binarizar():
    try:
        binimg = pr.binarizar(np.array([
            range(0,255),
            range(0,255),
            range(0,255)],
            dtype="uint8"))
        assert np.unique(binimg).size <= 2
        if np.unique(binimg).size == 2:
            assert 1 in binimg
            assert 0 in binimg
    except Exception as e:
        print("\n Binarizacion mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
