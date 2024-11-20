def check_all(employees):
    if not employees:
        print("Словник порожній.")
    else:
        print("Записи співробітників:")
        for surname, address in employees.items():
            print(f"{surname}: {address}")


def add_employee(employees):
    surname = input("Введіть прізвище нового співробітника: ")
    address = input("Введіть адресу нового співробітника: ")
    employees[surname] = address
    print(f"Співробітник {surname} успішно доданий.")


def remove_employee(employees):
    surname = input("Введіть прізвище співробітника для видалення: ")
    if surname in employees:
        del employees[surname]
        print(f"Співробітник {surname} успішно видалений.")
    else:
        print(f"Співробітник {surname} не знайдено у словнику.")


def view_sorted(employees):
    sorted_surnames = sorted(employees.keys())
    print("Записи за відсортованими прізвищами:")
    for surname in sorted_surnames:
        print(f"{surname}: {employees[surname]}")


def check_employees(employees):
    surnames_to_check = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]
    found_addresses = {}

    for surname in surnames_to_check:
        if surname in employees:
            found_addresses[surname] = employees[surname]

    if found_addresses:
        print("Співробітники з вказаними прізвищами та їх адреси:")
        for surname, address in found_addresses.items():
            print(f"{surname}: {address}")
    else:
        print("Співробітники з вказаними прізвищами не знайдені.")


def main():
    employees = {
        "Кузін": "вул. Перемоги, 1",
        "Куравльов": "вул. Шевченка, 2",
        "Кульков": "вул. Франка, 4",
        "Кубиків": "вул. Гагаріна, 5",
        "Петров": "вул. Миру, 6",

    }

    while True:
        print("\nОберіть дію:")
        print("1. Вивести всі записи")
        print("2. Додати співробітника")
        print("3. Видалити співробітника")
        print("4. Переглянути вміст словника за відсортованими ключами")
        print("5. Перевірити співробітників за прізвищами")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            check_all(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            remove_employee(employees)
        elif choice == '4':
            view_sorted(employees)
        elif choice == '5':
            check_employees(employees)
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
