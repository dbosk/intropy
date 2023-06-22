from citizen import Citizen
from address import Address, input_address
import input_type as it
from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class ClientProfile:
    """Klient hos en bank."""
    citizen: Citizen  # medborgaren som ska vara en klient
    phone_number: int  # medborgarens telefonnummer

    def __str__(self):
        return f"{self.citizen} (telefon nummer: {self.phone_number})"


class Account:
    """Bankkonto."""
    def __init__(self, account_id: int, password: str,
                 owner_profile: ClientProfile):
        """`account_id` är ett unikt kontonummer hos en bank.
        `password` är lösenordet. Krav: minst 8 symboler lång.
        `owner_profile` är profilen till ägaren.
        """
        self.__account_id = account_id
        self.__owner_profile = owner_profile
        self.__balance = 0.0
        self.__password = None  # Obs: Här deklarerar vi bara att attributet
        # `__password` finns, och vi låter set_password-metoden tilldela kontot
        # sitt lösenord för att slippa kod-duplicering.
        self.set_password(password)

    def __str__(self):
        return str(self.__account_id)

    def __repr__(self):
        return f"Account({self.__account_id}, '{self.__password}', " \
               f"{self.__balance})"

    @property
    def account_id(self) -> int:
        """Kontonummer."""
        return self.__account_id

    @property
    def owner_profile(self) -> ClientProfile:
        """Kontonummer."""
        return self.__owner_profile

    @property
    def balance(self) -> float:
        """Kontots saldo."""
        return self.__balance

    def insert_money(self, amount: float):
        """Sätt in pengar."""
        self.__balance += amount

    def withdraw_money(self, amount: float):
        """Tar ut en summa pengar från kontot,
        kastar ett särfall ValueError vid för lite täckning på kontot"""
        if self.__balance < amount:
            raise ValueError(f"kontot saknar täckning, saldot {self.__balance} "
                             f"är mindre än uttaget {amount}.")

        self.__balance -= amount

    def set_password(self, password: str):
        """Byt lösenord. Krav: minst 8 bokstäver."""
        if len(password) < 8:
            raise ValueError("bankkontolösenordet är för kort.")

        self.__password = password

    def check_password(self, password: str) -> bool:
        """Är lösenordet korrekt?"""
        return self.__password == password


class Bank:
    """En bank."""
    def __init__(self, name: str):
        """`name` är namnet på banken."""
        self.__name = name
        # Personnummer till respektive klients ClientProfile-objekt:
        self.__clients = {}
        # Kontonummer till respektive Account-objekt:
        self.__accounts = {}
        # Personnummer till respektive Account-objekt (värdet är en lista):
        self.__client_accounts = {}
        # Följande hjälper oss att hitta på unika ID nummer för nya konton:
        self.__account_id_autoincrement = 1

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"Bank({self.__name}, {len(self.__clients)} clients, " \
               f"{len(self.__accounts)} accounts)"

    @property
    def name(self) -> str:
        return self.__name

    def create_account(self, personal_id: int, password: str) -> Account:
        """Skapar ett nytt konto åt klienten med personnumret `personal_id`,
        returnerar det nya kontot. `password` blir kontots lösenord.
        Se Account-klassen för krav på lösenordet."""
        owner_profile = self.__get_client_profile2(personal_id)
        new_account_id = self.__account_id_autoincrement
        account = Account(new_account_id, password, owner_profile)
        self.__accounts[account.account_id] = account
        self.__account_id_autoincrement += 1
        self.__client_accounts[personal_id].append(account)
        return account

    def __get_client_profile2(self, personal_id: int) -> ClientProfile:
        """Är personen en klient? Om ja, returnera klientens profil.
        Om inte, släng ett ValueError."""
        try:
            return self.get_client_profile(personal_id)
        except KeyError:
            raise ValueError(f"medborgare med personnummer {personal_id} "
                             f"är inte en klient.")

    def add_client(self, citizen: Citizen, phone_number: int):
        """Lägger till en ny klient."""
        self.__clients[citizen.personal_id] = \
            ClientProfile(citizen, phone_number)
        self.__client_accounts[citizen.personal_id] = []

    def get_client_accounts(self, personal_id: int) -> List[Account]:
        """Lista med alla konton som tillhör en klient."""
        self.__get_client_profile2(personal_id)
        try:
            return self.__client_accounts[personal_id].copy()
        except KeyError:
            return []

    def get_client_profile(self, personal_id: int) -> ClientProfile:
        """Returnerar profil till klient med personnumret `personal_id`,
        om inte denne är en klient så kastas ett KeyError."""
        return self.__clients[personal_id]

    def get_account(self, account_id: int) -> Account:
        """Returnerar ett konto med kontonumret `account_id`, om kontot inte
        existerar så kastas ett KeyError."""
        return self.__accounts[account_id]


def input_client(prompt: str = "") -> Tuple[Citizen, int]:
    """Låter användaren mata in uppgifter för en kund,
    returnerar ett Client-objekt"""
    if prompt:
        print(prompt)

    full_name = input("Fullständigt namn: ")
    personal_id = it.input_type(int, "Personnummer: ")
    address = input_address()
    phone_number = it.input_type(int, "Telefonnummer: ")

    return Citizen(full_name, personal_id, address, []), phone_number


def main():
    bank = Bank("LåtsasBanken")

    # Specificera medborgaren som ska bli en ny klient hos LåtsasBanken
    vilmas_id = 9911037621
    vilmas_address = Address("Trollgatan", "1", 50641, "Borås")
    vilma = Citizen("Vilma (totally legit) Andersson", vilmas_id,
                    vilmas_address, [])

    # Lägg till klient och skapa ett nya konton
    bank.add_client(vilma, 5555555)
    student_account = bank.create_account(vilmas_id, "pa$$word")
    savings_account = bank.create_account(vilmas_id, "pa$$word2")

    student_account.insert_money(100.0)
    student_account.withdraw_money(71.5)
    savings_account.insert_money(71.5)

    print(bank.get_client_accounts(vilmas_id))


if __name__ == "__main__":
    main()
