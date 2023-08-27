while True:
    try:
        x = float(input("Mata in ett tal: "))
    except ValueError as err:
        print(f"Tyvärr, det blev fel: {err}, försök igen.")
    else:
        break

print(x)
