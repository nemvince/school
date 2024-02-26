import random

class Car():
  def __init__(self, brand, model, year, horsepower, km):
    self.brand = brand
    self.model = model
    self.year = year
    self.horsepower = horsepower
    self.km = km
    self.value = random.randint(1000, 10000) * (2024 - year) / 10 * (1 - km / 300000) * (1 + horsepower / 1000)

  def changeValue(self):
    self.value = random.randint(1000, 10000) * (2024 - self.year) / 10 * (1 - self.km / 300000) * (1 + self.horsepower / 1000)

  def upgrade(self):
    self.horsepower += self.horsepower * 0.1
    self.changeValue()

  def ride(self):
    self.km += random.randint(1, 100)
    self.changeValue()

  def __str__(self):
    return f"{self.brand} {self.model} ({self.year}), {self.horsepower} HP, {self.km} km, {round(self.value)} EUR"

  def __repr__(self):
    return f"Car({self.brand}, {self.model}, {self.year}, {self.horsepower}, {self.km}, {self.value})"

def genCar():
  brands = ["Audi", "BMW", "Mercedes", "Volkswagen", "Ford", "Toyota", "Suzuki", "Opel", "Fiat", "Skoda"]
  models = ["A1", "A3", "A4", "A6", "A8", "X1", "X3", "X5", "X6", "C", "E", "S", "CLA", "CLS", "GLA", "GLC", "G", "A", "B", "C", "E", "S", "Golf", "Passat", "Polo", "Tiguan", "Touareg", "Focus", "Fiesta", "Mondeo", "Kuga", "Fusion", "Yaris", "Corolla", "Camry", "RAV4", "Auris", "Swift", "Vitara", "Ignis", "Baleno", "Grand Vitara", "Astra", "Corsa", "Insignia", "Mokka", "Adam", "Punto", "500", "Bravo", "Tipo", "Panda", "Fabia", "Octavia", "Rapid", "Superb"]
  return Car(random.choice(brands), random.choice(models), random.randint(1970, 2023), random.randint(50, 650), random.randint(0, 300000))

def main():
  cars = []
  for _ in range(10):
    cars.append(genCar())
  
  for index, car in enumerate(cars):
    print(f"{index}. {car}")

  while True:
    index = int(input("Melyik autót szeretné fejleszteni?"))
    cars[index].upgrade()
    print(cars[index])

    print("Melyik autóval szeretne menni?")
    index = int(input())
    cars[index].ride()
    print(cars[index])

    print("Szeretne még menni? (i/n)")
    answer = input()
    if answer == "n":
      break

if __name__ == "__main__":
  main()
