m = float(input('Digite o valor: '))
cm = m*100
mm = m*1000
km = m/1000
dam = m/10
hm = m/100

print('{} metros é igual a \n'
      '{} centimetros \n'
      '{} milimetros\n'
      '{} Kilomentros\n'
      '{} dam\n'
      '{} hm' .format(m, cm, mm, km, dam, hm))