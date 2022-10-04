#Обратная матрица c numpy
import numpy as np
print("Ввод элементов матрицы 3x3:")
A = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
        A[i][j]=int(input())
for i in (A):
    print(i)
det=np.linalg.det(A)
if det == 0:
    print("Обратной матрицы не существует, т.к. определитель равен нулю.")
else:
    ObM=np.linalg.inv(A)
    print(ObM)
