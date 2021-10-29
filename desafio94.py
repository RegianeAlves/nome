cont = soma = 0
lista = []
dicionario = {}

while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if dicionario['sexo'] not in 'MmFf':
        dicionario['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dicionario['idade'] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N] '))
    cont += 1
    soma += dicionario['idade']
    media = soma / cont
    lista.append(dicionario.copy())

    if continuar in 'Nn':
        break
print('-=' * 25)

print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for dic in lista:
    for key, valor in dic.items():
        if key == 'sexo' and valor == 'F':
            print(dic["nome"], end=' ')

print('\n- Lista de pessoas acima da média: ')
for dic in lista:
    for key, valor in dic.items():
        if key == 'idade' and valor >= media:
            print(f'nome = {dic["nome"]}; sexo = {dic["sexo"]}; idade = {dic["idade"]};')

print('>>>ENCERRADO<<<')




