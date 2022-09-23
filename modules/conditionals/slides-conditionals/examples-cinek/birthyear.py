"""Exempelprogram som frågar efter ålder"""

födelseår = int(input("Vilket år är du född?"))
if födelseår < 1995:
    print("Ojsan hoppsan, här var det riktigt gammalt!")
elif födelseår < 2000:
    print("Oj, du börjar bli gammal!")
else:
    print("Grattis, du är fortfarande ung och fräsch!")
