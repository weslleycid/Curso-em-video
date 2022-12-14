velocidade = int(input('Qual a velocidade do carro? '))
limite = int(80)
multa = float((velocidade - limite)*7)
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade da via ')
    print('Velocidade maxima permitida {} KM/H'.format(limite))
    print('Velocidade atiginda {} KM/H'.format(velocidade))
    print('O valor da multa: R${:.2f} '.format(multa))