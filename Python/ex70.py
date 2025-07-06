soma = cont_num_mil = 0
menor = None
nome_menor = ''

print('-'*30)
print('LOJA SUPER BARATÃO!')
print('-'*30)

while  True:
    nome = str(input('Nome do produto: ')).strip()

    while True:   
        try: 
            preco = int(input('Preço: R$'))
            soma +=(preco)
            if preco > 1000:
                cont_num_mil += 1
            break
        except ValueError:
            print('ERRO: ensira um valor valido.')

    while True:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
        if continua in ['S', 'N']:
            break
        else:
            print('ERRO: ensira um valor valido "S" ou "N".')

    if menor is None or preco < menor:
        menor = preco
        nome_menor = nome

    if continua == 'N':
        print('='*30)
        print(f'O total de gastos foi de R${soma:.2f}')
        print(f'{cont_num_mil} custam mais de R$1000')
        print(f'{nome_menor} é o produto com menor valor (R${menor:.2f})')
        print('='*30)
        break