while True:
    try:
        x = int(input("Nominator x = "))
        y = int(input("Demoninator y = "))
        print(f"{x} / {y} = {x/y}")
    except ZeroDivisionError:
        print("Sorry, the denominator must be non-zero.")
        continue
    except ValueError:
        print("Sorry, you must enter numbers.")
        continue
    except Exception as err:
        print(f"Sorry, an unexpected error occured: {err}")
    break

