valores = []
cont = 0
while True:
    valor = (int(input('Digite um valor: ')))
    for posicao in range(0, len(valores)):
        if valores[posicao] == valor:
            cont += 1
    if cont == 0:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = 0
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':  # while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

valores.sort()
print(f'Você digitou os valores {valores}')
