"""Innehåller funktioner för att beräkna area av diverse figurer"""

import math

def rektangel(basen, höjden):
    """Tar basen och höjden för en rektangel och returnerer arean"""
    print(f"rektangel({basen}, {höjden})")
    #area = basen * höjden
    #return area
    return basen * höjden

def cirkel(r):
    """Tar cirkelns radie och returnerar arean"""
    print(f"cirkel({r})")
    return r*r*math.pi

def rektangel_utan_cirkel(basen, höjden):
    """Tar basen, höjden och returnerar arean för rekt minus cirkel"""
    print(f"rektangel_utan_cirkel({basen}, {höjden})")
    rektangel_area = rektangel(basen, höjden)
    cirkel_area = cirkel(höjden/2)
    return rektangel_area - cirkel_area

def kvadrat_utan_cirkel(sida):
    """Tar sidan, returnerar arean för kvadrat minus cirkel i mitten"""
    print(f"kvadrat_utan_cirkel({sida})")
    return rektangel_utan_cirkel(sida, sida)

"""Testkod nedan"""
print(f"Rektangel med basen 3cm och höjden 4cm har arean {rektangel(3, 4)}cm^2")
print(f"Cirkel med radien 2cm har arean {cirkel(2)}cm^2")
print(f"Kvadrat med sidan 2 utan cirkeln i mitten ger area {kvadrat_utan_cirkel(2)}")
