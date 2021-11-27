import procedimientos
import numpy as np
import matplotlib.image as mpimg
import pytest

pytest.total = 100

def normalized_error(g_truth, proposed_solution):
    '''0 if eq; 1 if completely diff'''
    try:
        total = g_truth.shape[0] * g_truth.shape[1]
        sum_of_diff = abs((g_truth - proposed_solution)).sum()
    except Exception as e:
        print(type(e).__name__, ":" , e)
        return 0.
    return sum_of_diff/total

def test_histograma_norm():
    try:
        test_img = np.array([np.ones(100)*i for i in range(256)], 
                             dtype="uint8")
        # test histogram
        hist = procedimientos.histograma_norm(test_img)
        assert hist[0] * 256 == 1.0
        assert sum(hist) == 1.0
    except Exception as e:
        print("\nHistograma normalizado mal calculado :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_cum_dist_func():
    try:
        test_img = np.array([np.ones(100)*i for i in range(256)], 
                             dtype="uint8")
        # test histogram
        hist = procedimientos.histograma_norm(test_img)
        for i in range(256):
            assert hist[0]*(i+1) == procedimientos.cum_dist_func(hist, i)
    except Exception as e:
        print("\nProbabilidad acumulada mal calculada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_ecualizar():
    try:
        test_img = np.array([np.ones(100)*i for i in range(256)], 
                             dtype="uint8")
        img_ecualizada = procedimientos.ecualizar(test_img)
        assert False not in (test_img == img_ecualizada)
    except Exception as e:
        print("\nEcualizacion incorrecta :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 20
        raise(e)

def test_ecualizar_local():
    try:
        test_img_255 = np.ones((256, 100), dtype="uint8") * 255
        test_img_127 = np.ones((256, 100), dtype="uint8") * 127
        
        result = procedimientos.ecualizar_local(test_img_255, 3)
        result -= procedimientos.ecualizar_local(test_img_127, 3)
        assert result.sum() == 0.
    except Exception as e:
        print("\nEcualizacion local incorrecta :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 30
        raise(e)

def test_especificacion(capsys):
    try:
        rutas = [("../resources/resultados/gamma.png", 
                  "../solutions/adixans_nahuiolin_1924_gamma.png"),
                 ("../resources/resultados/laplace.png", 
                  "../solutions/adixans_nahuiolin_1924_laplace.png"),
                 ("../resources/resultados/lognorm.png", 
                  "../solutions/adixans_nahuiolin_1924_lognorm.png"),
                  ]
        errors = []
        for gt_path, st_path in rutas:
            gt = mpimg.imread(gt_path)
            st = mpimg.imread(st_path)

            errors.append(normalized_error(gt, st))

        error_minimo = min(errors)
        assert error_minimo <= .20 # Se tolera una diferencia de 20%

        img_difference = min(errors) * 30
        pytest.total -= img_difference
        with capsys.disabled():
            print("\nTotal especificacion: %d" % (30 - img_difference))
            print("Total final: %d" % (pytest.total))
    except Exception as e:
        print("\nEspecificacion no conseguida :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 30
        raise(e)
