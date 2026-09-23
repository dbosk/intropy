---
title: 'Föreläsning: Upprepningar, listor och moduler'
regex: '^Föreläsning: Upprepningar, listor och moduler$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Upprepningar, listor och moduler$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har fyra delar: *Upprepningar*, *Behållare: Listor*,
*Behållare: Tupler* och *Moduler och paket*. Bilderna visas under
föreläsningen. Anteckningarna till varje del finns som ett interaktivt
dokument (FeedbackFruits) här i modulen: *Upprepningar
(föreläsningsanteckningar)*, *Behållare: Listor
(föreläsningsanteckningar)*, *Behållare: Tupler
(föreläsningsanteckningar)* och *Moduler och paket
(föreläsningsanteckningar)*; läs dem efter föreläsningen, eller i stället
för den om du inte kan komma, och svara på frågorna i dokumenten. Som
komplement finns kursens videogenomgångar här i modulen, märkta
*(videoföreläsning)*: en till varje del, och två till *Behållare: Listor*.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

### Upprepningar

Den här delen handlar om att låta datorn göra samma sak om och om igen.
Vi utgår från en uppgift som går att lösa genom att skriva ut samma steg
femtio gånger, och ser varför man inte vill göra det för hand. Ur den
kontrasten växer tre sätt att uttrycka en upprepning: `for`, som gör
något för varje element i en samling; `while`, som upprepar tills ett
villkor inte längre gäller; och rekursion, där en funktion anropar sig
själv på ett mindre problem. Vi tittar noga på vad som egentligen
upprepas i en slinga, hur indraget avgör vilka rader som hör till den,
och hur en sträng kan gås igenom tecken för tecken precis som vilken
annan samling som helst. Delen avslutas med att välja mellan de tre
formerna på ett och samma problem, och med en återanvändbar funktion för
inmatning som frågar om igen tills användaren har svarat begripligt.

### Behållare: Listor

Hittills har varje variabel burit ett enda värde. Den här delen inför
listan: en behållare som håller många värden samtidigt, i en bestämd
ordning, under ett enda namn. Vi skapar listor, plockar ut enskilda
element med index och delar av listan med skivning, och låter listan
växa och krympa med `append`, `extend`, `insert`, `remove` och `pop`. Att
en lista kan ändras är dess styrka och dess fälla: två namn kan syfta på
samma lista, och då syns varje ändring i båda. Vi går igenom listor med
`for`, precis som i delen *Upprepningar*, och bygger nya listor ur gamla.
Till sist söker vi i listor med `in` och en egen sökfunktion, och
sorterar med `sorted` och `sort`.

### Behållare: Tupler

Listan är en behållare som kan ändras. Den här delen inför dess
oföränderliga syskon, tupeln: en följd av värden som hör ihop och som
inte ska kunna ändras efteråt, till exempel en koordinat eller ett
fullständigt namn. Vi ser vad som skiljer en tupel från en lista genom
att göra samma sak med båda, och använder uppackning för att plocka isär
en tupel i flera variabler. Det gör det möjligt för en funktion att
lämna tillbaka flera värden på en gång, och det är den formen
`enumerate` har när vi vill ha både numret och elementet ur en
behållare.

### Moduler och paket

Funktioner lät oss skriva en sak en gång och använda den många gånger,
men bara inom ett och samma program. Så snart två program behöver samma
funktion står vi där med en kopia i varje fil, och kopior glider isär.
Den här delen handlar om nästa steg i att dela upp ett program: att
lägga en funktion i en egen fil, en modul, och hämta den därifrån med
`import`. Vi ser vad de olika formerna av `import` gör med namnen i
vårt program, vad som händer när en modul importeras (den körs), och hur
en modul skrivs så att den både går att importera och att köra för sig.
Sedan vänder vi blicken utåt: Python levereras med ett standardbibliotek
av färdiga moduler, och på PyPI delar andra programmerare med sig av
sina. Att hitta rätt modul och läsa dess dokumentation är en färdighet i
sig, liksom att veta när ett paket inte behöver installeras.

