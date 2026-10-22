"""Klasser för en bank med konton"""


class Bank:
    """En bank med sina konton"""

    def __init__(self):
        self.__accounts = {}
        self.__transfers = []

    def open_account(self, number, owner, balance=0):
        """Öppnar ett konto och lämnar tillbaka det."""
        if number in self.__accounts:
            raise ValueError(f"kontot {number} finns redan")

        self.__accounts[number] = Account(number, owner, balance)
        return self.__accounts[number]

    def account(self, number):
        """Lämnar tillbaka kontot med numret number."""
        if number not in self.__accounts:
            raise ValueError(f"det finns inget konto {number}")

        return self.__accounts[number]

    def transfer(self, source, target, amount):
        """För över amount kronor från kontot source till target."""
        self.account(source).withdraw(amount)
        self.account(target).deposit(amount)
        self.__transfers.append((source, target, amount))

    def __str__(self):
        numbers = sorted(self.__accounts)
        rows = [str(self.account(number)) for number in numbers]
        return "\n".join(rows)

    def undo(self):
        """Ångrar den senaste överföringen."""
        if not self.__transfers:
            raise ValueError("det finns inget att ångra")

        source, target, amount = self.__transfers.pop()
        self.account(target).withdraw(amount)
        self.account(source).deposit(amount)


class Account:
    """Ett bankkonto med nummer, ägare och saldo"""

    def __init__(self, number, owner, balance=0):
        self.__number = number
        self.__owner = owner
        self.__balance = balance

    def get_number(self):
        """Returnerar kontonumret"""
        return self.__number

    def get_owner(self):
        """Returnerar kontots ägare"""
        return self.__owner

    def get_balance(self):
        """Returnerar saldot"""
        return self.__balance

    def deposit(self, amount):
        """Sätter in amount kronor på kontot."""
        if amount <= 0:
            raise ValueError("beloppet måste vara positivt")

        self.__balance += amount

    def withdraw(self, amount):
        """Tar ut amount kronor, om de finns på kontot."""
        if amount <= 0:
            raise ValueError("beloppet måste vara positivt")
        if amount > self.__balance:
            raise ValueError(f"{self.__number} har inte {amount} kr")

        self.__balance -= amount

    def __str__(self):
        return f"{self.__number}: {self.__owner}, {self.__balance} kr"


class Person:
    """En person som kan äga ett konto"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        """Returnerar namnet"""
        return self.__name

    def __str__(self):
        return self.__name


def test_account():
    """Provar en insättning och ett uttag"""
    account = Account("1001", Person("Ronja"), 500)
    account.deposit(100)
    account.withdraw(200)
    print(account)


def test_bank():
    """Provar en överföring mellan två konton"""
    bank = Bank()
    bank.open_account("1001", Person("Ronja"), 500)
    bank.open_account("1002", Person("Pippi"), 100)
    bank.transfer("1001", "1002", 200)
    print(bank)


def test_undo():
    """Provar att ångra en överföring"""
    bank = Bank()
    bank.open_account("1001", Person("Ronja"), 500)
    bank.open_account("1002", Person("Pippi"), 100)
    bank.transfer("1001", "1002", 200)
    bank.undo()
    print(bank)


def tests():
    """Provar bankens klasser"""
    test_account()
    test_bank()
    test_undo()


if __name__ == "__main__":
    tests()
