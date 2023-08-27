"""Program som räknar ned"""

import time

def count_down(n):
    """Räkna ned till noll, börja på n."""
    while n > 0:
        print(f"n = {n}")
        #n = n - 1
        n -= 1
        time.sleep(1)

count_down(10)
print("Gott nytt år!")
