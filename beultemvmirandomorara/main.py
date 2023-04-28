from datetime import datetime
from enum import Enum

class Gender(Enum):
   male = "f"
   female = "n"

class Person:
  def __init__(self, name, birth, gender, points):
    self.name = name
    self.points = float(points)
    self.gender = calculate_gender(gender)
    self.age = calculate_age(birth)

def calculate_gender(gender_str: str) -> Gender:
    return Gender.female if gender_str == "n" else Gender.male

def calculate_age(birthdate: str) -> int:
    birthdate_datetime = datetime.strptime(birthdate, "%Y.%m.%d")
    today = datetime.now()
    age = today.year - birthdate_datetime.year - ((today.month, today.day) < (birthdate_datetime.month, birthdate_datetime.day))
    return age

encodings = ['utf-8', 'ascii', 'windows-1250', 'windows-1252', 'iso8859_1']
for e in encodings:
    try:
        with open("start.txt", "r", encoding=e) as f, open("final.txt", "r", encoding=e) as f2:
            start_data = [x.split("\t") for x in f.read().strip().split("\n")][1:]
            final_data = [x.split("\t") for x in f2.read().strip().split("\n")][1:]    
            start_data.sort(key=lambda x: x[0])
            final_data.sort(key=lambda x: x[0])
    except UnicodeDecodeError:
        print(f"A fájl űgy tűnik nem {e} kódolású, újrapróbálkozás...")
    except FileNotFoundError:
        print(f"A fájl nem létezik!")
        exit()
    else:
        print(f"A fájl megnyitása {e} kódolással...")
        break

people = []
for (x, y) in zip(start_data, final_data):
    people.append(Person(x[0], x[1], x[2], y[1]))

def feladat1(people: list) -> int:
    return len(people)

def feladat2(people: list) -> int:
    females = 0
    for person in people:
        if person.gender == Gender.female:
            females += 1
    return females

def feladat3(people: list) -> int:
    underage = 0
    for person in people:
        if person.age < 14:
            underage += 1
    return underage

def feladat4(people: list) -> int:
    fem_points = 0
    champion_points = 0 
    for person in people:
        if person.gender == Gender.female:
            fem_points += person.points
        if person.points > champion_points:
            champion_points = person.points
    return "A nőknek több pontja volt mint a bajnoknak" if champion_points < fem_points else ("A bajnokoknak és a nőknek ugyanannyi pontja van" if champion_points == fem_points else "A bajnoknak több pontja volt mint a nőknek")

def feladat5(people):
    sorted_people = sorted(people, key=lambda s: s.points, reverse=True)
    return [s.name for s in sorted_people[:3]]

def feladat6(people):
    sorted_people = sorted(people, key=lambda s: s.points, reverse=True)
    for person in sorted_people[3:]:
        if person.gender == Gender.female:
            return person.name
    return "Nem volt legjobb, nem díjazott nő"

def feladat7(people):
    sorted_people = sorted(people, key=lambda s: s.points, reverse=True)
    for person in sorted_people[3:]:
        if person.age in range(15,19):
            return person.name
    return "Nem volt legjobb, nem díjazott U18"

def feladat8(people):
    sorted_people = sorted(people, key=lambda s: s.points, reverse=True)
    for person in sorted_people[3:]:
        if person.age <= 14:
            return person.name
    return "Nem volt legjobb, nem díjazott U14"

def feladat9(people):
    sorted_people = sorted(people, key=lambda s: s.age, reverse=True)
    return sorted_people[0].name

def feladat10(people):
    sorted_people = sorted(people, key=lambda s: s.age, reverse=False)
    return sorted_people[0].name

def feladat11(people):
    sorted_people = sorted(people, key=lambda s: s.name, reverse=False)
    with open('final2.txt', 'w') as file:
        for person in sorted_people:
            file.write(f'{person.name}\t{person.points}\n')
        return "final2.txt kiírva"

function_names = ['feladat1', 'feladat2', 'feladat3', 'feladat4', 'feladat5', 'feladat6', 'feladat7', 'feladat8', 'feladat9', 'feladat10', 'feladat11']

def main(people):
    for name in function_names:
        func = globals()[name]
        result = func(people)
        print(f'{str(name).replace("feladat", "Feladat ")}: {result}')

main(people)