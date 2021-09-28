from random import randint

contador = 0
while True:
    aleatorio = randint(0, 10)
    n = int(input('Diga um valor: '))
    soma = aleatorio + n
    n2 = ' '
    while n2 not in 'SI':
        n2 = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    if soma % 2 == 0:
        print(f'O computador pensou em {aleatorio} e você jogou {n}. A Soma deu {soma} deu Par')
        if n2 == 'P':
            print('Parabens você venceu!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    else:
        print(f'O computador pensou em {aleatorio} e você jogou {n}. A Soma deu {soma} deu Impar')
        if n2 == 'I':
            print('Parabens você venceu!')
            contador += 1
        else:
            print('Você perdeu!')
            break

print(f'Você venceu {contador} vezes')
