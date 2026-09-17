---
title: 'Föreläsning: Fler behållare och mer om klasser'
regex: '^Föreläsning: Fler behållare och mer om klasser$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Fler behållare och mer om klasser$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har fem delar: *Behållare: Uppslagslistor*, *Behållare:
Mängder, stackar och köer*, *Behållare: Ett gissningsspel*,
*Operatoröverlagring* och *Praktiska tillämpningar av klasser*. Bilderna
visas under föreläsningen. Anteckningarna till varje del finns som ett
interaktivt dokument (FeedbackFruits) här i modulen: *Behållare:
Uppslagslistor (föreläsningsanteckningar)*, *Behållare: Mängder, stackar
och köer (föreläsningsanteckningar)*, *Behållare: Ett gissningsspel
(föreläsningsanteckningar)*, *Operatoröverlagring
(föreläsningsanteckningar)* och *Praktiska tillämpningar av klasser
(föreläsningsanteckningar)*; läs dem efter föreläsningen, eller i
stället för den om du inte kan komma, och svara på frågorna i
dokumenten. Som komplement finns kursens videogenomgångar *Behållare:
Gissningsspel* till delen *Behållare: Ett gissningsspel*, och *Klasser:
Operatoröverlagring* till delen *Operatoröverlagring*.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

### Behållare: Uppslagslistor

En lista håller reda på värden efter deras plats: det första, det andra,
det tredje. Men det vi oftast vill slå upp något efter är inte en plats
utan ett namn, till exempel telefonnumret som hör till Ronja. Den här
delen inför uppslagslistan (dictionary), behållaren som parar ihop en
nyckel med ett värde. Vi slår upp, lägger till och ändrar, hanterar
nycklar som saknas, går igenom både nycklar och par, och jämför
uppslagslistan med listan för att kunna välja rätt behållare utifrån
vilka operationer programmet behöver. Delen avslutas med en telefonbok:
ett program som byggs upp av användaren, skrivs ut i bokstavsordning på
snygga rader och går att söka i.

### Behållare: Mängder, stackar och köer

Listan, tupeln och uppslagslistan täcker det mesta, men inte allt. Den
här delen inför tre behållare till, som var och en svarar på sin egen
fråga. Mängden svarar på vilka olika värden som finns: den har inga
dubbletter och ingen ordning, och kan jämföras med andra mängder med
union, snitt och differens. Stacken och kön svarar på vilket element som
ska tas härnäst, och de svarar olika: stacken lämnar ut det som lades in
sist, kön det som lades in först. Vi bygger stacken av en lista och kön
av `collections.deque`, och ser i Pythons dokumentation varför det inte
blir tvärtom. Delen avslutas med att sätta alla behållarna bredvid
varandra: valet styrs av vilka operationer programmet behöver.

### Behållare: Ett gissningsspel

Den här delen bygger ett enda program, från början till slut: ett
gissningsspel som spelas i flera omgångar och som till sist berättar hur
många försök du behövde i genomsnitt. Programmet är litet, men det
kräver allt vi gått igenom samtidigt — en behållare som samlar
resultaten medan spelet pågår, upprepningar som driver omgångarna och
gissningarna, funktioner som delar upp arbetet, och felhantering för att
användaren kan skriva vad som helst. Vi utvecklar det med stegvis
förfining, och tar upp frågan om hur man får ett program som slumpar att
bete sig likadant två gånger.

### Operatoröverlagring

Den här delen fördjupar kunskapen i objektorienterad programmering genom
att visa hur vi överlagrar operatorer i Python: hur våra egna klasser
kan bete sig som språkets inbyggda typer. Vi bygger en klass för
matematiska bråk, `Fraction`, steg för steg: en konstruktor som tar emot
flera slags argument, egenskaper för att läsa täljare och nämnare,
typkonvertering till sträng, flyttal och heltal, addition, subtraktion
och multiplikation med både bråk och heltal på vardera sidan om
operatorn, och till sist automatisk förkortning. På vägen ser vi varför
`1 + a` kräver en annan dundermetod än `a + 1`, och när den ena kan
återanvända den andra.

### Praktiska tillämpningar av klasser

Den här delen tillämpar klasser på två större exempel: en inköpslista
och ett enkelt banksystem. Inköpslistan är en klass som har en behållare
av varor som attribut och metoder som lägger till, visar, bockar av och
tar bort varor i den; vi frågar oss sedan om varje vara ska vara en
uppslagslista eller en egen klass, och väger enkelhet mot struktur.
Banksystemet består av flera klasser som samverkar — person, adress,
konto och medborgare — och visar komposition (en klass har ett objekt
av en annan som attribut) och arv (en klass specialiserar en annan) sida
vid sida, så att valet mellan dem blir tydligt. Delen avslutas med de
designprinciper exemplen praktiserar.

## Lärandemål

Efter föreläsningen ska du kunna

**Behållare: Uppslagslistor:**

