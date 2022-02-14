def n_to_10n(number, base):
    notation10_def = int(number, base)
    return notation10_def


def n10_to_n(number10, base, abc):
    number_answer = ''
    while number10 > 0:
        number_answer = abc[number10 % base] + number_answer
        number10 //= base
    return number_answer


if __name__ == '__main__':
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    num = input('Your number ')
    base1 = int(input('Base of number '))
    base2 = int(input('Output number with base (up to 37) '))

    number10n = n_to_10n(num, base1)
    number_answer_n2 = n10_to_n(number10n, base2, alphabet)

    print(f'\n {num} ({base1}) --> {number10n} (10) --> {number_answer_n2} ({base2})')
