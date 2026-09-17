---
title: 'Föreläsning: Grafiskt gränssnitt'
regex: '^Föreläsning: Grafiskt gränssnitt$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Grafiskt gränssnitt$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har en del: *Grafiska användargränssnitt*. Bilderna visas
under föreläsningen. Anteckningarna finns som ett interaktivt dokument
(FeedbackFruits) här i modulen, *Grafiska användargränssnitt
(föreläsningsanteckningar)*: läs dem efter föreläsningen, eller i
stället för den om du inte kan komma, och svara på frågorna i
dokumentet. Som komplement finns kursens videogenomgång *Grafiska
gränssnitt*.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

### Grafiska användargränssnitt

Föreläsningen handlar om grafiska användargränssnitt: hur ett program
med fönster, knappar och textfält är uppbyggt, och hur vi skriver ett
sådant med biblioteket `tkinter`. Det stora skiftet mot tidigare program
är händelseprogrammering: i stället för att programmet frågar användaren
i tur och ordning väntar det på händelser — klick, tangenttryckningar,
tid som går — och anropar en funktion för varje händelse. Vi börjar med
ett minimalt fönster och bygger ut det stegvis med in- och utmatning,
och ser hur koden blir tydligare när gränssnittet skrivs som en klass
som ärver från `tkinter`s egna klasser. Föreläsningen avslutar med ett
ritprogram som lyssnar på musens rörelser och knapptryckningar, och som
får knappar för att byta färg.

## Lärandemål

Efter föreläsningen ska du kunna

- förklara hur ett grafiskt program drivs av en händelseslinga och vad
  en callbackfunktion är,
- konstruera ett enkelt grafiskt gränssnitt med `tkinter` med fönster,
  etiketter, textfält och knappar,
- koppla händelser från användaren (knapptryck, tangenter) och från
  klockan till funktioner och metoder som uppdaterar gränssnittet,
- strukturera ett grafiskt program med klasser, till exempel genom att
  ärva från `tkinter`-klasser, så att gränssnitt och programlogik hålls
  isär,
- hitta och använda dokumentationen för ett programbibliotek för att
  lösa ett problem du inte sett förut.

## Förkunskaper

Föreläsningen bygger på *Klasser och objekt* och dess fördjupning
*Praktiska tillämpningar av klasser*: du ska kunna skapa klasser, ärva
från en klass och anropa `super()`. Att skicka en funktion som argument
till en annan funktion övades med `key` till `sorted` i *Behållare:
Listor*. Att läsa dokumentationen för ett programbibliotek du inte
använt förut övades i *Behållare: Mängder, stackar och köer*.

## Efter föreläsningen

Modulen är frivillig: den behövs bara om du siktar på högsta betyg på
projektet. Fortsätt enligt veckoöversikten: gå på *Övning grafiskt
gränssnitt eller repetition* och välj spår, grafiska gränssnitt eller
repetition inför datorprovet. Vill du, arbeta med *Laboration
(frivillig) grafiska gränssnitt*, gärna i par.
