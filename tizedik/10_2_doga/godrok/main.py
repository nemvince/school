with open("melyseg.txt", "r", encoding="utf-8") as f:
  data = [int(e) for e in f.read().strip().split("\n")]

# 1. feladat
print(f"A fájl adatainak száma: {len(data)}")

# 2. feladat
try:
  distance = int(input("Adjon meg egy távolságértéket!"))
except ValueError:
  print("Nem számot adott meg!")
  exit()
print(f"Ezen a helyen a felszín {data[distance]} méter mélyen van.")

# 3. feladat
percent_untouched = round(data.count(0) / len(data) * 100, 2)
print(f"Az érintetlen terület aránya {percent_untouched}%.")

# 4. feladat
craters = 0

with open("godrok.txt", "w", encoding="utf-8") as f:
  # t.u azt mondta jo de a feladat szerint nem igy kene
  #for index, entry in enumerate(data):
  #  f.write(f"A {index+1}. gödör {entry}m mély.\n")

  temp = []

  for entry in data:
    if entry:
      temp.append(entry)
    else:
      if len(temp) != 0:
        craters += 1
        f.write(' '.join([str(e) for e in temp])+'\n')
      temp = []

# 5. feladat
print(f"A gödrök száma: {craters}")

# 6. feladat
if data[distance]:
  start = distance
  while data[start] != 0:
    start -= 1
  start += 1

  end = distance
  while data[end] != 0:
    end += 1

  print("a)")
  print(f"A gödör kezdete: {start+1} méter, a gödör vége: {end} méter.")

  depth = max(data[start:end])
  print("b)")
  print(f"A legnagyobb mélysége {depth} méter.")

  isdeepening = True
  for index in range(start, end):
    if data[index] < data[index+1]:
      isdeepening = False
      break

  print("c)")
  print("Folyamatosan mélyül" if isdeepening else "Nem mélyül folyamatosan.")

  print("d)")
  print(f"A gödör térfogata {sum(data[start:end])*10} m^3.")

  print("e)")
  water = 0
  for index in range(start, end):
    if data[index] >= 1:
      water += data[index] - 1
  print(f"A vízmennyiség {water*10} m^3.")
  
else:
  print("Az adott helyen nincs gödör.")