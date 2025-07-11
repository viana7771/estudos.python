cont = 0
numero = list()

for n in range(4):
    num = int(input('Digite um número: '))
    numero.append(num)

for n in tuple(numero):
    if n == 9:
        cont += 1

if cont > 0:
    print(f'O número 9 apareceu {cont} vez(es).\n')
else:
    print('O numero 9 não apareceu nenhuma vez.\n')
        
if 3 in tuple(numero):
    posicao = tuple(numero).index(3)
    print(f'A primeira vez que o número 3 aparece dentro da tupla é na posição {posicao}.\n')
else:
    print('O número 3 não foi digitado.\n')

par = list()

for n in tuple(numero):
    if n % 2 == 0:
        par.append(n)

if par:
    print(f'Números pares digitados:', *tuple(par))
else:
    print('Não apareceu nenhum número par.')