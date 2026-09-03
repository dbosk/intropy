"""Banksystem med klasser"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} år)"

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode
    
    def __str__(self):
        return f"{self.street}, {self.zipcode} {self.city}"

class PersonWithAddress:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address  # Ett Address-objekt
    
    def __str__(self):
        return f"{self.name} ({self.age} år)\n{self.address}"

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner  # Ett Person-objekt
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def __str__(self):
        return f"Konto: {self.owner.name}\nSaldo: {self.balance} kr"

class Citizen(PersonWithAddress):
    def __init__(self, name, age, address, ssn):
        super().__init__(name, age, address)
        self.ssn = ssn  # Personnummer
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nPersonnummer: {self.ssn}"

def main():
    """Exempel på användning"""
    # Enkel person
    person = Person("Anna Andersson", 30)
    print(person)
    
    # Person med adress
    address = Address("Storgatan 1", "Stockholm", "12345")
    person_with_addr = PersonWithAddress("Bertil Bertilsson", 35, address)
    
    # Skapa ett konto
    account = BankAccount(person_with_addr, 1000)
    
    # Utför transaktioner
    account.deposit(500)
    print(f"Efter insättning: {account.balance} kr")
    
    if account.withdraw(200):
        print(f"Efter uttag: {account.balance} kr")
    else:
        print("Uttaget misslyckades!")
    
    # Medborgare med personnummer
    address2 = Address("Kungsgatan 5", "Göteborg", "41234")
    citizen = Citizen("Erik Eriksson", 45, address2, "450101-1234")
    
    account2 = BankAccount(citizen, 5000)
    print(account2)

if __name__ == "__main__":
    main()
