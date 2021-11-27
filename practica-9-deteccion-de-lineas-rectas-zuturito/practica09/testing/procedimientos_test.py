import procedimientos as pr
import numpy as np
import pytest

pytest.total = 100

def test_segmentacion_de_notas():
    try:
        ground_truth = np.load("../resources/notas_gt.npz")["gt"]
        solution = np.load("../solutions/notas_encontradas.npz")['solucion']
        total_notes = ground_truth.size 

        # Checamos traslape simple
        matched = ground_truth == solution
        matched_total = ground_truth[matched].size
    
        # Aciertos / total
        percentage = matched_total / total_notes
        pytest.total = int(percentage*100)

        assert pytest.total >= 70
    except Exception as e:
        print("\n No es suficiente para pasar :(")
        print(type(e).__name__, ":" , e)
        raise(e)

def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
