primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('Posição: {} / Valor: {}'.format(cont, primeiro))
    primeiro = primeiro + razao
    cont += 1