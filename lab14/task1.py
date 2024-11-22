import numpy as np
import matplotlib.pyplot as plt


def Y(x):
    return (1 / x) * np.sin(5 * x)


x = np.linspace(-5, 5, 400)

y = Y(x)

plt.plot(x, y, linestyle='-', color='b', linewidth=2, label=r'$Y(x) = \frac{1}{x} \sin(5x)$')

plt.xlabel('x')
plt.ylabel('Y(x)')

plt.title('Y(x) = 1/x * sin(5x)')

plt.legend()

plt.grid(True)
plt.show()

