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

if a <= 5 or b >= 13:
  print(True)
else: print(False)

if a >= 0:
  print(True)
else: print(False)

if b < 0:
  print(True)
else: print(False)


# 2. feladat
# ez nem egy python feladat


# 3. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if not a % 10:
  print("A szám osztható 10-zel!")


# 4. feladat
try:
  a = int(input("Kérek egy számot: "))
  b = int(input("Kérek egy másik számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if b == 0:
  print("Hiba! A nevező nem lehet 0!")

# nem volt más megadva (???)


# 5. feladat
try:
  a = int(input("Kérek egy számot: "))
  if a not in range(100, 1000):
    print("A szám nem 3 jegyű!")
    exit()
except ValueError:
  print("Ez nem egy szám!")
  exit()

# check if armstrong number
sum = 0
for c in str(a):
  sum += int(c)**3

if sum == a:
  print("A szám Armstrong szám!")
else: print("A szám nem Armstrong szám!")


# 6. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

#▪ A megadott szám a 4-es.#
if a == 4:
  print("A megadott szám a 4-es.")
if a < 10:
  print("A megadott szám kisebb mint 10.")
if not a % 2:
  print("A megadott szám páros.")
if a in range(0, 11):
  print("A megadott szám a [0,10] intervallumba esik.")


# 7. feladat
try:
  a = int(input("Kérek egy számot: "))
  b = int(input("Kérek egy másik számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a == b:
  print("A két szám egyenlő.")
if a % 2 and b % 2:
  print("Mind a két szám páratlan.")
if not a % 3 or not b % 3:
  print("Legalább az egyik szám osztható hárommal.")
if a < 0 and b < 0:
  print("Mind a két szám negatív.")
if a < 0 or b < 0:
  print("Az egyik szám negatív, a másik szám pozitív.")


# 8. feladat
try:
  a = int(input("Kérem a téglalap egyik oldalát: "))
  b = int(input("Kérem a téglalap másik oldalát: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a == b:
  print("Ez egy négyzet!")
else: print("Ez egy téglalap!")


# 9. feladat
# háromszög
try:
  a = int(input("Kérem a háromszög egyik oldalát: "))
  b = int(input("Kérem a háromszög másik oldalát: "))
  c = int(input("Kérem a háromszög harmadik oldalát: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a == b == c:
  print("Ez egy szabályos háromszög!")
else: print("Ez nem egy szabályos háromszög!")


# 10. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a == 10:
  print("A szám 10.")
elif a == 100:
  print("A szám 100.")
elif a == 1000:
  print("A szám 1000.")
else: print("A szám nem 10, 100 vagy 1000.")


# 11. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a in range(1,10):
  print("A szám benne van a [1,10] intervallumban.")
else:
  print("A szám nincs benne a [1,10] intervallumban.")


# 12. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a < 0 and a % 2:
  print("A szám negatív és páratlan.")


# 13. feladat
try:
  a = int(input("Kérek egy számot: "))
  b = int(input("Kérek egy másik számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if not b % a:
  print("A második szám osztható az elsővel.")


# 14. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

# mivel nem vonunk gyököt nem kell importálni
#from math import sqrt

if a > 0:
  print("A számból lehet gyököt vonni.")


# 15. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()


# 16. feladat
try:
  a = int(input("Kérem az időt: "))
  b = int(input("Kérem a távolságot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

c = b / a
if c > 145 or c < 80:
  print("Nem megfelelő sebességgel közlekedett.")
else: print("Minden rendben!")


# 17. feladat
try:
  a = int(input("Kérek egy számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a == 0:
  print("A szám nulla.")
else:
  print(f"A szám előjele: {'pozitív' if a > 0 else 'negatív'}")


# 18. feladat
try:
  a = int(input("Kérek egy számot: "))
  b = int(input("Kérek egy másik számot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print(f"{'Az első' if a > b else 'A második'} a nagyobb szám.")


# 19. feladat
try:
  a = int(input("Kérem a víz hőmérsékletét: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print(f"A víz halmazállapota: {'szilárd' if a < 0 else 'folyékony' if a < 100 else 'gáz'}")


# 20. feladat
a = input("Add meg a pont kordinátáit x,y formában: ").split(",")

if int(a[0]) > 0 and int(a[1]) > 0:
  print("A pont az első síknegyedben van.")
elif int(a[0]) < 0 and int(a[1]) > 0:
  print("A pont a második síknegyedben van.")
elif int(a[0]) < 0 and int(a[1]) < 0:
  print("A pont a harmadik síknegyedben van.")
elif int(a[0]) > 0 and int(a[1]) < 0:
  print("A pont a negyedik síknegyedben van.")


# 21. feladat
try:
  a = int(input("Kérem a pontszámot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("elégtelen" if a < 43 else "elégséges" if a < 58 else "közepes" if a < 73 else "jó" if a < 88 else "jeles")


# 22. feladat
try:
  a = int(input("Kérem az életkort: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()
if a < 0:
  print("Ez nem egy életkor!")
  exit()

print("Gyerek" if a < 14 else "Fiatalkorú" if a < 18 else "Ifjú" if a < 24 else "Felnőtt" if a < 60 else "Idős")


# 23. feladat
try:
  a = int(input("Kérem a tárgy sűrűségét: "))
  b = int(input("Kérem a folyadék sűrűségét: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("A tárgy elmerül." if a > b else "A tárgy úszik." if a < b else "A tárgy lebeg.")


# 24. feladat
#Készítsünk programot, amely beolvassa egy diák igazolatlan hiányzásainak számát. Ennek megfelelően írassuk ki a 
#magatartás jegyét.(0 igazolatlan: 5, 1-3 igazolatlan: 4, 4-9 igazolatlan: 3, 10 igazolatlantól: 2) Tíz igazolatlan hiányzás 
#elérésekor (vagy ha ezt túlhaladtuk) kérjük be a tanuló születési évét. Ha a diák még nincs 18 éves, akkor írjuk ki a 
#képernyőre: “szülői értesítés szükséges”, ha a diák nagykorú, akkor pedig azt, hogy “felszólítás kiküldése szükséges”.

try:
  a = int(input("Kérem a hiányzások számát: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a >= 10:
  from datetime import datetime
  b = int(input("Kérem a tanuló születési évét: "))
  if datetime.now().year - b < 18:
    print("Szülői értesítés szükséges.")
  else: print("Felszólítás kiküldése szükséges.")
  del datetime

print("5" if a == 0 else "4" if a in range(1,4) else "3" if a in range(4,10) else "2")


# 25. feladat
a = input("Kérek egy karaktert: ")
if len(a) != 1:
  print("Ez nem egy karakter te kis csibész!")
  exit()

print(ord(a))
if a.isnumeric():
  print(a)
elif a.isupper():
  print(a.lower())
else: print(a.upper())


# 26. feladat
try:
  a = int(input("Kérem a sebességet km/h-ban: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("csiga" if a in range(0, 2) else
      "csuka" if a in range(1, 7) else
      "bálna" if a in range(7, 33) else
      "ezüst sirály" if a in range(32, 49) else
      "nyúl" if a in range(48, 65) else
      "strucc" if a in range(65, 71) else
      "gepárd" if a in range(71, 111) else
      "vadászsólyom")


# 27. feladat
try:
  a = int(input("Kérem a távolságot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("500 Ft" if a in range(1, 3) else
      "700 Ft" if a in range(3, 6) else
      "900 Ft" if a in range(6, 11) else
      "1400 Ft" if a in range(11, 21) else
      "2000 Ft" if a in range(21, 31) else
      "Túl drága a benzin, szállítsa a búbánatos fityfene.")


# 28. feladat
try:
  a = int(input("Kérem a telek szélességét: "))
  b = int(input("Kérem a telek hosszúságát: "))
  c = int(input("Kérem a telek adóját: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

if a < 15 or b < 25:
  print(f"A telek adója {c * 0.8} Ft.")
else: print(f"A telek adója {c} Ft.")


# 29. feladat

try:
  a = int(input("Kérem az évszámot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

A = a % 19
B = a % 4
C = a % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5) % 7
H = 22 + D + E

if E == 6 and D == 29:
  H = 50
elif E == 6 and D == 28 and A > 10:
  H = 49

if H <= 31:
  print(f"Húsvét vasárnapja március {H}.")
else: print(f"Húsvét vasárnapja április {H - 31}.")


# 30. feladat
try:
  a = int(input("Kérem az érdemjegyet: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("Elégtelen" if a == 1 else
      "Elégséges" if a == 2 else
      "Közepes" if a == 3 else
      "Jó" if a == 4 else
      "Jeles")


# 31. feladat
# Kérjünk be a felhasználótól egy egész számot: a hét egyik napját. Adjuk meg a nap nevét (Hétfő, Kedd… )

try:
  a = int(input("Kérem a nap sorszámát: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

print("Hétfő" if a == 1 else
      "Kedd" if a == 2 else
      "Szerda" if a == 3 else
      "Csütörtök" if a == 4 else
      "Péntek" if a == 5 else
      "Szombat" if a == 6 else
      "Vasárnap" if a == 7 else
      "Nincs ilyen nap.")


# 32. feladat
# Kérjünk be a felhasználótól egy dátumot: Az évet, a hónapot és a napot. Alakítsuk át, majd írjuk ki a képernyőre a 
#dátumot úgy, hogy a hónap szöveggel legyen kiírva

try:
  y = int(input("Kérem az évet: "))
  m = int(input("Kérem a hónapot: "))
  d = int(input("Kérem a napot: "))
except ValueError:
  print("Ez nem egy szám!")
  exit()

m = "Január" if m == 1 else \
    "Február" if m == 2 else \
    "Március" if m == 3 else \
    "Április" if m == 4 else \
    "Május" if m == 5 else \
    "Június" if m == 6 else \
    "Július" if m == 7 else \
    "Augusztus" if m == 8 else \
    "Szeptember" if m == 9 else \
    "Október" if m == 10 else \
    "November" if m == 11 else \
    "December" if m == 12 else \
    None

if not m or d > 31 or d < 1:
  print("Nincs ilyen dátum!")
  exit()

print(f"{y}. {m}. {d}.")


# 33. feladat
from random import randint
a = randint(1, 6)
print("Gyenge!" if a in range(1, 3) else
      "Nem rossz!" if a in range(3, 5) else
      "Jó!" if a == 5 else
      "Kiváló!")