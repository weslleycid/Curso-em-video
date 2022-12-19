velocidade = int(input('Qual a velocidade do carro? '))
limite = int(80)
multa = float((velocidade - limite)*7)
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade da via ')
    print('Velocidade maxima permitida {} KM/H'.format(limite))
    print('Velocidade atiginda {} KM/H'.format(velocidade))
    print('\033[7:30:41mO valor da multa: R${:.2f} \033[m'.format(multa)) # O sete no tipo de texto causa a
    # inversão de cores entre cor do terminal e cor do texto