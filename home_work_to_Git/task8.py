# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".


a = 1001
if str(a)[0] == str(a)[3] and str(a)[1] == str(a)[2]:
    print("Данное четырехзначное число читается одинаково слева направо и справа налево")
else:
    print("Неправильно")