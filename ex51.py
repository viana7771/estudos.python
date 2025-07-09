print('='*10)
print('10 TERMOS DE UMA PA')
print('='*10)
p = int(input('Primeiro termo: '))
r = int(input('A razão: '))
d = (10 + p) * r
for i in range(p, d, r):
    print(i, end=' ➡️  ')
print('ACABOU')