nome = input('Digite seu nome completo: ').strip()
nome1 = nome.upper()
teste = ('SILVA' in nome1)
print('O nome: {} possui SILVA em sua composição? {} '.format(nome1, teste))