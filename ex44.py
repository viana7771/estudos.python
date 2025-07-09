preco = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTOS')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    desconto10 = preco - (preco * 0.1)
    print(f'Sua compra de R${preco:.2f} vai custar {desconto10:.2f}')
elif opcao == 2:
    desconto5 = preco - (preco * 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar {desconto5:.2f}')
elif opcao == 3:
    print(f'Sua compra vai custar {preco:.2f}')
else:
    juros = preco + (preco * 0.2)
    print(f'Sua compra de {preco:.2f} vai custar {juros:.2f}')