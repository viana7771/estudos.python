from datetime import datetime

ano = int(input('Que ano você nasceu: '))
ano_atual = datetime.now().year
idade = ano_atual - ano
if 0 <= idade <= 9:
    print('Mirim')
elif 10 <= idade <= 14:
    print('Infantil')
elif 15 <= idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
else:
    print('Maxter')