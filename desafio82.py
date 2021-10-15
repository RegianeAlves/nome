valores = []
pares = []
impares = []

while True:
    valor = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    valores.append(valor)
    #     pares.append(valor)
    # if valor % 2 == 0:
    # else:
    #     impares.append(valor)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for p in range(0, len(valores)):
    if valores[p] % 2 == 0:
        pares.append(valores[p])
    else:
        impares.append(valores[p])

print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
