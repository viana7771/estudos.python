import random
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

cont = 0

while True:
    num = int(input('Escolha um numero aleatorio entre 1 e 10: '))
    p_ou_i = str(input('Escolha par ou ímpar [P/I]: ')).upper()
    ale_num = random.randint(0, 10)
    soma = num + ale_num
    result = soma % 2
    cont += 1
    if result == 0 and p_ou_i  == 'P':
        print(f'Voce jogou {num} e o computador jogou {ale_num} o total é de {soma}. Deu PAR você ganhou!')
    elif result == 0  and p_ou_i == 'I':
        print(f'Voce jogou {num} e o computador jogou {ale_num} o total é de {soma}. Deu PAR você perdeu!')
        print(f'Voce ganhou {cont-1} vezes')
        break
    elif result != 0 and p_ou_i == 'I':
        print(f'Voce jogou {num} e o computador jogou {ale_num} o total é de {soma}. Deu ÍMPAR você ganhou!')
    elif result != 0 and p_ou_i == 'P':
        print(f'Voce jogou {num} e o computador jogou {ale_num} o total é de {soma}. Deu ÍMPAR você perdeu!')
        print(f'Voce ganhou {cont-1} vezes')
        break
