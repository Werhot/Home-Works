list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
list_3 = set(list_1 + list_2)
print(list_3)
print()







list_of_countrys = [('Austria', 'Vienna'), ('Germany', 'Berlin'), ('Switzerland', 'Bern')]
user_country = input('Введите название страны на Английском, с большой буквы:\n')
for country in list_of_countrys:
    for i in country:
        if user_country in country:
            print(f'Страна {user_country}, столица: {country[1]}')
           
            break
print()






a = 3 
b = 'g'
list_of_touples = [(1, 'fdgfgh'), (1, '214124'), (a, b), (1, '214124')]
new_list_of_touples_1 = []
for i in list_of_touples:
    for j in i:
        new_list_of_touples_1.append(j)

new_list_1 = set(new_list_of_touples_1)        
print(new_list_1)
print()






user_str_1 = 'fdhgfddfhfdh'
new_str_1 = set(user_str_1)
print(new_str_1)
print()






print('"добавить"| Добавить слово')
print('"удалить"| Удалить слово')
print('"найти"| Найти слово')
print('"заменить"| Заменить слово')
print('"выход"| Выйти из прогоаммы')
print()
words = {}
while True:
    choise = input('Выберите действие: ')

    if choise == 'выход':
        break

    elif choise == 'добавить':
        title = input('Введите слово: ')
        translate = input('Введите перевод этого слова: ')
        words[title] = {
            'перевод': translate,
        }
        print(f'Слово {title} добавленно в словарь')
        print()

    elif choise == 'удалить':
        print('Удаление слова')
        print()
        title = input('Введите слово: ')
        if title in words:
            del words[title]
            print(f'Слово {title} удалено')
            print()
        else:
            print('Не удалось найти такое слово')
            print()

    elif choise == 'найти':
        title = input('Введите слово: ')
        if title in words:
            words_info = words[title]
            print(f'Слово {title} перевод: {words_info}')
            print()
        else:
            print('Не удалось найти такое слово')
            print()

    elif choise == 'заменить':
        title = input('Введите слово: ')
        if title in words:
            translate = input('Введите перевод этого слова: ')
            print()
            if translate:
                words[title]['перевод'] = translate
            print(f'Информация о слове обновлена')
            print()
        else:
            print('Не удалось найти такое слово')
            print()
    
    else:
        print("Вы ввели неверную комманду")