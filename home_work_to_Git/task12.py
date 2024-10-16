#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
mass_unit = 5

#Введите  массу тела
mass = 0.7

# Ответ: 1000 кг

match mass_unit:
    case 1:
         print(f"Ответ: {1 * mass} кг")
    case 2:
         print(f"Ответ: {0.000001 * mass} кг")
    case 3:
        print(f"Ответ: {0.001 * mass} кг")
    case 4:
        print(f"Ответ: {1000 * mass} кг")
    case 5:
        print(f"Ответ: {100 * mass} кг")
    case _:
        pass

