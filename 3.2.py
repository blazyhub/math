from sympy import *


x, y = symbols('x y')

u = exp(x) * (x * cos(y) - y * sin(y))
display(u)

dux = diff(u, x)  
duy = diff(u, y)  


uxx = diff(dux, x)  
uyy = diff(duy, y)  


w = uxx + uyy
w1= simplified (w) 

print('Ans :',float(w1))
