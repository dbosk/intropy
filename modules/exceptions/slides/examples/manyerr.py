"""Program som illustrerar hur man fångar flera typer av fel"""

while True:
    try:
        x = int(input("Nominator x = "))
        y = int(input("Demoninator y = "))
        print(f"{x} / {y} = {x/y}")
        break

    except ZeroDivisionError:
        print("Sorry, the denominator must be non-zero.")

    except ValueError:
        print("Sorry, you must enter numbers.")

    except Exception as err:
        print(f"Sorry, an unexpected error occured: {err}")

