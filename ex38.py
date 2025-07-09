num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'{num1} é maior que o {num2}.')
elif num2 > num1:
    print(f'{num2} é maior que o {num1}.')
else: 
    print('Nenhum dos dois numeros digitados são maiores, eles são iguais!')