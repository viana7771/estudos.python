num = int(input('Digite um numero: '))
print('''qual base numerica deseja converter?
                [1] para binario
                [2] para octadecimal
                [3] para hexadecimal''')
opcao = int(input('Escolha uma das opções acima: '))
if opcao == 1:
    print(f'{num} convertido para binario fica {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octadecimal fica {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal fica {hex(num)[2:]}')
else:
    print('Resultado Invalido.')