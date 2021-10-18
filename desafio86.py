numeros = []
num = []

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [0, {c}]: ')))
numeros.append(num[:])
num.clear()

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [1, {c}]: ')))
numeros.append(num[:])
num.clear()

for c in range(0, 3):
    num.append(int(input(f'Digite um valor para [2, {c}]: ')))
numeros.append(num[:])
num.clear()

print(f'{numeros[0]}')
print(f'{numeros[1]}')
print(f'{numeros[2]}')
