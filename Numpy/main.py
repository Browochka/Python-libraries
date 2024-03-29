from typing import Any
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#a=np.arange(0,26,5)

#e=np.array([2,3,4,6,9,1])

#a=np.sqrt(a) #корень

#b=np.linspace(0,50,5)

#c=np.random.random((5))

#d=(10-5)*np.random.random_sample((5)) + 5  #числа в диапазоне [5;10]

#f=np.random.randint(5,10,8)

# np.insert -вставить значение

#j=np.array([1,2,3,4,5,10,15,3,2,11])
#print(j[(j>5) & (j < 12)])

"МАТРИЦЫ"

matrix=np.array([[(1,2,3)],[(3,3,3)]],dtype=np.float64)
#secomatrix=np.array([(1,2,3),(3,3,3)],dtype=np.float64)
#matrix.shape-указывает размерность
#reshape- транспонирует, объединяет
#np.eye(5) единичная матрица NxN
print(matrix.reshape(3,2))

