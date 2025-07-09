s = 0
c = 0 
for i in range(6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'A soma dos {c} numeros pares que foram digitados é {s}')