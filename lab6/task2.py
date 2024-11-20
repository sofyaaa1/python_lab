def search_element():
    user_input = input("Введіть числові елементи списку, розділені пробілом: ")
    lst = list(map(int, user_input.split()))
    target = int(input("Введіть число для пошуку: "))

    try:
        index = lst.index(target)
        print('Індекс вашого елементy:', index)
    except ValueError:
        print('Елемент не знайдено')


search_element()
