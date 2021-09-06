nome = input('Digite uma frase: ').upper().strip()
print('aparece {} vezes a letra A'.format(nome.count('A')))
print('primeira vez {}'.format(nome.find('A')))
print('ultima vez {}'.format(nome.rfind('A')))

