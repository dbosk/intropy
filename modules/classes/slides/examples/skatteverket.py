""" Reperesenting Skatteverket's pupulation register """

from person_str import PersonStr
from address import Address

class Person(PersonStr):
    """ Represents a real/physical person """
    def __init__(self, person_id, full_name, parents, address):
        names = full_name.split()
        super().__init__(" ".join(names[:-1]), names[-1], person_id)
        self.__parents = parents
        self.__address = address
        self.__old_addresses = []

    def get_parents(self):
        """ Returns the parents """
        return self.__parents.copy()

    def get_address(self):
        """ Returns the address """
        return self.__address

    def change_address(self, new_address):
        """ Changes the address (registers a move) """
        self.__old_addresses.append(self.__address)
        self.__address = new_address


def main():
    """ Skatteverket test program """
    alice = Person("1950-01-01-1234", "Alice Adamsson", None,
                   Address("Vägen 1", "Orten"))
    bob = Person("1950-01-01-1235", "Bob Bertilsson", None,
                 Address("Vägen 1", "Orten"))
    cecilia = Person("1970-01-01-1234", "Cecilia Adamsson-Bertilsson",
                     [alice, bob],
                     Address("Vägen 1", "Orten"))
    print(f"{cecilia} bor på {cecilia.get_address()}")
    cecilia.change_address(Address("Vägen 2", "Orten"))
    print(f"{cecilia} bor på {cecilia.get_address()}")
    print(f"{alice} och {bob} bor fortfarande på {alice.get_address()}")

if __name__ == "__main__":
    main()
