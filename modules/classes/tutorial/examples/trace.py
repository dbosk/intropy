from book import Book


def two_books():
    """Returns two new books, neither of them read"""
    return (
        Book("Ronja Rövardotter", "Astrid Lindgren", 235),
        Book("Madicken", "Astrid Lindgren", 174),
    )


def main():
    """Test program"""
    ronja, madicken = two_books()
    ronja.read(50)
    ronja.read(30)
    print(ronja)
    print(madicken)

    ronja, madicken = two_books()
    ronja.read(50)
    madicken.read(30)
    print(ronja)
    print(madicken)


if __name__ == "__main__":
    main()
