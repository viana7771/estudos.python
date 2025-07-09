n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('só mais um agr: '))
if n1 > n2 > n3:
    print(f'{n1} é o maior numero e {n3} é o menor')
elif n2 > n1 > n3:
    print(f'{n2} é o maior numero e {n3} é o menor')
elif n2 > n3 > n1:
    print(f'{n2} é o maior numero e {n1} é o menor')
elif n3 > n1 > n2:
    print(f'{n3} é o maior numero e {n2} é o menor')
else:
    print(f'{n3} é o maior numero e {n1} é o menor')