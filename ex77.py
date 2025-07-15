palavras = (
    'APRENDER',
    'PROGRAMA',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO'
)

for i in palavras:
    vogais = []
    for letras in i:
        if letras in ['A', 'E', 'I', 'O', 'U', 'ÃO']:
            vogais.append(letras)
    print(f'NA palavra {i} temos:', *tuple(vogais))
