BARN_PRIS = 10
VUXEN_PRIS = 20

def totalpris(antal_barn, antal_vuxna,
              barn_pris=BARN_PRIS,
              vuxen_pris=VUXEN_PRIS):
    """
    Tar antalet barn och vuxna, returnerar totalt prisbelopp.
    """
    return antal_barn * barn_pris + antal_vuxna * vuxen_pris

def fråga_heltal(frågan):
    """
    Ställer frågan och låter användaren svara. Upprepar tills att vi får ett heltal.
    """
    while True: 
        try:
            heltalet = int(input(frågan))
            break  # return heltalet
        except ValueError:
            print("Du måste skriva in ett heltal med siffror.")

    return heltalet

def fråga_antal(frågan, minimum=0):
    """
    Ställer frågan och låter användaren mata in något som ska tolkas som ett antal.
    D.v.s. ett icke-negativt heltal (>= 0).

    Om man anger minimum, så måste antalet vara minst det.
    """ 
    heltal = fråga_heltal(frågan)
    while heltal < minimum:
        print(f"Du måste skriva in något som är minst {minimum}.")
        heltal = fråga_heltal(frågan)

    return heltal 

def main():
    """
    Huvudprogrammet
    """ 
    antal_biljetter = fråga_antal("Hur många biljetter vill du köpa? ", 1)
    while (antal_vuxen := fråga_antal("Hur många av de biljetterna är för en vuxen? ")) > antal_biljetter:
        print(f"Antal vunxa kan maximalt vara {antal_biljetter}. Ange lägre.")
    
    antal_barn = antal_biljetter - antal_vuxen
    
    if antal_vuxen > antal_biljetter:
        print("Du kan inte ha fler vuxna än totala antalet biljetter.")
    else:
        print("Du ska betala:")
        print(totalpris(antal_barn, antal_vuxen))
    

#print(f"{__name__=}")
if __name__ == "__main__":
    main()