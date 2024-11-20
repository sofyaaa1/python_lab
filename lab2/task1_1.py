import math
from mod import newfunc_2


def func_1(a):
    z = math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a)

    print("Значення z =", z)


def func_2(n):
    y = 1
    for i in range(1, n + 1):
        y *= (2 * i - 1)

    print("Значення y =", y)


a = float(input("Введіть значення α (в радіанах): "))
func_1(a)

n = int(input("Введіть натуральне число n: "))

func_2(n)
print('Результат до другого завдання: ')
newfunc_2(n)
