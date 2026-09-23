---
title: 'Föreläsning: Inmatning, felhantering och styrstrukturer'
regex: '^Föreläsning: Inmatning, felhantering och styrstrukturer$'
published: true
front_page: false
editing_roles: teachers
modules:
  - module: '^Inmatning, felhantering och styrstrukturer$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har två delar: *Inmatning och felhantering* och *Villkor och
styrstrukturer*. Bilderna visas under föreläsningen. Anteckningarna till
varje del finns som ett interaktivt dokument (FeedbackFruits) här i
modulen: *Inmatning och felhantering (föreläsningsanteckningar)* och
*Villkor och styrstrukturer (föreläsningsanteckningar)*; läs dem efter
föreläsningen, eller i stället för den om du inte kan komma, och svara på
frågorna i dokumenten. Som komplement finns kursens videogenomgångar
*Inmatning och felhantering (videoföreläsning)* och *Villkor och
styrstrukturer (videoföreläsning)*.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<iframe id="kmsembed-0_wkocb39u" class="kmsembed" title="Kaltura Player" src="https://play.kth.se/embed/secure/iframe/entryId/0_wkocb39u/uiConfId/23453971" width="650" height="366" sandbox="allow-forms allow-same-origin allow-scripts allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen" allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0" loading="lazy"></iframe>

## Översikt

### Inmatning och felhantering

Åldersprogrammet i föreläsningen *Variabler och utskrifter* frågade den
som körde det efter namn och födelseår, men vi sa bara ett par meningar
om hur det gick till. Den här delen tar upp de raderna igen. Vi läser in
text med `input` och upptäcker att det som kommer tillbaka alltid är en
sträng, även när användaren skriver siffror, och därför behöver vi
typkonvertering och behöver veta vad varje operation gör med varje
datatyp. Vi utformar frågorna så att den som kör programmet förstår vad
som förväntas. Sedan svarar användaren något vi inte kan räkna med och
programmet går sönder: körningen avbryts och Python skriver en
spårutskrift (traceback), som vi lär oss läsa. Till sist tar vi hand om
felet själva med `try` och `except` — en gren per sorts fel, de
specifika först — och ser hur våra egna funktioner kan skicka särfall
vidare till den som anropat dem.

### Villkor och styrstrukturer

De flesta program vi skrivit hittills går rakt igenom, rad för rad, och
gör samma sak varje gång oavsett vad användaren svarar. Den här delen ger
dem två förmågor: att *välja*, en sak om ett villkor är sant och en annan
annars, med `if`, `elif` och `else` (en `if` skymtade redan i
*Inmatning och felhantering*; här tittar vi ordentligt på den); och att
*upprepa*, göra om något så länge ett villkor gäller, med `while`. Båda
styrs av ett villkor, så vi börjar med villkoren själva: jämförelser, den
booleska typen och operatorerna `and`, `or` och `not`, och två vanliga
misstag — att skriva `=` när man menar `==`, och att bara skriva ena
ledet i en jämförelse med två värden. Sedan bygger vi ett program som
frågar efter längd och vikt och rekommenderar en säng, och till sist
låter vi det fråga om igen när svaret inte går att använda, först med en
egen kontroll av svaret och sedan genom att låta `int` själv upptäcka och
hantera felet.

## Lärandemål

Efter föreläsningen ska du kunna

**Inmatning och felhantering:**

- läsa in text från användaren med `input` och förklara att resultatet
  alltid är en sträng, oavsett vad användaren skrev,
- omvandla en inläst sträng till `int` eller `float` med
  typkonvertering, och avgöra var i programmet omvandlingen hör hemma,
- använda de vanligaste operationerna och metoderna på tal och strängar,
  och förutsäga vilken typ och vilket värde resultatet får,
- utforma frågor, utskrifter och felmeddelanden så att den som kör
  programmet förstår vad som förväntas, vad svaret betydde och vad hon
  kan göra när något gick fel,
- förklara vad ett särfall (exception) är, och redogöra för vad som
  händer när ett särfall inträffar,
- läsa en spårutskrift (traceback) och ur den utläsa var felet uppstod,
  vilken sorts fel det var och vad som var fel,
- fånga särfall med `try` och `except` — de specifika sorterna före den
  allmänna — och redogöra för vad som händer i programmet,
- läsa och skriva `raise` i en egen funktion, och förklara hur ett
  särfall sprider sig uppåt till den som anropat funktionen.

**Villkor och styrstrukturer:**

- skriva villkor med jämförelseoperatorer och de booleska operatorerna
  `and`, `or` och `not`, och förutsäga om ett villkor blir sant eller
  falskt,
- styra programmets flöde med `if`, `elif` och `else`, och redogöra för
  att exakt en gren exekveras och att programmet fortsätter efteråt,
- upprepa en del av programmet tills ett villkor är uppfyllt med
  `while`, och avgöra när uppgiften kräver en upprepning och när ett val
  räcker,
- följa exekveringen genom villkor och slingor för hand, ett steg i
  taget, för att förutsäga vad ett program gör och hitta fel i det,
- utforma en inmatningsdialog som frågar om igen tills svaret går att
  använda, i stället för att upprepa samma fråga i koden.

## Förkunskaper

Föreläsningen bygger på förra veckans föreläsningar *Variabler och
utskrifter* och *Funktioner* i modulen *Funktioner och variabler*: du ska
kunna använda variabler, datatyperna `int`, `float` och `str`, skriva ut
med `print`, och skriva egna funktioner med parametrar och returvärden.
Delen *Villkor och styrstrukturer* bygger också på den här föreläsningens
första del, *Inmatning och felhantering*: att `input` ger en sträng, att
strängen omvandlas med `int` eller `float`, strängmetoden `isdigit`, och
att `try` och `except` tar hand om en omvandling som misslyckas.

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning inmatning, felhantering
och styrstrukturer* för din grupp, och arbeta i par med *Laboration (2)
inmatning, felhantering och styrstrukturer (kamratgranskning)*. Vill du
fördjupa dig, gör *Fördjupande övning inmatning, felhantering och
styrstrukturer*.
