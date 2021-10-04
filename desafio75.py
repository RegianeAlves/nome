num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
contDe9 = contDe3 = contPar = 0
print(f'Você digitou os valores: {(num1, num2, num3, num4)}')

for c in range(0, 4):
    if tupla[c] == 9:
        contDe9 += 1
    if tupla[c] == 3:
        contDe3 += 1
    if tupla[c] % 2 == 0:
        contPar += 1
        if contPar == 1:
            print(f'Os valores pares digitados foram {tupla[c]}', end=' ')
        else:
            print(tupla[c], end=' ')
print(' ')
if contDe3 != 0:
    print(f"O valor 3 apareceu na {tupla.index((3) + 1)}ª posição")
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'O valor 9 apareceu {contDe9} vezes')
