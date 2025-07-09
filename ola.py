from random import randint

numero_aleatorio = randint(1, 1000)
print('Escolha um numero de 1 a 1000!')

while True:
    escolha = int(input('escolha um número: '))
    if escolha == numero_aleatorio:
        print('Parabéns,''\033[1;32m''você acertou!''\033[m')
        print(f'O numero  correto era {numero_aleatorio}')
        break
    elif escolha > numero_aleatorio:
        print('O numero que voce escolheu está errado.')
        print('O numero correto é menor, tente novamente.')
    else:
        print('o numero que você escolheu está errado.')
        print('O numero correto é maior, tente novamente.')
