"""
Ett program för lunchbeställningar
"""

import bio

def main():
    """
    Huvudprogram
    """
    # fråga användaren hur många som ska äta lunch
    antal_lunchare = bio.fråga_antal("Hur många ska äta lunch? ", minimum=1)
    # ta en beställning för varje lunchare
    beställningar = [] 
    for beställningsnr in range(antal_lunchare):
        # ta en beställning
        beställning = input(f"{beställningsnr+1}: Vad vill du äta? ") 
        beställningar.append(beställning)
    # skriv ut en sammanställning med totalpris 
    print("Ni har beställt följande: ") 
    for beställningsnr, beställning in enumerate(beställningar):
        print(f"{beställningsnr+1}: {beställning}")

if __name__ == "__main__":
    main() 