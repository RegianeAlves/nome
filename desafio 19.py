import random
nome = input('nome 1: ')
nome2 = input('nome 2: ')
nome3 = input('nome 3: ')
nome4 = input('nome 4: ')
l = [nome, nome2, nome3, nome4]
r = random.choice(l)
print('O nome escolhido é: {}'.format(r))
