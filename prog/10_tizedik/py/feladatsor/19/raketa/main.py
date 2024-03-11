target = int(input("Hány órás visszaszámlálást tervezünk? "))
elapsed = 0
while target > 0:
  block = input("Fel kell függeszteni a visszaszámlálst (i/n)? ")
  if block == "i":
    elapsed += 1
  elapsed += 1
  target -= 1
  print(f"Visszaszámlálás: {target}")

print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {elapsed}")