def main(name, age, games):
    print(f"{name}\t{age} év\n")
    g1, g2, g3 = games
    print(f"{g1}", f"{g2}", f"{g3}", sep=" -=- ")


if __name__ == "__main__":
    main("Vince", 15, ["Minecraft", "Gran Turismo 4", "Paper Mario"])
