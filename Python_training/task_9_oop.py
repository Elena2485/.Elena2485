class Button:

    type: str = 'Кнопка'
    def __init__(self, text, link):
        self.text = text
        self.link = link

 # создаем экземпляры класса
home = Button( 'Домой' , '/home')
catalog_msk = Button('Каталог ', '/msk/catalog')

# Получаем доступ к атрибутам

print(home.text)
print(home.type)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print(catalog_msk.type)
print('Кнопка ' + catalog_msk.text + 'имеет ссылку ' + catalog_msk.link)

#########################################
class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc  = loc

    def click(self):
        return 'Клик по локатору  - {}'.format(self.loc) #self.loc будет передана в фигурные скобки

# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')
# вызываем метод
print(home_two.click())
