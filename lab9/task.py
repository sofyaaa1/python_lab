import re


def create_file(filename):
    try:
        with open(filename, 'w') as file:
            lines = [
                "Текст з числами: 123 4567 і 89.",
                "ще текст 123456789.",
                "рядок без чисел",
                "Знову 12 числа 34567 890."
            ]
            for line in lines:
                file.write(line + "\n")
        print(f"Файл '{filename}' створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")


def extract(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            numbers = re.findall(r'\d{3,}', content)
            with open(output_filename, 'w') as output_file:
                output_file.write(' '.join(numbers))
        print(f"Числа з файлу '{input_filename}' записано у файл '{output_filename}'.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")



input_file = 'TF2_1.txt'
output_file = 'TF2_2.txt'

create_file(input_file)
extract(input_file, output_file)
