#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

f = open("text.txt", "r+t")
f.write("Hello\n")
text = f.read()
print(text)

f.close()
