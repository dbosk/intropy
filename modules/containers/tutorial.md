---
title: 'Övning: Fler behållare och mer om klasser'
regex: '^Övning: Fler behållare och mer om klasser$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Fler behållare och mer om klasser$'
    position: 3
---
Den här veckan går vi igenom det nya innehållet på övningarna, eftersom
föreläsningen är en repetition av hela kursen. Övningarna är frivilliga
och ges för hela klassen, i D37 och på [Zoom][zoom-room]; tider och plats
står i veckoöversikten överst i modulen. På tisdagen tar vi allt du
behöver till *Laboration (5) behållare och klasser (kamratgranskning)*,
och på onsdagen operatoröverlagring och arv. Onsdagens övning bygger inte
på tisdagens, så du kan komma på den ena utan den andra. Samtidigt med
onsdagens övning leder en assistent, oftast Emelie, en repetition i ett
eget grupprum på Zoom, så långt tillbaka i kursen som behövs.

Kan du inte komma, eller föredrar du att läsa, står allt vi går igenom i
anteckningarna till veckans fyra delar, se *Veckans fyra delar* nedan.
Uppgifterna och deras lösningsförslag finns i det interaktiva dokumentet
(FeedbackFruits) här i modulen, *Övning: Fler behållare och mer om
klasser (övningsanteckningar)*: pröva varje uppgift innan du läser
lösningen.

[zoom-room]: https://kth-se.zoom.us/j/61952197407

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Vad vi går igenom på övningarna

### Tisdag: det laborationen behöver

1. **Uppgift 4: Banken.** Bygga en bank vars konton ligger i en behållare
   inuti klassen. Ska kontona ligga i en lista eller i en uppslagslista,
   och vad ska ett konto i så fall hittas med? Det är frågan om att välja
   behållare, samma fråga som laborationen ställer. På vägen: egenskaper
   med `@property`, ett konto som *har* en person som ägare, och om ett
   misslyckat uttag ska kasta ett särfall eller lämna tillbaka `False`.
   Banken har samma form som laborationen: en klass som har en behållare
   av andra objekt.
2. **Om vi hinner: uppslagslista eller klass?** Avsnittet *Att
   representera varor: uppslagslistor eller klass?* i anteckningarna
   *Praktiska tillämpningar av klasser*: varor som uppslagslistor i ett
   litet program, `items1.py`, och vad en egen klass för varorna ändrar.

### Onsdag: operatoröverlagring och arv

1. **Operatoröverlagring.** I anteckningarna *Operatoröverlagring*
   bygger vi en klass för bråk: konstruktorn, addition med `__add__`, och
   varför `a + 1` fungerar medan `1 + a` kräver en annan dundermetod,
   `__radd__`. Sedan subtraktionen, och varför `__rsub__` inte kan
   återanvända `__sub__` på samma sätt (avsnitten *Konstruktorn*,
   *Addition* och *Subtraktion*).
2. **Arv.** Avsnittet *Arv: medborgare med personnummer* i
   anteckningarna *Praktiska tillämpningar av klasser*: en klass som
   specialiserar en annan, och föräldraklassens metoder med `super()`.
3. **Komposition eller arv.** Avsnittet med samma namn i samma
   anteckningar: när en klass ska *ha* ett objekt av en annan klass, och
   när den ska *vara* en sådan.

## På egen hand

Resten av övningens uppgifter gör du på egen tid; lösningsförslagen i
dokumentet låter dig kontrollera dina egna svar.

1. **Uppgift 1: Giltiga e-postadresser.** Kontrollera inlästa
   e-postadresser och samla de unika domänerna i en mängd. Hör till den
   valfria delen *Behållare: Mängder, stackar och köer*.
2. **Uppgift 2: Bokstavsräknaren.** Räkna hur ofta varje bokstav
   förekommer i en text, med en uppslagslista som byggs upp medan
   programmet läser.
3. **Uppgift 3: Bråk som går att jämföra.** Bygga ut bråkklassen med
   jämförelse, division och en dundermetod som gör bråk dugliga som
   nyckel i en uppslagslista.
4. **Uppgift 5: Att ångra det senaste.** Bygga ut banken från Uppgift 4
   så att den minns överföringarna och kan ångra dem. Hör till den valfria
   delen *Behållare: Mängder, stackar och köer*. Har du inte löst Banken
   själv kan du utgå från [bankmodulen som Uppgift 4 lämnar den][bank-start];
   hela lösningen, [bank.py med ångrandet][bank], tittar du på när du har
   försökt.
