info = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(info))
print('Só espaços? ', info.isspace()) #verifica se a só espaços
print('É um numero?', info.isnumeric()) #Verifica se é um numero
print('É alfabetico? ', info.isalpha()) #Verifica se alfabetico
print('É alfanumerico? ', info.isalnum()) #verifica se é alfanumerico
print('Está em maiusculas? ', info.isupper()) #verifica se está em maiuscula
print('Está em minusculas? ', info.islower()) #verifica se está em minusculas
print('Está capitalizada? ', info.istitle()) #Verifica se está capitalizada