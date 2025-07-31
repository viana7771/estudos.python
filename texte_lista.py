num = [15, 4, 6, 301, 99]
num.append(2043)
num.sort(reverse=True)
num.pop()
num.append(8)
if 300 in num:
    num.remove(300)
print(num)
print(f'Essa lista tem {len(num)} índices.')