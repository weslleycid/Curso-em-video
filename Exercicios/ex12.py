preco = float(input('Digite o preço do produto: '))
desc = (preco * 5)/100
resultado = preco - desc

print('O preco atual do produto é R${}. \n'
      'Você receberá de desconto R${:.2f} equivalente a 5% do valor do produto. \n'
      ' O preço final com desconto é R${:.2f} '. format(preco, desc, resultado))