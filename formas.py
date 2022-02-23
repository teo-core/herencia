from math import pi

class RadioError(Exception):
    pass

class Forma():
    #PI = 3.1415
    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self) -> str:
        return type(self).__name__
    
class Circulo(Forma):
    def __init__(self, radio) -> None:
        if type(radio) in (int,float) and radio >= 0:
            self.__radio = radio
        else:
            raise RadioError('El radio debe ser un número positivo')

    def area(self):
        return pi * self.__radio * self.__radio
    
    def perimetro(self):
        return 2 * pi * self.__radio

class Rectangulo(Forma):
    def __init__(self, base, altura) -> None:
        self.__base = base
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura
    
    def perimetro(self):
        return 2 * (self.__base + self.__altura)

class Cuadrado(Rectangulo):
    def __init__(self, lado) -> None:
        super().__init__(lado,lado)

        