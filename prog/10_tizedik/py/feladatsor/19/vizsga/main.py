while True:
  name = input("Add meg a vizsgázó nevét! ")
  if name == "": break
  points = int(input("Add meg a pontszámát! "))
  print(f"{name} vizsgája {"sikeres" if points >= 48 else "sikertelen"}.")