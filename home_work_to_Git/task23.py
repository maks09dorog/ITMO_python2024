# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

import codecs
fileObj = codecs.open( "message.txt", "r", "utf_8_sig" )
# text = fileObj.readlines(5)
#
# print(text)

print(fileObj.readline())
print(fileObj.readline())
print(fileObj.readline())
print(fileObj.readline())
print(fileObj.readline())

fileObj.close()

def text_crypting():
    crypted_text = ''
    text_ = []
    fileObj = codecs.open( "message.txt", "r", "utf_8_sig" )
    line = fileObj.readline()
    while line:
        text_.append(line.strip())
        line = fileObj.readline()
    fileObj.close()



    for num_line in range(len(text_)):
        move = num_line + 1
        for letter in text_[num_line]:
            if 'а' <= letter <= 'я':
                crypted_letter = chr((ord(letter) - ord('а') + move) % 32 + ord('а'))
            elif 'А' <= letter <= 'Я':
                crypted_letter = chr((ord(letter) - ord('А') + move) % 32 + ord('А'))
            else:
                crypted_letter = letter
            crypted_text += crypted_letter
        crypted_text += '\n'
    return crypted_text


def create_new_message():
    fileObj = codecs.open( "message.txt", "r", "utf_8_sig" )
    fileObj.write(text_crypting())
    fileObj.close()

print(text_crypting())