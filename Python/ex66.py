cont = soma = 0

while True:
    num =  int(input('Digite um número [Digite 999 para parar]: ')) 
    if num != 999:
        cont += 1
        soma += num 
    else:
        break
print(f'Foram digitados {cont} números e a soma entre todos os números digitados é de {soma}.')