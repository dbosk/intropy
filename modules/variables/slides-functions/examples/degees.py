def farenheit(celcius):
    """Returnerar grader Celcius konverterade till Farenheit"""
    return celcius * 9/5 + 32

def celcius(farenheit):
    """Returnerar grader Farenheit konverterade till Celcius"""
    return (farenheit-32)*5/9

print(f"20 degC = {farenheit(20)}")
print(f"65 degF = {celcius(65)}")
print(f"celcius(farenheit(20)) = {celcius(farenheit(20))}")
