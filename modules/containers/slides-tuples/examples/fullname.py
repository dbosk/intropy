"""Program som visar tuplar."""

def input_full_name():
    """Ber användaren mata in namn, returnerar (förnamn, efternamn)."""
    firstname = input("Ange förnamn: ")
    lastname = input("Ange efternamn: ")
    return firstname, lastname

first, last = input_full_name()
print(f"Hej, {first.capitalize()}, välkommen till programmet!")
print(f"Dear Mr/Mrs/Miss {last.capitalize()}, welcome to the program!")
