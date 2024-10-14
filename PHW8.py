import os
import json

if os.path.exists('Employees.json'):
    with open('Employees.json', 'r') as f:
        employees = json.load(f)

print('"Д"| Добавить сотрудника')
print('"У"| Удалить сотрудника')
print('"Н"| Найти сотрудника по фамилии')
print('"Р"| Редактировать информацию о сотруднике')
print('"П"| Показать всех сотрудников')
print('"В"| Выйти из прогоаммы')
print()

info = {}
while True:
    choise = input('Выберите действие: ')

    if choise == 'В':
        break

    elif choise == 'Д':

        surname = input('Введите фамилию сотрудника: ')
        age = input('Введите возраст сотрудника: ')
        employees[info] = {
            'surname': surname,
            'age': age
        }

        employees.append(info)
        with open('Employees.json', 'A') as f:
            json.dump(employees, f, indent=4)

        print(f'сотрудник {info} добавлен')
        print()

    elif choise == 'У':

        print('Удаление сотрудника по фамилии')
        print()
        info = input('Введите фамилию сотрудника: ')
        if info in employees:
            del employees[info]

            print(f'Сотрудник: {info} удалена')
            print()
        else:
            print('Не удалось найти такого сотрудника')
            print()

    elif choise == 'Н':
        info = input('Введите фамилию сотрудника: ')
        if info in employees:
            e_info = employees[info]

            print(f'Сотрудник: {info}: {e_info}')
            print()
        else:
            print('Не удалось найти такую книгу')
            print()

    elif choise == 'Р':
        info = input('Введите название книги: ')
        if info in employees:
            surname = input('Введите фамилию сотрудника: ')
            age = input('Введите возраст сотрудника: ')
            
            if surname:
                employees[info]['surname'] = surname
            if age:
                employees[info]['age'] = age
            
            with open('Employees.json'[info], 'w') as f:
                json.dump(employees, f, indent=4)

            print(f'Информация о сотруднике обновлена')
            print()
        else:
            print('Не удалось найти такую книгу')
            print()

    elif choise == 'П':
            ch = input('Выберите действие: ')
            print('"ПФ"| Поиск по фамилии')
            print('"ПВ"| Поиск по возасту')
            print()

            if ch == 'ПФ':
                surname = input('Введите фамилию сотрудника: ')
                if employees:
                    for info, surname in employees.items():
                        print(f'Фамилия: {surname}, общая информация: {info}')
                        print()
                else:
                    print('Сотрудников пока нет')
            elif ch == 'ПВ':
                age = input('Введите возраст сотрудника: ')
                if employees:
                    for info, surname in employees.items():
                        print(f'Фамилия: {age}, общая информация: {info}')
                        print()
                else:
                    print('Сотрудников пока нет')
    else:
        print("Вы ввели неверную комманду")

with open('Employees.json', 'A') as f:
    json.dump(employees, f, indent=4)

print()