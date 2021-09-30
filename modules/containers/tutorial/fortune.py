"""Ett program för att imitera fortune-kommandot"""

import cowsay_good
import random

def fortune():
    """Returnerar en slumpad fortune cookie"""
    fortunes = [
        "Du kommer att bli bra på att programmera!",
        "Datorprovet kommer att ställas in!",
        "Alla kommer att få A på matematiktentan!",
        "Det är en lovande dag för dig!"
    ]
    return random.choice(fortunes)

def main():
    cowsay_good.cowsay(fortune())

if __name__ == "__main__":
    main()
