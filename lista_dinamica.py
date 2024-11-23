"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []


while True:
    print('\nSelecione uma opção:')
    opcao = input('[i] inserir, [a] apagar, [l] listar ou [s] sair: ')
    opcao_minusculo = opcao.lower()  # Converte a entrada para minúsculo

    if opcao_minusculo == 's':
        print('\n Você não está mais na lista.\n')
        break

    if opcao_minusculo == 'i':
        os.system('cls')
        produto = input("Ponha o que você precisa na lista: ")
        lista.append(produto)
        print(lista)

    elif opcao_minusculo == 'a':
        os.system('cls')
        str_index = input('Qual índice deseja apagar? ')

        if str_index.isdigit():
            index = int(str_index)
            if 0 <= index < len(lista):
                del lista[index]
                print('Lista atual:', lista)
            else:
                print('Índice inválido.')
        else:
            print('Digite um número válido.')

    elif opcao_minusculo == 'l':
        os.system('cls')
        for i, item in enumerate(lista):
            print(f'{i} {item}')
    else:
        print("\n Escolha uma das opções.")
