import re

# user_text1 = input()
# pattern1 = r"\b[AAaа]\w+"
# new_text1 = re.findall(pattern1, user_text1)
# print(user_text1)
# print()
# print(new_text1)
# print()






# user_text2 = input()
# pattern2 = r"(Old|old)"
# new_text2 = re.sub(pattern2, 'new', user_text2)
# print(user_text2)
# print()
# print(new_text2)
# print()






# user_text3 = input()
# pattern3 = r"[0-9]"
# new_text3 = re.findall(pattern3, user_text3)
# print(user_text3)
# print()
# print(new_text3)
# print()






# number = input()
# result = re.match(r'((^\+7)\s(\(\d{3}\))\s(\d{3})-(\d{4}))', number)
# print(bool(result))






date = '23:59:59'
result = re.match(r'^[0-2][0-3]:[0-5][0-9]:[0-5][0-9]$', date)
print(bool(result))