- skapa en uppslagslista, slå upp ett värde med sin nyckel, samt lägga
  till och ändra par, och förklara varför en nyckel inte är ett index,
- hantera att en nyckel saknas, med `in`, med `try`/`except KeyError`
  eller med `get`, och välja mellan sätten,
- gå igenom en uppslagslista: dess nycklar, dess värden och dess par med
  `items`, samt i sorterad ordning,
- välja mellan lista och uppslagslista utifrån vilka operationer
  programmet behöver, och motivera valet,
- bygga ett program som samlar in data i en uppslagslista, skriver ut
  den läsbart och låter användaren söka i den,
- hitta och läsa dokumentationen för uppslagslistor och därifrån
  använda en metod som inte gåtts igenom på föreläsningen.

**Behållare: Mängder, stackar och köer:**

- skapa och använda en mängd — unika element, medlemskap, samt union,
  snitt och differens — och förklara varför en mängd varken har ordning
  eller dubbletter,
- använda en lista som stack, med `append` och `pop`, och förklara
  sist-in-först-ut,
- använda `collections.deque` som kö, med `append` och `popleft`,
  förklara först-in-först-ut, och motivera varför en lista är ett sämre
  val för en kö,
- välja behållare — lista, tupel, mängd, uppslagslista, stack eller kö
  — utifrån vilka operationer programmet behöver, och motivera valet,
- hitta och läsa dokumentationen för Pythons behållare och därifrån
  använda en behållare eller metod som inte gåtts igenom på
  föreläsningen.

**Behållare: Ett gissningsspel:**

- använda en lista för att samla resultat under körningen, och
  sammanfatta den efteråt med `sum` och `len`,
- skriva en återanvändbar funktion som läser in och kontrollerar
  användarens inmatning och frågar om igen tills den duger,
- utveckla ett program som kombinerar behållare, upprepningar,
  funktioner och felhantering, genom stegvis förfining från överblick
  till körbar kod,
- förklara varför ett program som slumpar är svårt att testa, och göra
  en körning upprepbar genom att sätta slumpgeneratorns startvärde.

**Operatoröverlagring:**

- implementera operatoröverlagring med dundermetoder som `__add__`,
  `__sub__` och `__mul__`,
- förklara skillnaden mellan `__add__` och `__radd__` (och motsvarande
  för andra operatorer), och redogöra för när Python anropar vilken,
- använda dekoratorn `@property` för att läsa attribut som egenskaper,
- implementera typkonvertering med `__str__`, `__float__` och
  `__int__`,
- avgöra när en omvänd operator kan återanvända den vanliga — när
  operationen är kommutativ — och när den inte kan det,
- designa en klass som representerar en matematisk storhet, med en
  entydig representation av varje värde,
- använda `isinstance()` för att låta en metod hantera argument av
  olika typer.

**Praktiska tillämpningar av klasser:**

- konstruera program där en klass har en behållare av andra objekt som
  attribut, och där metoderna söker i och uppdaterar behållaren,
- välja mellan att representera data med en uppslagslista eller med en
  egen klass, och motivera valet utifrån programmets storlek och behov,
- använda komposition för att bygga klasser av andra klasser,
- använda arv för att specialisera en klass, och anropa
  föräldraklassens metoder med `super()`,
- avgöra när komposition respektive arv passar bäst, och känna igen
  designprinciperna bakom valet i egen och andras kod.

## Förkunskaper

Föreläsningen bygger på tidigare veckors föreläsningar *Funktioner*,
*Inmatning och felhantering*, *Upprepningar*, *Behållare: Listor* och
*Behållare: Tupler* samt på *Klasser och objekt* från vecka 41: du ska
kunna skriva egna funktioner, fånga särfall med `try`/`except`, använda
`for`- och `while`-slingor, arbeta med listor och tupler, och skriva en
klass med attribut, metoder, parametern `self` och dundermetoderna
`__init__` och `__str__`. Inom föreläsningen bygger *Behållare: Mängder,
stackar och köer* och *Praktiska tillämpningar av klasser* vidare på
dess första del, *Behållare: Uppslagslistor*; *Operatoröverlagring*
bygger dessutom på bråkräkning från matematiken (gemensam nämnare,
förkortning och största gemensamma delare); och *Praktiska tillämpningar
av klasser* bygger också på sin föregående del, *Operatoröverlagring*,
och på *Behållare: Listor*, inklusive listbyggare (list comprehensions).

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning fler behållare och mer om
klasser* för din grupp — ha dokumentationen för Pythons behållare uppe
under övningen — och arbeta i par med *Laboration (5) behållare och
klasser (kamratgranskning)*. Läsförståelseövningen *Läsförståelse:
Dokumentation för olika behållare* hör till veckans behållardelar och
arbetar med samma dokumentation som de hänvisar till. Vill du fördjupa
dig, gör *Fördjupande övning fler behållare och mer om klasser*.
