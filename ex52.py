n = int(input('Digite um número: '))
d = 0
for c in range(1, n + 1):
    if n % c == 0:
        d += 1
        print('\033[0;32m', end=' ')
    else:
        print('\033[0;31m', end=' ')
    print(c, end=' ')
print(f'\n\033[m O número {n} foi divisível {d} vezes.')
if d == 2:
    print(f' {n} É UM NÚMERO PRIMO.')
else:
    print(f' {n} NÃO É UM NÚMERO PRIMO.')