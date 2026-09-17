---
title: 'Föreläsning: Filhantering'
regex: '^Föreläsning: Filhantering$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Filhantering$'
    position: 2
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har en del: *Arbeta med filer*. Bilderna visas under
föreläsningen. Anteckningarna finns som ett interaktivt dokument
(FeedbackFruits) här i modulen, *Arbeta med filer
(föreläsningsanteckningar)*: läs dem efter föreläsningen, eller i
stället för den om du inte kan komma, och svara på frågorna i
dokumentet.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Inspelning

Föreläsningen spelas in. Inspelningen läggs upp här när den är klar.

<!-- TODO: ersätt med länk till inspelningen (kaltura/Canvas Studio). -->

## Översikt

### Arbeta med filer

Hittills har allt programmet vet försvunnit när det avslutas. Den här
föreläsningen handlar om filer: hur programmet läser data från en fil i
stället för att fråga användaren om allt, och hur det sparar data så att
den finns kvar nästa gång programmet körs. Vi utgår från skillnaden
mellan flyktigt och oflyktigt minne och ser varför filer behövs. Sedan
lär vi oss öppna och stänga filer med `open` och `with`, ta hand om att
filen inte finns så att användaren får en ny fråga i stället för en
krasch, läsa en fil rad för rad och skriva till den, samt skilja
textfiler från binärfiler. Sist tittar vi på filformat: ett eget enkelt
format, vad som går sönder i det, och de vanliga formaten CSV och JSON
med Pythons standardbibliotek. Genomgående kopplas filerna till det vi
redan kan om `print` och `input`: samma mönster, en annan destination.

## Lärandemål

Efter föreläsningen ska du kunna

- förklara vad en fil är, skillnaden mellan primärminne och
  sekundärminne, och varför program behöver filer,
- skilja mellan textfiler och binärfiler, och välja rätt läge när filen
  öppnas,
- öppna och stänga filer på rätt sätt med `open` och `with`, och
  förklara varför filen måste stängas,
- läsa data från en fil rad för rad, tolka raderna och lagra dem i
  lämpliga behållare,
- skriva data från programmet till en fil i ett format som programmet
  senare kan läsa tillbaka,
- hantera fel vid filhantering, som att filen inte finns, så att
  användaren får en begriplig fråga i stället för en krasch,
- läsa och skriva vanliga filformat som CSV och JSON med hjälp av
  Pythons standardbibliotek och dess dokumentation.

## Förkunskaper

Föreläsningen bygger på föreläsningarna *Inmatning och felhantering*,
*Behållare: Listor*, *Behållare: Tupler*, *Behållare: Uppslagslistor*,
*Upprepningar* och *Funktioner*: du ska kunna arbeta med strängar och
strängmetoder, läsa in text med `input` och omvandla den, samla data i
listor, tupler och uppslagslistor, upprepa med `for` och `while`, skriva
egna funktioner, och fånga ett särfall med `try` och `except` — att
öppna en fil som inte finns är ett typiskt fel som programmet måste
hantera.

## Efter föreläsningen

Fortsätt enligt veckoöversikten: gå på *Övning filer och filhantering*
för din grupp, och arbeta i par med *Laboration (6) filhantering* — den
sista obligatoriska laborationen före datorprovet. Vill du fördjupa dig,
gör *Fördjupande övning filer och filhantering*<!-- Canvas-namnet har
två mellanslag: "Fördjupande övning  filer och filhantering". -->.
