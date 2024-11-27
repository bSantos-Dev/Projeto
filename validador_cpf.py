import re
import sys

user_input = input('Digite seu CPF: ')

# Remove caracteres não numéricos e Verifica se todos os números são iguais (sequenciais)
clean_cpf = re.sub(r'[^0-9]', '', user_input)

is_sequential = clean_cpf == clean_cpf[0] * len(clean_cpf)

if is_sequential:
    print('CPF inválido: números sequenciais.')
    sys.exit()

# Primeiro dígito
first_nine_digits = clean_cpf[:9]
first_multiplier = 10

first_digit_sum = 0
for digit in first_nine_digits:
    first_digit_sum += int(digit) * first_multiplier
    first_multiplier -= 1

first_verifier_digit = (first_digit_sum * 10) % 11
first_verifier_digit = first_verifier_digit if first_verifier_digit <= 9 else 0


first_ten_digits = first_nine_digits + str(first_verifier_digit)
second_multiplier = 11

# Segundo Dígito
second_digit_sum = 0
for digit in first_ten_digits:
    second_digit_sum += int(digit) * second_multiplier
    second_multiplier -= 1

second_verifier_digit = (second_digit_sum * 10) % 11
second_verifier_digit = second_verifier_digit if second_verifier_digit <= 9 else 0


generated_cpf = f'{first_nine_digits}{
    first_verifier_digit}{second_verifier_digit}'

if clean_cpf == generated_cpf:
    print(f'{clean_cpf} é válido.')
else:
    print('CPF inválido.')
