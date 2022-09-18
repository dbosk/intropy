"""Ett bibliotek för att animera en bomb i terminalen

ASCII-art från ASCII Art Archive:

    https://www.asciiart.eu/weapons/explosives"""

import time
import sys

SCREEN_SIZE = 50

def detonera():
    """Denna funktion detonerar bomben"""
    oantänd()
    time.sleep(0.5)

    antänd()
    time.sleep(0.5)

    for n in range(6):
        explodera(n)
        time.sleep(0.1)

    sys.exit(1)

def oantänd():
    """Skriver ut en oantänd dynamit"""
    for x in range(SCREEN_SIZE):
        print()
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
    for x in range(SCREEN_SIZE):
        print()
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
    for x in range(SCREEN_SIZE):
        print()
    if n == 0:
        print("""
    .---.
    : | :
    :-o-:
    :_|_:
""")
    elif n == 1:
        print("""
    .---.
    (\|/)
    --0--
    (/|\)
""")
    elif n == 2:
        print("""
   '.\|/.'
   (\   /)
   - -O- -
   (/   \)
   ,'/|\'.
""")
    elif n == 3:
        print("""
'.  \ | /  ,'
  `. `.' ,'
 ( .`.|,' .)
 - ~ -0- ~ -
""")
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
