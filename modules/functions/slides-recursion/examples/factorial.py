"""Calculate factorial"""

import input_type

def factorial(num):
    """returns the factorial of num"""
    if num == 1:
        return 1
    elif num < 1:
        raise Exception("Must be positive numbers")
    return num*factorial(num-1)

def main():
    """test the functions in this module"""
    num = input_type.input_type(int, "Enter a number: ")
    try:
        print(f"{num}! = {factorial(num)}")
    except Exception as err:
        print(err)
        return

if __name__ == "__main__":
    main()
