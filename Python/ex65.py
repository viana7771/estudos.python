continuar = num = cont = media = soma = 0
maior = menor = 0
while continuar != 'N':
    num = int(input('Digite um numero: '))
    continuar = str(input('Quer contimuar? [S/N] ')).upper()
    cont += 1
    soma += num
    media = soma // cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
print(f'Você digitou {cont} números e a media foi {media}')
print(f'O menor número é {menor} e o maior número {maior}.')