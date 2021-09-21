contador = 0
maior = 0
menor = 0
soma = 0
opcao = 0
while opcao != 2:
    num = int(input('Digite um número: '))
    print('''Quer continuar?
    [ 1 ] Sim
    [ 2 ] Não''')
    opcao = int(input('Qual opção? '))
    soma = soma + num
    contador += 1
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print('O maior número foi {}, e o menor foi {}'.format(maior, menor))
media = soma / contador
print('A média dos números foi {:.2f}'.format(media))
