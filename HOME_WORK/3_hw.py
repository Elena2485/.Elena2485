# Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.

def sravn_2( a: int, b: int):
    return max(a, b)

print (sravn_2(111, 520))


# Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”

c = 100
d = 235
if c-d == 135 or c-d == -135:
    print('Yes')
else:
    print('No')


# Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# название сезона года в консоль (зима, весна, лето, осень)

x = 1

if x > 12:
    print('Некорректный номер месяца!! Введите число меньше 12')
elif x in range(3,6):
    print('весна')
elif x in range(6,9):
    print('лето')
elif x in range(9,12):
    print('осень')
else:
    print('зима')


# Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”

k = 102
l = 22
m = 110

if k > 10 and l > 10 and m > 10:
    print('Yes')
else:
    print('No')


# Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

#spisok_5 = [10, 11, 12, 13, 14]
# for elem in spisok_5
#   > 0
# print spisok_5(elem >0) ## Не получилось в списке сравнить

# Некрасиво, туповато, но работает ###########
n = -21
p = 22
r = 23
s = 24
t = 25

x1 = x2 = x3 = x4 = x5 = 0

if 0 < n:
    x1 = 1
else:
    x1 = 0

if 0 < p:
    x2 = 1
else:
    x2 = 0

if 0 < c:
    x3 = 1
else:
    x3 = 0
if 0 < c:
    x4 = 1
else:
    x4 = 0

if 0 < c:
    x5 = 1
else:
    x5 = 0

print(x1 + x2 + x3 + x4 + x5)

# 7.Функция на вход получает 2 переменные.
# a. Кол-во лет (int), # b.	Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

kol_let = 10
kol_mes = 3
# Kol_dney_v_godu = 12 * 29 * kol_let
# Kol_dney_v_mes = 29 * kol_mes
#def Itog_dney(Kol_dney_v_godu: int, Kol_dney_v_mes: int):

if kol_let >= 0 and kol_mes >= 0:
    Kol_dney_v_godu = 12 * 29 * kol_let
    Kol_dney_v_mes = 29 * kol_mes
    print(Kol_dney_v_godu + Kol_dney_v_mes)
else:
    print('Введите значение')
