import random

with open("input.txt") as f:
    d = f.read().splitlines()


def filter():
    return [x for x in d if len(x) > 8]


def map():
    return [x.upper() for x in d]


def calc():
    return [len(x) for x in d]


def select():
    return [x for x in d if x[0] in "aeiouAEIOU"]


def rand():
    return random.choice(d)[::-1]


def parts(w):
    return d.count(w)


def main():
    print(d)

    print("1. feladat:")
    print(filter())

    print("2. feladat:")
    print(map())

    print("3. feladat:")
    print(calc())

    print("4. feladat:")
    print(select())

    print("5. feladat:")
    print(rand())

    print("6. feladat:")
    w = input("Adjon meg egy szót: ")
    print(parts(w))


if __name__ == "__main__":
    main()
