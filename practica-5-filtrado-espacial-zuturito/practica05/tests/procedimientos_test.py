import procedimientos as pr
import numpy as np
import pytest

pytest.total = 100

def image_generator():
    row = np.array(range(0, 100))
    imagen = np.copy(row)
    for i in range(99):
        imagen = np.vstack([imagen, np.copy(row)])
    return imagen.astype("uint8")

# Non-linear filters
def test_non_linear():
    try:
        imagen = image_generator()
        
        filtro_3_min = pr.filtro_min(imagen, 3)
        gt_filtro_3_min = np.loadtxt("../resources/gt_filtro_3_min.csv",
                                     dtype="uint8")
        assert (gt_filtro_3_min != filtro_3_min).sum() == 0
        
        filtro_7_med = pr.filtro_mediana(imagen, 7)
        gt_filtro_7_med = np.loadtxt("../resources/gt_filtro_7_med.csv",
                                     dtype="uint8")
        assert (gt_filtro_7_med != filtro_7_med).sum() == 0
    except Exception as e:
        print("\nFiltros no lineales mal implementados :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 20
        raise(e)

# Linear filters
def test_linear():
    try:
        imagen = image_generator()
        k_9_mean = pr.kernel_promedio(9).astype("float16")
        gt_k_9_mean = np.loadtxt("../resources/gt_k_9_mean.csv",
                                 dtype="float16")
        assert (k_9_mean != gt_k_9_mean).sum() == 0

        f_9_boxfilter = pr.convolucion(imagen, k_9_mean, return_type="uint8")
        gt_f_9_boxfilter = np.loadtxt("../resources/gt_f_9_boxfilter.csv",
                                      dtype="uint8")
        assert (f_9_boxfilter != gt_f_9_boxfilter).sum() == 0
        
        k_5_sigma_1_gauss = pr.kernel_gaussiano(5, 1, 1).astype("float16")
        gt_k_5_sigma_1_gauss = np.loadtxt("../resources/gt_k_5_sigma_1_gauss.csv",
                                          dtype="float16")
        assert (k_5_sigma_1_gauss != gt_k_5_sigma_1_gauss).sum() == 0
        
        k_7_sigma_1_gauss = pr.kernel_gaussiano(7, 1, 1).astype("float16")
        gt_k_7_sigma_1_gauss = np.loadtxt("../resources/gt_k_7_sigma_1_gauss.csv",
                                          dtype="float16")
        assert (k_7_sigma_1_gauss != gt_k_7_sigma_1_gauss).sum() == 0

        k_n_sigma_7_gauss = pr.kernel_seis_sigma(1, 7).astype("float16")
        gt_k_n_sigma_7_gauss = np.loadtxt("../resources/gt_k_n_sigma_7_gauss.csv", dtype="float16")
        assert (k_n_sigma_7_gauss != gt_k_n_sigma_7_gauss).sum() == 0
        
        f_7_sigma_1_gauss = pr.convolucion(imagen, k_7_sigma_1_gauss).astype("float16")
        gt_f_7_sigma_1_gauss = np.loadtxt("../resources/gt_f_7_sigma_1_gauss.csv",
                                          dtype="float16")
        assert (f_7_sigma_1_gauss != gt_f_7_sigma_1_gauss).sum() <= 10
    except Exception as e:
        print("\nFiltros lineales mal implementados :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 40
        raise(e)

# Highboost filter
def test_high_boost():
    try:
        imagen = image_generator()
        k_7_sigma_1_gauss = pr.kernel_gaussiano(7, 1, 1)
        k_7_sigma_1_gauss_norm = (1/k_7_sigma_1_gauss.sum()) *\
                k_7_sigma_1_gauss
        f_7_sigma_1_gauss = pr.convolucion(imagen, k_7_sigma_1_gauss_norm, 
                return_type="uint8")
        high_boost = pr.filtro_mascara_borrosa(imagen, f_7_sigma_1_gauss, 1)
        gt_high_boost = np.loadtxt("../resources/gt_high_boost.csv",
                                   dtype="uint8")
        assert (high_boost != gt_high_boost).sum() == 0
    except Exception as e:
        print("\nFiltro de mascara borrosa mal implementado :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 20
        raise(e)

# Derivative filters
def test_derivatives():
    try:
        imagen = image_generator()
        
        f_sobel = pr.gradiente_sobel(imagen).astype("float16")
        gt_f_sobel = np.loadtxt("../resources/gt_f_sobel.csv",
                                dtype="float16")
        assert (f_sobel != gt_f_sobel).sum() == 0
        
        f_laplace = pr.laplaciano(imagen).astype("int32")
        gt_f_laplace = np.loadtxt("../resources/gt_f_laplace.csv",
                                  dtype="int32")
        assert (f_laplace != gt_f_laplace).sum() == 0
    except Exception as e:
        print("\nOperadores derivativos mal implementados :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 20
        raise(e)
    
def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
