num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num = 0
while num != 5:
    print('''Oque você quer fazer com eles? 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa''')
    num = int(input('Qual opção? '))
    if num == 1:
        n = num1 + num2
        print('A soma é {}'.format(n))
    elif num == 2:
        n = num1 * num2
        print('O resultado da multiplicação é {}'.format(n))
    elif num == 3:
        if num1 == num2:
            print('Os dois números {} e {} são iguais'.format(num1, num2))
        elif num1 > num2:
            print('O número {} é maior que o número {}'.format(num1, num2))
        else:
            print('O número {} é maior que o número {}'.format(num2, num1))
    elif num == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif num == 5:
        print('Saindo do programa! Tchau')



