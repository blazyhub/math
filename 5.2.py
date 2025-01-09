from sympy import symbols, Function, Derivative, dsolve, Eq, tan, sec, display


x = symbols('x')
y = Function('y')(x)

y1 = Derivative(y, x)

z1 = dsolve(Eq(y1 + y * tan(x) - y**3 * sec(x), 0), y)
display(z1)
