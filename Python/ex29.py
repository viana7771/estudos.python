velocidade = int(input('Qual a velocidade que o carro passou no radar? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado por ultrapassar o limite de velocidade! Sua multa é de {multa:.2f}R$')
else:
    print('Você esta dentro do limite de velocidade!')