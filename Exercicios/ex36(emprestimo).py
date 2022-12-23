emprestimo = float(input('Qual o valor do emprestimo? '))
salario = float(input('Qual é o seu salário mensal? '))
qtdAnos = int(input('Quantos anos pretende pagar '))
limite = int(30)

qtdPrestacoes = qtdAnos*12
valorPrestacoes = emprestimo / qtdPrestacoes
porcentagem = (valorPrestacoes * 100) / salario

if porcentagem > limite:
    print('O valor da prestação, que é de R${:.2f}, consome {:.2f}% do seu salario, portanto infelizmente seu emprestimo foi NEGADO!'.format(valorPrestacoes,porcentagem))

else:
    print('O valor da prestação que é de R${:.2f}, consome {:.2f}% do seu salario, portanto seu empréstimo foi APROVADO! \n Parabéns!! '.format(valorPrestacoes,porcentagem))