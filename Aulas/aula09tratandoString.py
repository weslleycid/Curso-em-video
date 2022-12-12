# Em um fatiamento de string o ultimo numero não entra no resultado. EX:
frase = 'Curso em video python'
print(frase[0:4])
# Nesse caso ele retornou 'curs' pois na contagem que começa em zero a casa 4 serio O porém o termo identificado
# na casa 4 não entra na reprrodução, ou seja, sempre mostrará uma casa a menos do que o numero inserido ao fim.
print(frase[9:21:2])
# mostra do 9 ao 21 pulando de dois em dois
print(frase[:5])
# nesse caso ele começa da casa 0
print(frase[15:])
# Nesse caso ele começa no 15 e vai até o último caracter
#Analise

# comprimento
print(len(frase))

# contando a quantidade de vezes que aparece uma letra especifica \ Lembrando que ele diferencia maiusculas de minusculas.
print(frase.count('o'))
# contando a quantidade de vezes que aparece uma letra dentro de um intervalo
print(frase.count('o',0,13))
# encontrando o termo deo, neste caso ele apresenta onde o numero do caracter inicial
print(frase.find('deo'))
# quando se usa find em na busca de um termo que não existe ele retorno o -1 indicando não existir tal expressão
print(frase.find('por'))
# Pesquisando tal termo dentro da variável frase, ele retorna True ou False. Lembrando que há diferenciação entre maiusculas e minusculas
print('Curso' in frase)
# esse metodo substitui determinado termo dentro da variável caso ela exista por outra. Neste caso a primeira será substituida pela segunda
frase.replace('Curso','Treinamento')
print(frase)

# esse metodo coloca toda a string em frase em letras MAIUSCULA
print(frase.upper())
# Coloca toda a string de frase em minusculas
print(frase.lower())
# Inicia a string de frase em Maiuscula e o restante em minuscula
print(frase.capitalize())
# Coloca o inicio de cada palavra de frase em maiuscula
print(frase.title())
frase1 = '   Vc vai ser o melhor programador do Brasil   '
print(frase1)
# função strip remove espaços 'inuteis'

print(frase1.strip()) #todos
print(frase1.rstrip()) #a Direita
print(frase1.lstrip()) #A esquerda
# Divide a frase em listas que partem e se encerram nos espaços.
dividir = frase.split()
# apresentou o primeiro item da lista.
print(dividir[0])
# Apresentou a quarta letra do primeiro item da lista.
print(dividir[0][3])



