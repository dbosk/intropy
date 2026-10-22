"""Tar bilderna av föreläsningens två fönster, till anteckningarna.

Skriptet körs i examples/, där de tanglade programmen ligger, under en
X-server, helst en virtuell (make screenshots).  Det skapar varje fönster
med programmets egen klass, gör det användaren gör --- skriver i fältet,
trycker på knappen --- och fotograferar fönstret med ImageMagicks import.
"""

import subprocess
import sys
import tkinter as tk
import tkinter.font

from bank import Account
from bankomat import ATM
from raknare import Counter

# Fönstren ritas i tredubbel storlek, så att bilden blir skarp i tryck.
FONT_SCALE = 3


def enlarge_fonts(window):
    """Ritar fönstrets text i FONT_SCALE gånger standardstorleken"""
    for name in ["TkDefaultFont", "TkTextFont"]:
        font = tkinter.font.nametofont(name, root=window)
        font.configure(size=FONT_SCALE * font.cget("size"))


def children(window, kind):
    """Lämnar tillbaka fönstrets komponenter av sorten kind"""
    found = window.winfo_children()
    return [child for child in found if isinstance(child, kind)]


def photograph(window, filename):
    """Sparar en bild av fönstret, utan ram, i filen filename"""
    window.update()
    command = ["import", "-window", window.wm_frame(), filename]
    subprocess.run(command, check=True)
    window.destroy()


def main():
    outdir = sys.argv[1]

    atm = ATM(Account("1001", "Ronja", 1000))
    enlarge_fonts(atm)
    children(atm, tk.Entry)[0].insert(0, "200")
    children(atm, tk.Button)[0].invoke()
    photograph(atm, f"{outdir}/bankomat.png")

    counter = Counter()
    enlarge_fonts(counter)
    for _ in range(3):
        counter.button.invoke()
    photograph(counter, f"{outdir}/raknare.png")


if __name__ == "__main__":
    main()
