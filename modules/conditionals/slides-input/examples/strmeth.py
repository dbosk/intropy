def str_methods(string1, string2):
    """Visar sträng-experiment med string"""
    print(f"string1 = '{string1}'")
    print(f"string2 = '{string2}'")
    print(f"string1.capitalize() = '{string1.capitalize()}'")
    print(f"string1.upper() = '{string1.upper()}'")
    print(f"string1.center(20, '=') = '{string1.center(20, '=')}'")
    print(f"string2.strip() = '{string2.strip()}'")
    print(f"string1.find(string2) = '{string1.find(string2)}'")
    print(f"string1.find(string2.strip()) = '{string1.find(string2.strip())}'")

str_methods("hej på dig", " hej ")
print()
str_methods("hej på dig", " på ")
