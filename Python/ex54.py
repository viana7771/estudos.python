from datetime import datetime

ano_atual = datetime.now().year
m = 0
mn = 0
pessoa = 1
for ano in range(0, 7):
    ano = int(input(f'Em que o ano a {pessoa}º pessoa nasceu? '))
    idade = ano_atual - ano
    pessoa += 1
    if idade >= 18:
        m += 1
    else:
        mn += 1
print('Ao todo são ''\033[;033m'f'{m}''\033[m'' pessoas maiores de idade.')
print('Ao todo são ''\033[;033m'f'{mn}''\033[m'' pessoas menores de idade.')