soma = 0
contador = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        contador += contador
print('você informou {} números pares e a soma foi {}'.format(contador, soma))

