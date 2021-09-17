import random
palpites = 0
n = int(input('Digite um número de 0 a 10: '))
num = random.randint(0, 10)
while n != num:
    print('Você errou! Digite outro número: ')
    n = int(input('Digite um número de 0 a 10: '))
    palpites += 1
if n == num:
    palpites += 1
    print('Parabéns você acertou!')
    print('Com {} tentativas'.format(palpites))


