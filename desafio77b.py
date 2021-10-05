palavras = ('coca', 'lasanha', 'esfiha', 'pizza',
            'coxinha', 'hamburguer', 'pudim', 'cafe',
            'brigadeiro', 'churrasco', 'sushi', 'beijinho')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c]} temos ', end='')
    for vogal in range(0, len(vogais)):
        quant = palavras[c].count(vogais[vogal])
        for quantV in range(0, quant):
            print(vogais[vogal], end=' ')
    print('')
