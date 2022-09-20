"""Program som beräknar area"""

def area_rekt(höjd, bredd):
    """Beräknar arean av en rektangel."""
    return höjd * bredd

def area_cirkel(radie, pi=3.14):
    """Beräknar arean av cirkel med radien radie."""
    return radie**2 * pi

def main():
    """Huvudprogrammet"""
    r = 4
    print(f"area_cirkel({r}) = {area_cirkel(r)}")

    b = 2
    h = 3
    print(f"area_rekt({b}, {h}) = {area_rekt(b, h)}")

main()
