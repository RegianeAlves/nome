contador = 0
n = 0
num = 0
while n != 999:
    num = num + n
    n = int(input('Digite um número: '))
    contador += 1
print(num)
print('Números digitados {}'.format(contador - 1))
print('Tchau')
