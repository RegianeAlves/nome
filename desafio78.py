valores = []
for posicao in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {posicao}: ')))

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for posicao in range(0, 5):
    if valores[posicao] == max(valores):
        print(f'{posicao + 1}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for posicao in range(0, 5):
    if valores[posicao] == min(valores):
        print(f'{posicao + 1}...', end='')

# num = []
# num.append(int(input('Digite um valor posição 0: ')))
# num.append(int(input('Digite um valor posição 1: ')))
# num.append(int(input('Digite um valor posição 2: ')))
# num.append(int(input('Digite um valor posição 3: ')))
# num.append(int(input('Digite um valor posição 4: ')))
# num[2] = 3
