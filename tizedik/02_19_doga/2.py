class Product:
  def __init__(self, name, price, quantity) -> None:
    self.name = name
    self.price = price
    self.quantity = quantity

  def total(self):
    return self.price * self.quantity

  def __str__(self) -> str:
    return f"{self.name}, {self.price}Ft, {self.quantity}db, össz. {self.total()}Ft"

def main():
  products = [
    Product("Dyson Hajszárító", 50000, 2),
    Product("Samsung Galaxy S21", 300000, 1),
    Product("Apple MacBook", 1000000, 43),
  ]

  for product in products:
    print(product)

if __name__ == "__main__":
  main()