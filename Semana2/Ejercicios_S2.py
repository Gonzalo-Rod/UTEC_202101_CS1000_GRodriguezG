#Ej 9 13

base = 8
num = int(input("Elige el numer que quieres convertir [587 / 3054]: "))

#Primera ZeroDivisionE
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

# Terceras division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

#Cuarta Divisin
residuo = cociente % base
cociente = cociente // base
n4 = residuo

print("{} = {}{}{}{}".format(num, n4, n3, n2, n1))