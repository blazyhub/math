from sympy import symbols, Function, Derivative, dsolve, Eq, cos, display

x = symbols('x')
y = Function('y')(x)

y1 = Derivative(y, x)

z1 = dsolve(Eq(x**3 * y1 - x**2 * y + y**4 * cos(x), 0), y)
display(z1)
