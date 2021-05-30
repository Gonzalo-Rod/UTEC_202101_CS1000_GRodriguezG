base = 8
num = int(input("Elige el numer que quieres convertir [13 / 18]: "))

#Primera ZeroDivisionE
residuo = num % base
cociente = num // base

print("{} = {}{}".format(num, cociente, residuo))