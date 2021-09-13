soma = 0
maior = 0
contador = 0
velho = 0
for c in range(0, 3):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (homem/mulher): ')
    soma = soma + idade
    if idade > maior and sexo == 'homem':
        velho = nome
        maior = idade
    if idade <= 21 and sexo == 'mulher':
        contador = contador + 1
somaidade = soma / 4
print('A média de idade é {} anos'.format(somaidade))
print('O homem mais velho tem {} anos, e se seu nome é {}'.format(maior, velho))
print('{} mulher(es) tem menos de 21 anos!'.format(contador))