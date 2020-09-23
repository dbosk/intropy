# def skapaPokemon()
# 	Fråga användaren om namn, vikt, styrka och snabbhet av deras pokemon
# 	Returnera listan [namn, vikt, styrka, snabbhet]
# def göraStarkare(styrka)
# 	Öka pokemonens styrka med ett värde
# 	Returnera den nya styrkan
# def göraSnabbare(snabbhet)
# 	Öka pokemonens snabbhet med ett värde
# 	Returnera den nya snabbheten
# def göraTjockare(vikt, snabbhet, styrka)
# 	Öka pokemonens snabbhet med ett värde
# 	Returnera den nya vikten, snabbheten och styrkan

# Skapa en pokemon och lek med att göra den starkare, snabbare och tjockare
# Skriv ut listan på pokemonen och dess egenskaper så att man ser hur vikten, styrkan och snabbheten ändras



def skapaPokemon():
	namn = input("vad heter din pokemon? ")
	vikt = int(input ("hur många kilo väger din pokemon (1-50) "))
	styrka = int(input("vad är din pokemons styrka? (1-10) "))
	snabbhet = int(input ("vad är din pokemons snabbhet? (1-10)"))

	minPokemon = [namn, vikt, styrka, snabbhet]
	return minPokemon

def göraStarkare(styrka):
	styrka = styrka + 2
	return styrka 

def göraSnabbare(snabbhet):
	snabbhet += 1
	return snabbhet 
	
def göraTjockare(vikt, snabbhet, styrka):
	vikt += 2
	snabbhet -= 1
	styrka -= 2
	return vikt, snabbhet, styrka
	
pokemon = skapaPokemon()
print(pokemon)
pokemon[1], pokemon[3], pokemon[2] = göraTjockare(pokemon[1], pokemon[3], pokemon[2])
print(pokemon)

