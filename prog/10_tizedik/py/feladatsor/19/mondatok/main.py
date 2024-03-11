import random

names = []
while True:
  name = input("Adj meg egy nevet! ")
  if name == "": break
  names.append(name)

def getLocation():
  return random.choice(["tengerpartra", "hegyekbe", "városba", "tóhoz", "Balatonhoz", "nagyvárosba", "kisvárosba"])

def getCompany():
  return random.choice(["családjával", "barátaival", "testvérével", "feleségével", "férjével", "anyjával", "nagyapjával"])

def genSentence(name):
  location = getLocation()
  lArticle = "az" if location[0] in "aeiou" else "a"
  company = getCompany()
  cArticle = "az" if company[0] in "aeiou" else "a"

  return f"{name} idén nyáron {lArticle} {location} utazik {cArticle} {company}."

for name in names:
  print(genSentence(name))