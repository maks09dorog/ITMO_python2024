#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

import codecs
fileObj = codecs.open( "text.txt", "r", "utf_8_sig" )
text = fileObj.read()

f = open("text.txt", "r+t")
f.write("Hello\n")

# f.close()

f = open("text.txt", "rt")

print(f.read())
f.close()