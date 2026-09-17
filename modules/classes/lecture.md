---
title: 'Föreläsning: Klasser och objekt'
regex: '^Föreläsning: Klasser och objekt$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Klasser och objekt$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har en del: *Klasser och objekt*. Bilderna visas under
föreläsningen. Anteckningarna finns som ett interaktivt dokument
(FeedbackFruits) här i modulen, *Klasser och objekt
(föreläsningsanteckningar)*: läs dem efter föreläsningen, eller i
stället för den om du inte kan komma, och svara på frågorna i
dokumentet. Som komplement finns kursens videogenomgång *Klasser*.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

### Klasser och objekt

Den här föreläsningen introducerar objektorienterad programmering i
Python genom klasser: egna sammansatta datatyper som samlar data och de
funktioner som hör till datan på ett ställe. Vi börjar med att lösa
samma problem, en telefonbok, på två sätt: först med det vi redan kan
(uppslagslistor) och sedan med en klass, för att se konkret vad klassen
tillför. Därefter går vi igenom grundbegreppen klass, objekt, attribut
och metod, parametern `self` och dundermetoder som `__init__`,
`__str__` och `__lt__`, med vilka våra egna objekt kan skrivas ut,
jämföras och sorteras som Pythons inbyggda. Föreläsningen avslutar med
arv: hur en ny klass byggs på en befintlig utan att koden upprepas.

## Lärandemål

Efter föreläsningen ska du kunna

- förklara skillnaden mellan en klass och ett objekt,
- skapa klasser med attribut och metoder,
- förklara vad parametern `self` är, och använda den i metoder,
- implementera dundermetoder så att egna objekt kan skrivas ut och
  jämföras med varandra: `__init__`, `__str__` och `__lt__`,
- använda inkapsling för att skydda ett objekts data,
- välja mellan att representera data med en klass eller med en
  uppslagslista, och motivera valet.

Vill du fördjupa dig har du dessutom möjlighet att lära dig skapa
underklasser med arv, överlagra metoder i underklasser och anropa
föräldraklassens metoder med `super()`, samt avgöra när arv respektive
komposition passar bäst.

## Förkunskaper

Föreläsningen bygger på föreläsningarna *Funktioner*, *Villkor och
styrstrukturer*, *Upprepningar* och *Behållare: Listor*: du ska kunna
skriva en funktion med parametrar och returvärde, använda villkor och
upprepningar och lagra data i listor. Det inledande exemplet använder
också en uppslagslista (`dict`), som föreläsningen *Behållare:
Uppslagslistor* går igenom först senare; det som behövs förklaras där
den används. Strängar och f-strängar används genomgående, och särfall
(`try` och `except`) förekommer i det inledande exemplet; de behandlas i
föreläsningen *Inmatning och felhantering*.
<!-- REVIEW: classes/slides/abstract.tex listar Behållare: Uppslagslistor
     som förkunskap fast den ges vecka 44; decket bör säga vad det
     förutsätter om dict eller stryka förkunskapen. -->

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning klasser och
objekt*<!-- Canvas-namnet har två mellanslag: "Övning  klasser och
objekt". --> för din grupp, och arbeta i par med *Laboration (4) klasser
och objekt (kamratgranskning)*. Redovisa laboration 3 på ditt
redovisningspass enligt veckoöversikten. Vill du fördjupa dig, gör
*Fördjupande övning klasser och objekt*<!-- Canvas-namnet har två
mellanslag: "Fördjupande övning  klasser och objekt". -->.
