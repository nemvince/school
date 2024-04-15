from random import randint

def throwDice():
    dice = [randint(1, 6) for _ in range(3)]
    
    print(f"Dobás {' + '.join(map(str, dice))} = {sum(dice)}\tNyert: {'Anni' if sum(dice) < 10 else 'Panni'}")
    return (dice, sum(dice) < 10)


def runGame(n):
    res = []
    for _ in range(n):
        res.append(throwDice()[1])
    print(f"A játék során {sum(res)} alkalommal Annyi, {n - sum(res)} alkalommal Panni nyert.")


if __name__ == '__main__':
    runGame(int(input("Hány alkalommal legyen feldobás? ")))