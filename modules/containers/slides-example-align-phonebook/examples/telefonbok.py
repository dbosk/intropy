"""Ett bibliotek för telefonböcker"""

def skriv_ut_telefonbok(telefonbok):
    """Skriver ut telefonbok på skärmen, i bokstavsordning"""
    for person in sorted(telefonbok):
        print(person.capitalize())

def input_person(prompt):
    """Låter användaren skriva in namnet på en person,
    returnerar namnet"""
    return input(prompt).lower()

def slå_upp_i_telefonbok(person, telefonbok):
    """Slår upp person i telefonbok, returnerar telefonnummer"""
    return telefonbok[person]

