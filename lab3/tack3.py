text = input("Введіть речення: ")

words = text.split()

for i in words:
    if i.lower() != 'привіт':
        print(i, end=' ')
