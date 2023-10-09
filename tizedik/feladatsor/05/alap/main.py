def take_int(msg, range_start=None, range_end=None):
  while True:
    try:
            
      num = int(input(msg))
      if range_start == None and range_end == None:
        return num
      elif range_start <= num <= range_end:
        return num
      else:
        print(f"A megadott szám nem esik a {range_start}-{range_end} intervallumba!")
    except ValueError:
      print("A megadott érték nem szám!")

# 1. feladat
a = take_int("Kérek egy számot 1-10: ", 1, 10)

for i in range(1, a+1):
  print(f"{i}. Egy fecske nem csinál nyarat.")

# 2. feladat
a = take_int("Kérek egy számot 1-10: ", 1, 10)

for i in range(1, a+1):
  print(f"Megmondtam már {i}-szer, hogy semmit nem mondok el kétszer.")


# 3. feladat
for i in range(0, 51):
  print(i)

for i in range(182, 213):
  print(i)

for i in range(100, 201, 2):
  print(i)

for i in range(89, 56, -2):
  print(i)

for i in range(1, 21):
  print(f"{i} {i**2}")

for i in range(99, 0, -3):
  print(i)

for i in range(101, 49, -5):
  print(i*2)

for i in range(1, 1001):
  if i == 1000:
    print(i, end=".")
  else:
    print(i, end=", ")

for i in range(1000, 0, -3):
  print(i, end=", ")


# 4. feladat
#Írjunk ki a képernyőre 100 db csillagot!
#▪ Írjunk ki a képernyőre bekért darabszámú, bekért karaktert!
#▪ Kérjünk be egy szöveget, majd keretezzük körbe csillagokkal!
#▪ Rajzoljunk le egy 8*8-as sakktáblát csillagokból és szóközökből!


