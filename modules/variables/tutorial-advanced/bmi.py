
# Ditt namn
NAMN = "Peter"
# Din vikt i kilogram (kg)
VIKT = 80
# Din längd i centimeter (cm)
LÄNGD = 185


def bmi(vikt: float | int, längd: float | int) -> float:
    """Returnerar Body Mass Index (BMI) givet en vikt i kg
    och en längd i cm."""
    return vikt / ((längd / 100) ** 2)


def main():
    print(f"Välkommen till BMI räknaren, {NAMN}!")
    print("Information om BMI:")
    print("       BMI < 18.5 ==> Du är underviktig")
    print("18.5 ≤ BMI < 25.0 ==> Du är normalviktig")
    print("25.0 ≤ BMI        ==> Du är överviktig")
    print()
    print(f"Ditt BMI är: {bmi(VIKT, LÄNGD):.2f}")


if __name__ == "__main__":
    main()
