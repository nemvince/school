import math

class Character:
  def __init__(self, name, strength, gender, abilities, xp) -> None:
    self.name = name
    self.strength = strength
    self.gender = gender
    self.abilities = abilities.split(",")
    self.xp = xp

  def __str__(self) -> str:
    return f"{self.name} {self.strength}PP {self.xp}XP {self.abilities} {self.gender} karakter"

  def losePower(self, amount):
    self.strength -= amount

  def gainPower(self, amount):
    self.strength += amount

  def hasAbility(self, ability):
    return ability in self.abilities

  def getLevel(self):
    return math.ceil(self.xp / 15)

  def gainXp(self, amount):
    self.xp += amount

  def addAbility(self, ability):
    self.abilities.append(ability)