5. **Fördjupning: Uppgift 6: Ett bättre cowsay.** Radbryta text i en
   pratbubbla, med en `deque` som håller reda på orden som återstår.
6. **Fördjupning: Uppgift 7: Lyckokakor och kon.** Sätta samman en
   lyckokaksmodul och kon-modulen i ett eget program med reproducerbar
   slump.

[bank-start]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/examples/start/bank.py
[bank]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/examples/bank.py

## Veckans fyra delar

Anteckningarna till var och en av delarna finns som ett interaktivt
dokument (FeedbackFruits) här i modulen, *Behållare: Mängder, stackar och
köer (föreläsningsanteckningar)* och så vidare; läs dem och svara på
frågorna i dokumenten. *Behållare: Ett gissningsspel* och
*Operatoröverlagring* finns också som videoföreläsningar, *Behållare: Ett
gissningsspel (videoföreläsning)* och *Operatoröverlagring
(videoföreläsning)*.

<!-- TODO: FBF-dokumenten skapas av författaren -->

### Behållare: Mängder, stackar och köer (valfritt)

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

**Att läsa:** hela delen är valfri fördjupning.

Efter den här delen ska du kunna

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
  använda en behållare eller metod som inte gåtts igenom i
  anteckningarna.

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

**Att läsa:** hela delen. **Före labben:** avsnittet *Att läsa in en
gissning*, en återanvändbar funktion som läser in och kontrollerar
inmatning.

Efter den här delen ska du kunna

- använda en lista för att samla resultat under körningen, och
  sammanfatta den efteråt med `min` och `statistics.mean`,
- skriva en återanvändbar funktion som läser in och kontrollerar
  användarens inmatning och frågar om igen tills den duger,
- utveckla ett program som kombinerar behållare, upprepningar,
  funktioner och felhantering, genom stegvis förfining från överblick
  till körbar kod,
- förklara varför ett program som slumpar är svårt att testa, och göra
  en körning upprepbar genom att sätta slumpgeneratorns startvärde.

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

**Att läsa:** avsnitten *Attribut som egenskaper*, *Typkonvertering*,
*Negation*, *Multiplikation*, *Förkortning* och *Sammanfattning*. Resten
går vi igenom på onsdagens övning.

Efter den här delen ska du kunna

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

**Att läsa:** **före labben** avsnittet *Inköpslistor med klasser*. I
övrigt resten, utom *Arv: medborgare med personnummer* och *Komposition
eller arv*, som vi går igenom på onsdagens övning.

Efter den här delen ska du kunna

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

Veckans delar bygger på föreläsningarna *Funktioner*, *Inmatning och
felhantering*, *Upprepningar*, *Behållare: Listor*, *Behållare: Tupler*,
*Behållare: Uppslagslistor* och *Klasser och objekt*: du ska kunna
skriva egna funktioner, fånga särfall med `try`/`except`, använda `for`-
och `while`-slingor, arbeta med listor, tupler och uppslagslistor, och
skriva en klass med attribut, metoder, parametern `self` och
dundermetoderna `__init__` och `__str__`. *Operatoröverlagring* bygger
dessutom på bråkräkning från matematiken (gemensam nämnare, förkortning
och största gemensamma delare), och *Praktiska tillämpningar av klasser*
bygger på *Operatoröverlagring* och på listbyggare (list comprehensions)
från *Behållare: Listor*.

## Förberedelser

Till övningarna behöver du inget utöver förkunskaperna ovan. Ha
dokumentationen för Pythons behållare uppe, kapitlet [Data
Structures][datastructures] i Pythons handledning: att hitta och läsa i
den är en stor del av veckans mål. Till onsdagens övning behöver du inget
från tisdagens. Vill du göra Uppgift 5 utan att ha löst Banken, utgå från
[bankmodulen som Uppgift 4 lämnar den][bank-start].

[datastructures]: https://docs.python.org/3/tutorial/datastructures.html

## Efter övningen

Fortsätt enligt veckoöversikten: arbeta i par med *Laboration (5)
behållare och klasser (kamratgranskning)*. Före labben behöver du
Banken från tisdagens övning och, i anteckningarna, avsnittet *Att läsa
in en gissning* i *Behållare: Ett gissningsspel* och avsnittet
*Inköpslistor med klasser* i *Praktiska tillämpningar av klasser*.
Labbens frivilliga extrauppgift bygger på arv, som vi går igenom på
onsdagens övning. Läsförståelseövningen *Läsförståelse: Dokumentation för
olika behållare* arbetar med samma dokumentation som veckans
behållardelar hänvisar till.
