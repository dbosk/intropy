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

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.nominator * other, self.denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.nominator * other.nominator,
                            self.denominator * other.denominator)
        raise TypeError(f"can't multiply type {type(other)}")

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        nom1 = self.nominator * other.denominator
        nom2 = other.nominator * self.denominator
        return nom1 < nom2

    def __eq__(self, other):
        nom1 = self.nominator * other.denominator
        nom2 = other.nominator * self.denominator
        return nom1 == nom2


def main():
    """Test program"""
    frac_a = Fraction(1, 2)
    frac_b = Fraction(2, 4)
    if frac_a == frac_b: # frac_a.__eq__(frac_b)
        print(f"{frac_a} = {frac_b}")
    elif frac_a > frac_b: # frac_a.__gt__(frac_b) --> not (a <= b)
        print(f"{frac_a} > {frac_b}")
    elif frac_a < frac_b: # frac_a.__lt__(frac_b)
        print(f"{frac_a} <= {frac_b}")

    fracs = sorted([Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)])
    #fracs = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
    #fracs.sort()
    for frac in fracs:
        print(frac)

    print(f"Summan är {sum(fracs)}")

if __name__ == "__main__":
    main()
