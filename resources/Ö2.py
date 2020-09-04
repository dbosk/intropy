# ovning 2
##
##def rektangel (rad, kolumn):
##    for i in range (rad):
##        s = ""
##        for j in range (kolumn):
##            s = s + "*"
##        print (s)
##
##
##svar = input("hur många rader? ")
##rad = int(svar)
##
##svar = input ("hur manga kolumner? ")
##kolumn = int (svar)
##
##rektangel (rad, kolumn)

import random

secretnumber = random.randint(0,100)
n = 0
guess = -1

while ((guess != secretnumber) and (n<10)):

    svar = input("gissa på ditt tal mellan 0-100:  ")
    guess = int(svar)

    n += 1
    
    if (guess > secretnumber):
        print ("gissa lägre")
        
    elif (guess < secretnumber):
        print ("gissa högre")

    elif (guess == secretnumber):
        print ("WOOOWWWW du gissa rätt")

if (n == 10):
    print ("för många försök loser")







    
