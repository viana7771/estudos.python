valores = []

for v in range(0, 5):
    valores.append(int(input('Adicione um valor: ')))

maior = valores[0]
indice_maior = [i for i, v in enumerate(valores) if v == maior]

for i, v in enumerate(valores):
    if v > maior:
        maior = v
        print(f'No indice {indice_maior} está o maior número da lista, {maior}')

menor = valores[0]
indice_menor = [i for i, v in enumerate(valores) if v == menor]

for i, v in enumerate(valores):
    if v < menor:
        menor = v
        print(f'No indice {indice_menor} está o menor número da lista, {menor}')