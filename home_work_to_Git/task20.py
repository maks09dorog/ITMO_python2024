#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
text_ = [
"Beautiful is better than ugly.\n"
"Explicit is better than implicit.\n"
"Simple is better than complex.\n"
"Complex is better than complicated.\n"
]
#
# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

f = open('import_this.txt', 'rt')

a = (f.readlines())
print(a[::-1])

f.close()
