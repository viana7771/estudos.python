reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('comprimento da segunda reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1: 
    print('É possivel formar um triangulo! ')
else: 
    print('Não é possivel formar um triangulo! ')