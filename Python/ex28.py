from random import randint
from time import sleep

numeros = randint(0, 5)

while True:
    print('O computador vai sortear um numero aleatorio e você deve tentar acertar qual numero é.')
    num = int(input('Escolhar um numero aleatorio entre 0 e 5: '))
    print('PROCESSANDO...')
    sleep(2)
    if num == numeros:
        print(f'Você acertou! O numero que o computador escolheu foi o {numeros}')
        break
    else:
        print(f'você errou!')