import random
import os

print('\n***SORTEIO***')

saved_num = []

while True:
    continuar = input(
        '\nEscolha uma opção:\n'
        ' [l] Listar números sorteados\n'
        ' [s] Gerar números\n'
        ' [n] Encerrar\n'
        ' Opção: '
    )
    opcao = continuar.strip().lower()

    if opcao == 'n':
        print('\nFim de sorteio. Obrigado por participar!\n')
        break

    elif opcao == 's':
        os.system('cls')
        start = 0
        stop = 2000
        drawn_num = random.randint(start, stop)
        saved_num.append(drawn_num)
        print(
            "__________________________________________\n"
            f'\nO número sorteado foi: {drawn_num}\n'
        )

    elif opcao == 'l':
        if saved_num:
            print("\nNúmeros sorteados até agora:")
            for index, num in enumerate(saved_num, start=1):
                print(f'{index}: {num}')
        else:
            print("\nNenhum número foi sorteado ainda.")
    else:
        print('Opção inválida! Escolha apenas [l], [s] ou [n].')
