"""
Exempelprogram för tidsmätning

Vi sparar klockslaget vid start och klockslaget vid slut, sedan tar vi 
skillnaden.
"""

import datetime as dt

start_time = dt.datetime.now()

svar = input("Vad är svaret på frågan? ")

end_time = dt.datetime.now()

print(f"Tidsåtgång: {end_time-start_time}")
