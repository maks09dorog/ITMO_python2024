# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year_number = int(input())
print(f"Для {year_number} года номер столетия {(year_number - 1)//100 + 1}")