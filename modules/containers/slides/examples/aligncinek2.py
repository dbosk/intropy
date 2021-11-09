"""Funktioner för att skriva ut en lista snyggt och prydligt"""

def max_elementbredd(lista):
    """Returnerar bredden för det bredaste elementet i lista"""
    max_bredd = 0
    for element in lista:
        element_bredd = len(str(element))
        if element_bredd > max_bredd:
            max_bredd = element_bredd

    return max_bredd

def print_with_spaces(item, max_bredd, brytning):
    """Skriver ut item med bredden max_bredd"""
    item_str = str(item)
    print(item_str + " "*(max_bredd-len(item_str)), end=brytning)

def print_list(lista, max_skärm_bredd):
    """Skriver ut listan snyggt och prydligt"""
    max_bredd = max_elementbredd(lista)
    max_element_per_rad = max_skärm_bredd // max_bredd

    for index, element in enumerate(lista):
        if (index+1) % max_element_per_rad == 0:
            print_with_spaces(element, max_bredd, "\n")
        else:
            print_with_spaces(element, max_bredd, "")

