print('='*10)
print('Os 10 termos de uma PA!')
print('='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('A razão: '))
termo = primeiro
c = 1
while c < 10:
    print(f' {termo} ➡️ ', end='\n')
    termo += razao
    c += 1
    continuar = int(input('Quantos termos você quer mostrar mais? '))
    if continuar != 0:
        print(f'{termo} ➡️ ', end='')
        termo += continuar
    else:
        (f'O total foi de {c} termos.')