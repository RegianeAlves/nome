total = mais = menos = contador = nomeMenor = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preco
    contador += 1
    if contador == 1:
        menos = preco
    else:
        if preco < menos:
            menos = preco
            nomeMenor = nome
    if preco >= 1000:
        mais += 1
    if continuar == 'N':
        break
print(f'O total da compra foi R${total}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenor} que custa R${menos}')
