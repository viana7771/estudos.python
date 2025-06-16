frase = str(input('Digite uma frase: ')).upper()
palavra = frase.split()
fse = ''.join(palavra)
inverso = ''
for letra in range(len(fse) -1, -1, -1):
    inverso += fse[letra]
print(f'O inverso de {fse} é {inverso}') 
if fse == inverso:
    print('A frase é palindroma')
else:
    print('A frase não é palindroma')