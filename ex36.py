from time import sleep

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
ano = int(input('Em quantos anos vai pagar? '))
prestacao = casa // (ano * 12)
porcentagem = salario * 0.3
print()
print('PROCESSANDO...')
sleep(2)
print()
print('Deseja financiar uma casa no valor de ''\033[1;31m'f'R${casa:.2f}''\033[m'' com prestações de ''\033[1;31m'f'R${prestacao:.2f}''\033[m'' por mês.')
if prestacao < porcentagem:
    print('O financiamento foi ''\033[1;32m''aprovado!''\033[m')
else: 
    print('O financiamento não foi a aprovado!''\033[1;31m''\033[m')