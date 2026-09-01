---
title: 'Veckoöversikt: Terminalen och "Hello World!"'
regex: '^Veckoöversikt: Terminalen och "Hello World!"$'
published: true
front_page: false
editing_roles: teachers
weeks: 2026w37
modules:
  - module: '^Terminalen och "Hello World!"$'
    position: 1
---
Den här veckan (vecka 37) börjar kursens *Pythondel*. Innan vi kan
programmera behöver vi en fungerande arbetsmiljö: en terminal att köra
program i, ett filsystem att hitta i och en textredigerare att skriva kod
i. Veckan slutar med att du skriver och kör ditt första pythonprogram,
*Hello World!*, och får en första inblick i versionshantering med Git.
Det är ovant för många och tar tid, men allt som kommer sedan bygger på
det.

Den här sidan innehåller också en översikt över hela Pythondelen och dess
lärandemål, så att du vet vart vi är på väg. Varje vecka har sedan en
egen sida som den här överst i sin modul.

## Pythondelen i översikt

Pythondelen består av tre kursmoment. **LAB1** (1,5 hp) är sex
laborationer som ni gör i par under vecka 38–45. **LAB2** (1,5 hp) är ett
individuellt datorprov som kontrollerar att du själv kan det ni lärt er i
LAB1. **LAB3** (3,0 hp) är projektet, P-uppgiften, en större individuell
programmeringsuppgift som avgör ditt betyg på kursen. Se sidan
*Deadlines, examination av olika moment, betyg och fusk* för detaljerna.

| Vecka | Modul i Canvas | Moment |
|-------|----------------|--------|
| 37 | Terminalen och "Hello World!" | Laboration 0 |
| 38 | Funktioner och variabler | Laboration 1 |
| 39 | Inmatning, felhantering och styrstrukturer | Laboration 2 |
| 40 | Upprepningar, listor och moduler | Laboration 3 |
| 41 | Klasser och objekt | Laboration 4; redovisning av laboration 3 |
| 42–43 | *Tentaperiod, ingen undervisning* | |
| 44 | Fler behållare och mer om klasser | Laboration 5 |
| 45 | Filhantering | Laboration 6 |
| 46 | Grafiskt gränssnitt (frivillig) | Repetition |
| 47–48 | Summativ bedömning (datorprov) | Redovisning av laboration 6; datorprov 26/11 |
| 48–51 | Projektet | Specifikation, granskning, redovisning |
| 1–2 (2027) | Projektet, datorprov | Redovisningar; omprov 11/1 |

Varje undervisningsvecka har samma rytm, i den här ordningen:

1. **Föreläsningen** ges live så att du kan ställa frågor. Föredrar du att
   se den i efterhand eller läsa i stället finns inspelningen och
   föreläsningsanteckningarna på föreläsningens sida i modulen.
2. **Övningen** i din grupp går igenom veckans innehåll genom egen
   problemlösning tillsammans med andra; vi hinner ett urval av problemen
   och resten finns med lösningar på övningens sida.
3. **Laborationen** gör ni i par. På labbpassen finns lärare och
   assistenter för att hjälpa er när ni fastnar.

Alla tillfällen utom föreläsningarna är delade mellan grupp A–F och
grupp G–L; du går bara på passen för din grupp.

## Lärandemål för hela Pythondelen

Kursens mål är att du ska kunna använda programmering för att lösa
problem, tillämpa problemlösningsmetodiken även utanför programmeringen
och bedöma befintliga program. Konkret innebär det att du efter
Pythondelen ska kunna

- dela upp ett problem i lämpliga delproblem och sätta ihop lösningarna
  till en lösning på det ursprungliga problemet (*algoritmiskt
  tänkande*),
- skriva funktioner som löser delproblemen och sätta ihop dem till ett
  program, med variabler, styrstrukturer, upprepningar, behållare,
  klasser och filer (*programmeringsspråket*),
- utforma användbara textbaserade gränssnitt med begriplig inmatning och
  utmatning (*användbarhet*),
- skriva källkod som är läsbar för människor: bra namn, uppdelning i
  funktioner och PEP 8 (*läsbarhet*),
- granska källkod som andra har skrivit (*granskning*).

Vecka för vecka är målen följande.

**Vecka 37, Terminalen och "Hello World!":**

- styra datorn från terminalen och hitta i filsystemet,
- installera Python och en textredigerare eller IDE och skriva program i
  den,
