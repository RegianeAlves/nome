palavras = ('coca', 'lasanha', 'esfiha', 'pizza',
            'coxinha', 'hamburguer', 'pudim', 'cafe',
            'brigadeiro', 'churrasco', 'sushi', 'beijinho')

for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c]} temos ',end='')
    quantA = palavras[c].count('a')
    if quantA > 0:
        for a in range(0, quantA):
            print('a',end=' ')
    quantE = palavras[c].count('e')
    if quantE > 0:
        for e in range(0, quantE):
            print('e',end=' ')
    quantI = palavras[c].count('i')
    if quantI > 0:
        for e in range(0, quantI):
            print('i',end=' ')
    quantO = palavras[c].count('o')
    if quantO > 0:
        for o in range(0, quantO):
            print('o',end=' ')
    quantU = palavras[c].count('u')
    if quantU > 0:
        for u in range(0, quantU):
            print('u',end=' ')
    print('')
