import random

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_aleatorio = random.choice(numeros)
c = 0
n = 0
print('VAMOS JOGAR')
while n != numero_aleatorio:
    n = int(input('Tente adivinhar em que numero estou pensando entre 0 e 10: '))
    c += 1
    if n == numero_aleatorio:
        print('Voce acertou!')
        print(f'Foram {c} tentativas para voce acertar.')
    else:
        print('Você errou!')