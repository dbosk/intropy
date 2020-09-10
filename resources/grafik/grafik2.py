#Visar StringVar kopplad till komponent, och kontrollutskrift

from tkinter import *

def kontrollutskrift(variabel):
    print(variabel.get())

# Skapa rotfönstret
roten = Tk()

# Variabler att spara ord i  skapar tkintervariabler  
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

# offvalue= The value corresponding to a non-checked button.
# The default is 0. (offValue/Value)
# onvalue=
# The value corresponding to a checked button.
# The default is 1. (onValue/Value)

kryssruta1= Checkbutton(roten, text="modig", variable=adj1, \
                        command = lambda: kontrollutskrift(adj1), onvalue=" modig ")
kryssruta2= Checkbutton(roten, text="smart", variable=adj2, \
                        command = lambda: kontrollutskrift(adj2), onvalue=" smart")
kryssruta3= Checkbutton(roten, text="obetänksam", variable=adj3, \
                        command = lambda: kontrollutskrift(adj3), onvalue=" obetänksam")

radio1 = Radiobutton(roten, text="trollkarl", variable=varelse, \
                     command = lambda: kontrollutskrift(varelse), value="trollkarl")
radio2 = Radiobutton(roten, text="jediriddare", variable=varelse, \
                     command = lambda: kontrollutskrift(varelse), value="jediriddare")
radio3 = Radiobutton(roten, text="grekisk gud", variable=varelse, \
                     command = lambda: kontrollutskrift(varelse), value="grekisk gud")


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

radio1.grid(row=5, column=1)
radio2.grid(row=5, column=2)
radio3.grid(row=5, column=3)

# Visa fönstret och vänta på händelser
roten.mainloop()  
