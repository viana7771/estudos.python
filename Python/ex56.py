media = 0
soma_idades = 0
mais_velho = 0
nome_velho = ''
mulher20 = 0
for i in range(1, 5):
    print(f'===== {i}ª pessoa =====')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma_idades += idade
    media = soma_idades / 4

    if i == 1 and sexo in 'Mm':
        mais_velho = idade
        if sexo in 'Mm' and idade > mais_velho:
            mais_velho = idade
            nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

print(f'A media de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')
print(f'Ao todos são {mulher20} mulheres com menos de 20 anos.')