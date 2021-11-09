"""Experiment med testklass"""

class Testklass:
    """En testklass att experimentera med"""

    def __init__(self, argument):
        """Konstruktor, körs när objekt skapas"""
        self.__argument = argument

    def get_argument(self):
        """Returnerar argumentet"""
        return self.__argument

def main():
    """Testprogram"""
    objekt1 = Testklass("objekt1 argument")
    print(objekt1.get_argument())
    objekt2 = Testklass("objekt2 argument")
    print(objekt2.get_argument())

if __name__ == "__main__":
    main()
