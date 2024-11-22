import matplotlib.pyplot as plt
from collections import Counter

data = [
    {"surname": "Іванов", "address": "вул. Шевченка, 10", "position": "менеджер"},
    {"surname": "Петренко", "address": "вул. Грушевського, 15", "position": "директор"},
    {"surname": "Сидоров", "address": "вул. Франка, 7", "position": "аналітик"},
    {"surname": "Коваленко", "address": "вул. Лесі Українки, 20", "position": "програміст"},
    {"surname": "Мельник", "address": "вул. Кобзаря, 8", "position": "маркетолог"},
    {"surname": "Шевченко", "address": "вул. Леніна, 5", "position": "економіст"},
    {"surname": "Коваль", "address": "вул. Червоноармійська, 3", "position": "бухгалтер"},
    {"surname": "Гречко", "address": "вул. Довженка, 11", "position": "системний адміністратор"},
    {"surname": "Кузьменко", "address": "вул. Пушкина, 2", "position": "технік"},
    {"surname": "Тимошенко", "address": "вул. Пирогова, 18", "position": "юрист"},
    {"surname": "Бабенко", "address": "Миру 25", "position": "Студент"},
    {"surname": "Гавриленко", "address": "Шевченка 25", "position": "технік"},
    {"surname": "Євтушенко", "address": "Петропавлівська 25", "position": "бухгалтер"}
]


surname_lengths = [len(person['surname']) for person in data]
print(surname_lengths)

categories = []
for length in surname_lengths:
    if length < 6:
        categories.append("Менше 6 символів")
    elif length == 6:
        categories.append("6 символів")
    elif length == 7:
        categories.append("7 символів")
    elif length == 8:
        categories.append("8 символів")
    else:
        categories.append("Більше 8 символів")

print(categories)
length_counts = Counter(categories)

print(length_counts)
labels = length_counts.keys()
sizes = length_counts.values()


plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Розподіл за кількістю символів у прізвищах")
plt.axis('equal')
plt.show()
