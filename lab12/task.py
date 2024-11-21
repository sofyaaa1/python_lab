import json


employees = [
    {"surname": "Іванов", "address": "вул. Шевченка, 10", "position": "менеджер"},
    {"surname": "Петренко", "address": "вул. Грушевського, 15", "position": "директор"},
    {"surname": "Сидоров", "address": "вул. Франка, 7", "position": "аналітик"},
    {"surname": "Коваленко", "address": "вул. Лесі Українки, 20", "position": "програміст"},
    {"surname": "Мельник", "address": "вул. Кобзаря, 8", "position": "маркетолог"},
    {"surname": "Шевченко", "address": "вул. Леніна, 5", "position": "економіст"},
    {"surname": "Коваль", "address": "вул. Червоноармійська, 3", "position": "бухгалтер"},
    {"surname": "Гречко", "address": "вул. Довженка, 11", "position": "системний адміністратор"},
    {"surname": "Кузьменко", "address": "вул. Пушкина, 2", "position": "технік"},
    {"surname": "Тимошенко", "address": "вул. Пирогова, 18", "position": "юрист"}
]


def write_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def display_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(json.dumps(data, ensure_ascii=False, indent=4))
    except FileNotFoundError:
        print("Файл не знайдено!")


def add_employee(filename):
    surname = input("Введіть прізвище: ")
    address = input("Введіть адресу: ")
    position = input("Введіть посаду: ")
    new_employee = {"surname": surname, "address": address, "position": position}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(new_employee)
    write_to_json(filename, data)
    print("Новий співробітник доданий!")


def delete_employee(filename):
    surname = input("Введіть прізвище співробітника, якого потрібно видалити: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return

    data = [employee for employee in data if employee["surname"] != surname]
    write_to_json(filename, data)
    print(f"Співробітник {surname} видалений!")


def search_by_letter(filename):
    letter = input("Введіть літеру для пошуку прізвищ: ").lower()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return

    found = False
    for employee in data:
        if employee["surname"][0].lower() == letter:
            print(f"Прізвище: {employee['surname']}, Адреса: {employee['address']}, Посада: {employee['position']}")
            found = True

    if not found:
        print(f"Співробітників з прізвищем на літеру '{letter.upper()}' не знайдено.")


if __name__ == "__main__":
    write_to_json("employees.json", employees)  # Запис початкових даних у файл
    filename = "employees.json"

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати нового співробітника")
        print("3. Видалити співробітника")
        print("4. Пошук співробітників за першою літерою прізвища")
        print("5. Вихід")

        choice = input("Виберіть дію (1-5): ")

        if choice == '1':
            display_json(filename)
        elif choice == '2':
            add_employee(filename)
        elif choice == '3':
            delete_employee(filename)
        elif choice == '4':
            search_by_letter(filename)
        elif choice == '5':
            break
        else:
            print("Невірний вибір, спробуйте знову.")
