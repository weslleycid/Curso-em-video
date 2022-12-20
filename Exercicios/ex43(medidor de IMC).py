peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = float(peso/(altura*altura))
print('Seu IMC é igual a {:.2f}'.format(imc))
if imc < 16:
    print('Você está muito abaixo do peso ideal, procure ajuda médica')
elif imc == 16 or imc <17:
    print('Você está abaixo do peso!')
elif imc == 17 or imc <18.5:
    print('Você está um pouco abaixo do peso')
elif imc == 18.5 or imc <25:
    print('Você está no peso ideal!\n'
          'Parabéns!!\n Continue se cuidando!')
elif imc == 25 or imc < 30:
    print('Você está com sobrepeso, cuide-se')
elif imc == 30 or imc < 35:
    print('obesidade grau 1 ATENÇÃO!!')
else:
    print('Obesidade SEVERA!\n '
          'Procure ajuda IMEDIATAMENTE!')
