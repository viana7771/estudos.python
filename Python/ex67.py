import time

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:
        print('Esse número é negativo, não posso mostrar a tabuada.')
        print('Encerrando programa em...') 
        for i in range(3, 0, -1):   
            print(f'{i}...')
            time.sleep(1)
        print('FIM! Volte sempre ;)')
        break
    for i in range(1, 11):
        tab = num * i
        print(f'{num} x {i} = {tab}')