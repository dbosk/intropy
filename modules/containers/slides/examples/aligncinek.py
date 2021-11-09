"""Funktioner för att skriva ut en lista snyggt och prydligt"""

def max_elementbredd(lista):
    """Returnerar bredden för det bredaste elementet i lista"""
    max_bredd = 0
    for element in lista:
        element_bredd = len(str(element))
        if element_bredd > max_bredd:
            max_bredd = element_bredd

    return max_bredd

def print_list(lista, max_skärm_bredd):
    """Skriver ut listan snyggt och prydligt"""
    max_bredd = max_elementbredd(lista)
    max_element_per_rad = max_skärm_bredd // max_bredd

    for index, element in enumerate(lista):
        if (index+1) % max_element_per_rad == 0:
            print(f"{element:{max_bredd}s}")
        else:
            print(f"{element:{max_bredd}s}", end="")

print_list(["adam", "bertil", "cesar", "ada", "beda", "cissi", "benjamin"], 30)
