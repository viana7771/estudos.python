cont_maior_idade = cont_homem = cont_mulher = 0

while True:
    idade = int(input('Qual o idade que deseja inserir? '))
    if idade >= 18:
        cont_maior_idade += 1 

    sexo = str(input('Qual o sexo que deseja inserir? [M/F] ')).upper()
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher += 1

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print(f'{cont_maior_idade} pessoas tem mais de 18 anos.')
        print(f'{cont_homem} homens foram cadastrados.')
        print(f'{cont_mulher} mulheres tem menos de 20 anos.')
        break