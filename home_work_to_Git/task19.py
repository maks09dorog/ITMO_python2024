#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.

f = open("algoritm.csv", "w+t")

for i in range(len(algoritm)):
    str_ = (str(i + 1), "%", algoritm[i], '\n')
    f_str = ' '.join(str_)
    f.write(f_str)
    print(f_str)

# lines = [
# "New string\n",
# "Another string\n",
# ]
# f.writelines(lines)
f.close()
