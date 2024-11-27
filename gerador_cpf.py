import random
import os

while True:
    first_nine_digits = ''
    for i in range(9):
        first_nine_digits += str(random.randint(0, 9))

    first_multiplier = 10

    first_digit_sum = 0
    for digit in first_nine_digits:
        first_digit_sum += int(digit) * first_multiplier
        first_multiplier -= 1

    first_verifier_digit = (first_digit_sum * 10) % 11
    first_verifier_digit = first_verifier_digit if first_verifier_digit <= 9 else 0

    first_ten_digits = first_nine_digits + str(first_verifier_digit)
    second_multiplier = 11

    second_digit_sum = 0
    for digit in first_ten_digits:
        second_digit_sum += int(digit) * second_multiplier
        second_multiplier -= 1

    second_verifier_digit = (second_digit_sum * 10) % 11
    second_verifier_digit = second_verifier_digit if second_verifier_digit <= 9 else 0

    generated_cpf = f'{first_nine_digits}{
        first_verifier_digit}{second_verifier_digit}'

    print(f'\n{generated_cpf}\n')

    entrada = input('Gerar outro CPF? [s/n]: ')

    if entrada == 'n':
        os.system('cls')  # ou clear
        break
