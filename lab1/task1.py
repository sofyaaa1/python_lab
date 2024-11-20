a = int(input('enter a: '))
b = int(input('enter b: '))

if a > 0 and b > 0:
    if a > b:
        print(a * b - 3)
    elif a == b:
        print(2)
    else:
        print((a ** 3 + 1) / b)
else:
    print("користувач не повинен вводити від'ємні числа")