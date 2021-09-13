maior = 0
menor = 500
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor))

