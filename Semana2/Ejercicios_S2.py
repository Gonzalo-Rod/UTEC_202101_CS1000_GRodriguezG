base = 16
num = 48

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

if n1 == 10:
  n1 = "a"

elif n1 == 11:
  n1 = "b"

elif n1 == 12:
  n1 = "c"

elif n1 == 13:
  n1 = "d"

elif n1 == 14:
  n1 = "e"

elif n1 == 15:
  n1 = "f"

if n2 == 10:
  n2 = "a"

elif n2 == 11:
  n2 = "b"

elif n2 == 12:
  n2 = "c"

elif n2 == 13:
  n2 = "d"

elif n2 == 14:
  n2 = "e"

elif n2 == 15:
  n2 = "f"

print("{} = {}{}".format(num, n2, n1))