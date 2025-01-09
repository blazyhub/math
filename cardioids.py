import numpy as np
import matplotlib.pyplot as plt
import math
plt.axes(projection='polar')


a = 3
rad = np.arange(0, 2 * np.pi, 0.01)


for i in rad:
    r = a + (a * np.cos(i))  
    plt.polar(i, r, 'g.')  

    r1 = a - (a * np.cos(i))
    plt.polar(i, r1, 'r.')  


plt.show()
