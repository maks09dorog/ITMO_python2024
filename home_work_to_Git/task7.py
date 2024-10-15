#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

(a, b, c) = int(input()), int(input()), int(input())
if c > a:
    AC = c - a
else:
    AC = a - c
if c > b:
    BC = c - b
else:
    BC = b - c
print(f"Длина отрезка AC равна {AC}",
      f"Длина отрезка BC равна {BC}",
      f"Сумма длин отрезков AC и BC равна {AC + BC}", sep= '\n')