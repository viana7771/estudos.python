loja_games = (
    "Console PlayStation 5", 4499.99,
    "Xbox Series X", 4299.99,
    "Nintendo Switch OLED", 2499.99,
    "Controle DualSense", 349.90,
    "Controle Xbox", 299.90,
    "Jogo God of War: Ragnarök", 249.90,
    "Jogo Elden Ring", 199.90,
    "Headset Gamer", 399.90,
    "Cadeira Gamer", 899.90,
    "Gift Card PSN R$100", 100.00
)
print('-'*80)
print(f'{'COMPANIA DOS GAMES':-^80}') # Centraliza com traços
print('-'*80)
print()

# Percorre os índeces da tupla de 0 até o fim
for i in range(0, len(loja_games)):
    if i % 2 == 0:
        # Nome do produto (índece par)
        print(f'{loja_games[i]:.<40}', end='')
    if i % 2 != 0:
        # Nome do produto (índece ímpar)
        print(f'R${loja_games[i]:.>40}') # Formata o preço alinhado a direita
print()
print('-'*80)