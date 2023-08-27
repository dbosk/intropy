"""
Ett bibliotek för att animera i terminalen

Av: Daniel Bosk, Emelie Wästlund

ANSI-escape för att flytta markören:

    https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html

Cow av Shanaka Dias: https://www.asciiart.eu/animals/cows
"""

import math
import os
import platform
import time
import shutil

WIDTH, HEIGHT = shutil.get_terminal_size((80, 20))

def init_canvas(width=WIDTH, height=HEIGHT):
    """Initierar ritområdet"""
    canvas = "\n"*height
    render(canvas)
    erase(canvas)

def frame(canvas, seconds):
    """Kör en frame med canvas i seconds sekunder"""
    render(canvas)
    time.sleep(seconds)
    erase(canvas)

def render(canvas):
    """Skriver ut canvas på skärmen"""
    print(canvas)

def erase(canvas):
    """Suddar allt, tar bort det som gjorts av render"""
    for _ in canvas.splitlines():
        # ANSI-escapes för att flytta markören i terminalen
        print("\033[K", end="") # ta bort allt på raden
        print("\033[1A", end="") # flytta en rad upp

    print("\033[K", end="") # ta bort allt på sista raden också

def erase_windows(_):
    """Suddar allt"""
    os.system("cls")

if platform.system() == "Windows":
    erase = erase_windows

def position(sprite, x, y, x_max=WIDTH, y_max=HEIGHT):
    """Returnerar en canvas där sprite är på position x och y"""
    sprite = sprite.strip("\n")

    max_width = max(map(len, sprite.splitlines()))

    if x < 0:
        sprite = cut_left(sprite, -x)
    if x > WIDTH - max_width:
        sprite = cut_right(sprite, max_width-(x_max-x))

    if x > 0:
        sprite = fill_left(sprite, x)

    if y < 0:
        sprite = cut_top(sprite, -y)
    elif y > 0:
        sprite = "\n"*y + sprite

    if (height := len(sprite.splitlines())) > y_max:
        sprite = cut_bottom(sprite, height-y_max)

    return sprite

def cut_left(sprite, n):
    """Klipp bort n tecken på vänster sida"""
    spritelines = sprite.splitlines()

    for row in range(len(spritelines)):
        try:
            spritelines[row] = spritelines[row][n:]
        except IndexError:
            pass

    return "\n".join(spritelines)

def cut_right(sprite, n):
    """Klipp bort n tecken på höger sida"""
    spritelines = sprite.splitlines()
    max_width = max(map(len, spritelines))

    for row in range(len(spritelines)):
        row_width = len(spritelines[row])
        to_cut = row_width - (max_width - n)
        if to_cut > 0:
            spritelines[row] = spritelines[row][:-to_cut]

    return "\n".join(spritelines)

def fill_left(sprite, n):
    """Fyller på med n blanktecken till vänter om sprite"""
    spritelines = sprite.splitlines()

    for row in range(len(spritelines)):
        spritelines[row] = " "*n + spritelines[row]

    return "\n".join(spritelines)

def cut_top(sprite, n):
    """Klipp bort de n översta raderna"""
    try:
        return "\n".join(sprite.splitlines()[n:])
    except IndexError:
        pass

    return sprite

def cut_bottom(sprite, n):
    """Klipper bort de n nedersta raderna"""
    spritelines = sprite.splitlines()

    try:
        return "\n".join(spritelines[:len(spritelines)-n])
    except IndexError:
        pass

    return sprite

def sprite_size(sprite):
    """Returnerar (bredd, höjd) för sprite"""
    spritelines = sprite.splitlines()

    max_width = max(map(len, spritelines))
    max_height = len(spritelines)

    return (max_width, max_height)

def toggle_cursor(mode):
    """Ändrar visningen av markör; på om mode=True, av om mode=False"""
    if mode:
        print("\033[?25h", end="") # slå på markör
    else:
        print("\033[?25l", end="") # slå av markör

def test():
    """Denna funktion testar animationsfunktionerna"""
    COW_SPRITE = """
         __n__n__
  .------`-\00/-'
 /  ##  ## (oo)
/ \## __   ./
   |//YY \|/
   |||   |||
"""

    toggle_cursor(False)
    init_canvas()

    frame(position(COW_SPRITE, 0, 0), 0.5)
    for n in range(10):
        frame(position(COW_SPRITE, -n, 0), 0.1)
    for n in range(10):
        frame(position(COW_SPRITE, -10+n, 0), 0.1)
    for n in range(WIDTH):
        frame(position(COW_SPRITE, n, math.ceil(n*HEIGHT/WIDTH)), 0.1)

    render(position(COW_SPRITE, WIDTH, math.floor(HEIGHT)))
    toggle_cursor(True)


if __name__ == "__main__":
    test()
