""" Reperesenting Skatteverket's pupulation register """

import person
from address import Adress as Address

# vi kan ha "samma namn" på dem, fast egentligen är det inte samma namn:
# den ena heter Person och den andra person.Person.
class Person(person.Person):
    """ Represents a real/physical person """
    def __init__(self, person_id, full_name, parents, address):
        names = full_name.split()
        super().__init__(" ".join(names[:-1]), names[-1], person_id, address)
        self.__parents = parents
        self.__address = address
        self.__old_addresses = []

    def __str__(self):
        """Returns a string representation of the person"""
        return f"{self.get_name()} ({self.get_personnummer()})"

    def get_parents(self):
        """ Returns the parents """
        return self.__parents.copy()

    def change_address(self, new_address):
        """ Changes the address (registers a move) """
        self.__old_addresses.append(self.__address)
        self.__address = new_address

    def get_address_history(self):
        """Returns the list of all addresses"""
        return self.__old_addresses.copy()


def main():
    """ Skatteverket test program """
    folkbokföring = {}

    alice = Person("1950-01-01-1234", "Alice Adamsdotter", None,
                   Address("Vägen", "1", "12345", "Orten"))

    folkbokföring["1950-01-01-1234"] = alice

    bob = Person("1950-01-01-1244", "Bob Evasson", None,
                 Address("Vägen", "1", "12345", "Orten"))

    folkbokföring["1950-01-01-1244"] = bob

    cecilia = Person("1970-01-01-1234", "Cecilia Adamsdotter-Evasson",
                     [alice, bob],
                     Address("Vägen", "1", "12345", "Orten"))

    folkbokföring["1970-01-01-1234"] = cecilia

    print(f"{cecilia} bor på {cecilia.get_address()}")

    cecilia.change_address(Address("Vägen", "2", "12345", "Orten"))
    print(f"{cecilia} bor på {cecilia.get_address()}")
    print(f"{cecilia} har tidigare bott på adresserna:")
    for address in cecilia.get_address_history():
        print(address)

    parents = cecilia.get_parents()
    print(f"{cecilia}s föräldrar heter {parents[0]} och {parents[1]}.")

    print(f"{alice} och {bob} bor fortfarande på {alice.get_address()}")

    print("Folkbokföringen")
    for person in sorted(folkbokföring.values()):
        print(person)

if __name__ == "__main__":
    main()
