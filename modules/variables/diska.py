"""Ett program som skriver ut vad man får i de olika stegen för handdisk"""

def diska(sak):
    """Diskar sak"""
    return skölj(gnugga(doppa_i_vatten(sak)))

def skölj(sak):
    """Sköjler en sak"""
    return f"avsköljt {sak}"

def gnugga(sak):
    """Gnuggar av en sak med diskborsten"""
    return "rengnuggat " + sak

def doppa_i_vatten(sak):
    """Doppar sak i diskvatten"""
    
    return "diskvattendränkt " + sak

print(diska("smutsigt glas"))
