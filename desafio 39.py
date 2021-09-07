from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
s = 18 - idade

if idade < 18:
    print('Você tem {} anos, ainda falta {} anos para se alistar'.format(idade, s))
elif idade == 18:
    print('Você tem {} anos, está na hora de se alistar'.format(idade))
else:
    s2 = idade - 18
    print('Você tem {} anos, já passou {} anos do tempo de se alistar'.format(idade, s2))
