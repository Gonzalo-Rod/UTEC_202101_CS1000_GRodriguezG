# Ej 7

base = 2
num = 254

#Primera Division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

# Terceras division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta Division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta Division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta Division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima Division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava  Division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

print("{} = {}{}{}{}{}{}{}{}".format(num,bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))