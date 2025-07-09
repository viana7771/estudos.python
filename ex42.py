reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('comprimento da segunda reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1: 
    print('É possivel formar um triangulo! ')
else: 
    print('Não é possivel formar um triangulo! ')

if reta1 == reta2 == reta3:
    print('E esse triangulo é um equilátero, quando todos os lados são iguais.')
elif reta1 == reta2 != reta3:
    print('E esse triangulo é um isósceles, quando apenas dois lados são iguais.')
elif reta3 == reta2 != reta1:
    print('E esse triangulo é um isósceles, quando apenas dois lados são iguais.')
elif reta3 == reta1 != reta2:
    print('E esse triangulo é um isósceles, quando apenas dois lados são iguais.')
else:
    print('E esse trinangulo é um escaleno, quando todos os lados são diferentes.')