listanum = []

while True:
    try:
        num = (int(input('Digite um número: ')))
        if num in listanum:
            print('Esse número já existe na lista.')
        else:
            listanum.append(num)
            print('Número Adicionado com sucesso!')
    except ValueError:
        print('Digite apenas números')
    cont = (str(input('Deseja continuar ? [S/N] '))).strip().upper()
    if cont == 'S':
        continue
    elif cont == 'N':
        break
    else:
        print('Digite apenas [S/N]')
print(sorted(listanum))