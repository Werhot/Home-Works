# bool_1 = True
# inner_list_1 = [1, 2, 3]
# inner_list_2 = ['afsaf', 'fdgfgdgf', 'qfaqf']
# inner_list_3 = [14.54, 'ouyuy', bool_1]
# list_1 = [inner_list_1, inner_list_2, inner_list_3]
# new_list_1 = inner_list_1 + inner_list_2 + inner_list_3
# print()
# print(list_1)
# print()
# print(new_list_1)
# print()






# target_1 = 5
# target_2 = 9

# inner_list_4 = [1, 3, 7, 9, 5]
# list_2 = [inner_list_4, 5, 9]

# for i in list_2:
#     for g in list_2:
#         if g == target_1 or g == target_2:
#             list_2.remove(g)
#     for j in inner_list_4:
#         if j == target_1 or j == target_2:
#             inner_list_4.remove(j)

# print()
# print(list_2)
# print()






# list_3 = [1, 2, 3, 4, 5, 6]
# list_4 = [1, 2, 3]
# print()
# print(set(list_4) - set(list_3) == set())
# print()






def return_lists(current_list):
    max_value = max(current_list, key=lambda a: len(a))
    max_len = len(max_value)
    return print([value.ljust(max_len, '_') for value in current_list])

return_lists(['153', '15475', '432452525'])
return_lists(['A', 'BB', 'CCC'])