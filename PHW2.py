# user_text = str(input("Введите текст: "))
# reserved_text = input("Введите список зарезервированных слов через пробел: ").split()

# for word in reserved_text:
#     user_text = user_text.replace(word, word.upper())

# print('Ваш текст: \n' + user_text)






# print("Введите два числа и арифметическое действие для них")

# result = ""
# x = int(input("ВВедите первое число: "))
# y = int(input("ВВедите второе число: "))
# c = str(input("Введите арифметическую операцию: + или - или * или / "))

# if c == '+':
#     result = x + y
# elif c == '-':
#     result = x - y
# elif c == '/' and y != 0:
#     result = x / y
# elif c == '*':
#     result = x * y
# else:
#     print("Была введена недопустимая операция")

# print("Ваш Результат = ",result)






# welcome = str(input('Введите ваш текст: \n'))
# index = welcome.split()
# print(index)






s = input('Введите ваш текст: \n'); 
a = b = c = 0 
for x in s: 
    if x.isalpha(): 
        a += 1 
    elif x.isnumeric(): 
        b += 1 
    else: 
        c += 1 
print(f'Букв: {a}; Цифр: {b}; Спец: {c}')