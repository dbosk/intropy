class Book:
    def __init__(self, t, a, p):
        self.t = t
        self.a = a
        self.p = p
        self.r = 0

    def read(self, n):
        self.r = self.r + n


b1 = Book("Ronja Rövardotter", "Astrid Lindgren", 235)
b2 = Book("Madicken", "Astrid Lindgren", 174)
b1.read(50)
b2.read(300)
print(f"{b1.t} av {b1.a} ({b1.r}/{b1.p} sidor lästa)")
print(f"{b2.t} av {b2.a} ({b2.r}/{b2.p} sidor lästa)")
