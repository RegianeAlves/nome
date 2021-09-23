contador = 0
n = 0
num = 0
while n != 999:
    num = num + n
    n = int(input('Digite um número: (Digite [999] para parar!) '))
    contador += 1
print('A soma desses números é: {}'.format(num))
print('Números digitados {}'.format(contador - 1))
print('Tchau!')
