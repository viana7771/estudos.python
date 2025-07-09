from random import choice

#APLICANDO A LOGICA DE ALEATORIEDADE DA MAQUINA
jkp = [1, 2, 3]
computador = choice(jkp)

while True: #APLIACANDO O LOOP
    print('''VAMOS JOGAR JOKENPO?
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    [4] SAIR DO JOGO''')
    opcao = int(input('''ESCOLHA A SUA OPÇÃO: '''))
    print('=-=' * 10)
    print(f'O computador escolheu {computador}')
    print(f'E você escolheu {opcao}')
    print('=-=' * 10)
    if opcao == 1: #VOCÊ JOGOU PEDRA
        if opcao == computador:
            print('Deu empate\n')
        elif computador == 2:
            print('Você perdeu\n')
        elif computador == 3:
            print('Você ganhou\n')
        else:
            print('Jogada invalida\n')
    elif opcao == 2: #VOCÊ JOGOU PAPEL
        if opcao == computador:
            print('Deu empate\n')
        elif computador == 3:
            print('Você perdeu\n')
        elif computador == 1:
            print('Você ganhou\n')
        else:
            print('Jogada invalida\n')
    elif opcao == 3: #VOCÊ JOGOU TESOURA
        if opcao == computador:
            print('Deu empate\n')
        elif computador == 1:
            print('Você perdeu\n')
        elif opcao == 2:
            print('Você ganhou\n')
        else:
            print('Jogada inavalida\n')
    elif opcao == 4: #FINALIZANDO O PROGRAMA
        print('Saindo do jogo!')
        break
    else: #LOGICA CASO SEJA INSERIDO UM NUMERO INVALIDO
        print('Jogada invalida, tente novamente!\n')
        