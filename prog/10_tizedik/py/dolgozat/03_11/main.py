class Order:
  def __init__(self, day, city, qty) -> None:
    self.day = int(day)
    self.city = city
    self.qty = int(qty)

  def __str__(self) -> str:
    return f"{self.day} {self.city} {self.qty}"


# 1-2. feladat
print("1-2. feladat")
with open("rendel.txt", encoding="utf-8") as f:
  d = [Order(*line.strip().split(" ")) for line in f]
print(f"Fájl beolvasva, rendelések száma: {len(d)}")

# 3. feladat
print("3. feladat")
day = int(input("Adjon meg egy napot: "))
print(f"{day}. napon történt rendelések száma: {len([o for o in d if o.day == day])}")


# 4. feladat
print("4. feladat")
no_nr = len(set(range(1, 31)) - {o.day for o in d if o.city == "NR"})
if no_nr:
  print(f"{no_nr} nap nem volt a reklámban nem érintett városból rendelés")
else:
  print("Minden nap volt rendelés a reklámban nem érintett városból")


# 5. feladat
print("5. feladat")
max_qty = max((o.qty for o in d))
print(f"A legnagyobb darabszám: {max_qty}, a rendelés napja: {[o.day for o in d if o.qty == max_qty][0]}")


# 6. feladat
print("6. feladat")
def osszes(city, day):
  return sum(o.qty for o in d if o.city == city and o.day == day)

city = input("Adjon meg egy várost: ")
day = int(input("Adjon meg egy napot: "))
print(f"{day}. napon {city} városból rendelt mennyiség: {osszes(city, day)}")
