# класс прямоугольника
class Pryamoug:
    def __init__(self, shirina, vysota):
        self.shirina = shirina
        self.vysota = vysota

    def perimetr(self):
        return 'Периметр прямоугольника равен - {}'.format ((self.shirina * 2) + (self.vysota * 2))
    def ploshad(self):
        return 'Площадь прямоугольника  равна - {}'.format(self.shirina * self.vysota)

Param1 = Pryamoug(5, 10)
print('№1 ' + Param1.perimetr())
print('№1 ' + Param1.ploshad())
print('=============================')
Param2 = Pryamoug(6, 11)
print('№2 ' + Param2.perimetr())
print('№2 ' + Param2.ploshad())
print('=============================')
Param3 = Pryamoug(7, 12)
print('№3 ' + Param3.perimetr())
print('№3 ' + Param3.ploshad())

######################
class Match:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self) -> str:
        return 'Результат сложения равен = {}'.format(self.a + self.b)
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a * self.b
    def subtraction(self):
        return self.a / self.b

data = Match(10, 5)
print('Задание 2 ### class Match ### class Match ### class Match ###')
print(data.addition())
print(data.multiplication())
print(data.division())
print(data.subtraction())