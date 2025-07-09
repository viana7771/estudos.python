num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    
    digite = int(input('Digite um número entre 0 e 20: '))

    if 0 <= digite <= 20:
        print(f'Você digitou o numero {num[digite]}.')
        break
    else:
        print('Tente novamente. Número fora do intevalo.')