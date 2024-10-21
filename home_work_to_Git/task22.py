#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

f = open("dump.txt", "rt" )
# message = f.read()
message = 'щсеняя погода очень осенняя погода'
litters = ['а','е','и','о','у','ю','я','ё','ы','э']

count = {}
for lit in litters:
    for mes in message:
        if lit in mes:
            count.setdefault(lit, 0)
            count[lit] = count[lit] + 1
# print(count)
for key , val in count.items():
    print(f"Количество букв {key} - {val}")