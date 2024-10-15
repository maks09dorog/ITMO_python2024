from os import remove

#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
mass = [1, 2,17,54,30,89,2,1,6,2]


# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

cur_val = 0
cur_index1 = []
cur_index2 = []
cur_index3 = []
cnt = 0
for i in range(len(mass)):
    cur_val = mass[i]
    if mass.count(cur_val) <= 1:
        print(f'Для числа {mass[i]} нет минимального растояния т.к элемент в массиве один.')
    elif 1 < mass.count(cur_val) <= 2:
        for j in range(i + 1, len(mass)):
            if mass[i] == mass[j]:
                print(f'Для числа {mass[i]} минимальное растояние в массиве по индексам:{i} и {j}')
    elif 2 < mass.count(cur_val):
        cur_index3.append(i)
        for k in range(len(cur_index3)):
            min_len = max(cur_index3)
            len_ = cur_index3[k + 1] - cur_index3[k]
            if len_ < min_len:
                len_ = min_len





print(cur_index3)

