from procedimientos import *
import numpy as np
import random
import pytest

pytest.total = 100

def inverse_normalized_error(g_truth, proposed_solution):
    '''1 if eq; 0 if completely diff'''
    try:
        total = g_truth.size * 255
        sum_of_diff = abs((g_truth - proposed_solution)).sum()
    except Exception as e:
        print(type(e).__name__, ":" , e)
        return 0.
    return 1. - sum_of_diff/total

def test_transformaciones_simples():
    try:
        gt_table_gamma_dist = np.loadtxt("../resources/gamma_2_punto_5.csv")
        gt_table_gamma_corr = np.loadtxt("../resources/gamma_1_entre_2_punto_5.csv")
        gt_table_inv = np.loadtxt("../resources/inv.csv")
        gt_table_log = np.loadtxt("../resources/log.csv")
        
        gamma_dist_table = construir_tabla_t_gamma(2.5, 1)
        gamma_corr_table = construir_tabla_t_gamma(1/2.5, 1)
        inv_table = construir_tabla_t_inv()
        log_table = construir_tabla_t_log(1)

        assert inverse_normalized_error(gt_table_gamma_dist, gamma_dist_table) == 1.
        assert inverse_normalized_error(gt_table_gamma_corr, gamma_corr_table) == 1.
        assert inverse_normalized_error(gt_table_inv, inv_table) == 1.
        assert inverse_normalized_error(gt_table_log, log_table) == 1.
    except Exception as e:
        pytest.total -= 30
        print("Falla construir tablas de busqueda: -30%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)

def test_mapeo():
    try:
        test_table = np.zeros(256, dtype="uint8")
        test_img = np.ones((100, 100), dtype="uint8") * 255

        transformation = mapeo(test_img, test_table)

        assert transformation.sum() == 0
    except Exception as e:
        pytest.total -= 30
        print("Falla mapear pixeles mediante tablas de busqueda: -30%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)

def test_compression():
    try:
        test_img = np.ones((100, 100), dtype="uint8") * 255
        result = comprimir(test_img) - 240
        assert result.sum() == 0
        
        test_img = np.ones((100, 100), dtype="uint8") * 15
        result = comprimir(test_img)
        assert result.sum() == 0
    except Exception as e:
        pytest.total -= 40
        print("Falla separar y recomponer planos de bits: -40%")
        print("Total actual: %d/100" % pytest.total)
        raise(e)
