#Обратная матрица
def Ad(matrix): #алгебраическое дополнение
    return ((-1)**(i+j))*(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

def minor(matrix, i, j): #минор
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp

print("Ввод элементов матрицы 3x3:")
A = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        print("Введите элемент матрицы А с индексом ", i+1,j+1,":", end='')
        A[i][j]=int(input())
for i in (A):
    print(i)
det = (A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[1][0]*A[2][1]*A[0][2]) - (A[0][2]*A[1][1]*A[2][0] + A[0][1]*A[1][0]*A[2][2] + A[1][2]*A[2][1]*A[0][0])
if det == 0:
    print("Обратной матрицы не существует, т.к. определитель равен нулю.")
else:
    om=[]
    for i in range(3):
        for j in range(3):
            om+=[(Ad(minor(A,i,j)))/det]
    a1=[om[0],om[1],om[2]]
    a2=[om[3],om[4],om[5]]
    a3=[om[6],om[7],om[8]]
    As=[a1,a2,a3]
    transp = [[As[i][j] for i in range(len(As))] for j in range(len(As[0]))]
    print("Обратная матрица:" )
    for i in (transp):
        print(i)
