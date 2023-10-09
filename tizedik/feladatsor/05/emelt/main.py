class Player():
  def __init__(self, rank, name, country, prize) -> None:
    self.rank = rank
    self.name = name
    self.country = country
    self.prize = int(prize)

  def __repr__(self) -> str:
    return f"{self.rank}. {self.name} ({self.country}): {self.prize}"

players = []

# 100% readable code
with open("snooker.txt", encoding='utf-8') as f:
  d = [players.append(Player(*x.strip().split(";"))) for x in f.read().split('\n')[1:]]

countries = {}
for player in players:
  if player.country in countries:
    countries[player.country] += 1
  else:
    countries[player.country] = 1

print(f"3. feladat: A világranglistán {len(players)} versenyző szerepel.")

print(f"4. feladat: A versenyzők átlagosan {str(format(sum([x.prize for x in players]) / len(players), '.2f')).replace('.', ',')} fontot kerestek.")

best_chinese = sorted([p for p in players if p.country ==  'Kína'], key=lambda x: int(x.prize))[-1]
print(f"5. feladat: A legjobban kereső kínai versenyző:")
print(f"\tHelyezés: {best_chinese.rank}")
print(f"\tNév: {best_chinese.name}")
print(f"\tOrszág: {best_chinese.country}")
print(f"\tNyeremény összege {'{:,}'.format(best_chinese.prize*380).replace(',', ' ')} Ft")

print(f"6. feladat: A versenyzők között {"van" if len([p for p in players if p.country == "Norvégia"]) else "nincs"} norvég versenyző.")

print("7. feladat: Statisztika")
for country, count in countries.items():
  if count > 4:
    print(f"\t{country} - {count}")
