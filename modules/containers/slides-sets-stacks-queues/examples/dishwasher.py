"""Ett program som skriver ut vad man får i de olika stegen för handdisk"""

def diska(saker):
    """Diskar sakerna i listan saker"""
    diskho = []
    sköljho = []
    rena_saker = []

    print("Fyll diskho med varmt vatten och diskmedel.")
    print("Fyll sköljho med kallt rent vatten.")

    for sak in saker:
        stoppa_i_diskhon(sak, diskho)

    while diskho:
        sak = ta_upp_ur_diskhon(diskho)
        stoppa_i_diskhon(gnugga(sak), sköljho)

    while sköljho:
        sak = ta_upp_ur_diskhon(sköljho)
        rena_saker.append(torka(skölj(sak)))

    return rena_saker

def stoppa_i_diskhon(sak, diskho):
    """Stoppar sak (sträng) i diskho (lista)."""
    diskho.append(sak)
    print(f"Lägger {sak} i disk-/sköljhon, resultat: {diskho}")

def ta_upp_ur_diskhon(diskho):
    """Tar upp en sak ur diskho (lista)"""
    sak = diskho.pop()
    print(f"Tar upp {sak} ur disk-/sköljhon, resultat: {diskho}")
    return sak

def genus(sak):
    """Returnerar en, ett eller flera för att indikera genus på sak,
    utrum (en-ord) och neutrum (ett-ord)"""
    if "smutsigt" in sak:
        return "t"
    elif "smutsiga" in sak:
        return "flera"
    elif not ("smutsigt" in sak or "smutsiga" in sak):
        return "n"

def skölj(sak):
    """Sköljer en sak"""
    genuset = genus(sak)

    if genuset == "t":
        return f"avsköljt {sak}"
    elif genuset == "n":
        return f"avsköljd {sak}"

    return f"avsköljda {sak}"

def torka(sak):
    """Torkar en sak"""
    genuset = genus(sak)

    if genuset == "t":
        return f"torkat {sak}"
    elif genuset == "n":
        return f"torkad {sak}"

    return f"torkade {sak}"

def gnugga(sak):
    """Gnuggar av en sak med diskborsten"""
    genuset = genus(sak)

    if genuset == "t":
        return f"rengnuggat {sak}"
    elif genuset == "n":
        return f"rengnuggad {sak}"

    return "rengnuggade " + sak


if __name__ == "__main__":
    disk = ["smutsig tallrik", "smutsigt glas", "smutsiga bestick"]

    print("Vår disk:")
    for sak in disk:
        print(f"- {sak}")

    print()

    rent = diska(disk)
    print("\nVår rena disk:")
    for sak in rent:
        print(f"- {sak}")

