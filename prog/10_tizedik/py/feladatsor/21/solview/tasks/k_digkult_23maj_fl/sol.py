from random import choice

words = ['fuvola', 'csirke', 'adatok', 'asztal', 'fogoly', 'bicska', 'farkas', 'almafa', 'babona', 'gerinc', 'dervis', 'bagoly', 'ecetes', 'angyal', 'boglya']

def runGame():
    word = choice(words)
    print("Üdvözöllek a játékban! A szó hossza:", len(word))
    print(f"DEBUG: {word}")

    guess = input("Tippelj egy szót: ")
    while guess != "stop":
        if len(guess) != len(word):
            print("A tipped hossza nem egyezik a szó hosszával!")
            guess = input("Tippelj egy szót: ")
            continue
        formatted = [word[i] if word[i] == guess[i] else "." for i in range(len(guess))]
        if "".join(formatted) == word:
            print("Gratulálok, kitaláltad a szót!")
            break
        print("".join(formatted))

        guess = input("Tippelj egy szót: ")

if __name__ == '__main__':
    runGame()