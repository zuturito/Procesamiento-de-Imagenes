import procedimientos as pr
import numpy as np
import pytest

pytest.total = 100

def image_generator(size, center_value, border_value):
    '''Generates: 

    border_img: a squared image with center_value intensity pixels, 
    surrounded by a border of border_value intensity pixels. 
    
    ramp: a 255 intensity ramp.
    '''
    assert size % 4 == 0
    central_square = np.ones((int(size/2), int(size/2))) * center_value
    border_img = np.pad(central_square, int(size/4), mode="constant", constant_values=border_value).astype("uint8")

    ramp = np.array(range(256))
    for i in range(256):
        ramp = np.vstack([ramp, np.array(range(256))])
    ramp = ramp.astype("uint8")
    return border_img, ramp

def test_umbralizacion_global():
    '''if the function is correct, should return
    (400/2)**2 ones (number of 191-intensity pixels)'''
    try:
        b_img, _ = image_generator(400, 191, 63)
        assert pr.umbralizacion_global(b_img, 127).sum() == 40000
    except Exception as e:
        print("\nFuncion de umbral global mal implementada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 10
        raise(e)

def test_metodo_otsu():
    '''if the function is correct it should return
    a very certain threshold for b_img (it is very separable, thus 
    eta_b>eta_r) and Otsu's candidates would be ALL numbers between 
    63 and 190 (exactly the same interclass variance). 

    Moreover, if Otsu is correct r_img should be exactly in the middle,
    thus 127 (it is a uniform intenisty ramp, so the maximum interclass 
    variance would be obtained by cutting it in half).'''
    try:
        b_img, r_img = image_generator(400, 191, 63)
        T_otsu_b, eta_b = pr.metodo_otsu(b_img)
        T_otsu_r, eta_r = pr.metodo_otsu(r_img)
        
        assert T_otsu_b == 63
        assert T_otsu_r == 127
        assert eta_b > eta_r
    except Exception as e:
        print("\nMetodo de Otsu mal implementado :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 30
        raise(e)

def test_umbralizacion_adaptiva():
    '''The adaptive threshold should only find differences in
    the square's borders and corners. Each border is of size 
    400/2=200. Plus 4 corners, we have:

        (200*4 + 4)'''
    try:
        b_img, _ = image_generator(400, 191, 63)
        b_img_t = pr.umbralizacion_adaptiva(b_img, 3, 2, 1)

        assert (b_img_t == False).sum() == (200*4 + 4)
    except Exception as e:
        print("\nUmbral adaptivo mal implementado :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 30
        raise(e)

def test_umbralizacion_mascara():
    '''The Sobel operator will find and duplicate the square's borders 
    (it considers change in both sides). Thus, for the top percentiles, 
    the mask should be of size:
    
    200*2*4

    This will recover both 63 and 191 pixels in about the same 
    proportion as the original b_img (though, not exactly the same). 
    Thus, the Otsu threshold should be in the same 63-190 interval with 
    high eta.
    '''
    try:
        b_img, _ = image_generator(400, 191, 63)
        b_mask = pr.mascara_de_umbralizacion_gradiente(b_img, 99)
        
        assert b_mask.sum() == (200*2*4)
        
        T_otsu_mask_b, _ = pr.metodo_otsu(b_mask * b_img)

        assert T_otsu_mask_b == 63
    except Exception as e:
        print("\nMascara de umbralizacion mal calculada :(")
        print(type(e).__name__, ":" , e)
        pytest.total -= 30
        raise(e)

def test_grade(capsys):
    with capsys.disabled():
        print("Total final: %d" % (pytest.total))
