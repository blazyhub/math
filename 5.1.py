from sympy import symbols, Function, Derivative, dsolve, Eq, init_printing

init_printing()


t, r = symbols('t r')
P = Function('P')(t)  
C1 = symbols('C1')  

print("\nDifferential Equation:")
DE1 = Eq(Derivative(P, t), r) 
display(DE1)


print("\nGeneral Solution:")
GS1 = dsolve(DE1)  
display(GS1)

print("\nParticular Solution:")
PS1 = GS1.subs({C1: 2})  
display(PS1)
