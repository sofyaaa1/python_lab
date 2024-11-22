import numpy as np

import matplotlib.pyplot as plt

x = np.array([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])

y = np.array([3091927, 295091, 2814709, 2687929, 2565898, 2453879, 2357852, 2280979, 2229030, 2202166, 2201728])

z = np.array([24218918, 24221628, 24239361, 24268279, 24340251, 24305423, 24315924, 24319872, 24255493, 24238820, 24255391])


plt.plot(x, z, label='USA', color="purple")

plt.plot(x, y, label='Ukraine', color="yellow")

plt.title('Population of compulsory school age, female (number)', fontsize=15)

plt.xlabel('Year', fontsize=12, color='red')

plt.ylabel('Indicator', fontsize=12, color='red')

plt.legend()

plt.grid(True)

plt.show()

plt.bar(x, z, color='red')

plt.bar(x, y, color='blue')
plt.title('Стовпчаста діаграма для України та США: Population of compulsory school age, female (number)')
plt.xlabel('Year')
plt.ylabel('Indicator')


plt.show()