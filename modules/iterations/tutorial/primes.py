"""Ett program som primtalsfaktoriserar tal"""

import math

def primtalsfaktorer(heltal):
    """Returnerar en sträng med primtalsfaktorerna för heltal (int)"""
    if heltal == -1 or heltal == 0 or heltal == 1:
        return heltal

    # vi skulle kunna ha range(2, heltal) också, men då gör vi dubbelt arbete
    for tal in range(2, math.ceil(math.sqrt(heltal))):
        if heltal % tal == 0:
            return f"{tal}*{primtalsfaktorer(heltal//tal)}"

    return str(heltal)

print(f"0 = {primtalsfaktorer(0)}")
print(f"1 = {primtalsfaktorer(1)}")
print(f"5 = {primtalsfaktorer(5)}")
# 12 är ett intressant exempel då det har två faktorer 2 (2*2*3).
# Rekursionen löser det smidigt, för då börjar for-loopen om från 2 igen.
print(f"12 = {primtalsfaktorer(12)}")
print(f"15 = {primtalsfaktorer(15)}")
