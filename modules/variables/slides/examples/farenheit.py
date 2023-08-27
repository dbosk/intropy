"""Ett program som skriver ut olika former av data"""

def farenheit(celsius):
    """Konverterar grader Celsius till grader Farenheit"""
    return 9/5*celsius + 32

välkomstfras = "Bonjour"
namn = "Daniel"

tal_1 = 5
tal_2 = 2

print(f"{välkomstfras}, {namn}!")
print(välkomstfras + ", " + namn + "!")
print(välkomstfras, ", ", namn, "!")
print(f"{tal_1} + {tal_2} = {tal_1+tal_2}")
print(str(tal_1) + " + " + str(tal_2) + " = " + str(tal_1+tal_2))

print(f"20 grader C blir {farenheit(20)} grader F")
