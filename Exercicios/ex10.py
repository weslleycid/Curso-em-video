c = float(input('Digite quanto vc tem: '))
d = 5.37
e = 5.98
compraDolar = c/d
compraEuro = c/e
print('Você tem {} reais o dolar atualmente custa {} reais \n convertendo, você comprará {:.2f} dolares \n'
      'e {:.2f} Euros'.format(c, d, compraDolar, compraEuro))