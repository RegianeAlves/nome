from datetime import date

ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print('Idade {} anos, você é da Categoria Mirim'.format(idade))
elif idade <= 14:
    print('Idade {} anos, você é da Categoria Infantil'.format(idade))
elif idade <= 19:
    print('Idade {} anos, você é da Categoria Junior'.format(idade))
elif idade <= 20:
    print('Idade {} anos, você é da Categoria Sênior'.format(idade))
else:
    print('Idade {} anos, você é da Categoria Master'.format(idade))