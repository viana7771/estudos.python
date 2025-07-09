from datetime import datetime

ano_nascimento = int(input('Qual o ano que você nasceu? '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
alistamento = 18
if idade < alistamento:
    quanto_falta = alistamento - idade
    print(f'Você ainda vai se alistar, e faltam {quanto_falta} anos para você se alistar.')
elif idade == alistamento:
    print(f'Está na hora de você se alistar.')
else:
    quanto_passou = idade - alistamento
    print(f'Já passou {quanto_passou} anos que era pra você ter se alistado.')