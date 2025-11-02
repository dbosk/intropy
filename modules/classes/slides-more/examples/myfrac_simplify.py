""" Fractions library with simplification """

import math

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
        
        # Simplify the fraction
        self.__simplify()

    def __simplify(self):
        """Simplify the fraction by dividing by GCD"""
        gcd = math.gcd(self.__nominator, self.__denominator)
        self.__nominator //= gcd
        self.__denominator //= gcd

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
            other = Fraction(other)
        if isinstance(other, Fraction):
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
            other = Fraction(other)
        if isinstance(other, Fraction):
            return Fraction(self.nominator * other.nominator,
                            self.denominator * other.denominator)
        raise TypeError(f"can't multiply type {type(other)}")

    def __rmul__(self, other):
        return self * other


def main():
    """Test program"""
    # Test simplification in constructor
    frac1 = Fraction(6, 12)
    print(f"Fraction(6, 12) = {frac1}")
    
    frac2 = Fraction(2, 6)
    print(f"Fraction(2, 6) = {frac2}")
    
    # Test simplification after operations
    frac3 = Fraction(1, 2) + Fraction(1, 4)
    print(f"1/2 + 1/4 = {frac3}")
    
    frac4 = Fraction(1, 2) * Fraction(2, 3)
    print(f"1/2 * 2/3 = {frac4}")
    
    frac5 = Fraction(2, 3) - Fraction(1, 6)
    print(f"2/3 - 1/6 = {frac5}")

if __name__ == "__main__":
    main()
