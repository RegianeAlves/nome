import random
n = int(input('Digite um numero: '))
num = random.randint(0, 5)
print('Você venceu!' if n==num else 'Você perdeu')
