import pandas as pd
import random

employees = {
    "Кузін": "вул. Перемоги, 1",
    "Куравльов": "вул. Шевченка, 2",
    "Кульков": "вул. Франка, 4",
    "Кубиків": "вул. Гагаріна, 5",
    "Петров": "вул. Миру, 6",
}

data = {
    'name': list(employees.keys()),
    'address': list(employees.values()),
    'age': [random.randint(25, 50) for _ in employees],
    'department': [random.choice(['HR', 'Developer', 'Finance', 'Marketing']) for _ in employees],
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
