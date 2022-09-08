from functools import lru_cache
from time import sleep


@lru_cache
def multiplicera_med_15(tal: float) -> float:
    """Multiplicera ett tal med 15."""
    sleep(10)
    return tal * 15


def fråga_om_multiplikation():
    """Fråga användaren om vilket tal denne vill multiplicera med 15."""
    tal = float(input("Skriv ett tal som du vill multiplicera med 15: "))
    print("Multiplicerar... ", end="")
    print(multiplicera_med_15(tal))


if __name__ == "__main__":
    fråga_om_multiplikation()
    fråga_om_multiplikation()
    fråga_om_multiplikation()
    fråga_om_multiplikation()
