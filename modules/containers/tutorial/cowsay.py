"""Ett program som immiterar `cowsay`"""

def pratbubbla(text):
    """Skriver ut text i en pratbubbla"""
    print(" ", end="")
    for _ in range(len(text)+2):
        print("-", end="")
    print()
    print(f"| {text} |")
    print(" ", end="")
    for _ in range(len(text)+2):
        print("-", end="")

def ko():
    """Skriver ut en ko"""
    print("""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||""")

def cowsay(text):
    """Skriver ut text i en pratbubbla från en ko"""
    pratbubbla(text)
    ko()

cowsay("Smaka på den här utmaningen! Fast så svår är den inte.")
