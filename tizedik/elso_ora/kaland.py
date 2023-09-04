from random import randint, shuffle



def init():
  inv = {
    "food": False,
    "water": False,
    "bonus": False
  }

  questions = {
    "Mi az: drót végén van, és fekete? ": ["Kezdő villanyszerelő", "Anakonda", "Koczka tanár úr"],
    "Mit énekelnek a molyok a szekrényben?": ["Edda-blúzt", "Queent", "Juice WRLD-öt"],
    "Mi az: piros, berreg és nehéz lenyelni?": ["Traktor", "Alma", "World Trade Center"]
  }

  l = list(questions.items())
  shuffle(l)
  questions = dict(l)

  return inv, questions

def gnome_questions(inv, questions):
  for question in questions.keys():
    print(question)
    answers = questions.get(question)
    for index, answer in enumerate(answers):
      print(f"{index+1}. {answer}")
    response = input()
    if response == "1":
      inv["food"] = True
      print(f"Ügyes vagy, most már van élelmed.")
      break
    else:
      print("Nem talált!")
  if not inv["food"]:
    print("Egy kérdést sem találtál el. Meghaltál.")
    exit()

def math_task(inv):
  answer = input("Mennyi 9 gyöke?")
  if answer == "3":
    inv['water'] = True
    print("Ügyes vagy, most már van vized is")
  else:
    print("Sajnos nem találtad el.")

def palindrome_door(inv):
  in_word = input("Írj be egy palindróm szót.")
  if in_word != in_word[::-1]:
    print("Nem talált!")
  else:
    print("Talált! Találtál: lma, futópad, gépfegyver, kiskés, gránát, olló, kanál")
    inv['bonus'] = True

def rng_task(inv):
  throw = randint(1,6)
  if throw == 6:
    print("Szerencséd van, elkerülted az utolsó akadályt!")
  else:
    print("Fellógattak egy fára!")
    if inv['bonus']:
      print("Volt nálad kés, ezért megszöktél.")
    else:
      print("Meghaltál.")
      exit()

def bossfight(inv):
  if inv['bonus']:
    print("Volt nálad gépfegyver, ezért a szörnyet legyőzted!")
  else:
    p_throws = [randint(1,6) for _ in range(3)]
    m_throws = [randint(1,6) for _ in range(3)]
    if sum(p_throws) > sum(m_throws):
      print("Többet dobtál a szörnyél, nyertél!")
    else:
      print("szopi xd")

inv, questions = init()
gnome_questions(inv, questions)
math_task(inv)
palindrome_door(inv)
rng_task(inv)
bossfight(inv)


