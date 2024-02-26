import random


def story():
    # csúcskreativitás elérve :D
    return "A régi templom mélyén egy rejtélyes kincs rejlik, amelyről azt tartják, hogy hatalmas erővel rendelkezik. Ahhoz, hogy megszerezd, először meg kell oldanod néhány logikai feladványt és kikerülnöd az ősi csapdákat."


def number():
    c = random.randint(1, 5)
    u = int(input("Tippelj egy számot 1 és 5 között: "))

    if u == c:
        print("Gratulálok! Helyes tipp!")
        return True
    else:
        print(f"Sajnálom, a helyes szám {c} volt.")
        return False


def word():
    w = ["python", "program", "kincs", "öngyilkosság"]
    s = random.choice(w)
    g = "".join(random.sample(s, len(s)))

    print(f"Fejtsd meg a következő szót: {s}")
    user_guess = input("Mi lehet a helyes szó? ")

    if user_guess == g:
        print("Gratulálok! Helyes megfejtés!")
        return True
    else:
        print(f"Sajnálom, a helyes szó {s} volt.")
        return False


def obstacle():
    p = "titok"
    u = input("Adja meg a jelszót az akadály leküzdéséhez: ")

    if u == p:
        print("Jelszó elfogadva. Az akadály leküzdve!")
        return True
    else:
        print("Hibás jelszó. Az akadály nem lett leküzdve.")
        return False


def main():
    print(story())

    if number() and word() and obstacle():
        print("Gratulálok! Sikeresen megszerezted a kincset!")
    else:
        print("Sajnálom, nem sikerült megszerezni a kincset.")


if __name__ == "__main__":
    main()
