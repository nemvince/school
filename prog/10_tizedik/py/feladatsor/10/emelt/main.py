import datetime

with open("taborok.txt") as f:
  d = f.read().splitlines()

class Tabor():
  def __init__(self, start_month, start_day, end_month, end_day, interested_students, theme) -> None:
    self.start_date, self.end_date = self.getDays(start_day, start_month, end_day, end_month)
    self.interested_students = list(interested_students)
    self.theme = theme

  def __str__(self) -> str:
    return f"{self.start_date} - {self.end_date} | {self.theme} | {self.interested_students}"

  def getDays(self, start_day, start_month, end_day, end_month):
    current_year = datetime.datetime.now().year
    fmt_start = datetime.datetime(current_year, int(start_month), int(start_day))
    fmt_end = datetime.datetime(current_year, int(end_month), int(end_day))

    if fmt_end < fmt_start:
      raise Exception("End date is before start date")
    
    if fmt_start < datetime.datetime(current_year, 6, 16) or fmt_end > datetime.datetime(current_year, 8, 31):
      raise Exception("Dates are not between june 16 and august 31")

    return fmt_start, fmt_end

camps = []

for camp in d:
  camps.append(Tabor(*camp.split("\t")))


print("2. feladat")

print(f"A fájl {len(camps)} tábor adatait tartalmazza.")

print(f"Az először rögzített tábor témája: {camps[0].theme}")

print(f"Az utoljára rögzített tábor témája: {camps[-1].theme}")


print("3. feladat")

music_camp = list(filter(lambda x: x.theme == "zenei", camps))

for camp in music_camp:
  print(f"Zenei tábor kezdődik: {camp.start_date.month}. hó {camp.start_date.day}. napján")


print("4. feladat")

# get most popular camp but also handle ties

most_popular = max(camps, key=lambda x: len(x.interested_students))

most_popular_camps = list(filter(lambda x: len(x.interested_students) == len(most_popular.interested_students), camps))

print("Legnépszerűbbek:")

for camp in most_popular_camps:
  print(f"{camp.start_date.month} {camp.start_date.day} {camp.theme}")


# 5. feladat

def getDayIndex(in_date):
  # get how many days away from june 16

  june_16 = datetime.datetime(datetime.datetime.now().year, 6, 16)

  return (in_date - june_16).days


print("6. feladat")

month = input("hó: ")
day = input("nap: ")

# get all camps that are active on the given day

camps_on_day = list(filter(lambda x: getDayIndex(x.start_date) <= getDayIndex(datetime.datetime(datetime.datetime.now().year, int(month), int(day))) <= getDayIndex(x.end_date), camps))

if len(camps_on_day) == 0:
  print("Ezen a napon nem volt táborozás!")
else:
  print(f"Ekkor éppen {len(camps_on_day)} tábor tart.")


print("7. feladat")

# get a student name, check if any camps are active on the same day

student_name = input("Adja meg egy tanuló betűjelét: ")

student_camps = list(filter(lambda x: student_name in x.interested_students, camps))

student_camps.sort(key=lambda x: x.start_date)

with open("egytanulo.txt", "w") as f:
  f.write("\n".join([f"{camp.start_date.month}.{camp.start_date.day}-{camp.end_date.month}.{camp.end_date.day}. {camp.theme}" for camp in student_camps]))

overlap = False

for camp in student_camps:
  for other_camp in student_camps:
    if camp != other_camp:
      if getDayIndex(camp.start_date) <= getDayIndex(other_camp.start_date) <= getDayIndex(camp.end_date) or getDayIndex(camp.start_date) <= getDayIndex(other_camp.end_date) <= getDayIndex(camp.end_date):
        overlap = True

if overlap:
  print("Nem mehet el mindegyik táborba.")