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
print(b1.t + " av " + b1.a + " (" + str(b1.r) + "/" + str(b1.p) + ")")
print(b2.t + " av " + b2.a + " (" + str(b2.r) + "/" + str(b2.p) + ")")
