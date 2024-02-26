import random

class GameCharacter():
    def __init__(self, name, level, experience, attack_power, health):
        self.name = name
        self.level = level
        self.experience = experience
        self.attack_power = attack_power
        self.health = health
        self.score = random.randint(100, 1000) * (10 + self.level) / (1 + self.experience / 100) * (1 + self.attack_power / 100)

    def changeScore(self):
        self.score = random.randint(100, 1000) * (10 + self.level) / (1 + self.experience / 100) * (1 + self.attack_power / 100)

    def levelUp(self):
        self.level += 1
        self.changeScore()

    def attack(self):
        self.experience += random.randint(1, 50)
        self.changeScore()

    def __str__(self):
        return f"{self.name} (Level {self.level}), Attack Power: {self.attack_power}, Health: {self.health}, Score: {round(self.score)}"

    def __repr__(self):
        return f"GameCharacter({self.name}, {self.level}, {self.experience}, {self.attack_power}, {self.health}, {self.score})"

def genCharacter():
    names = ["Warrior", "Mage", "Rogue", "Paladin", "Archer", "Sorcerer", "Necromancer", "Knight", "Barbarian", "Assassin"]
    return GameCharacter(random.choice(names), random.randint(1, 10), random.randint(0, 100), random.randint(10, 100), random.randint(50, 200))

def main():
    characters = []
    for _ in range(5):
        characters.append(genCharacter())

    for index, character in enumerate(characters):
        print(f"{index}. {character}")

    while True:
        index = int(input("Melyik karaktert szeretné fejleszteni? "))
        characters[index].levelUp()
        print(characters[index])

        print("Melyik karakterrel szeretne támadni?")
        index = int(input())
        characters[index].attack()
        print(characters[index])

        print("Szeretne még támadni? (i/n)")
        answer = input()
        if answer.lower() == "n":
            break

if __name__ == "__main__":
    main()
