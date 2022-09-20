"""Ett program som visar defaultparametrar"""

def hello(who="World"):
    """Skriver ut 'Hello {who}!', om who inte anges används 'World'"""
    print(f"Hello {who}!")

hello("Daniel")
hello()
