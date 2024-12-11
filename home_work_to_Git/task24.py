#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!


def do_phrase(text : list):
    letter = ''
    for current_symbol in digit_to_letter:
        if current_symbol.isdigit():
            current_symbol = int(current_symbol)
            if current_symbol in range(1, len(eng_alpha) + 1):
                letter += eng_alpha[current_symbol - 1]
            if current_symbol == 0:
                letter += ' '
        else:
            letter += current_symbol

    return letter


digit_to_letter = [i for i in input().split()]
eng_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(do_phrase(digit_to_letter))
