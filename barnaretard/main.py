class Plant():
    def __init__(self, name, part, start, end) -> None:
        self.name = name
        self.part = part
        self.start = int(start)
        self.end = int(end)

plants = []

with open("gyogynovenyek.txt", encoding="utf-8") as f:
    data = [x.split(";") for x in f.read().split("\n")]

for item in data:
    plants.append(Plant(*item))

def feladat1(plants):
    gyongyvirag = [p for p in plants if p.name == "Gyongyvirag"][0]
    return gyongyvirag.part

def feladat2(plants):
    levelek = [p for p in plants if p.part == "level"]
    return len(levelek)

def feladat3(plants):
    return ', '.join(set([p.part for p in plants]))

def feladat4(plants):
    osz = [p.name for p in plants if p.start == 9]
    return ', '.join(osz)

def feladat5(plants):
    virag = [p.name for p in plants if 'virag' in p.part]
    return len(virag)

def feladat6(plants):
    output = ["\t"]
    for plant in plants:
        output.append(f"{plant.name}: {abs(plant.end - plant.start)} hónapig")
    return '\n'.join(output)

def feladat7(plants):
    months = set([range(p.start, p.end) for p in plants])
    for i in range(1,12):
        if i not in months:
            return i

function_names = ['feladat1', 'feladat2', 'feladat3', 'feladat4', 'feladat5', 'feladat6', 'feladat7']

def main(plants):
    for name in function_names:
        func = globals()[name]
        result = func(plants)
        print(f'{str(name).replace("feladat", "Feladat ")}: {result}')

main(plants)