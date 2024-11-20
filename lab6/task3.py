def sort_set_elements():
    char_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return sorted(char_set)


print('Відсортований список в алфавітному порядку: ')
sorted_elements = sort_set_elements()
print(sorted_elements)

print("Елементи смножини в алфавітному порядку:")
print(set(sorted_elements))
