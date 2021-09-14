primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ultimo = (razao * 10) + primeiro
#ultimo = primeiro + (10 - 1) * razao
#for c in range(primeiro, ultimo + razao, razao):
i = 0
for c in range(primeiro, ultimo, razao):
    i += 1
    print('Posição: {} / Valor: {}'.format(i, c))