## Lärandemål

Efter föreläsningen ska du kunna

**Upprepningar:**

- använda `for` för att göra samma sak en gång för varje element i en
  samling, och avgöra vilka rader som upprepas och vilka som inte gör
  det,
- använda `while` för att upprepa så länge ett villkor gäller, och se
  till att villkoret kan bli falskt,
- läsa och skriva rekursiva funktioner med basfall och rekursivt anrop
  på ett mindre problem,
- välja mellan `for`, `while` och rekursion utifrån hur problemet ser
  ut, och motivera valet,
- se en sträng som en följd av tecken som går att gå igenom på samma
  sätt som vilken annan samling som helst,
- skriva en återanvändbar funktion för inmatning som frågar om igen
  tills användaren har matat in data som går att använda.

**Behållare: Listor:**

- skapa en lista, plocka ut ett enskilt element med index och en del av
  listan med skivning, samt ta reda på hur många element listan har med
  `len`,
- ändra en lista på plats: byta ut ett element och lägga till eller ta
  bort element med `append`, `extend`, `insert`, `remove` och `pop`,
- avgöra om två namn syftar på samma lista eller på två olika listor,
  och göra en kopia när en ändring inte ska synas på båda ställena,
- gå igenom en lista, element för element eller med index, bygga en ny
  lista ur en gammal, och undvika att ändra en lista medan den gås
  igenom,
- söka i en lista med `in` och med en egen sökfunktion, samt sortera
  med `sorted` och `sort` och styra ordningen med `key` och `reverse`,
- hitta och läsa dokumentationen för listor och därifrån använda en
  metod som inte gåtts igenom på föreläsningen.

**Behållare: Tupler:**

- skapa en tupel, plocka ut ett element ur den med index och gå igenom
  den med `for`,
- förklara vad som skiljer en tupel från en lista, och välja tupel när
  värdena hör ihop och inte ska ändras var för sig,
- packa upp en tupel i flera variabler, och använda det för att låta en
  funktion lämna tillbaka flera värden,
- gå igenom en behållare och få både elementets nummer och elementet,
  med `enumerate`, och förklara vad `enumerate` lämnar tillbaka,
- hitta och läsa dokumentationen för tupler och för `enumerate`, och
  därifrån svara på en fråga som inte besvarats på föreläsningen.

**Moduler och paket:**

- dela upp ett program i egna moduler, så att kod som flera program
  behöver bara står på ett ställe,
- läsa och skriva de olika formerna av `import`, och redogöra för
  vilket namn som blir tillgängligt i programmet och var Python letar
  efter modulen,
- redogöra för vad som händer när en modul importeras respektive körs
  som program, och skriva en modul som går att göra bådadera med,
- hitta en lämplig modul i standardbiblioteket och använda den genom
  att läsa dess dokumentation,
- installera ett paket från PyPI med `pip` och använda det, och avgöra
  när det är motiverat att installera något alls.

## Förkunskaper

Föreläsningen bygger på tidigare veckors föreläsningar *Variabler och
utskrifter*, *Funktioner*, *Inmatning och felhantering* och *Villkor och
styrstrukturer*: du ska kunna skriva en funktion med parametrar och
returvärde, läsa in text med `input` och omvandla den, fånga ett särfall
med `try`/`except`, och använda `if`, `elif`, `else` och villkor. Inom
föreläsningen bygger *Behållare: Tupler* på sin föregående del,
*Behållare: Listor* (index, `len` och `for` över en lista), och *Moduler
och paket* bygger på *Upprepningar*: exemplen fortsätter på funktionen
som frågar om igen tills användaren matat in ett heltal.

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning upprepningar, listor och
moduler*<!-- Canvas-namnet har två mellanslag: "Övning  upprepningar,
listor och moduler". --> för din grupp, och arbeta i par med *Laboration
(3) upprepningar, listor och moduler*. Boka tid för redovisning av
laboration 3 nästa vecka enligt veckoöversikten. Vill du fördjupa dig,
gör *Fördjupande övning upprepningar, listor och moduler*.
