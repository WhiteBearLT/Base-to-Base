def n_to_bin(number, base):  # Input number to bin
    base_bin = int(number, base)
    return base_bin


def bin_to_nBase(number10, base, abc):  # Returned bin to input base2
    number_answer = ''
    while number10 > 0:
        number_answer = abc[number10 % base] + number_answer
        number10 //= base
    return number_answer


if __name__ == '__main__':
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # abc's use for base bigger then 10

    num = input('Your number ')  # Num
    base1 = int(input('Base of number '))  # Base of input num
    base2 = int(input('Output number with base (up to 37) '))  # Output number's with base

    bin_number = n_to_bin(num, base1)
    out_number_withBase2 = bin_to_nBase(bin_number, base2, alphabet)

    # Output (input, base10, outBaseNum)
    print(f'\n {num} ({base1}) --> {bin_number} (10) --> {out_number_withBase2} ({base2})')

