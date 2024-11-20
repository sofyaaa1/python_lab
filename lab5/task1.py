n = int(input("Введіть довжину масиву: "))

mylist = []

for i in range(n):
    element = int(input(f"Введіть елемент {i + 1}: "))
    mylist.append(element)

max_element = mylist[0]
for i in mylist:
    if i > max_element:
        max_element = i

print("Максимальний елемент масиву:", max_element)
