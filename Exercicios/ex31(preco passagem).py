viagem = float(input('Distancia da viagem: '))

if viagem<=200:
    print('Teste')
    c=viagem*0.50
    print('O preço da viagem para seu destino é: R${:.2f}'.format(c))
elif viagem>200:
    c=viagem*0.45
    print('A viagem para o destino escolhido custará: R${:.2f}'.format(c))