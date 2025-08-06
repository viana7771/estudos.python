valores = []

for v in range(0, 5):
    valores.append(int(input(f'Adicione um valor na posição {v}°: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor} nas posições ', end='' )
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='') 