primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
num = 0

while cont <= 10:
    print('Posição: {} / Valor: {}'.format(cont, primeiro))
    primeiro = primeiro + razao
    cont += 1

print('''Você quer mostrar mais alguns termos? 
    [ 1 ] Sim
    [ 2 ] Não''')
num = int(input('Qual opção? '))
if num == 1:
    quant = 1
    while quant != 0:
        print('Digite 0 para sair do programa')
        quant = int(input('Digite a quantidade de termos: '))
        if quant != 0:
            quant += cont
            while cont <= quant - 1:
                print('Posição: {} / Valor: {}'.format(cont, primeiro))
                primeiro = primeiro + razao
                cont += 1
        else:
            print('Você saiu do programa! Tchau')

else:
    print('Você saiu do programa! Tchau')