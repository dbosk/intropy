"""Ett program som hanterar en telefonbok"""

import telefonbok as tb

telefonbok = {
    "adam": "0701234567",
    "adam": "08790000",
    "bertil": "0711234567",
    "ada": "0721234567"
}

tb.skriv_ut_telefonbok(telefonbok)

person = tb.input_person("Vems telefonnummer söker du? ")
while person != "":
    telefonnummer = tb.slå_upp_i_telefonbok(person, telefonbok)
    print(f"{person.capitalize()} har telefonnumret {telefonnummer}.")
    person = tb.input_person("Vems telefonnummer söker du? ")

