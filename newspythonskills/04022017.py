#map function
from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

#map function 2 self define
from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(map(func,x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

###python little dirty secret
#python2
>>> x = "This value will be changed in the list comprehension"
>>> res = [x for x in range(3)]
>>> res
[0, 1, 2]
>>> x
2
>>> res = [i for i in range(5)]
>>> i
4
>>>
#python3
Python 3.2 (r32:88445, Mar 25 2011, 19:28:28)
[GCC 4.5.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> x = "Python 3 fixed the dirty little secret"
>>> res = [x for x in range(3)]
>>> print(res)
[0, 1, 2]
>>> x
'Python 3 fixed the dirty little secret'
>>>

map(f,s) equal to [f(x) fir x in S]

filter(P,S) equal to [x for x in S if P(x)]
