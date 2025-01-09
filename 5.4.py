import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(y, t):
    k = 0.3
    dydt = -k * y
    return dydt


y0 = 5

t = np.linspace(0, 20, 100)  


y = odeint(model, y0, t)

plt.plot(t, y)
plt.title('Solution of dy/dt = -ky; k = 0.3, y(0) = 5')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.grid()
plt.show()
