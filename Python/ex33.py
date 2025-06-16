num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Preciso que digite só mais um numero: '))
# Verificando quem é o menor
menor = num1
if num1 > num2 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando quem é o maior
maior = num1
if num1 < num2 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O menor é {menor}')
print(f'O maior é {maior}')