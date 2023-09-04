from random import randint

path = None
while not path:
  path = input("Melyik úton mész?\n1 - biztonságos de hosszú\n2 - rövid de veszélyes\n")

if path == "1":
  print("Megérkeztél a célba!")

elif path == "2":
  hp = 100
  steps = 1
  veszely = ["Találkoztál egy nagy, éhes tigrissel",
             "Átkeltél egy veszélyes folyón, és az áramlat elragadott.",
             "Megbotlottál egy csapdában.",
             "Eltévedtél a dzsungelben",
             "Rád támadt egy mérgező kígyó"]
  while hp > 0 and steps < 10:
    kocka = randint(1, 6)
    print(f"{kocka}-t dobtál.")
    if kocka == 1:
      print(veszely[randint(0, len(veszely)-1)])
      hp -= 8
      print("Életerőd: ", hp)
    else:
      steps += 1
    print(f"Még {10-steps} lépés van hátra.")
    input("Nyomj entert a folytatáshoz!")
    print("--------------")
  if hp <= 0:
    print("Meghaltál.")
  else:
    print("Megérkeztél a célba!")