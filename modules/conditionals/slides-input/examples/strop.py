def str_operators(string1, string2, number):
    """Visar sträng-experiment med string"""
    print(f"string1 = '{string1}'")
    print(f"string2 = '{string2}'")
    print(f"string1 + string2 = '{string1+string2}'")
    print(f"string1 * {number} = '{string1*number}'")
    print(f"string1[{number}] = '{string1[number]}'")
    print(f"string2[{number}] = '{string2[number]}'")
    print(f"string1[{number}:{number+3}] = '{string1[number:number+3]}'")
    print(f"string2[{number}:{number+3}] = '{string2[number:number+3]}'")

str_operators("hej på dig", "hello there", 3)
str_operators("hejsan", "svejsan", 2)
