#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


sentence = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for n in range(1, 26):

    for el in sentence:
        if el != ' ':
            cur_n = ord("a") + (ord(el) - ord("a") + 26 - n) % 26
            print(chr(cur_n), end="")
        else:
            print(' ', end='')
    print('')
    print("хотя поначалу этот способ может показаться неочевидным, если только вы не голландец")