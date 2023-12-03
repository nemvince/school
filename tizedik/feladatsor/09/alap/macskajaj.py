import random


def genPoints():
    return random.randint(0, 5) * 10


def genTeamPoints():
    team = [genPoints() for _ in range(7)]
    return team


def sumPoints(team):
    return sum(team)


def getWinner(index, cats, mice):
    print(f"Űrmacskák: {' '.join([str(x) for x in cats])} -> {sumPoints(cats)} pont")
    print(f"Egerek: {' '.join(str(x) for x in mice)} -> {sumPoints(mice)} pont")
    print(
        f"A {index}. forduló nyertese: {'macska' if sumPoints(cats) > sumPoints(mice) else 'egér'}"
    )
    if sumPoints(cats) > sumPoints(mice):
        return True
    return False


def mainGame():
    catsTotal = 0
    catsWins = 0
    miceTotal = 0
    miceWins = 0
    for i in range(1, 8):
        cats = genTeamPoints()
        mice = genTeamPoints()
        catsTotal += sumPoints(cats)
        miceTotal += sumPoints(mice)
        if getWinner(i, cats, mice):
            catsWins += 1
        else:
            miceWins += 1

    print(
        f"Összesen {catsTotal} pontot szereztek a macskák, {miceTotal} pontot pedig az egerek."
    )
    print(
        f"A macskák {catsWins} fordulót nyertek, az egerek pedig {miceWins} fordulót."
    )
    if catsTotal > miceTotal:
        print("A macskák nyerték a versenyt!")
    else:
        print("Az egerek nyerték a versenyt!")


mainGame()
