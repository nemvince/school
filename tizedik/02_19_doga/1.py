from random import randint, choice

class Food:
  def __init__(self, name, quantity, calories, allergens) -> None:
    self.name = name
    self.quantity = quantity
    self.calories = calories
    self.allergens = allergens.split(" ")

  def sensitivity(self, allergen):
    base = f"Az étel nem tartalmaz {allergen} allergént."
    if allergen not in self.allergens:
      return base.replace("nem ", "")
    return base

  def calorie(self):
    return self.calories * self.quantity

  def __str__(self) -> str:
    return f"{self.name}, {self.quantity}g, {self.calories}/100g, {self.calorie()} össz\t| Allergének: {', '.join(self.allergens)}"

def main():
  possible_foods = ["Spaghetti Bolognese", "Pizza", "Hamburger", "Hotdog", "Fried Chicken", "Salad", "Soup", "Sandwich", "Sushi", "Rice"]
  possible_allergens = ["milk", "egg", "peanut", "tree-nut", "soy", "wheat", "fish", "shellfish"]

  foods = []

  for _ in range(3):
    food = [choice(possible_foods), randint(1, 1000), randint(1, 1000), " ".join([choice(possible_allergens) for _ in range(randint(1, 4))])]
    foods.append(Food(*food))

  for food in foods:
    print(food)
    print(food.sensitivity("milk"))

if __name__ == "__main__":
  main()