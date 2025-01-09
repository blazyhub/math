import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001)


y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, label='sin(x)', color='blue')  
plt.plot(x, y2, label='cos(x)', color='red')   


plt.title("Sine and Cosine Curves")
plt.xlabel("Values of x")
plt.ylabel("Values of sin(x) and cos(x)")

plt.grid()
plt.legend()


plt.show()
