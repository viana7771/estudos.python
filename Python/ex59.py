escolha = 0
n1 = 0
n2 = 0
while escolha != 5: 
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    escolha = int(input('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')) 
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1} mais {n2} é {soma}.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'{n1} X {n2} é {mult}.')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        else:
            print(f'{n2} é maior que {n1}.') 
    elif escolha == 4:
        print('Escolha novamente.')
    else:
        print('Finalizando programa.')