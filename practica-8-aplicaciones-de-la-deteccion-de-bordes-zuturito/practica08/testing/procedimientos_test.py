import procedimientos as pr
import numpy as np
import pytest
import zipfile

from auxiliar import cargar_imagen

pytest.total = 100

def test_segmentacion_de_notas():
    try:
        ground_truth = np.load("../resources/balleto_ponce_gt.npz")["gt"]
        connected_components = np.load("../solutions/notas_encontradas.npz")['solucion']
        expected_positives = 173 

        found_labels = np.unique(
                connected_components[connected_components != 0]).size
       
        # Verdaderos positivos son los que traslapan
        overlapping = connected_components * ground_truth
        true_positives = np.unique(overlapping[overlapping != 0]).size
        true_positives = min(expected_positives, true_positives)
        
        # Falsos positivos son los que encontraron que no traslapan
        false_positives = found_labels - true_positives
        
        # Falsos negativos son los que no encontraron
        false_negatives = expected_positives - true_positives

        # Calculamos la metrica f1
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1_score = 2 * ((precision * recall) / (precision + recall))
        
        pytest.total = int(f1_score * 100)

        assert f1_score * 100 >= 70
    except ZeroDivisionError as e:
        print("\n No es suficiente para pasar :(")
        print(type(e).__name__, ":" , e)
        pytest.total = 0.
        raise(e)
    except Exception as e:
        print("\n No es suficiente para pasar :(")
        print(type(e).__name__, ":" , e)
        raise(e)

def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
