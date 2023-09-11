##ii.	Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
##iii.	Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
##iv.	Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type  = type
        self.year = year
    def start(self):
        print('Автомобиль заведен')
    def shutdown(self):
        print('Автомобиль заглушен')
    def god(self):
        print('Год выпуска автомобиля ' + self.year)
    def tip(self):
        print('Тип автомобиля - ' + self.type)
    def tsvet(self):
        print('Цвет автомобиля - ' + self.color)

avto = Car('Blue','Хэтчбек', '2023')

avto.start()
avto.shutdown()
avto.god()
avto.tip()
avto.tsvet()