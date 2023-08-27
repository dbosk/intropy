from bank import *
import input_type as it


def menu(bank):
    """Skriver ut menyn, låter användaren välja ett alternativ.
    Returnerar ett korrekt alternativ."""
    print(f"Välkommen till {bank}, hur kan vi hjälpa dig?")
    print("""
[1] Avsluta.
[2] Registrera dig som klient.
[3] Skapa ett konto.
[4] Se dina konton.
[5] Sätt in pengar.
[6] Ta ut pengar.
""")
    choice = it.input_type(int, "Välj ett alternativ: ")
    while choice < 1 or choice > 6:
        print("Tyvärr är det inte ett giltigt alternativ, försök igen, "
              "talet måste vara 1, 2, 3, 4, 5 eller 6.")
        choice = it.input_type(int, "Välj ett alternativ: ")

    return choice


def register_client(bank):
    """Menyvalet att registrera en ny klient."""
    try:
        citizen, phone_number = input_client("Registrera dig som klient genom "
                                             "att fylla i formuläret.")
        bank.add_client(citizen, phone_number)
    except KeyError:
        print("Tyvärr verkar du redan vara registrerad som klient.")
    except ValueError:
        print("Namnet du angav var ogiltigt.")


def create_account(bank):
    """Menyvalet att skapa ett konto."""
    personal_id = it.input_type(int, "Ange ditt personnummer: ")
    password = input("Ange ett lösenord för kontot: ")
    try:
        bank.create_account(personal_id, password)
    except KeyError:
        print(f"Finns ingen klient med personnummer {personal_id}.")
    except ValueError:
        print("Lösenordet är för kort.")


def list_accounts(bank):
    """Listar klientens konton."""
    personal_id = it.input_type(int, "Ange personnummer: ")
    try:
        accounts = bank.get_client_accounts(personal_id)
    except ValueError:
        print(f"Finns ingen klient med personnummer {personal_id}.")
        return

    for account in accounts:
        print(f"{account}: {account.balance} kr")


def get_account(bank):
    """Låt användaren mata in kontonummer och hämta konto."""
    account_id = it.input_type(int, "Ange kontonummer: ")
    try:
        account = bank.get_account(account_id)
    except KeyError:
        print(f"Tyvärr finns inte något konto {account_id}.")
        account = None

    return account


def insert_money(account):
    """Låter användaren mata in summa att sätta in på konto."""
    amount = it.input_type(int, "Ange summa att sätta in: ")
    account.insert_money(amount)


def withdraw_money(account):
    """Låter användaren mata in summa att ta ut från konto."""
    personal_id = it.input_type(int, "Ange ägarens personnummer: ")
    password = input("Ange kontots lösenord: ")
    if account.owner_profile.citizen.personal_id != personal_id or \
       not account.check_password(password):
        print("Tyvärr autentiseringen misslyckades!")
        return

    while True:
        amount = it.input_type(int, "Ange summa att ta ut: ")
        try:
            account.withdraw_money(amount)
            return
        except ValueError as error:
            print(error)


def main():
    """Huvudprogram"""
    bank = Bank("Sveriges Riksbank")

    choice = menu(bank)
    while choice != 1:
        if choice == 2:
            register_client(bank)
        elif choice == 3:
            create_account(bank)
        elif choice == 4:
            list_accounts(bank)
        elif choice == 5 or choice == 6:
            account = get_account(bank)
            if not account:
                continue

            if choice == 5:
                insert_money(account)
            else:
                withdraw_money(account)

        choice = menu(bank)


if __name__ == "__main__":
    main()
