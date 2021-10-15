"""Modul för att arbeta med talföljder"""

def läs_tal(fil):
    """ Läser tal från fil, returnerar lista med dessa tal"""
    q = []
    for rad in fil:
        q.append(float(rad))
    return q


class ArithmeticSequence:
    """Klass för en aritmetisk talföljd"""

    def __init__(self, a1, d):
        """a1 är första talet i följden, d är differensen mellan talen i 
        följden"""
        self.a1 = a1
        self.d = d

    def __getitem__(self, n):
        """Returnerar det n:te talet i talföljden"""
        if n < 0:
            raise IndexError("kan inte plocka ut sista värdet i en "
                             "oändlig lista")
            # eller bara raise IndexError

        return self.a1+self.d*(n-1)

class GeometricSequence:
    """Klass för en geometrisk talföljd"""

    def __init__(self, g1, q):
        """g1 är första talet i följden, q är kvoten mellan talen i följden"""
        self.g1 = g1
        self.q = q

    def __getitem__(self, n):
        """Returnerar det n:te talet i talföljden"""
        if n < 0:
            raise IndexError

        return self.g1*(self.q**n-1)/(self.q-1)

class MultiplicativeSequenceFromFile:
    """Klass för en ändlig  multiplikativ 'talföljd', där kvoten varierar 
    mellan talen i följden"""

    def __init__(self, filnamn):
        """Läser in kvoterna i följden från en fil med namnet filnamn 
        (sträng)"""
        try:
            fil = open(filnamn, 'r')
        except FileNotFoundError:
            # snyggar till felmeddelandet
            raise FileNotFoundError(
                filnamn+" existerar inte (i den katalogen).")
        self.talserie = läs_tal(fil)

    def __getitem__(self, n):
        """Returnerar det n:te talet i följden,
        negativa n börjar från slutet i listan."""
        return self.talserie[n]
