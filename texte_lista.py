valores = []

for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for i, v in enumerate(valores):
    print(f'Na indice {i} é encontrado o valor {v}')
print