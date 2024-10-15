# todo: База данных пользователя.
# Задан массив объектов пользователя

from operator import itemgetter
users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]


#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# # 1. По возрасту
# # 2. По первой букве
# # 3. По группе
#
# # тип сортировки: 1
# #
# # #Затем сообщение для ввода
# # Ввидите критерии поиска: 16
#
# # Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"
#
sorted_list_age= sorted(users, key=itemgetter('age'))
print(sorted_list_age)

sorted_list_login= sorted(users, key=itemgetter('login'))
print(sorted_list_login)

sorted_list_group= sorted(users, key=itemgetter('group'))
print(sorted_list_group)





