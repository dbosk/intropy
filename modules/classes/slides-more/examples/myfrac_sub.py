""" Fractions library """

class Fraction:
    """ Class for fractions """
    def __init__(self, nominator, denominator=1):
        if isinstance(nominator, Fraction):
            self.__nominator = nominator.nominator
            self.__denominator = nominator.denominator * denominator
        elif isinstance(nominator, int):
            self.__nominator = nominator
            self.__denominator = denominator
        else:
            raise TypeError(f"can't create fraction from {type(nominator)}")

    @property
    def nominator(self):
        """nominator getter"""
        return self.__nominator

    @property
    def denominator(self):
        """demoninator getter"""
        return self.__denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return self.nominator / self.denominator

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.nominator + other * self.denominator,
                            self.denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.nominator * other.denominator +
                            other.nominator * self.denominator,
                            self.denominator * other.denominator)
        raise TypeError(f"can't add with type {type(other)}")

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Fraction(-self.nominator, self.denominator)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return Fraction(other) - self


def main():
    """Test program"""
    frac_a = Fraction(1, 2)
    print(1 - frac_a)

if __name__ == "__main__":
    main()
