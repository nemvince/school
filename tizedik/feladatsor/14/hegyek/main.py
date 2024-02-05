with open("hegyekMo.txt") as f:
    hegyek = [s.strip() for s in f.readlines()[1:]]

hegyek = [s.split(";") for s in hegyek]

print("3. feladat")
print(f"A fájlban {len(hegyek)} hegy található")

print("4. feladat")
atlag = sum([int(s[2]) for s in hegyek]) / len(hegyek)
print(f"A hegyek átlagos magassága: {atlag:.2f}")

print("5. feladat")
legmagasabb = max(hegyek, key=lambda x: int(x[2]))
print(f"A legmagasabb hegy adatai:")
print(f"Név: {legmagasabb[0]}")
print(f"Magasság: {legmagasabb[1]}")
print(f"Hely: {legmagasabb[2]}")

print("6. feladat")
n = int(input("Kérem adjon meg egy magasságot: "))
borzsony = any([s for s in hegyek if s[1] == "Börzsöny" and int(s[2]) > n])
if borzsony:
  print("Van Börzsönyben " + str(n) + "m-nél magasabb csúcs")
else:
  print("Nincs Börzsönyben " + str(n) + "m-nél magasabb csúcs")

print("7. feladat")
print(f"3000 lábnál magasabb csúcsok száma: {len([s for s in hegyek if int(s[2]) * 3.280839895 > 3000])} db")

print("8. feladat")
print("Statisztika:")
hegyseg = {}
for s in hegyek:
  if s[1] not in hegyseg:
    hegyseg[s[1]] = 1
  else:
    hegyseg[s[1]] += 1

for k, v in hegyseg.items():
  print(f"{k} - {v} db")

print("9. feladat")
print("bukk-videk.txt")
with open("bukk-videk.txt", "w") as f:
  f.write("Hegycsúcs neve;Magasság láb\n")
  for s in hegyek:
    if s[1] == "Bükk-vidék":
      f.write(f"{s[0]};{round(int(s[2]) * 3.280839895, 1)}\n")
