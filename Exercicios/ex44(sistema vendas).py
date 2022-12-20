preco = float(input('Digite o valor do produto R$: '))

op = str(input(
                   '[1] À vista DINHEIRO / DEBITO / PIX\n'
                   '[2] Cartão de crédito à vista\n'
                   '[3] 2 x no cartão de crédito\n'
                   '[4] 3 x no cartão de crédito\n'
                   'Escolha a forma de pagamento: '))

while op != '1' and op != '2' and op != '3' and op != '4':
    op = str(input(
                   '[1] À vista DINHEIRO / DEBITO / PIX\n'
                   '[2] Cartão de crédito à vista\n'
                   '[3] 2 x no cartão de crédito\n'
                   '[4] 3 x no cartão de crédito\n'
                    'Escolha a forma de pagamento: '))

if op == '1':
    desc = preco - ((preco*10)/100)
    print('Você recebeu um desconto de 10%')
    print('Preço a pagar R${:.2f}'.format(preco - preco*10/100))
elif op =='2':
    print('Você recebeu um desconto de 5%')
    print('preço a pagar R${:.2f}'.format(preco - preco*5/100))
elif op == '3':
    print('São 2 parcelas de R${:.2f}'
          'O valor a pagar é R${:.2f}'.format(preco/2, preco))
else:
    vezes = int(input('Digite o número de parcelas: '))
    juros = preco*20/100
    print('Preço do produto: R${:.2f}\n '
          'são {} parcelas de R${:.2f}\n'
          'Preço a pagar: R${:.2f}'.format(preco,vezes, (preco+juros)/vezes, preco + juros ))