#Visar komponenterna: Label, Entry, Checkbutton, Radiobutton
#Visar layout-hanteraren Grid

from tkinter import *

# Skapa rotfönstret
roten = Tk()               

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

kryssruta1= Checkbutton(roten, text="modig")
kryssruta2= Checkbutton(roten, text="smart")
kryssruta3= Checkbutton(roten, text="obetänksam")

radio1 = Radiobutton(roten, text="trollkarl")
radio2 = Radiobutton(roten, text="jediriddare")
radio3 = Radiobutton(roten, text="grekisk gud")


# Organisera i rader och kolumner
# Sticky: What to do if the cell is larger than widget
# https://effbot.org/tkinterbook/tkinter-application-windows.htm

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

# There is a method known by the name mainloop() is
# used when you are ready for the application to run. mainloop()
# is an infinite loop used to run the application,
# wait for an event to occur and process the event till the window is not closed.




