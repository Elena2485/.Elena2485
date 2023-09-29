####c.	наследуйте все классы от класса Checks
####i.	чтобы использовать класс из другого файла его нужно импортировать
#### from название файла(без расширения) import название класса
####d.	переделайте все 4 класса в файле task_9_oop_1.py так чтоб
####    в объектах можно было использовать методы родительского класса
####e.	распечатайте в консоль результаты метода .check_text() вызванного
# от каждого объекта классов файла task_9_oop_1.py
class Checks:
    def __init__(self, loc):
        self.loc  = loc

    def check_text(self):
        return self.loc

#   from Python_training.task_9_oop import Input(Checks)
    def __init__(self, loc, text):
        super().__init__(text)
            self.loc = ''
            self.text = 'text'


txt = Checks(' ', ' из файла task_9_oop_1')
#txt = Checks(Input())
txt.check_text()
#.check_text()

