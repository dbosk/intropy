---
title: "Veckoöversikt: Fler behållare och mer om klasser"
regex: '^Veckoöversikt: Fler behållare och mer om klasser$'
published: true
front_page: false
editing_roles: teachers
weeks: 2026w44
modules:
  - module: '^Fler behållare och mer om klasser$'
    position: 1
---
Välkommen tillbaka efter tentaperioden! Efter två veckor utan Python
börjar vi med att repetera kursens grunder, och bygger sedan vidare på
uppslagslistorna och klasserna åt två håll. Dels *fler behållare*: att
välja behållare efter vilka operationer programmet behöver, och ett helt
program, ett gissningsspel, som sätter ihop det vi har lärt oss. Dels *mer
om klasser*: hur egna klasser kan bete sig som Pythons inbyggda typer
genom operatoröverlagring (`+`, `==`, `<` och så vidare), så att till
exempel ett bråk kan adderas med `a + b`, och hur en klass kan ha en
behållare av andra objekt som attribut, vilket är hur de flesta riktiga
program är uppbyggda. Mängder, stackar och köer finns som fördjupning för
den som vill.

Innan du börjar bör du kunna skriva en egen klass med `__init__` och
`__str__`, arbeta med listor, uppslagslistor och for-slingor samt läsa in
och kontrollera inmatning från användaren.

## Efter veckan ska du kunna

- välja lämplig behållare (lista, tupel eller uppslagslista) för ett
  givet problem och motivera valet utifrån vilka operationer som behövs,
- implementera operatoröverlagring med dundermetoder som `__add__`,
  `__eq__` och `__lt__` samt typkonvertering med `__str__`, `__float__`
  och `__int__`,
- konstruera program där en klass har en behållare av andra objekt som
  attribut och där metoderna söker i och uppdaterar behållaren,
- hitta och läsa dokumentationen för Pythons behållare och använda den för
  att lösa problem du inte sett förut.

### Fördjupning (valfritt)

- använda mängder för att samla unika värden, pröva om ett värde finns
  bland dem och iterera över dem,
- använda en lista som stack och `collections.deque` som kö, och välja
  mängd, stack eller kö när programmet behöver just deras operationer.

## Gör så här, i ordning

1. **Gå på föreläsningen (måndag).** Den här gången är föreläsningen en
   repetition av hela kursen: det vi har mött hittills och en förhandstitt
   på det som kommer. Den har en egen sida här i modulen, *Föreläsning:
   Fler behållare och mer om klasser*. Kan du inte komma finns
   inspelningen där.
2. **Gå gärna på övningarna (tisdag och onsdag).** Veckans nya innehåll
   går vi igenom på övningarna; se sidan *Övning: Fler behållare och mer om
   klasser* här i modulen. På tisdagen tar vi allt du behöver till
   laborationen: uppgiften *Banken*, en klass som har en behållare av andra
   objekt, där valet mellan lista och uppslagslista är själva frågan. På
   onsdagen tar vi operatoröverlagring och arv. Onsdagens övning bygger
   inte på tisdagens. Övningarna är frivilliga och ges för hela klassen, i
   D37 och på [Zoom][zoom-room]. Samtidigt med onsdagens övning leder en
   assistent, oftast Emelie, en repetition i ett eget grupprum på Zoom; den
   går så långt tillbaka i kursen som behövs, anpassad efter dem som
   kommer. Uppgifterna och lösningarna till alla övningens uppgifter finns
   i det interaktiva dokumentet (FeedbackFruits), så att du kan fortsätta
   på egen hand. Att hitta och läsa dokumentationen för Pythons behållare
   är en stor del av veckans mål, så ha den uppe under övningen.
3. **Läs anteckningarna** till veckans fyra delar, se *Att läsa* nedan.
   Det som är märkt **före labben** behöver du till laborationen; resten
   läser du när du hinner. Anteckningarna är också alternativet för den som
   inte kan komma på övningarna: allt vi går igenom där står i dem.
4. **Arbeta med** *Laboration (5) behållare och klasser (kamratgranskning)* i
   par. På labbpassen finns lärare och assistenter för att hjälpa er när ni
   fastnar; det mesta av arbetet gör ni på egen tid.
5. **Vill du fördjupa dig?** Gör övningens fördjupningsuppgifter, Uppgift
   6 och 7, och läs den valfria delen *Behållare: Mängder, stackar och
   köer*.

[zoom-room]: https://kth-se.zoom.us/j/61952197407

## Att läsa

Anteckningarna till var och en av de fyra delarna finns som ett
interaktivt dokument (FeedbackFruits) här i modulen, till exempel
*Operatoröverlagring (föreläsningsanteckningar)*. Två av delarna finns
också som videoföreläsning, *Behållare: Ett gissningsspel
(videoföreläsning)* och *Operatoröverlagring (videoföreläsning)*. Sidan
*Övning: Fler behållare och mer om klasser* beskriver varje del och vad
du ska kunna efteråt.

- *Behållare: Mängder, stackar och köer*: valfritt, hela. Till den hör
  övningens Uppgift 1 (e-postadresser) och Uppgift 5 (att ångra det
  senaste).
- *Behållare: Ett gissningsspel*: hela. **Före labben:** avsnittet *Att
  läsa in en gissning*, en återanvändbar funktion som läser in och
  kontrollerar inmatning.
- *Operatoröverlagring*: avsnitten *Attribut som egenskaper*,
  *Typkonvertering*, *Negation*, *Multiplikation*, *Förkortning* och
  *Sammanfattning*; resten går vi igenom på onsdagens övning.
- *Praktiska tillämpningar av klasser*: **före labben:** avsnittet
  *Inköpslistor med klasser*, en klass som har en behållare av andra
  objekt. I övrigt resten, utom *Arv: medborgare med personnummer* och
  *Komposition eller arv*, som vi går igenom på onsdagens övning.
- Övningens Uppgift 2, 3, 6 och 7, på egen hand.

## Schema

<!-- schema:start -->
- **Mån 26/10**
  - 10:00–12:00 Föreläsning (helklass) — D3, Zoom — Grundläggande lärarledd undervisning, hybrid
- **Tis 27/10**
  - 10:00–12:00 Övning (helklass) — D37, Zoom — Lärarledd undervisning, genomgång och problemlösning
- **Ons 28/10**
  - 15:00–17:00 Övning (helklass) — D37, Zoom — Fördjupning eller repetition.
- **Tor 29/10**
  - 08:00–10:00 Labb (grupp A–F) — 4V5Grö (Grön), 4V6 Bru (Brun), D41 — Hjälpsession
  - 10:00–12:00 Labb (grupp G–L) — 4V5Grö (Grön), 4V6 Bru (Brun), D41 — Hjälpsession
<!-- schema:end -->

Du går bara på labbpassen för din grupp (A–F eller G–L); föreläsningen
och övningarna är gemensamma för hela klassen. Tiderna anges som i TimeEdit,
utan akademisk kvart: föreläsningar och övningar börjar kvart över.

## Deadlines och hjälp

Datum för inlämningar står på respektive uppgift i Canvas; se sidan
*Deadlines, examination av olika moment, betyg och fusk* för hur momenten
examineras. Fastnar du mellan passen, se sidan *Få hjälp*.

## Nästa vecka

Nästa vecka fortsätter vi med modulen *Filhantering*: hur programmet läser
data från och sparar data till filer, så att det inte glömmer allt när det
avslutas.
