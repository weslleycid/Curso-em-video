import math
an = float(input('Digite o angulo desejado: '))
seno = math.sin(math.radians(an))
print('O seno de {} é {:.2f} '.format(an,seno))
coseno = math.cos(math.radians(an))
print('O coseno de {} é {:.2f} '.format(an,coseno))
tangente = math.tan(math.radians(an))
print('A tengente de {} é {:.2f} '.format(an,tangente))
