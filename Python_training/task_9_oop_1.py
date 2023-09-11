class Input:

        def __init__(self, loc, text):
            self.loc = loc
            self.text = text

search = Input ('Произвольный текст 1 ', '/Input1' )
print(search.loc, search.text)
####################################
class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search2 = Input('Произвольный текст 2 ', '/Button2')
print(search2.loc, search2.text)
#####################################
class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search3 = Title('Произвольный текст 3 ', '/Title3')
print(search3.loc, search3.text)
#####################
class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search4 = Link('Произвольный текст 4 ', '/Link4')
print(search4.loc, search4.text)