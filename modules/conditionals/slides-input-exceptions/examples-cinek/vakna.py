"""Program som räknar ut hur länge du varit vaken"""

def skillnad(nu, vaknade):
    """Tar nuvarande tid, tiden för vaknandet och returnerar skillnaden i timmar"""
    return nu - vaknade

def hhmm_till_flyttal(hh, mm):
    """Tar hh och mm och returnerar som flyttal"""
    return int(hh) + int(mm)/60

def flyttal_till_hhmm(timmar):
    """Tar timmar i flyttalsform, returnerar hh och mm"""
    hh = int(timmar)
    mm = round((timmar - hh)*60)
    return str(hh), str(mm)

def main():
    klockan_nu = input("Hur mycket är klockan just nu? (Ange hh:mm) ")
    klockan_vaknade = input("Hur mycket var klockan när du vaknade? ")

    hh_nu, mm_nu = klockan_nu.split(":")
    hh_vaknade, mm_vaknade = klockan_vaknade.split(":")

    flyttal_vaken = skillnad(
            hhmm_till_flyttal(hh_nu, mm_nu),
            hhmm_till_flyttal(hh_vaknade, mm_vaknade))

    timmar_vaken, minuter_vaken = flyttal_till_hhmm(flyttal_vaken)

    print(f"Du har varit vaken i {timmar_vaken} timmar och {minuter_vaken} minuter.")

if __name__ == "__main__":
    main()
