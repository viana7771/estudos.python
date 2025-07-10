import random # importando a biblioteca random

numero = () # criando a tupla

# gerar os 5 números aleatórios
for i in range(5):
    num_ale = random.randint(0, 4) # criando a logica para gerar 5 números aletórios 
    lista_numero = list(numero) # convertendo a tupla em lista
    lista_numero.append(num_ale) # adicionando os números aleatórios na lsita
    numero = tuple(lista_numero) # convertendo a lista em número novamente

    # inicia as variaveis com o primeiro número da tupla
    maior = menor = numero[0]
    
    # percorre a tupla e atualiza o maior e menor 
    for n in numero:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
            

print(numero)
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
