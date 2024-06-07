import numpy as np
#le dimensões da matriz
nl = int(input('Informe o numero de linhas: '))
nc = int(input('Informe o numero de colunas: '))

#cria a matriz
A = np.empty((nl, nc))

#le do teclado
for i in range(0, nl): #linhas vao de 0 a nl-1
    for j in range(0, nc): #colunas vão de 0 a nc-1
        s= 'Informe o elemento A[%d] [%d]: ' % (i, j)
        A[i][j] = float(input(s))

print("Imprime Matriz...")
for i in range(0, nl):
    for j in range(0, nc):
        print('%5.1f' % (A[i][j]), end='')
    print() #imprime quebra de linha