"""Program som räknar ned"""

import time

n = 10

while n > 0:
    print(f"n = {n}")
    #n = n - 1
    n -= 1
    time.sleep(1)

print("Gott nytt år!")
