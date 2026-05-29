x = 5
y = 2 * x + 5

print(y)

S C:\Users\uberp> python
Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> x = 5
>>> y = 2 * x + 5
>>> print(y)
15
>>> passed = 8
>>> total = 10
>>> probability = passed/total
>>> print(probability)
0.8
>>> import numpy as np
>>> 
>>> scores = [70, 80, 90]
>>> 
>>> print(np.mean(scores))
80.0
>>> import numpy as np
>>> 
>>> v = np.array([1, 2, 3])
>>> 
>>> print(v)
[1 2 3]
>>> w = np.array([2, 1, 3])
>>> x = np.array([4, 5, 6])
>>> 
>>> print(np.dot(w, x))
31
>>> def f(x):
...     return x**2
... 
>>> x = 3
>>> h = 0.001
>>> 
>>> derivative = (f(x + h) - f(x)) / h
>>> 
>>> print(derivative)
6.000999999999479
>>> for x in range(5):
...     y = x ** 2
...     print(x, y)
... 
0 0
1 1
2 4
3 9
4 16
>>> 