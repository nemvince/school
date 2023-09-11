from ui import GameUI
import random

materials = ["Gold", "Crystal", "Fuel"]

# Define classes
class GameEvents:
    def generate_random_event(self):
        events = [
            "Asteroid Field",
            "Abandoned Chuck E Cheese",
            "Pirate Attack",
        ]

        selected_event = random.choice(events)
        return selected_event

    def generate_random_mission(self):
        missions = [
            "Explore a New Galaxy",
            "Retrieve Lost Technology",
            "Negotiate a Peace Treaty",
        ]
        selected_mission = random.choice(missions)
        return selected_mission

    def generate_random_target(self):
        targets = [
            "Planet",
            "Space Station",
            "Asteroid",
            "Black Hole",
        ]
        selected_target = random.choice(targets)
        return selected_target

    def generate_random_material(self):
        materials = [
            "Gold",
            "Crystal",
            "Fuel",
        ]
        selected_material = random.choice(materials)
        return selected_material


class Spaceship:
    def __init__(self, power, weapons, armor):
        self.power = power
        self.weapons = weapons
        self.armor = armor

    def move(self):
        print("Moving spaceship...")
        found = GameEvents.generate_random_target(self)
        reward = GameEvents.generate_random_material(self)
        reward_amount = random.randint(1, 10)
        print(f"Found {found}!")
        if found == "Black Hole":
            print("You died!")
            exit()

    def shoot(self):
        print("Firing weapons...")


class SpaceStation:
    def __init__(self):
        self.resources = {}

    def build_spacecraft(self, spacecraft_type):
        print(f"Building a {spacecraft_type} spacecraft...")

    def upgrade_spacecraft(self, spacecraft):
        print(f"Upgrading {spacecraft}...")


class Spacecraft:
    def __init__(self, speed, armor, weaponry):
        self.speed = speed
        self.armor = armor
        self.weaponry = weaponry


def main(raw_materials):
    spaceship = Spaceship(power=100, weapons=3, armor=50)
    station = SpaceStation()
    events = GameEvents()

    while True:
        print("\n--- Galactic Adventures ---")
        print("1. Move Spaceship")
        print("2. Fire Weapons")
        print("3. Generate Random Mission")
        print("4. Build Spacecraft")
        print("5. Upgrade Spacecraft")
        print("6. Collect Resources")
        print("7. Generate Random Event")
        print("9. Quit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                spaceship.move()

            case "2":
                spaceship.shoot()

            case "3":
                print(events.generate_random_mission())

            case "4":
                spacecraft_type = input("Enter spacecraft type: ")
                station.build_spacecraft(spacecraft_type)

            case "5":
                spacecraft = input("Enter spacecraft: ")
                station.upgrade_spacecraft(spacecraft)

            case "6":
                resources = {}
                for material in raw_materials:
                    quantity = int(input(f"Enter quantity of {material}: "))
                    resources[material] = quantity
                station.store_resources(resources)

            case "7":
                print(events.generate_random_event())

            case "9":
                print("Goodbye!")
                exit()

            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main(raw_materials=materials)
