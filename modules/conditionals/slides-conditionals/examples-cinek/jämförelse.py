"""Ett program som jämför returvärden från funktionsanrop"""

def kvadrat(x):
    """Returnerar x i kvadrat"""
    return x*x

sträng1 = input("Säg något: ")
sträng2 = input("Säg något annat: ")

if sträng1 != sträng2:
    print("Grattis, du följde instruktionen!")
    print(f"Första gången sa du '{sträng1}', andra gången sa du '{sträng2}'.")

x = float(input("Skriv ett flyttal: "))
x2 = kvadrat(x)
print(f"{x} i kvadrat blir {x2}.")
if x2 == round(x2):
    print(f"{x2} saknar decimalföljd.")
