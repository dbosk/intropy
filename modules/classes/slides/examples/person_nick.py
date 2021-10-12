""" Class for a person """

from person import Person

class PersonNick(Person):
    """ Class for a person """
    def __init__(self, first_name, last_name, birthday,
                 address, phone, nickname=""):
        super().__init__(first_name, last_name, birthday,
                         address, phone)
        self.__nick = nickname

    def set_nick(self, nick):
        """ Sets nickname """
        self.__nick = nick

    def get_nick(self):
        """ Returns the nickname """
        return self.__nick

    def get_name(self):
        """ Returns nickname as name, overloads Person """
        if not self.get_nick():
            return self.get_first_name()
        return self.get_nick()

    def get_full_name(self):
        """ Returns the full name """
        return super().get_name()


def main():
    """ Test program """
    person = PersonNick("Anne-Marie", "Ingeström", "1907-08-28",
                        "Vimmerby", "okänt")
    print(person)
    person.change_name("Margareta Engström")
    person.set_nick("Madicken")
    print(f"{person.get_name()} är född {person.get_birthday()}.")

if __name__ == "__main__":
    main()
