import random
lista = ['pedra', 'papel', 'tesoura']
random.shuffle(lista)
aleatorio = str(input('Escolha entre: Pedra,papel ou tesoura: '))
if aleatorio == lista[0]:
    print('Deu empate! Eu escolhi: {}, Você escolheu: {}'.format(lista[0], aleatorio))
elif aleatorio == 'pedra' and lista[0] == 'tesoura':
    print('Parabens você ganhou! Eu escolhi: {}, Você escolheu: {}'.format(lista[0], aleatorio))
elif aleatorio == 'papel' and lista[0] == 'pedra':
    print('Parabens você ganhou! Eu escolhi: {}, Você escolheu: {}'.format(lista[0], aleatorio))
elif aleatorio == 'tesoura' and lista[0] =='papel':
    print('Parabens você ganhou! Eu escolhi: {}, Você escolheu: {}'.format(lista[0], aleatorio))
else:
    print('Você perdeu! Eu escolhi: {}, Você escolheu: {}'.format(lista[0], aleatorio))
