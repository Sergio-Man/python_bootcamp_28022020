from mathematica.geometry.figures import square_area, triangle_area

def test_square_area():
    assert square_area(4) == 16
    assert square_area(3) == 9

def test_triangle_area():
    assert triangle_area(10, 6) == 30
    assert triangle_area(4, 8) == 16