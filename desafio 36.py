casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos = int(input('Quantos anos vai pagar: '))
m = anos * 12
c = casa / m
s = salario * 0.30
if s >= c:
    print('emprestimo aprovado!')
else:
    print('emprestimo negado!')
