import unittest
from formas import Circulo, Cuadrado, Forma, RadioError
from math import pi

class TestFormas(unittest.TestCase):
    def test_existencia_formas(self):
        f = Forma()
        self.assertIsNotNone(f)
    
    def test_nombre_forma(self):
        f = Forma()
        self.assertEqual(f.__str__(),'Forma')

class TestCirculo(unittest.TestCase):
    def test_existe_circulo(self):
        c = Circulo(1)
        self.assertIsNotNone(c)

    def test_circulo_radio1_perimetro_2pi(self):
        c = Circulo(1)
        peri = c.perimetro()
        self.assertEqual(peri,2*pi)
    
    def test_radio_negativo_da_error(self):
        with self.assertRaises(RadioError):
            c = Circulo(-1)

class TestCuadrado(unittest.TestCase):
    def test_lado_1_perimetro_4(self):
        c = Cuadrado(1)
        peri = c.perimetro()
        self.assertEqual(peri,4)
    
    def test_area_lado_1_1(self):
        c = Cuadrado(1)
        a = c.area()
        self.assertEqual(a,1)