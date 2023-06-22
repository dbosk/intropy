def welcome(name, origin):
    """Returnerar en välkomsttext"""
    return f"Välkommen {name}, du som rest ända från {origin}!"

var1 = "Daniel"
var2 = "Kungsängen"

print(welcome(var1, var2))
print(welcome(var2, var1))
