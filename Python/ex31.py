import locale

distancia = int(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    tarifa = locale.currency(0,50 * distancia)
    print(f'A sua viagem vai custar {tarifa}.')
else:
    tarifa2 = locale.currency(0,45 * distancia)
    print(f'A sua viagem vai custar {tarifa2}.')