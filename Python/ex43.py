peso =  float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura **  2)
if 0 < imc <= 18.5:
    print('A baixo do peso.')
elif 18.5 < imc <= 25:
    print('Peso ideal.')
elif 25 < imc <= 30:
    print('Acima do peso.')
elif 30 < imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade morbida.')
