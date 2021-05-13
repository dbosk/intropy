""" Class for a person """

from person_nick import PersonNick

class PersonStr(PersonNick):
    """ Class for a person """
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_pid()})"

    def __eq__(self, other):
        if self.get_full_name() == other.get_full_name():
            return True
        return False


def main():
    """ Test program """
    person1 = PersonStr("Anne-Marie", "Ingeström", "1907-08-28-1234")
    person2 = PersonStr("Margareta", "Engström", "1907-08-28-1234")
    if person1 == person2:
        print("Yes!")
    else:
        print("No!")

if __name__ == "__main__":
    main()
