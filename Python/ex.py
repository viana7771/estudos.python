from calendar import isleap

ano = int(input('Digite um ano qualquer: '))
if isleap(ano):
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')