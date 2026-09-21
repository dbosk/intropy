---
title: 'Föreläsning: Funktioner'
regex: '^Föreläsning: Funktioner$'
published: true
front_page: false
editing_roles: teachers
modules:
  - module: '^Funktioner och variabler$'
    position: 7
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har två delar med var sin sida här i modulen: den här sidan
gäller den andra delen, *Funktioner*; den första delen är *Variabler och
utskrifter*. Bilderna visas under föreläsningen. Anteckningarna till den
här delen finns som ett interaktivt dokument (FeedbackFruits) här i
modulen, *Funktioner (föreläsningsanteckningar)*: läs dem efter
föreläsningen, eller i stället för den om du inte kan komma, och svara på
frågorna i dokumentet. Som komplement finns kursens videogenomgång
*Funktioner (videoföreläsning)*.

## Inspelning

Föreläsningen spelas in. Inspelningen av den andra delen läggs upp här när den
är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

Ett program som växer blir förr eller senare oöverskådligt, och det som
gör det oöverskådligt är nästan alltid att samma sak står på flera
ställen. Den här delen av föreläsningen inför verktyget mot det:
*funktionen*. Vi börjar i ett program som upprepar sig, skriver om det som
en namngiven delalgoritm, precis det vi kallade en funktion i
föreläsningen *Algoritmiskt tänkande*, och tar reda på vad som egentligen
händer när en funktion *anropas*: exekveringen fortsätter i funktionens
kropp, parametrarna får argumentens värden, och en `return`-sats lämnar
tillbaka ett värde och avslutar funktionen där och då. På vägen skiljer vi
funktionens egna namn från huvudprogrammets, ser vad argumentens *ordning*
betyder och när ett *standardvärde* är på sin plats. Delen avslutas med
att dela upp det upprepande programmet i funktioner, och med att sätta
namn på de tre principer uppdelningen följer: DRY, SRP och KISS.

## Lärandemål

Efter föreläsningen ska du kunna

- förklara vad man vinner på att dela upp ett program i funktioner, och
  känna igen den kodupprepning som motiverar en funktion,
- skriva egna funktioner med `def`, med parametrar och returvärde, och
  anropa dem,
- följa exekveringen genom ett funktionsanrop, och redogöra för vad
  anropet gör med argumenten och för vad funktionen lämnar tillbaka,
- skilja på parametrar, argument och returvärden, och på funktionens
  lokala namn och huvudprogrammets, samt avgöra vad argumentens ordning
  och ett standardvärde betyder för ett anrop,
- dela upp ett program i funktioner så att kod inte upprepas, och namnge
  de principer uppdelningen följer: DRY, SRP och KISS,
- dokumentera en funktion med en docstring enligt PEP 257, så att den som
  ska *använda* funktionen slipper läsa dess kropp.

## Förkunskaper

Föreläsningen bygger på sin första del, *Variabler och utskrifter*: du ska
kunna följa ett pythonprogram uppifrån och ned, sats för sats, veta vad en
tilldelning gör och kunna skriva ut värden med `print` och f-strängar.
Från förra veckans föreläsning *Algoritmiskt tänkande* förutsätts
begreppet delalgoritm, en namngiven grupp steg som en algoritm hänvisar
till, och principen DRY.

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning funktioner och variabler*
för din grupp, se *Genomgång inför laboration 1* och arbeta i par med
*Laboration (1) funktioner, variabler och utskrifter (kamratgranskning)*,
som du sedan granskar två andra studenters lösningar av. Konventionen för
docstrings hittar du i *PEP 257 – Docstring Conventions* och
namngivnings- och formateringsreglerna i *pep8.org — The Prettiest Way to
View the PEP 8 Python Style Guide*, båda här i modulen.
