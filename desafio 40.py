nota1 = float(input('Digite a primera nota:  '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 5 and media <= 6.9:
    print('Você tirou {:.2f}, você está de recuperação! Estude mais'.format(media))
elif media >= 7.0:
    print('Você tirou {:.2f}, você foi aprovado parabéns!'.format(media))
else:
    print('Você tirou {:.2f}, você foi reprovado! Estude mais'.format(media))
