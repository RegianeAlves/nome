frase = input('Digite uma frase: ')
fraseInvertida = frase[::-1]
v = "".join(frase.split())
v2 = "".join(fraseInvertida.split())
if v == v2:
    print('A frase {} é políndromo!\nA frase invertida fica: {}'.format(frase, fraseInvertida))
else:
    print('A frase {} não é políndromo!\nA frase invertida fica: {}'.format(frase, fraseInvertida))