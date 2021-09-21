"""
Skapa en fil med matvaror
Läs in matvarorna vid körning
Låt användare lägga till matvaror
Spara dessa i fil
BONUS: Lägg till möjlighet att ta bort mat
"""

def läsFil(filnamn):
    fil = open(filnamn, "r")
    innehåll = [i.strip() for i in fil.readlines()]
    variabel = "hej"
    return innehåll

def printaMat(mat):
	for m in mat: 
		print(m)
    
def sparaMatTillFil(mat, filnamn):
	fil = open(filnamn, "w")
	for m in mat:
		fil.write(m + "\n")
	fil.close()

def läggTillMat(mat):
	nymat = input("Vad vill du lägga till för mat?")
	if nymat not in mat: 
		mat.append(nymat)
   
def main():
    filnamn = "mat.txt"
    mat = läsFil(filnamn)

    print(" Välkommen till min matbutik ")
    svar = ""

    while svar != "3":
    	svar = input("1. Visa mat, 2. Lägg till mat i listan, 3. Avsluta: ")
    	if svar == "1":
    		printaMat(mat)
    	elif svar == "2":
    		läggTillMat(mat)
    	elif svar == "3": 
    		sparaMatTillFil(mat, filnamn)
    		print("hej då tack för oss!")
main()
