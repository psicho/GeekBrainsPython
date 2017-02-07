# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def height(self):
        h = str(abs(self.b[0] - self.a[0]))
        return 'Высота треугольника: ' + h + ' метр'

    def perim(self):
        ab = sqrt((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2)
        bc = sqrt((self.b[0] - self.c[0])**2 + (self.b[1] - self.c[1])**2)
        ac = sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2)
        p = ab + bc + ac
        return 'Периметр треугольника: ' + str(p)

    def area(self):
        h1 = abs(self.b[0] - self.a[0])
        ac1 = sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2)
        s = 1/2 * h1 * ac1
        return s

a = (1, 1)
b = (2, 2)
c = (1, 2)

Triangle1 = Triangle(a, b, c)


print(Triangle1.height())
print(Triangle1.perim())
print(Triangle1.area())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

