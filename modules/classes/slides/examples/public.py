"""
An example with classes with public attributes and methods.
"""

class PublicExample:
    def __init__(self, value):
        self.value = value  # Public attribute

    def get_value(self):  # Public method
        return self.value

    def set_value(self, new_value):  # Public method
        self.value = new_value

def main():
    """Example program"""
    example = PublicExample(10)
    print(f"Initial value: {example.get_value()}")
    example.set_value(20)
    print(f"Updated value: {example.get_value()}")
    example.value = 30
    print(f"Directly modified value: {example.value}")

if __name__ == "__main__":
    main()
