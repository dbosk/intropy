""" A class for addresses """

class Address:
    """ A class to handle an address """
    def __init__(self,
                 street,
                 area,
                 country=""):
        self.__street = street
        self.__area = area
        self.__country = country

    def get_street(self):
        """ Returns the street (incl any number) """
        return self.__street

    def get_area(self):
        """ Returns the area """
        return self.__area

    def __str__(self):
        """ Returns abbreviated address """
        return self.get_street() + ", " + self.get_area()

    def get_fulladdr(self):
        """ Returns full address, incl area code """
        addr = f"{self.get_street()}, {self.get_area()}"
        if not self.__country:
            addr += ", " + self.__country
        return addr
