#Ej 14

base = 2
num = 5785

#Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

#Tercera division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

#Novena division
residuo = cociente % base
cociente = cociente // base
bit9 = residuo

#Decima division
residuo = cociente % base
cociente = cociente // base
bit10 = residuo

#Undecima division
residuo = cociente % base
cociente = cociente // base
bit11 = residuo

#Duodecima division
residuo = cociente % base
cociente = cociente // base
bit12 = residuo

#Trigesima division
residuo = cociente % base
cociente = cociente // base
bit13 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}{}{}{}".format(num, bit13, bit12, bit11, bit10, bit9, bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))
