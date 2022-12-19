A = float(input('Digite a altura:'))
L = float(input('Digite a largura: '))
Area = A*L
tinta = 2
qtd = Area / tinta

print('A altura é {} \n A largura é {} \n a area {}m² \n A quantidade de latas de tinta necessárias é {:.2f}L de tinta  '.format(A, L, Area, qtd))