- skriva, spara och köra ett enkelt pythonprogram från terminalen,
- förklara vad ett program och ett programmeringsspråk är,
- versionshantera källkod med Git (fördjupning).

**Vecka 38, Funktioner och variabler:**

- förklara hur ett pythonprogram körs uppifrån och ned och följa
  exekveringen rad för rad, till exempel med PythonTutor,
- skriva program som lagrar värden i variabler med beskrivande namn och
  skriver ut dem läsbart med `print` och f-strängar,
- skilja på datatyperna `int`, `float` och `str` och veta vilka
  operationer som passar för vilken typ,
- dela upp ett problem i delproblem och skriva en funktion för varje del,
  med parametrar och returvärden, så att kod inte upprepas,
- skriva kod som följer PEP 8 och förklarar sig själv med kommentarer och
  docstrings enligt PEP 257.

**Vecka 39, Inmatning, felhantering och styrstrukturer:**

- läsa in text från användaren med `input` och omvandla den till rätt
  datatyp, till exempel `int` eller `float`,
- förklara vad ett särfall (*exception*) är och fånga det med
  `try`/`except` så att programmet ger ett begripligt meddelande i
  stället för att krascha,
- skriva villkor med jämförelser och de booleska operatorerna `and`, `or`
  och `not`, och styra programmets flöde med `if`/`elif`/`else`,
- upprepa en del av programmet tills ett villkor är uppfyllt med `while`,
- utforma inmatning och utskrifter så att programmet blir begripligt och
  användarvänligt, även när något går fel.

**Vecka 40, Upprepningar, listor och moduler:**

- välja och använda rätt form av upprepning för uppgiften: `for` över en
  samling, `while` tills ett villkor är uppfyllt, eller rekursion,
- skapa listor och tupler, lägga till, ta bort, söka och sortera element
  och gå igenom dem med `for`,
- se en sträng som en följd av tecken som går att gå igenom på samma
  sätt som en lista,
- dela upp ett program i egna moduler som du importerar, och använda
  moduler från standardbiblioteket och PyPI genom att läsa deras
  dokumentation,
- skriva återanvändbara funktioner för inmatning som frågar igen tills
  användaren har matat in korrekt data.

**Vecka 41, Klasser och objekt:**

- förklara skillnaden mellan en klass och ett objekt,
- skapa klasser med attribut och metoder och förstå vad parametern `self`
  är,
- implementera dundermetoder som `__init__`, `__str__`, `__eq__` och
  `__lt__`,
- använda inkapsling för att skydda ett objekts data,
- välja mellan att representera data med en klass eller med en
  uppslagslista och motivera valet.

**Vecka 44, Fler behållare och mer om klasser:**

- välja lämplig behållare (lista, tuppel, mängd, uppslagslista, stack
  eller kö) för ett givet problem och motivera valet utifrån vilka
  operationer som behövs,
- använda uppslagslistor och mängder för att lagra och slå upp data, och
  iterera över dem,
- implementera operatoröverlagring med dundermetoder som `__add__`,
  `__eq__` och `__lt__` samt typkonvertering med `__str__`, `__float__`
  och `__int__`,
- konstruera program där en klass har en behållare av andra objekt som
  attribut och där metoderna söker i och uppdaterar behållaren,
- hitta och läsa dokumentationen för Pythons behållare och använda den för
  att lösa problem du inte sett förut.

**Vecka 45, Filhantering:**

- förklara vad en fil är och skillnaden mellan text- och binärfiler,
- öppna och stänga filer på rätt sätt med `open` och `with`, och förklara
  varför filen måste stängas,
- läsa data från en fil rad för rad, tolka raderna (till exempel dela upp
  dem i fält) och lagra dem i lämpliga behållare,
- skriva data från programmet till en fil i ett format som programmet
  senare kan läsa tillbaka,
- hantera fel vid filhantering, som att filen inte finns, så att
  användaren får en begriplig fråga i stället för en krasch,
- läsa och skriva vanliga filformat som CSV och JSON med hjälp av Pythons
  standardbibliotek och dess dokumentation.

**Vecka 46, Grafiskt gränssnitt (frivillig):**

- förklara hur ett grafiskt program drivs av en händelseslinga och vad en
  callbackfunktion är,
- konstruera ett enkelt grafiskt gränssnitt med `tkinter` med fönster,
  etiketter, textfält och knappar,
