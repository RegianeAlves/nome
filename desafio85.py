valores = []
pares = []
impares = []

for v in range(1, 8):
    num = int(input(f'Digite o {v}o. valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)


valores.append(pares)
valores.append(impares)
valores.sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')