"""Ett exempelprogram som "dansar" ett antal steg

Funktionen dansa(n) dansar tills att n = 0. Så dansa(5) kommer att dansa fem 
takter i dansen, exempelvis ta fem steg, tills att "takterna är slut".

Det är som en automat eller Turingmaskin, om man så vill."""

import random

def flytta_fot(n, fot, riktning):
    """Flyttar foten fot i riktningen riktning, returnerar n-1 (steg tar en 
    takt)"""
    print(f"{fot} fot {riktning}")
    return n-1

def slumpa_fot():
    """Returnerar "höger" eller "vänter"."""
    if random.randint(0, 1) == 0:
        return "höger"
    else:
        return "vänster"

def slumpa_riktning():
    """Returnerar en riktning"""
    slumptal = random.randint(0, 4)
    if slumptal < 1:
        return "framåt"
    elif slumptal < 2:
        return "bakåt"
    elif slumptal < 3:
        return "höger"
    else:
        return "vänster"

def snurra(n):
    """Snurrar i dansen, returnerar n-2 (snurr tar två takter)"""
    print("Snurra!")
    return n-2

def dansa(n):
    """Tar stegen för n takter i dansen"""
    if n <= 0:
        return

    slump = random.randint(0, 1)

    if slump < 1:
        n = flytta_fot(n, slumpa_fot(), slumpa_riktning())
    else:
        n = snurra(n)

    dansa(n)

dansa(5)
