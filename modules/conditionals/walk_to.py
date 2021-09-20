"""Ett program med instruktioner för att hitta från Daniels hus till hans 
postlåda"""

def gå(meter, språk="sv"):
    """Går meter antal meter, språk anger språk för instruktionerna"""
    if språk == "sv":
        return f"Gå {meter} m rakt fram."

    return f"Walk {meter} m stright ahead."

def sväng(riktning, språk="sv"):
    """Svänger höger eller vänster, språk anger språk för instruktionerna.
    Riktning anges på svenska, "höger" och "vänster" översätts.
    """
    if språk == "sv":
        return f"Sväng {riktning}."
    elif riktning == "höger":
        return "Turn right."
    elif riktning == "vänster":
        return "Turn left."

    return f"Turn {riktning}."

def gå_till_postlådan(språk="sv"):
    """Ger instruktioner för att gå till affären, språk anger språk för 
    utmatningen."""
    return gå(50, språk=språk) + " " + \
            sväng("höger", språk=språk) + " " + \
            gå(200, språk=språk) + " " + \
            sväng("vänster", språk=språk) + " " + \
            gå(500, språk=språk) + " " + \
            sväng("vänster", språk=språk) + " " + \
            "Framme!"

print(gå_till_postlådan("sv"))
print(gå_till_postlådan("en"))