- koppla händelser från användaren (knapptryck, tangenter) och från
  klockan till funktioner och metoder som uppdaterar gränssnittet,
- strukturera ett grafiskt program med klasser, till exempel genom att
  ärva från `tkinter`-klasser, så att gränssnitt och programlogik hålls
  isär,
- hitta och använda dokumentationen för ett programbibliotek för att lösa
  ett problem du inte sett förut.

**Vecka 47–48, datorprovet** testar målen för vecka 38–45 individuellt.

**Vecka 48 och framåt, projektet:**

- specificera ett program (algoritm, datastrukturer, klasser och
  funktioner) innan du skriver det,
- dela upp ett större problem i funktioner och klasser utan kodupprepning,
- skriva läsbar och dokumenterad kod som följer PEP 8 och PEP 257,
- granska en annan students program med hjälp av granskningsprotokollet
  och ta till dig återkoppling på ditt eget,
- presentera och motivera din egen kod för en handledare.

## Efter veckan ska du kunna

- styra datorn från terminalen och hitta i filsystemet: flytta dig mellan
  kataloger, lista och skapa filer och köra program,
- installera Python och en textredigerare eller IDE och skriva program i
  den,
- skriva, spara och köra ett enkelt pythonprogram från terminalen,
- förklara vad ett program och ett programmeringsspråk är och vad som
  händer när Python kör din fil,
- ha en första förståelse för varför källkod versionshanteras med Git
  (fördjupning).

## Gör så här, i ordning

1. **Gå på föreläsningen** (onsdag): introduktion till terminalen,
   filsystemet och textredigerare. Den ges live så att du kan ställa frågor;
   kan du inte komma finns inspelningen och anteckningarna på föreläsningens
   sida här i modulen.
2. **Gå på labbpasset för din grupp** direkt efter föreläsningen (onsdag
   eller torsdag): det är en hjälpsession för att få igång din arbetsmiljö.
   Arbeta med *Laboration (0) kom igång med Hello World* och markera den som
   klar när ditt program kör. Materialet från terminalkursen DD1301 överst i
   modulen (från *Briefly on interfaces* till *Choosing an editor*) förklarar
   hur du hittar och använder terminalen på just din dator (Ubuntu, macOS
   eller Windows); *Guide to accessing the terminal* och *The terminal*
   sammanfattar. Ett extra labbpass för dem som inte hunnit klart ges
   måndagen vecka 38.
3. **Gå på övningen för din grupp:** *Övning: Terminalen och köra kod*, där
   vi övar på att köra kod från terminalen och introducerar versionshantering
   med Git.
4. **Vill du fördjupa dig?** Gör *Fördjupande övning: Terminalen, IDE:er och
   versionshantering*.

## Schema

<!-- schema:start -->
- **Ons 9/9**
  - 13:00–15:00 Föreläsning (helklass) — D2, Zoom — Intro terminal, filsystem och textredigerare
  - 15:00–17:00 Labb (grupp A–F) — 4V4Gul (Gul), 4V6 Bru (Brun) — Intro labbmiljö, hjälpsession.
- **Tor 10/9**
  - 08:00–10:00 Övning (grupp A–F) — D37, Zoom, E32 — Lärarledd undervisning, genomgång och problemlösning. Git.
  - 16:00–18:00 Labb (grupp G–L) — 4V4Gul (Gul), 4V6 Bru (Brun) — Intro labbmiljö, hjälpsession.
- **Fre 11/9**
  - 15:00–17:00 Övning (grupp G–L) — D37, Zoom, E32 — Lärarledd undervisning, genomgång och problemlösning. Git.
<!-- schema:end -->

Du går bara på övnings- och labbpassen för din grupp (A–F eller G–L);
föreläsningen är gemensam för hela klassen. Tiderna anges som i TimeEdit,
utan akademisk kvart: föreläsningar och övningar börjar kvart över.

## Deadlines och hjälp

Laboration 0 markerar du själv som klar i Canvas; den redovisas inte.
Datum för övriga inlämningar står på respektive uppgift; se sidan
*Deadlines, examination av olika moment, betyg och fusk* för hur momenten
examineras. Fastnar du mellan passen, se sidan *Få hjälp*.

## Nästa vecka

Vecka 38 börjar programmerandet på allvar med modulen *Funktioner och
variabler*. Se till att din arbetsmiljö fungerar innan dess.
