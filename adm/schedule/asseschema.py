#!/usr/bin/python3
#Skapar html-fil där assarna kan boka in sig på labbar
#Indata (schemat som kommaseparerad csv från TimeEdit): tildah21schema.txt
#Utdata: utfil.html
import sys
from datetime import date
from pandas import *
from math import ceil

class Datum:
    """ Ger datum med veckodag på svenska """
    
    VECKODAG = ["","mån","tis","ons","tor","fre","lör","sön"]
    MÅNAD = ["","jan","feb","mar","apr","maj","juni","juli","aug","sep","okt","nov","dec"]

    def __init__(self, datum):
        [y,m,d] = datum.split("-")
        datumobjekt = date(int(y),int(m),int(d))
        self.dag = datumobjekt.day
        self.veckodag = self.VECKODAG[datumobjekt.isoweekday()]
        self.månad = self.MÅNAD[datumobjekt.month]

    def __str__(self):
        return self.veckodag + " " + str(self.dag) + " " + self.månad

class Labb:
    """ Representerar en labb (Labb1, Labb 2, etc)"""
    
    def __init__(self, labb):
        self.labb = labb

    def __str__(self):
        if "DL" in self.labb:
            nr = self.labb.split(" ")[1]
            return "Labb " + str(int(nr) -1)
        return self.labb


class Labbtid:
    """ Representerar en labbtid i schemat """

    # Förväntat antal assar per studentgrupp ht 2021
    ASSAR = {"CINEK3-PFRI":2.5, "CITEH3":2.5, "CLGYM2-TEDA":1.5, "CMETE2":5.5, "TPRMM1":1}
    
    def __init__(self, datum, starttid, sluttid, labb, grupp):
        self.datum = Datum(datum)
        start = starttid.split(":")[0]
        slut = sluttid.split(":")[0]
        self.tid = start + "-" + slut
        self.labb = Labb(labb)
        self.grupp = grupp

    def __str__(self):
        return str(self.datum) + " " + self.tid + " " + str(self.labb)

    def addera_grupp(self, ny_grupp):
        """ Lägger till en grupp studenter till denna labb """
        self.grupp += "; " + ny_grupp

    def gruppsumma(self):
        """ Uppskattar hur många assar som behövs per pass """  
        grupplista = self.grupp.split("; ")
        summa = 0
        for grupp in grupplista:
            summa += self.ASSAR[grupp]
        return ceil(summa)
        

def justera(rad):
    """ Ordnar rader med flera grupper:
        "CINEK3-PFRI, CLGYM2-TEDA" => CINEK3-PFRI; CLGYM2-TEDA
    """
    del1,del2,_ = rad.split('"')
    del2 = del2.replace(",",";")
    rad = del1 + del2
    return rad


def läs_schema(filnamn):
    """ Läser in schemafilen (kommaseparerad .csv),
        avgör vilken typ av rad som lästs in,
        skapar nytt Labbtid-objekt,
        och lägger till i labblista,
        som returneras. """
    
    with open(filnamn) as schemafil:
        # Ta bort info-raderna i början av filen
        for radnr in range(4):
            schemafil.readline()

        labblista = []
        aktuellt_datum = ""
        aktuell_starttid = ""
        for rad in schemafil:
            rad = rad.strip()
            if '"' in rad:
                rad = justera(rad)
            [datum1,starttid,datum2,sluttid,aktivitet,labb,grupp] = rad.split(",")
            if datum1 != aktuellt_datum:
                # Ny datumrad (dvs nytt labbtillfälle)
                aktuellt_datum = datum1
                aktuell_starttid = starttid
                nytt = Labbtid(datum1, starttid, sluttid, labb, grupp)
                labblista.append(nytt)
            else:
                if starttid != aktuell_starttid:
                    # Samma datum men ny tid (dvs nytt labbtillfälle)
                    aktuell_starttid = starttid
                    nytt = Labbtid(datum1, starttid, sluttid, labb, grupp)
                    labblista.append(nytt)
                else:
                    # Samma labbtillfälle men ny grupp studenter
                    nytt.addera_grupp(grupp) 
    return labblista

def skapa_kolumner(labblista):
    """ Skapar kolumner för html-utskrift """
    datumen = []
    tiderna = []
    labbarna = []
    assarna = []
    antal_assar = []
    grupperna = []
    for objekt in labblista:
        datumen.append(str(objekt.datum))
        tiderna.append(str(objekt.tid))
        labbarna.append(str(objekt.labb))
        assar_per_pass = objekt.gruppsumma()
        antal_assar.append(assar_per_pass)
        asselista_x = ""
        for i in range(assar_per_pass):
            asselista_x += "x "
        assarna.append(asselista_x) 
        grupperna.append(objekt.grupp)
    return datumen, tiderna, labbarna, assarna, antal_assar, grupperna
        
        
def skriv_schema(labblista):
    """ Skriv ut schemat som text """
    for objekt in labblista:
        print(objekt, objekt.gruppsumma())


def main():
    labblista = läs_schema(sys.argv[1])
    skriv_schema(labblista)
    datumen, tiderna, labbarna, assarna, antal_assar, grupperna = skapa_kolumner(labblista)
    # Skriver ut som html-tabell på filen "utfil.html"
    schematabell = pandas.DataFrame({"Datum": datumen, "Tid": tiderna, "Labb": labbarna, "Assar": assarna, "Antal": antal_assar, "Grupper": grupperna})
    schematabell.to_html("utfil.html", index = False)   
                
main()
