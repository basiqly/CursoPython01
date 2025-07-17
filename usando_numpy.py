import numpy as np

#Criar um array numpy (vector)
arr = np.array([1, 2, 3, 4, 5 ])
print('Array do Numpy')

#Operações matematicas usando os arrays
print('\n Array multiplicado por 2')
print(arr * 2)

#Operações entre dois arrays
arr2 = np.array([10, 20, 30, 40, 50])
print('\n Soma entre dois arrays')
print(arr + arr2)

#Criar uma matriz (2d)
matriz = np.array([[1, 2, 3], [4, 5, 6 ]])
print('\n Matrix 2x3')
print(matriz)


#Somar elementos da matriz
print('\n Soma de todos os elementos da matriz')
print(np.sum(matriz))

#Media dos dados da matriz
print('\n Media dos elementos da matriz')
print(np.mean(matriz))

#Transposta da Matriz
print('\n Matriz transporta')
print(matriz.T)

#Gerar valores aleatorios
print('\n Numeros aleatorios entre 0 a 1')
print(np.random.rand(3,3)) #gera uma matriz de 3x3 com valores aleatorios entre 0 e 1
