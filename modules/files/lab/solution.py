""" Läser sparkapital, antal månader och ränta som kan vara olika varja månad och räknar ut
värdeökningen.
"""
from lastal import läs_decimaltal, läs_heltal

def läs_filnamn(prompt):
    """Läser ett filnamn till des att filen går att öppna"""
    fil_öppnad = False
    while not fil_öppnad:
        filnamn = input(prompt)
        try:
            fil = open(filnamn, 'r')
            fil_öppnad = True
        except FileNotFoundError:
            print(filnamn, "existerar inte (i den katalogen). Vänligen försök igen.")
    return fil
    
def läs_räntor(fil):
    """ Läser räntor från fil, returnerar lista med dessa räntor"""
    q=[]
    for rad in fil:
        q.append(float(rad))
    return q

sparkapital = läs_decimaltal("Hur mycket sparkapital har du (ange i kr)?", "Sparkapital")
q=läs_räntor(läs_filnamn("Ange fil med förväntad ränteutveckling: "))

print("    Total     Ökning")
ökning = 0
for m in range(len(q)):
    print("Månad%2d: %8.2f kr %6.2f kr" % (m, sparkapital, ökning))
    ökning = sparkapital*q[m]/100
    sparkapital += ökning
print("Månad%2d: %8.2f kr %6.2f kr" % (m+1, sparkapital, ökning))
