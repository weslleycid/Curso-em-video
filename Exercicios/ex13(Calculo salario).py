S = float(input('Digite o seu Salario: '))
aumento = (S*15)/100
newSalario = S+aumento

print('Seu sálario é R${:.2f} \n Você recebeu um aumento de 15% que dá um total de R${:.2f} \n'
      'Seu novo Salario é R${:.2f}'.format(S, aumento, newSalario))