""" Class for a person """

class Person:
    """ Class for a person """
    def __init__(self, first_name, last_name, birthday, address, phone):
        """first_name: string with first name.
        last_name: string with last name.
        birthday: string with birthday,
        address: string or Adress object with address.
        phone: string with phone number"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthday = birthday
        self.__address = address
        self.__phone = phone

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

    def get_birthday(self):
        """ Return birthday """
        return self.__birthday

    def get_address(self):
        """ Return address """
        return self.__address

    def get_phone(self):
        """ Returns phone number """
        return self.__phone

    def __lt__(self, other):
        """Returns True if self is younger than other,
        False otherwise"""
        # smaller birthday means older
        return self.get_birthday() > other.get_birthday()

    def __repr__(self):
        """Returns unique representation"""
        return f"({self}, {self.get_birthday()}, {self.get_address()}, " \
                f"{self.get_phone()})"


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
        print(f"{person} är yngre än {person2}.")
    else:
        print(f"{person2} är yngre än {person}.")

    lista = [person, person2]
    print(lista)
    lista.sort()
    print(lista)

if __name__ == "__main__":
    main()
