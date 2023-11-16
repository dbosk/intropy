pile = []
pile.append(1)
pile.append(2)
pile.append(3)
print(f"pile = {pile}")

while pile:
    print(f"pile.pop() = {pile.pop()}")
    print(f"pile = {pile}")
