import random


def throw():
    return random.randint(1, 6)


def calcPoints(name, n):
    throws = [throw() for _ in range(n)]

    print(
        f"{name} dobásai: {' '.join([str(x) for x in throws])}. Összesen {sum(throws)} pontot dobott."
    )

    return sum(throws)


def playRound(names):
    players = {}
    for name in names:
        players[name] = calcPoints(name, throw())

    winner = max(players, key=players.get)
    print(f"{winner} nyert {players[winner]} ponttal.")
    return winner


def mainGame():
    players = {
        "Attila": 0,
        "Elemér": 0,
    }

    for i in range(1, 6):
        print(f"{i}. kör:")
        winner = playRound(players)
        players[winner] += 1

    winner = max(players, key=players.get)

    print(f"{winner} nyerte a játékot {players[winner]} körrel.")


mainGame()
