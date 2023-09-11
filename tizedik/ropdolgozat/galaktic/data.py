class Materials:
  def __init__(self):
    self.iron = {"name": "Iron", "value": 1}
    self.copper = {"name": "Copper", "value": 2}
    self.gold = {"name": "Gold", "value": 3}
    self.crystal = {"name": "Crystal", "value": 4}
    self.fuel = {"name": "Fuel", "value": 5}

class Locations:
  def __init__(self):
    self.mcdonalds = {"name": "McDonalds", 'reward': Materials.iron}
    self.chuckecheese = {"name": "Chuck E Cheese", 'reward': Materials.copper}
    self.walmart = {"name": "Walmart", 'reward': Materials.gold}
    self.target = {"name": "Target", 'reward': Materials.crystal}
    self.gamestop = {"name": "Gamestop", 'reward': Materials.fuel}
    self.black_hole = {"name": "Black Hole", 'reward': lambda: exit()}
    self.locations = [self.mcdonalds, self.chuckecheese, self.walmart, self.target, self.gamestop, self.black_hole]

class Events:
  def __init__(self):
    self.asteroid_field = {"name": "Asteroid Field", "reward": None}
    self.pirate_attack = {"name": "Pirate Attack", "reward": None}
    self.events = [self.asteroid_field, self.pirate_attack, self.abandoned_chuckecheese]
