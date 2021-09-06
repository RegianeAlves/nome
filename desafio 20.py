import random
n = input('Nome 1 ')
n2 = input('Nome 2 ')
n3 = input ('Nome 3 ')
n4 = input('Nome 4 ')
l = [n, n2, n3 ,n4]
random.shuffle(l)
print('a ordem de apresentação é: ')
print(l)