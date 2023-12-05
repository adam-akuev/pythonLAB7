import random

try:
    n = int(input('Введите количество чисел в массиве: '))
    m = int(input('Введите количество массивов: '))
    matrix = [[random.randint(-100, 100) for k in range(n)] for g in range(m)]
    k = [[matrisa_k[i] for matrisa_k in matrix] for i in range(len(matrix[0]))]
    print(matrix)
    print(f'Транспонированный список: {k}')
except ValueError:
    print("Введите 1 число в каждом пункте!!!")
