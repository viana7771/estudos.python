s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
            s += i
            c += 1
print(f'a soma dos {c} numeros solicitados é de {s}.')