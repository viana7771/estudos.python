salario = float(input('Qual o valor do seu salario? '))
if salario > 1250.00:
    aumento = salario * 0.1 + salario
    print(f'Você vai ter um aumento de 10%, seu salario vai ser de {aumento:2}')
else:
    aumento2 = salario * 0.15 + salario
    print(f'Você vai ter um aumento de 15%, seu salario vai ser de {aumento2:2}')