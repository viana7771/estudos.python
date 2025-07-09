nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Reprovado. A sua media foi de {media}')
elif 5 <= media <= 6.9:
    print(f'Recuperação. A sua media foi de {media}')
else:
    print(f'Aprovado. A sua media foi de {media}')