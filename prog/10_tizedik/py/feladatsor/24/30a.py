def readData(filename: str) -> list:
  data = []
  with open(filename, 'r') as file:
    for line in file:
      data.append(line.strip())
  return data

def stationSearch(data: list, query: str) -> bool:
  for station in data:
    if query.lower() == station.lower().replace('mh.', ''):
      return True
  return False

def stationIndex(data: list, query: str) -> int:
  for index, station in enumerate(data):
    if query.lower() == station.lower().replace('mh.', '').strip():
      return index
  return -1

def main():
  data = readData('30a.txt')
  print("2. feladat:")
  query = input('Kérlek, adj meg egy megállóhelyet: ')
  index = stationIndex(data, query)
  if index != -1:
    print(f"Van ilyen nevű megállóhely a listában, a {index+1}. helyen")
  else:
    print("Nincs ilyen megállóhely a listában.")  
  
if __name__ == "__main__":
  main()