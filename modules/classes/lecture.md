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
modulen. Den har två delar: *Behållare: Uppslagslistor* och *Klasser och
objekt*. Bilderna visas under föreläsningen. Anteckningarna till varje
del finns som ett interaktivt dokument (FeedbackFruits) här i modulen:
*Behållare: Uppslagslistor (föreläsningsanteckningar)* och *Klasser och
objekt (föreläsningsanteckningar)*; läs dem efter föreläsningen, eller i
stället för den om du inte kan komma, och svara på frågorna i
dokumenten. Som komplement finns kursens videogenomgång *Klasser och
objekt (videoföreläsning)*.

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

### Klasser och objekt

Den här delen introducerar objektorienterad programmering i
Python genom klasser: egna sammansatta datatyper som samlar data och de
funktioner som hör till datan på ett ställe. Vi börjar med att lösa
samma problem, en telefonbok, på två sätt: först med det vi redan kan
(uppslagslistor, från föreläsningens första del) och sedan med en klass,
för att se konkret vad klassen tillför. Därefter går vi igenom grundbegreppen klass, objekt, attribut
och metod, parametern `self` och dundermetoder som `__init__`,
`__str__` och `__lt__`, med vilka våra egna objekt kan skrivas ut,
jämföras och sorteras som Pythons inbyggda. Delen avslutas med
arv: hur en ny klass byggs på en befintlig utan att koden upprepas.

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

**Klasser och objekt:**

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

Föreläsningen bygger på tidigare veckors föreläsningar *Funktioner*,
*Inmatning och felhantering*, *Villkor och styrstrukturer*,
*Upprepningar*, *Behållare: Listor*, *Behållare: Tupler* och *Moduler
och paket*: du ska kunna skriva en funktion med parametrar och
returvärde, fånga särfall med `try` och `except`, använda villkor och
upprepningar, lagra data i listor och tupler och importera en egen
modul. Strängar och f-strängar används genomgående. Delen *Klasser och
objekt* bygger också på föreläsningens första del, *Behållare:
Uppslagslistor*: den börjar med en telefonbok i en uppslagslista.

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning klasser och
objekt*<!-- Canvas-namnet har två mellanslag: "Övning  klasser och
objekt". --> för din grupp, och arbeta i par med *Laboration (4) klasser
och objekt (kamratgranskning)*. Redovisa laboration 3 på ditt
redovisningspass enligt veckoöversikten. Vill du fördjupa dig, gör
*Fördjupande övning klasser och objekt*<!-- Canvas-namnet har två
mellanslag: "Fördjupande övning  klasser och objekt". -->.
