f = int(input("Выберите функцию:\n1-Транспонирование матрицы\n2-Умножение матриц \n3-Определение ранга матрицы\n"))
#Транспонирование матрицы
if f == 1:
    print("Выберите размер матрицы из предложенных:1x2, 2x1, 1x3, 3x1, 2x2, 3x3:")
    n = int(input("Введите кол-во строк:")) #строка
    m = int(input("Введите кол-во столбцов:")) #столбец
    print(n,"x",m)
    A = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
            A[i][j]=int(input())
    for i in (A):
        print(i)
    transp = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    print("Транспонированная матрица:" )
    for i in (transp):
        print(i)
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
#умножение
    C = [[0]*m1 for i in range(n)]
    for i in range(n):
        for j in range(m1):
            for a in range(n1):
                C[i][j] += A[i][a] * B[a][j]
    print("Результат умножения матрицы А на матрицу В:")
    for i in (C):
        print(i)
#Определение ранга матрицы
if f == 3:
    print("Выберите размер матрицы из предложенных:2x2, 3x3:")
    n = int(input("Введите кол-во строк:"))
    m = int(input("Введите кол-во столбцов:"))
    print(n,"x",m)
    A = [[0 for i in range (m)] for j in range (n)]
    for i in range(n):
        for j in range(m):
            print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
            A[i][j]=int(input())
    for i in (A):
        print(i)
    #для матрицы 2х2
    if n == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        if A[0][0] == 0 and A[0][1] == 0 and A[1][0] == 0 and A[1][1] == 0:
            print("Ранг матрицы = 0.")
        elif det == 0:
            print("Ранг матрицы = 1")
        else:
            print("Ранг матрицы = 2")
    #для матрицы 3х3
    if n == 3:
        summ = 0
        det = (A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[1][0]*A[2][1]*A[0][2]) - (A[0][2]*A[1][1]*A[2][0] + A[0][1]*A[1][0]*A[2][2] + A[1][2]*A[2][1]*A[0][0])
        for i in range(n):
            for j in range(m):
                summ += A[i][j]
        if summ == 0:
            print("Ранг матрицы = 0.")
        elif det == 0:
            def det2(A):
                return A[0][0] * A[1][1] - A[0][1] * A[1][0]

            def minor(A, i, j):
                tmp = [row for k, row in enumerate(A) if k != i]
                tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
                return tmp

            om = []
            for i in range(3):
                for j in range(3):
                    om += [det2(minor(A,i,j))]
            if om[0]!=0 or om[1]!=0 or om[2]!=0 or om[3]!=0 or om[4]!=0 or om[5]!=0 or om[6]!=0 or om[7]!=0 or om[8]!=0:
                c=1
            else:
                c = 0
            if c == 1:
                print("Ранг матрицы = 2.")
            if c == 0:
                print("Ранг матрицы = 1.")
        else:
            print("Ранг матрицы = 3.")
