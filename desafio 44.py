preconormal = float(input('Digite o preço do produto: '))
print('Escolha o número com base no método de pagamento: ')
print('1 - A vista: Dinheiro/Cartão: 10% de desconto!')
print('2 - A vista no cartão: 5% de desconto!')
print('3 - Em até 2x no cartão: preço normal!')
print('4 - 3x ou mais no cartão: 20% de juros!')
pagamento = int(input())
if pagamento == 3:
    parcela = preconormal / 2
    print('Sua compra sera parcelada em 2x de: R$ {:.2f}!'.format(parcela))
elif pagamento == 1:
    n1 = preconormal - (preconormal * 0.10)
    print('A vista no dinheiro/cartão o valor fica: R$ {:.2f}!'.format(n1))
elif pagamento == 2:
    n2 = preconormal - (preconormal * 0.05)
    print('A vista no cartão o valor fica: R$ {:.2f}!'.format(n2))
elif pagamento == 4:
    n3 = preconormal + (preconormal * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = n3 / totparc
    print('Sua compra sera parcelada em {}x de R$ {:.2f} com juros'.format(totparc, parcela))
else:
    print('Opção invalida de pagamento.Tente novamente!')




