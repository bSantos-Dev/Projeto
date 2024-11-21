import os

secret_word = 'dictionary' # Alterável
guessed_letters = ''
attempt_count = 0

while True:
    entered_letter = input('Enter a letter: ')
    attempt_count += 1

    if len(entered_letter) > 1:
        print('Please enter only one letter.')
        continue

    if entered_letter in secret_word:
        guessed_letters += entered_letter

    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in guessed_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'

    print('Formed word:', formed_word)

    if formed_word == secret_word:
        os.system('cls') # Vai depender do sistema operacional. Pode usar o "clear"

        print('\nYOU WON!! CONGRATULATIONS!')
        print('The word was', secret_word)
        print(f'Attempts: {attempt_count} \n')
        
        guessed_letters = ''
        attempt_count = 0
        break