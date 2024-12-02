# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0

# Peguntas
for pergunta in perguntas:
    print(f"\n{pergunta['Pergunta']}")
    for alterativa, resposta in enumerate(pergunta['Opções'], start=1):
        print(f"{alterativa}. {resposta}")

    escolha = input('Escolha de 1-4:\n ↳ ')

    try:
        index = int(escolha) - 1
        if pergunta['Opções'][index] == pergunta['Resposta']:
            print('\nCerta resposta')
            acertos += 1
        else:
            print('\nResposta errada!')
            erros += 1

    except (ValueError, IndexError):
        print("Reposta inválida. Dado como erro.")
        erros += 1

print(f'\nVocê acertou {acertos} de {len(pergunta)} perguntas')
