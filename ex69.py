# Inicializa os contadores
cont_maior_idade = cont_homem = cont_mulher = idade =  0

while True:
    
    # Solicita a idade da pessoa
    while True:
        try:
            idade = int(input('Qual o idade que deseja inserir? '))
            break
        except ValueError:
            print('Erro: digite um numero inteiro valido. ')

    # Verifica se a pessoa tem mais de 18 anos
    if idade >= 18:
        cont_maior_idade += 1 

    # Soliciata o sexo da pessoa
    while True:
        sexo = str(input('Qual o sexo que deseja inserir? [M/F] ')).strip().upper()
        if sexo in ['M','F']:
            break
        else:
            print('Erro: digite uma entrada valida "M" ou "F". ')

    # Conta homens cadastrados
    if sexo == 'M':
        cont_homem += 1
    
    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        cont_mulher += 1

    # Pergunta de o usuario quer continuar
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print('Erro: digite uma entrada valida "S" ou "N"')

    # Se o unuario não quiser continuar, exibe os resultados e finaliza
    if continuar == 'N':
        print(f'{cont_maior_idade} pessoas tem mais de 18 anos.')
        print(f'{cont_homem} homens foram cadastrados.')
        print(f'{cont_mulher} mulheres tem menos de 20 anos.')
        break