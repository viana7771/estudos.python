cont = 16

time = (
    'Flamengo',
    'Cruzeiro',
    'Red Bull Bragantino',
    'Palmeiras',
    'Bahia',
    'Fluminense',
    'Atlético Mineiro',
    'Botafogo',
    'Mirasol',
    'Corinthians',
    'Grêmio',
    'Ceará',
    'Internacional',
    'Fortaleza',
    'Chapecoense',
    'Santos',
    'São Paulo',
    'Juventude',
    'Sport Recife',
    'Vasco da Gama',
    'Vitória'
)

print('Os 5 primeiro colocados no Brasileirão')

for i in range(5):
    print(f'{i+1}° {time[i]}')
print('\n')

print('Os 4 Ultimos colocados no Brasileirão')


for i in time[16:]:
    cont += 1
    print(f'{cont}° {i}')
print('\n')

times_ordenados = sorted(time)
print(times_ordenados)
print('\n')

for posicao, i in enumerate(time):
    if i == 'Chapecoense':
        print(f'o time da Chapecoence esta na posição {posicao}°')
