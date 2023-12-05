import random

try:
    n = int(input('Введите количество чисел в массиве: '))
    m = int(input('Введите количество массивов: '))
    matrix = [[random.randint(-100, 100) for k in range(n)] for g in range(m)]
    matrix_2 = [[matrix[i]] for i in range(1, m, 2)]
    if n<0 or m<0:
        matrix=[]
        matrix_2=[]
    print(f'Рандомный список:{matrix}')
    print(f'Массив на четном строке:{matrix_2}')
except ValueError:
    print("Введите 1 число в каждом пункте!!!")