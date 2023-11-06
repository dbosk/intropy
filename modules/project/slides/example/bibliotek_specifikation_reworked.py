# Bibliotek
# Projektspecifikation (WIP)
# Emelie Wästlund

# ----------------------------------------------------------------------------------------------------------------------------------

# User flow: (INKLUDERAS INTE I INLÄMNING!)
# 1. Presentera programmet för användaren
# 2. Visa meny med allt som kan göras i programmet
# 3. Användaren får välja ur menyn (steg 4), alternativt avsluta programmet (steg 6)
# 4. Användaren får göra det användaren har valt ur menyn
# 5. Programmet visar menyn igen (steg 2)
# 6. När användaren avslutat programmet säger programmet hejdå till användaren

# Algoritm:
# 1. Läs in böcker från fil och spara i datastruktur i programmet
# 2. Presentera programmet för användaren
# 3. Visa meny med allt som kan göras i programmet
# 4. Användaren får välja ur menyn (steg 5), alternativt avsluta programmet (steg 7)
# 5. Användaren får göra det användaren har valt ur menyn -> Funktion för valet anropas
    # Söka efter böcker
    # Låna böcker
    # Lämna tillbaka böcker
    # Lägg till böcker
    # Ta bort böcker
    # Skriv ut alla böcker
# 6. Programmet visar menyn igen (steg 3)
# 7. När användaren avslutat programmet säger programmet hejdå till användaren
# 8. Böcker skrivs tillbaka till fil

# ----------------------------------------------------------------------------------------------------------------------------------

# Datastrukturer:
# Bok-klass för att spara information om böcker, innehåller information om titel, författare, samt om boken är utlånad eller inte.
# Datastruktur för att hålla koll på alla böcker under körning
    # Förslagsvis 2 dictionaries, en med författare som nyckel och en med titel
# Textfil för att hålla koll på alla böcker mellan körningar

# ----------------------------------------------------------------------------------------------------------------------------------
# Klasser

class Bok():
    def __init__(self, titel, författare, utlånad = False):
        '''
        Attribut:
        titel (sträng)
        författare (sträng)
        utlånad (bool) 
        '''
        pass
    def __str__(self):
        '''
        Konverterar bok-objekt till sträng och returnerar
        '''
        return '' # placeholder
    def __lt__(self, other):
        '''
        Används för att kunna sortera böcker. En bok är mindre än en annan bok om författaren är mindre än den andras författare.
        '''
        return False # placeholder

# ----------------------------------------------------------------------------------------------------------------------------------
# Funktioner

def sök_efter_bok(titel_dictionary, författare_dictionary):
    '''
    1. hämtar inmatning från användaren: väljer om hen vill söka på titel eller författare (kräver felhantering)
    2. användaren får skriva in titel/författare (kräver inte felhantering)
    3. programmet använder titel/författare som nyckel och söker i rätt dictionary
    4. returnerar bok om funnen, annars None
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: bok (Bok?)
    '''
    return None # placeholder

def sök_och_skriv_ut_bok():
    pass

def låna_bok(titel_dictionary, författare_dictionary):
    '''
    1. söker efter en bok (sök_efter_bok)
    2. om funnen bok inte None, sätter bokens utlånad-attribut till true om icke redan utlånad
    3. skriver ut feedback till användaren
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def lämna_tillbaka_bok(titel_dictionary, författare_dictionary):
    '''
    1. söker efter en bok (sök_efter_bok)
    2. om funnen bok inte None, sätter bokens utlånad-attribut till false om utlånad
    3. skriver ut feedback till användaren
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def lägg_till_bok(titel_dictionary, författare_dictionary):
    '''
    1. låter användaren skriva in titel och författare (om felhantering krävs i egna funktioner)
    2. skapar ett Bok-objekt med användarens inmatning som attribut
    3. lägger till boken i våra 2 dictionaries
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def ta_bort_bok(titel_dictionary, författare_dictionary):
    '''
    1. söker efter en bok (sök_efter_bok)
    2. om funnen bok inte None, använder den funna bokens titel och författare som nycklar och tar bort boken ur båda våra 2 dictionaries
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def skriv_ut_böcker(författare_dictionary):
    '''
    Itererar genom vår dictionary, skapar en lista med alla Bok-objekt. Sorterar med hjälp av sort(), skriver sedan ut varje element i listan.
    IN: titel_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def meny(titel_dictionary, författare_dictionary):
    '''
    Visar och låter användaren välja vad som ska göras, anropar en funktion motsvarande användarens val. Möjliga val:
    # Söka efter böcker
    # Låna böcker
    # Lämna tillbaka böcker
    # Lägg till böcker
    # Ta bort böcker
    # Skriv ut alla böcker
    while True:
        val = input()
        if val == "val 1":
            val1()
        elif val == "q":
            break
        else:
            print("inte ett riktigt val")
    IN: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def läs_böcker_från_fil(filnamn):
    '''
    läser in böcker från fil (hårdkodat filnamn?), skapar 2 dictionaries (en med titel som nyckel och en med författare)
    och returnerar dessa
    IN: N/A
    UT: titel_dictionary (dict, sträng: Bok), författare_dictionary (dict, sträng: Bok)
    '''
    return titel_dictionary, författare_dictionary

def skriv_böcker_till_fil(filnamn, titel_dictionary):
    '''
    skriver böcker till fil med hjälp av en av våra 2 dictionaries
    skriver över allt som har stått i filen innan (ifall en bok har blivit borttagen) -> 'w' och inte 'a'
    IN: titel_dictionary (dict, sträng: Bok)
    UT: N/A
    '''
    pass

def presentera_programmet():
    '''
    Presenterar programmet för användaren
    IN: N/A
    UT: N/A
    '''
    pass

def main():
    '''
    0. presenterar programmet
    1. hämta filnamn (i egen funktion?) ELLER hårdkoda filnamn
    2. läser in böcker från fil
    3. anropar menyn för att köra huvudprogrammet
    4. säger hejdå till användaren (kort hejdå så kanske inte behöver en egen funktion)
    5. skriver böcker till fil
    IN: N/A
    UT: N/A
    '''
    pass
    
