class Contender:
    def __init__(self, name, country, tech, comp, minus) -> None:
        self.name = name
        self.country = country
        self.tech = float(tech)
        self.comp = float(comp)
        self.minus = int(minus)

    def __str__(self) -> str:
        return f"{self.name}\t{self.country}\t{self.tech} {self.comp} {self.minus}"

def loadFile(filename="input.csv"):
    with open(filename, encoding="utf-8") as f:
        return [Contender(*x) for x in [y.split(";") for y in f.read().strip().split("\n")[1:]]]

def getPoints(n):
    r = [x for x in d if x.name == n]
    if len(r) == 0: exit(1) # nem érdekel
    r = r[0]
    p = r.comp + r.tech - r.minus
    return p if p > 0 else 0

if __name__ == "__main__":
    d = loadFile()
    print(len(d))

    s = "Nem volt"
    if "HUN" in [x.country for x in d]: s = "Volt"
    print(s, "magyar versenyző")

    print(len([x for x in d if x.tech > 1000 or x.comp > 1000]))

    print(getPoints(input("Név? ")))

    w = ""
    for x in d:
        if x.minus == 0:
            w += f"{x.name}\t {round(getPoints(x.name), 2)}\n"

    with open("output.txt", "w") as f:
        f.write(w)
