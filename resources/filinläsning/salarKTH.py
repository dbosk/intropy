def lasInSalar():
    infil = open("salar.txt", "r", encoding="latin-1") #utf 8
    d = dict()
    rader = infil.readlines()
    for rad in rader:
        raddelar = rad.split(":")
        d[raddelar[0]] = int(raddelar[1])
    return d


# main ska inte ha returvärde!!!!
def main ():
    salar = lasInSalar()
    print ("Välkommen till bokningssystemet")
    svar = ""
    s = ""
    for k in salar.keys():
        s += " " + k
    print ("Lediga salar är: " + s)

    svar = input ("Vilka salar vill du boka (separera med mellanslag)!!")
    bokade = svar.split()

    datorer = 0
    for b in bokade:
        datorer += salar[b]

    print("du har bokat: ")
    for b in bokade:
          print (b, salar[b], "datorer")
    print ("Totalt", datorer, "datorer")

main()
