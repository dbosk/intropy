"""Program som illustrerar hur man fångar flera typer av fel"""

try:
    x = int(input("Nominator x = "))
    y = int(input("Denominator y = "))
    print(f"{x} / {y} = {x/y}")

except ZeroDivisionError:
    print("Sorry, the denominator must be non-zero.")

except ValueError:
    print("Sorry, you must enter numbers.")

except Exception as err:
    print(f"Sorry, an unexpected error occurred: {err}")

