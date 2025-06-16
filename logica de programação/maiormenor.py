# VARIAVEIS QUE SERÃO UTILIZADAS NO CODIGO
pessoa = 1
media = 0
soma_idades = 0

# LOGICA DO LOOP SOBRE AS 3 PERGUNTAS 
for i in range(1, 5):
    print('='*5,f'{pessoa}ª PESSOA','='*5)
    nome = str(input('NOME: ')).split()
    idade = int(input('IDADE: '))
    idades.append(idade)
    sexo = str(input('SEXO [M/F]: ')).split()
    pessoa += 1

    # MEDIA DA IDADE DO GRUPO
    soma_idades += idade
    media = soma_idades / 4
print(media)