n = "10"
"""
4.4f som format specification: den första fyran anger den *totala* bredden, 
  inklusive decimalerna. Därav hade den ingen effekt i vårt exempel, då vi hade 
  fyra decimaler och lite till. Om vi hade satt den till 10, skulle vi ha sett 
  effekt.
"""
print(f"n = {float(n):4.4f}")

