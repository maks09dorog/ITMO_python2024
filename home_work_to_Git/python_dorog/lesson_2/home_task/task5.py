#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

a, b = int(input()), int(input())
print(a+b, a-b, a/b, a*b, a//b, a%b, a**b)
print(f"Сумма чисел {a} и {b} равна {a+b}",
      f"Разность чисел {a} и {b} равна {a-b}",
      f"Частное чисел {a} и {b} равно {a/b}",
      f"Произведение чисел {a} и {b} равно {a*b}",
      f"Результат целочисленного деления чисел {a} и {b} равен {a//b}",
      f"Результат деления с остатком чисел {a} и {b} равен {a%b}",
      f"Результат возведения в степень чисел {a} и {b} равен {a**b}",
      sep="\n")
