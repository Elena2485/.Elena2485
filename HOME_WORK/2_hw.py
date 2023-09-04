def task_1(f: int, j: float, x: list, y: str, k: bool) -> bool:
    return  f * j and 'x' + 'y' and k
print(task_1(8, 3.14, ['Название', ' дерева', ' на английском:'], 'Tree', True))

#############  task_2 ########################
a = [1, 2, 3, 5, 8, 13, 21] #числа Фиббоначчи
def task_2(a: list) -> list:
    return a[0:3]
print(task_2(a))
##############  task_3 #########################
def task_3(a: int):
    return a**2
print(task_3(3))


