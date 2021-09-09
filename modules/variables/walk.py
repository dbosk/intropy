"""Ett program som illustrerar funktionsuppdelningen i att gå"""

def take_step_fwd():
    """En funktion som anropar funktionerna som behövs för att ta ett steg"""
    lift_leg("vänster")
    lean_body("framåt")
    lift_leg("höger")
    lean_body("bakåt")

def lift_leg(the_leg):
    """Lyfter ett ben, the_leg anger höger eller vänster"""
    print(f"lyft {the_leg} ben")

def lean_body(direction):
    """Luta kroppen, direction anger riktning"""
    print(f"luta kroppen {direction}")

def walk_two_steps():
    """En funktion som tar fem steg framåt"""
    take_step_fwd()
    take_step_fwd()

walk_two_steps()
