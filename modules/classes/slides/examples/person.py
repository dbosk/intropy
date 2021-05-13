""" Class for a person """

class Person:
    """ Class for a person """
    def __init__(self, first_name, last_name, person_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__person_id = person_id

    def get_name(self):
        """ Returns the full name as a concatenation """
        return self.__first_name + " " + self.__last_name

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

    def get_pid(self):
        """ Return 'personnummer' """
        return self.__person_id


def main():
    """ Test program """
    person = Person("Anne-Marie", "Ingeström", "1907-08-28-1234")
    print(person)
    print(f"{person.get_name()} har personnummer {person.get_pid()}")
    person.change_name("Margareta Engström")
    print(f"{person.get_name()} har personnummer {person.get_pid()}")
    print(person.get_first_name())
    print(person.get_last_name())

if __name__ == "__main__":
    main()
