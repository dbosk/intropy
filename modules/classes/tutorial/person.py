""" Class for a person """

class Person:
    """ Class for a person """
    def __init__(self, first_name, last_name, personnummer, address):
        """first_name: string with first name.
        last_name: string with last name.
        personnummer: string with personnummer,
        address: string or Adress object with address."""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__personnummer = personnummer
        self.__address = address

    def get_name(self):
        """ Returns the full name as a concatenation """
        return self.__first_name + " " + self.__last_name

    def __str__(self):
        """Returnerar en strängrepresentation lämpligt för utskrift"""
        return self.get_name()

    def get_first_name(self):
        """ Returns the first name """
        return self.__first_name

    def get_last_name(self):
        """ Returns the last name """
        return self.__last_name

    def change_name(self, name):
        """ Takes a concatenated name, sets last and first names """
        names = name.split()
        # Shorthand for the last element in the list
        self.__last_name = names[-1]
        # names[:-1] all elements except the last
        self.__first_name = " ".join(names[:-1])

    def get_personnummer(self):
        """ Return personnummer """
        return self.__personnummer

    def get_address(self):
        """ Return address """
        return self.__address

    def __lt__(self, other):
        """Returns True if self comes before other in alphabetical order"""
        if self.get_last_name() == other.get_last_name():
            return self.get_first_name() < other.get_first_name()

        return self.get_last_name() < other.get_last_name()

    def __repr__(self):
        """Returns unique representation"""
        return f"({self.get_name()}, {self.get_personnummer()}"


def main():
    """ Test program """
    person = Person("Anne-Marie", "Ingeström", "1907-08-28",
                    "Vimmerby", "okänt")
    print(f"{person.get_name()} har telefonnummer {person.get_phone()} "
          f"och bor på adressen {person.get_address()}")
    print(f"{person} har telefonnummer {person.get_phone()} "
          f"och bor på adressen {person.get_address()}")

    person.change_name("Margareta Engström")
    print(f"{person} bor på adressen {person.get_address()}")
    print(person.get_first_name())
    print(person.get_last_name())

    person2 = Person("Ada", "Bedasdotter", "1990-01-01",
                    "Kiruna", "070-1234567")
    if person < person2:
        print(f"{person} sorteras före {person2}.")
    else:
        print(f"{person2} sorteras före {person}.")

    lista = [person, person2]
    print(lista)
    lista.sort()
    print(lista)

if __name__ == "__main__":
    main()
