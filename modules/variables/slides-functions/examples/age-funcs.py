"""
Ett program om ålder. Illustrerar:

    - kommentarer,
    - utskrifter,
    - variabler,
    - datatyper
    - variabelnamn och konstanter
"""
THIS_YEAR = 2022

def age(birthyear, this_year):
    """Beräknar ålder utifrån två år."""
    return this_year - birthyear

def birthyear_age(age):
    """Retunerar födelseår för att vara age år gammal."""
    return THIS_YEAR - age

def age_game(name, birthyear):
    """Skriver ut lite skoj om ålder"""
    print(f"Hej, {name}")

    # beräkna ålder
    the_age = age(birthyear, THIS_YEAR)

    print(f"Du är {the_age} gammal.")
    print("Nu ska du får bli 25 år igen.")

    # beräkna nytt födelseår
    birthyear = birthyear_age(25)

    print(f"Du är {age(birthyear, THIS_YEAR)} år gammal, "
        f"det är {the_age-age(birthyear, THIS_YEAR)} år yngre.")

name = "Daniel"
birthyear = 1985

age_game(name, birthyear)
age_game("Urban", 1950)
