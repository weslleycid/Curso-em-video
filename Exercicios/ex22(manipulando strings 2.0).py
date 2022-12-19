nome = input('Digite seu nome: ').s

print(nome.upper())
print(nome.lower())
print('Seu nome Possui: {} letras'.format(len(nome.replace(' ',''))))
nomed = nome.split()
print('Seu Primeiro nome tem: {} letras '.format(len(nomed[0])))
