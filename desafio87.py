numeros = []
num = []
soma = s = cont = 0

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [0, {c}]: ')))
numeros.append(num[:])
cont += numeros[0][2]
num.clear()

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [1, {c}]: ')))
    m = max(num)
numeros.append(num[:])
cont += numeros[1][2]
num.clear()

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [2, {c}]: ')))
numeros.append(num[:])
cont += numeros[2][2]
num.clear()

for c in range(0, 3):
    for v in range(0, 3):
        if numeros[c][v] % 2 == 0:
            soma += numeros[v][c]
    s += numeros[c][2]

# for valores in numeros:
#     for valor in valores:
#         if valor % 2 == 0:
#             soma += valor
#     s += valores[2]

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {s}')
print(f'O maior valor da segunda linha é {m}')
print(max(numeros[1]))
print(cont)