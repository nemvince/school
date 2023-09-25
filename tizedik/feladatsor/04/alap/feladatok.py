# 1. feladat
try: 
  a = int(input("Kérek egy számot: "))
  b = int(input("Kérek egy másik számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a > 0 and b > 0:
  print(True)
else: print(False)

if a < 4 and b != 6:
  print(True)
else: print(False)

if a == 0 or b == 0:
  print(True)
else: print(False)

if a == 5 or b != 4:
  print(True)
else: print(False)

# majd a többi feladatot is megoldom itt a későbbiekben (ha lesz időm) :D
if a:
  pass