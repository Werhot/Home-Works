def max_number(a, b, c, d, e):
    return print(max(a, b, c, d, e))


max_number(1, 9, 3, 7, 5)
print()






def list_exponential(exp_value, list_for_operation):
    result = [i ** exp_value for i in list_for_operation]
    return result


list_1 = [1, 8, 4, 24, 7, 3, 23]
exp = 2
print(list_1)
print(list_exponential(exp, list_1))
print()   






import datetime 

def date_time_func(year, month, day):  
    
    date_1 = datetime.date(g, m, n) 
    
    day_1 = datetime.timedelta(days=1) 
    
    yesterday = date_1 - day_1 
    
    tomorrow = date_1 + day_1 
    
    print(f"Дата: {date_1}") 
    print(f"Завтра: {tomorrow}")
    print(f"Вчера: {yesterday}")
    print() 
    

g = 2024 
m = 4 
n = 30
date_time_func(g, m, n)






employees = [
    {"name": "Alice",
     "tasks_completed": 25,
     "quality": 0.9},
    {"name": "Bob",
     "tasks_completed": 30,
     "quality": 0.85},
    {"name": "Charlie",
     "tasks_completed": 20,
     "quality": 0.95},
]
def evaluate_performance(employees: list):
    rating_count = {}
    list_rating = []
    for employee in employees:
        manager = employee['name']
        rating = employee['tasks_completed'] * employee['quality']
        if manager in rating_count:
            rating_count[manager] += rating
        else:
            rating_count[manager] = rating
    print('Результат: \n\nРейтинг сотрудников:')
    for name, value in rating_count.items():
        print(f'- {name}: {value}')
    for name, value in rating_count.items():
        list_rating.append(value)
        max_value_rating = max(list_rating)
        min_value_rating = min(list_rating)
        if max_value_rating == value:
            best_employee = name
        if min_value_rating == value:
           worst_employee = name
    print(f'\nЛучший сотрудник: {best_employee}')
    print(f'Худший сотрудник: {worst_employee}')
evaluate_performance(employees)