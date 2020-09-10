from tkinter import *

#Hämtar data från komponenterna och skriver ut sagan i Text

def strdata(v):
    val = v.get()
    if val != "0":
        return val
    else:
        return ""

def skrivsaga():
    person   = inmatningPerson.get()
    plats    = inmatningPlats.get()
    verb     = inmatningVerb.get()
    adjektiv = strdata(adj1) + strdata(adj2) + strdata(adj3)
    varelsetyp = varelse.get()
    saga = "Det var en gång en föräldralös flicka som hette " + person
    saga += " som bodde med sin moster och morbror på " + plats
    saga += ". Hon räddas av en skäggig typ som visar sig vara en " + varelsetyp
    saga += ". " + person + ", som är mycket " + adjektiv
    saga += " lär sig också att bli en " + varelsetyp + " och "
    saga += verb + "r ondskans makter. Slut.\n\n"
    textruta.insert(END, saga)   # Skriv den sist i textrutan

# Skapa rotfönstret
roten = Tk()                 
roten.title("Din egen saga")

# Variabler att spara ord i
adj1 = StringVar()          
adj2 = StringVar()
adj3 = StringVar()
varelse= StringVar()

#Skapa grafiska komponenter
etikett0 = Label(roten, text="Fyll i information till sagan!")
etikett1 = Label(roten, text="Person:")
etikett2 = Label(roten, text="Plats:")
etikett3 = Label(roten, text="Verb:")
etikett4 = Label(roten, text="Adjektiv:")
etikett5 = Label(roten, text="Varelse:")

inmatningPerson = Entry(roten)
inmatningPlats = Entry(roten)
inmatningVerb = Entry(roten)

kryssruta1= Checkbutton(roten, text="modig", variable=adj1, onvalue="modig")
kryssruta1.deselect()
kryssruta2= Checkbutton(roten, text="smart", variable=adj2, onvalue="smart")
kryssruta2.deselect()
kryssruta3= Checkbutton(roten, text="obetänksam", variable=adj3, onvalue="obetänksam")
kryssruta3.deselect()

tryckknapp= Button(roten, text="Skriv saga", command=skrivsaga)

radio1 = Radiobutton(roten, text="trollkarl", variable=varelse, value="trollkarl")
radio2 = Radiobutton(roten, text="jediriddare", variable=varelse, value="jediriddare")
radio3 = Radiobutton(roten, text="grekisk gud", variable=varelse, value="grekisk gud")

textruta   = Text(roten, width=75, height=10, wrap=WORD)

# Organisera i rader och kolumner
roten.grid()                 
etikett0.grid(row=0, column=0, columnspan=2, sticky=W)
etikett1.grid(row=1, column=0, sticky=W)
etikett2.grid(row=2, column=0, sticky=W)

etikett3.grid(row=3, column=0, sticky=W)
etikett4.grid(row=4, column=0, sticky=W)
etikett5.grid(row=5, column=0, sticky=W)

inmatningPerson.grid(row=1, column=1, sticky=W)
inmatningPlats.grid(row=2, column=1, sticky=W)
inmatningVerb.grid(row=3, column=1, sticky=W)

kryssruta1.grid(row=4, column=1)
kryssruta2.grid(row=4, column=2)
kryssruta3.grid(row=4, column=3)
tryckknapp.grid(row=6, column=0, sticky=W)

radio1.grid(row=5, column=1)
radio2.grid(row=5, column=2)
radio3.grid(row=5, column=3)

textruta.grid(row=7, column=0,columnspan=4)

# Visa fönstret och vänta på händelser
roten.mainloop()             
