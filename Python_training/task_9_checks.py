####c.	наследуйте все классы от класса Checks
####i.	чтобы использовать класс из другого файла его нужно импортировать
#### from название файла(без расширения) import название класса
####d.	переделайте все 4 класса в файле task_9_oop_1.py так чтоб
####    в объектах можно было использовать методы родительского класса
####e.	распечатайте в консоль результаты метода .check_text() вызванного
# от каждого объекта классов файла task_9_oop_1.py
class Checks:
    def __init__(self, loc, text):
        self.loc  = loc
        self.text = text
#from task_9_oop_1 import Input()
    def check_text(self):
        print(self.loc + ' ' + self.text)


txt = Checks('ДЗ №4 Классы', 'Не получилось вытащить class из файла task_9_oop_1')
#txt = Checks(Input())
txt.check_text()

