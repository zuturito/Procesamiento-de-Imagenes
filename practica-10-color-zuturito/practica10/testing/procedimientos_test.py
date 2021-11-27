import procedimientos as pr
import numpy as np
import pytest

pytest.total = 100

def generar_imagen(a, b, c):
    imagen_test = np.zeros((100, 100, 3), dtype="uint8")
    imagen_test[:,:,0] = a
    imagen_test[:,:,1] = b
    imagen_test[:,:,2] = c
    return imagen_test

def distance(point_1, point_2):
    L1, A1, B1 = point_1 
    L2, A2, B2 = point_2 
    dlab = np.sqrt((L2 - L1)**2 + (A2 - A1)**2 + (B2 - B1)**2)
    return dlab

def test_separar_planos_color():
    try:
        a=63
        b=127
        c=191

        imagen_test = generar_imagen(a, b, c)

        R, G, B = pr.separar_planos_color(imagen_test)
        assert (R.sum() / (100*100)) == a
        assert (G.sum() / (100*100)) == b
        assert (B.sum() / (100*100)) == c
    except Exception as e:
        print("\n La separacion de planos de color es incorrecta :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 15
        raise(e)

def test_integrar_planos_color():
    try:
        a=63
        b=127
        c=191

        imagen_test_gt = generar_imagen(a, b, c)

        R = np.ones((100, 100), dtype="uint8") * a
        G = np.ones((100, 100), dtype="uint8") * b
        B = np.ones((100, 100), dtype="uint8") * c

        imagen_test = pr.integrar_planos_color(R, G, B)
        assert True not in (imagen_test != imagen_test_gt)
    except Exception as e:
        print("\n Composicion de planos de color es incorrecta :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 15
        raise(e)

def test_convertir_a_hsi():
    try:
        imagen_R = generar_imagen(255, 0, 0)
        imagen_G = generar_imagen(0, 255, 0)
        imagen_B = generar_imagen(0, 0, 255)

        imagen_S = generar_imagen(63, 127, 191)
        imagen_I = generar_imagen(63, 63, 63)

        H_R, _, _ = pr.convertir_a_hsi(imagen_R)
        H_G, _, _ = pr.convertir_a_hsi(imagen_G)
        H_B, _, _ = pr.convertir_a_hsi(imagen_B)
        
        assert (H_R.sum() / (100*100)) == 0
        assert (round(np.rad2deg(H_G.sum() / (100*100)))) == 120
        assert (round(np.rad2deg(H_B.sum() / (100*100)))) == 240
        
        _ , S, I = pr.convertir_a_hsi(imagen_S)
        print(int(S.sum()/100))
        assert int(S.sum()/100) == 50
        assert I.sum()/(100*100) == 127
       
        _ , S, I = pr.convertir_a_hsi(imagen_I)
        assert round(S.sum()) == 0
        assert I.sum()/(100*100) == 63
    except Exception as e:
        print("\n Conversion a HSI es incorrecta :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 35
        raise(e)

def test_segmentar():
    try:
        ground_truth = np.load("../resources/imagen_elefante.npz")["gt"]
        solution = np.load("../solutions/imagen_elefante.npz")['solucion']
        R_gt = ground_truth[:, :, 0]
        G_gt = ground_truth[:, :, 1]
        B_gt = ground_truth[:, :, 2]

        gt_point = (R_gt.mean(), G_gt.mean(), B_gt.mean())
        
        R_gt = solution[:, :, 0]
        G_gt = solution[:, :, 1]
        B_gt = solution[:, :, 2]

        sol_point = (R_gt.mean(), G_gt.mean(), B_gt.mean())

        result = distance(gt_point, sol_point)

        # Ample error margin for several segmentation thresholds
        #assert result < 1
        assert result < 1
    except Exception as e:
        print("\n Tu segmentacion no es la esperada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 35
        raise(e)

def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
