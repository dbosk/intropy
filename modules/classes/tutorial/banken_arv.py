"""Ett program som utför bankliga uppgifter"""

import bank_arv as bank
import input_type as it

def meny(banken="banken"):
    """Skriver ut menyn, låter användaren välja ett alternativ.
    Returnerar ett korrekt alternativ."""
    print(f"Välkommen till {banken}, hur kan vi hjälpa dig?")
    print("""
[1] Avsluta.
[2] Registrera dig som kund.
[3] Skapa ett konto.
[4] Se dina konton.
[5] Sätt in pengar.
[6] Ta ut pengar.
""")
    val = it.input_type(int, "Välj ett alternativ: ")
    while val < 1 or val > 6:
        print("Tyvärr är det inte ett giltigt alternaiv, försök igen, "
              "talet måste vara 1, 2, 3, 4, 5 eller 6.")
        val = it.input_type(int, "Välj ett alternativ: ")

    return val

def registrera_kund(banken):
    """Menyvalet att registrera en ny kund"""
    kund = bank.input_kund("Registrera dig som kund genom att "
                            "fylla i formuläret.")
    try:
        banken.registrera_kund(kund)
    except KeyError:
        print("Tyvärr verkar du redan vara registrerad som kund.")

def skapa_konto(banken):
    """Menyvalet att skapa ett konto"""
    personnummer = input("Ange ditt personnummer: ")
    try:
        konto = banken.skapa_konto(personnummer)
    except KeyError:
        print(f"Finns ingen kund med personnummer {personnummer}.")
        return

    lösenord = input("Ange ett lösenord för kontot: ")
    konto.sätt_lösenord(lösenord)

def lista_konton(banken):
    """Listar kundens konton"""
    personnummer = input("Ange personnummer: ")
    kund = banken.hämta_kund(personnummer)
    for konto in kund.konton:
        print(f"{konto}: {konto.saldo} kr")

def hämta_konto(banken):
    """Låt användaren mata in kontonummer och hämta konto"""
    kontonr = input("Ange kontonummer: ")
    try:
        konto = banken.hämta_konto(kontonr)
    except KeyError:
        print(f"Tyvärr finns inte något konto {kontonr}.")
        konto = None

    return konto

def sätt_in(konto):
    """Låter användaren mata in summa att sätta in på konto"""
    summa = it.input_type(int, "Ange summa att sätta in: ")
    konto.sätt_in(summa)

def ta_ut(konto):
    """Låter användaren mata in summa att ta ut från konto"""
    personnummer = input("Ange ägarens personnummer: ")
    lösenord = input("Ange kontots lösenord: ")
    if konto.ägare.get_personnummer() != personnummer or \
       not konto.korrekt_lösenord(lösenord):
        print("Tyvärr autentiseringen misslyckades!")
        return

    while True:
        summa = it.input_type(int, "Ange summa att ta ut: ")
        try:
            konto.ta_ut(summa)
            return
        except ValueError as err:
            print(err)


def main():
    """Huvudprogram"""
    banken = bank.Bank("Sveriges Riksbank")

    menyval = meny(banken)
    while menyval != 1:
        if menyval == 2:
            registrera_kund(banken)
        elif menyval == 3:
            skapa_konto(banken)
        elif menyval == 4:
            lista_konton(banken)
        elif menyval == 5 or menyval == 6:
            konto = hämta_konto(banken)
            if not konto:
                continue

            if menyval == 5:
                sätt_in(konto)
            else:
                ta_ut(konto)

        menyval = meny()

if __name__ == "__main__":
    main()
