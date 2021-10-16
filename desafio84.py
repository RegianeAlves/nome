pessoas = []
dados = []
cont = maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    for pessoa in pessoas:
        if cont == 1:
            maior = pessoa[1]
            menor = pessoa[1]
        else:
            if pessoa[1] > maior:
                maior = pessoa[1]
            elif pessoa[1] < menor:
                menor = pessoa[1]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi {maior}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end=' | ')
print(f'\nO menor peso foi {menor}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end=' | ')