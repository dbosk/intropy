"""
Ett program om ålder. Illustrerar:

    - kommentarer,
    - utskrifter,
    - variabler,
    - datatyper
    - variabelnamn och konstanter
"""

name = "Daniel"
birthyear = 1985

print(f"Hej, {name}")

# beräkna ålder
this_year = 2022
age = this_year - birthyear

print(f"Du är {age} gammal.")

print("Nu ska du får bli 25 år igen.")

# beräkna nytt födelseår
birthyear = this_year - 25

print(f"Du är {this_year-birthyear} år gammal, "
      f"det är {age-(this_year-birthyear)} år yngre.")
