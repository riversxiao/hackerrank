import numpy

my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)

import numpy

my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

import numpy as np
n,m=map(int, input().split())
matrix = np.array([list(map(int,input().split())) for i in range(n)])
t = np.min(matrix,axis=1)
g = np.max(t,)
print (g)
