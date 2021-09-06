preconormal = float(input('Digite o preço normal do produto: '))
print('Escolha o número com base no método de pagamento: ')
print('1 - A vista: Dinheiro/Cartão: 10% de desconto!')
print('2 - A vista no cartão: 5% de desconto!')
print('3 - Em até 2x no cartão: preço normal!')
print('4 - 3x ou mais no cartão: 20% de juros!')
pagamento = int(input())
if pagamento == 3:
    print('2x no cartão o valor fica normal: {:.2f}!'.format(preconormal))
elif pagamento == 1:
    n1 = preconormal - (preconormal * 0.10)
    print('A vista no dinheiro/cartão o valor fica: {:.2f}!'.format(n1))
elif pagamento == 2:
    n2 = preconormal - (preconormal * 0.05)
    print('A vista no cartão o valor fica: {:.2f}!'.format(n2))
elif pagamento == 4:
    n3 = preconormal + (preconormal * 0.20)
    print('3x ou mais no cartão o valor fica: {:.2f}!'.format(n3))



