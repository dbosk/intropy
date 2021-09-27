"""Olles exempelkörning"""

import tallista

tallista = tallista.läs_in_talföljd("Ge tal: ")
print(tallista)
tallista.append(17)
print(tallista)
tallista.sort()
print(tallista)
