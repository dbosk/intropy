"""Ett program som illustrerar funktionsuppdelningen i att gå."""


def take_step_fwd():
    """Skriver ut stegen som behövs för att ta ett steg framåt."""
    lift_leg("vänster")
    lean_body("framåt")
    lift_leg("höger")
    lean_body("bakåt")


def lift_leg(the_leg):
    """Skriver ut att benet the_leg lyfts."""
    print(f"lyft {the_leg} ben")


def lean_body(direction):
    """Skriver ut att kroppen lutas i riktningen direction."""
    print(f"luta kroppen {direction}")


def walk_two_steps():
    """Skriver ut stegen som behövs för att ta två steg framåt."""
    take_step_fwd()
    take_step_fwd()


walk_two_steps()
