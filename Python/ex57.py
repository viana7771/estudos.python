import time
r = 'S'
while r == 'S':
    s = str(input('Qual o seu sexo [M/F]: ')).upper()
    if s == 'M':
        print('Você é homem!')
    elif s == 'F':
        print('Você é mulher!')
    else:
        print('O valor registrado foi invalido, tente novamente.')
    r = str(input('Quer continuar [S/N]: ')).upper()
print('Encerando programa em...')
time.sleep(1)
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('Programa encerrado.')