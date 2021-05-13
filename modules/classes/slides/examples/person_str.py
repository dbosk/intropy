""" Class for a person """

from person_nick import PersonNick

class PersonStr(PersonNick):
    """ Class for a person """
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_pid()})"


def main():
    """ Test program """
    person = PersonStr("Anne-Marie", "Ingeström", "1907-08-28-1234")
    print(person)
    print(f"{person.get_name()} har personnummer {person.get_pid()}")
    person.change_name("Margareta Engström")
    print(f"{person.get_name()} har personnummer {person.get_pid()}")
    print(person.get_first_name())
    print(person.get_last_name())
    person.set_nick("Madicken")
    print(f"{person.get_name()} har personnummer {person.get_pid()}")

if __name__ == "__main__":
    main()
