def newinsert():
    user_input = input("Введіть елементи списку, розділені пробілом: ")
    lst = user_input.split()
    new_element = input("Введіть новий елемент для вставки: ")
    target_element = input("Введіть елемент перед яким потрібно вставити новий: ")
    try:
        index = lst.index(target_element)
        lst.insert(index, new_element)
        print(lst)
    except ValueError:
        print(f"Елемент '{target_element}' не знайдено у списку.")


newinsert()
