class Funktionslik:
    def __init__(self, max_antal):
        self.max_antal = max_antal
        self.anrop = 0

    def __call__(self, x):
        self.anrop += 1
        if self.anrop > self.max_antal:
            return None
        return x+1

def main():
    funk = Funktionslik(5)

    for i in range(10):
        print(funk(i))

main()
