"""
Ett bibliotek för att animera en bomb i terminalen

ASCII-art från ASCII Art Archive:

    https://www.asciiart.eu/weapons/explosives

ANSI-escape för att sudda animeringen från:

    https://gist.github.com/pfreixes/a911dd6e17aca6bcc6a2
"""

import time
import sys

def detonera():
    """Denna funktion detonerar bomben"""
    oantänd()
    time.sleep(0.5)
    sudda()

    antänd()
    time.sleep(0.5)

    for n in range(7):
        sudda()
        explodera(n)

    sys.exit(1)

def sudda():
    """Sudda 11 rader"""
    for n in range(11):
        print("\033[K", end="")
        print("\033[1A", end="")

def oantänd():
    """Skriver ut en oantänd dynamit"""
    print("""



      )
     (
    .-`-.
    :   :
    :TNT:
    :___:
          """)

def antänd():
    """Skriver ut en antänd dynamit"""
    print("""



    \|/
   - o -
    /-`-.
    :   :
    :TNT:
    :___:
          """)

def explodera(n):
    """Skriver ut steg n i explosionsförloppet, 0 <= n <= 5."""
    if n == 0:
        print("""





    .---.
    : | :
    :-o-:
    :_|_:
""")
        time.sleep(0.1)
    elif n == 1:
        print("""





    .---.
    (\|/)
    --0--
    (/|\)
""")
        time.sleep(0.1)
    elif n == 2:
        print("""




   '.\|/.'
   (\   /)
   - -O- -
   (/   \)
   ,'/|\'.
""")
        time.sleep(0.1)
    elif n == 3:
        print("""





'.  \ | /  ,'
  `. `.' ,'
 ( .`.|,' .)
 - ~ -0- ~ -
""")
        time.sleep(0.1)
    elif n == 4:
        print("""


','|'.` )
  .' .'. '.
,'  / | \  '.
    \ '  "  
 ` . `.' ,'
 . `` ,'. "
   ~ (   ~ -
""")
        time.sleep(0.1)
    elif n == 5:
        print("""
. ','|` ` .
  .'  "  '
,   ' , '  `

   (  ) (
    ) ( )
    (  )
     ) /
    ,---.
""")
        time.sleep(0.5)
    elif n == 6:
        print("""








   ,--.
""")
