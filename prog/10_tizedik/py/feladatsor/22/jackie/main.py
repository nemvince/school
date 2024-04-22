class Statistic:
    def __init__(self, year, races, wins, podiums, poles, fastests):
        self.year = int(year)
        self.races = int(races)
        self.wins = int(wins)
        self.podiums = int(podiums)
        self.poles = int(poles)
        self.fastests = int(fastests)

    def __str__(self):
        return f"{self.year}: {self.wins} wins, {self.podiums} podiums, {self.poles} poles, {self.fastests} fastest laps"

with open("jackie.txt", encoding="utf-8") as f:
    d = f.read().split("\n")[1:]
    d = [x.split("\t") for x in d]

    d = [Statistic(*x) for x in d]

print(f"3. feladat: {len(d)}")

print(f"4. feladat: {max(d, key=lambda x: x.races).year}")

print(f"5. feladat:")
print(f"\t60-as évek: {sum(x.wins for x in d if x.year >= 1960 and x.year < 1970)}")
print(f"\t70-es évek: {sum(x.wins for x in d if x.year >= 1970 and x.year < 1980)}")

print(f"6. feladat: jackie.html")
with open("jackie.html", "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head></head>\n")
    f.write("<style>td {border:1px solid black;}</style>\n")
    f.write("<body>\n")
    f.write("<h1>Jackie Stewart</h1>\n")
    f.write("<table>\n")
    f.write("\t<tr>\n")
    f.write("\t\t<th>Év</th>\n")
    f.write("\t\t<th>Versenyek</th>\n")
    f.write("\t\t<th>Győzelmek</th>\n")
    f.write("\t</tr>\n")
    for x in d:
        f.write("\t<tr>\n")
        f.write(f"\t\t<td>{x.year}</td>\n")
        f.write(f"\t\t<td>{x.races}</td>\n")
        f.write(f"\t\t<td>{x.wins}</td>\n")
        f.write("\t</tr>\n")
    f.write("</table>\n")
    f.write("</body>\n")
    f.write("</html>\n")
