nomeCompleto = str(input('Digite seu nome completo: ')).strip()
nomeCompleto1 = nomeCompleto.upper()#,nomeCompleto.split(), nomeCompleto.strip()
print(nomeCompleto1)
print('A letra A aparece {} vezes'.format(nomeCompleto1.count('A')))
print('A letra apareceu A apareceu a primeira vez na posição {}'.format(nomeCompleto1.find('A')+1))
print('A letra apareceu A apareceu pela ultima vez na posição {}'.format(nomeCompleto1.rfind('A')+1))