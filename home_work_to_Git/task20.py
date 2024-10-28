#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
from home_work_to_Git.task23 import fileObj

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

print(f.readlines(4))
print(f.readlines(3))
print(f.readlines(2))
print(f.readlines(1))

f.close()
#todo: readlines выодит от начала до конца
