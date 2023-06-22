"""Ett program som illustrerar funktionsuppdelningen i att gå, dock med en 
tämligen udda gångstil."""

def take_step_first(the_leg):
    """En funktion som anropar funktionerna som behövs för att ta ett steg"""
    lift_leg(the_leg)
    lean_body("framåt")

def take_step_second(the_leg):
    """En funktion som anropar funktionerna för att ta det kompletterande steget"""
    lift_leg(the_leg)
    lean_body("bakåt")
    put_leg(the_leg)

def lift_leg(the_leg):
    """Lyfter ett ben, the_leg anger höger eller vänster"""
    print(f"lyft {the_leg} ben")

def put_leg(the_leg):
    """Sätter ner ett ben som är i luften"""
    print(f"sätt ned {the_leg} ben")

def lean_body(direction):
    """Luta kroppen, direction anger riktning"""
    print(f"luta kroppen {direction}")

def walk_1m_fwd():
    """En funktion som går en meter framåt"""
    take_step_first("höger")
    take_step_second("vänster")

def walk_fwd(meters):
    """En funktion som går meters antal meter framåt"""
    if meters > 0:
        walk_1m_fwd()
        walk_fwd(meters-1)

walk_fwd(2)
