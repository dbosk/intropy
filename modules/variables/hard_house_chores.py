def blommor():
    print("Vill du vattna blommorna? ")
    yes = input()

    if yes == "yes":
        print("Vattnar blommorna")


def sopor(string):
    print(string)
    no = input()

    if not no == "no":
        print("Tar ut soporna")
        return True
    else:
        return False


chores = ["Tömma diskmaskinen", "Dammsuga mormors hus", "Gå ut med hunden"]

b = blommor()

sopor("Vill du ta ut soporna?")

print("Förutom att vattna blommor och ta ut sopor ska vi:")

def func():
    for x in chores:
        print(x)
        
func()
