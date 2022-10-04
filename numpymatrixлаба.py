import numpy as np
f=int(input("Выберите функцию:\n1-Транспонирование матрицы\n2-Умножение матриц \n3-Определение ранга матрицы\n"))
#Транспонирование матрицы
if f == 1:
    print("Выберите размер матрицы из предложенных:1x2, 2x1, 1x3, 3x1, 2x2, 3x3:")
    n = int(input("Введите кол-во строк:")) #строка
    m = int(input("Введите кол-во столбцов:")) #столбец
    print(n,"x",m)
    A=[[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
            A[i][j]=int(input())
    for i in (A):
        print(i)
    A=np.array(A)
    print("Транспонированная матрица:" )
    print(A.transpose())
#Умножение матриц
if f == 2:
    print("Выберите размер матрицы A из предложенных:1x2, 2x1, 1x3, 3x1, 2x2, 3x3:")
    n = int(input("Введите кол-во строк:")) #строка
    m = int(input("Введите кол-во столбцов:")) #столбец
    print(n,"x",m)
    #первая матрица
    A=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
            A[i][j]=int(input())
    for i in (A):
        print(i)
#вторая матрица
    print("Число строк матрицы В будет автоматически равно числу столбцов матрицы А,т.к. эти два числа должны быть равны, иначе умножение будет невозможным. \nВведите кол-во столбцов матрицы В.")
    n1 = m
    m1 = int(input("Введите кол-во столбцов:")) #столбец
    print(n1,"x",m1)
    B = [[0 for i in range(m1)] for j in range(n1)]
    for i in range(n1):
        for j in range(m1):
            print("Введите элемент матрицы B с индексом ", i+1,j+1,":", end='')
            B[i][j]=int(input())
    for i in (B):
        print(i)
    A=np.array(A)
    B=np.array(B)
    C=A.dot(B)
    print("Результат умножения матрицы А на матрицу В:")
    print(C)
#Определение ранга матрицы
if f == 3:
    print("Выберите размер матрицы из предложенных:2x2, 3x3:")
    n = int(input("Введите кол-во строк:")) #строка
    m = int(input("Введите кол-во столбцов:")) #столбец
    print(n,"x",m)
    A=[[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
            A[i][j]=int(input())
    for i in (A):
        print(i)
    A=np.array(A)
    rang = np.linalg.matrix_rank(A)
    print(rang)
