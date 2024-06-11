import random

class Late:
  def __init__(self, consequence, reason, count, min, max, avg) -> None:
    self.consequence = consequence.strip()
    self.reason = reason.strip()
    self.count = int(count)
    self.min = int(min)
    self.max = int(max)
    self.avg = float(avg.replace(",", "."))
    self.major = self.count > 100
    
  def __str__(self) -> str:
    return f"{self.consequence} {self.reason} {self.count} {self.min} {self.max} {self.avg:.2f}"
  
def readData(file: str) -> list:
  data = []
  with open(file, 'r') as f:
    for line in f.readlines()[1:]:
      lineData = line.strip().split(";")
      if all(lineData):
        data.append(Late(*lineData))
  return data

def getCountMinMax(data: list):
  return [sum([x.count for x in data]), min(data, key=lambda x: x.min).min, max(data, key=lambda x: x.max).max]

def getStormConsequence(data: list):
  return [x.consequence for x in data if x.reason == 'Vihar']

def createNotification(data: list):
  event = random.choice(data)
  totalDelay = int(round(event.avg*60, -1))
  return [event, totalDelay]
  

def main():
  data = readData('kesesek.csv')
  print("3. feladat:\nBeolvasás")
  
  count, min, max = getCountMinMax(data)
  print(f"Az adatok alapján {count} vonat késett, minimum {min} percet, maximum {max} percet.")
  
  stormConsequence = getStormConsequence(data)
  print(f"\nVihar miatti következmények: {', '.join(stormConsequence)}")
  
  event, delaySecs = createNotification(data)
  print("\nTájékoztató:")
  print(f"Következmény: {event.consequence}")
  print(f"Időjárási ok: {event.reason}")
  print(f"Késő vonatok száma: {event.count}; átlagos késés {delaySecs} másodperc")
  # ennél rondábban nem is lehetett volna megoldani a feladatot
  print(("Nem j" if not event.major else "J") + "elentős probléma.")
  # de jó lesz ez így is

if __name__ == "__main__":
  main()