altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é: {:.2f}, Você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é: {:.2f}, Você está com o peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é: {:.2f}, Você está com obesidade!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é: {:.2f}, Você está com sobrepeso!'.format(imc))
else:
    print('Seu IMC é: {:.2f}, Você está com obesidade mórbida!'.format(imc))