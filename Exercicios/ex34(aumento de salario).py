salario = float(input('Qual é o seu salário? '))

print('Parabéns!! Você recebeu um aumento!')
if salario < 1.250:
    aumento = salario+(salario*0.15)

    print('Você receneu um aumento de 15% seu novo salário é {:.2f} '.format(aumento))

else:
   aumento = salario+(salario*0.10)

   print('Voc^recebeu um aumento de 10% seu novo salário é: {:.2f}'.format(aumento))