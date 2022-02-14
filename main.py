def n_to_bin(number, base):  # Input number to bin
    try:
        base_bin = int(number, base)
        return base_bin
    except ValueError:
        return -1  # Error


def bin_to_nBase(binNumber, base, abc):  # Returned bin to input base2
    if binNumber == -1:
        return -1  # If (n_to_bin) get error
    else:
        try:
            if binNumber != 0:
                number_answer = ''
                while binNumber > 0:
                    number_answer = abc[binNumber % base] + number_answer
                    binNumber //= base
                return number_answer
            else:
                return 0  # Input number 0
        except ValueError:
            return -1  # When get error


if __name__ == '__main__':
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # abc's use for base bigger then 10

    flag = True
    while flag:
        try:
            num = input('Your number ')  # Num
            base1 = int(input('Base of number '))  # Base of input num
            base2 = int(input('Output number with base (up to 36) '))  # Output number's with base

            if base1 > 0 and base2 > 0:  # Base higher then 0 check
                bin_number = n_to_bin(num, base1)
                out_number_withBase2 = bin_to_nBase(bin_number, base2, alphabet)

                # Output (input, base10, outBaseNum)
                print(f'\n {num} ({base1}) --> {bin_number} (10) --> {out_number_withBase2} ({base2})')

                answer = input('\nYou want repeat program? (type \'y\' or \'n\') ')  # Repeat answer
                if answer == 'y' or answer == 'Y':
                    flag = True  # If answer y (yes)
                else:
                    flag = False  # Stop cycle flag if answer n (no)

            else:  # Base < 0
                print('\nUse base higher then 0')
                flag = True  # Cycle repeat
        except ValueError:
            print('\nTry again')  # When get error
            flag = True
