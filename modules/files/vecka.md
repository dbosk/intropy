---
title: "Veckoöversikt: Filhantering"
regex: '^Veckoöversikt: Filhantering$'
published: true
front_page: false
editing_roles: teachers
weeks: 2026w45
modules:
  - module: '^Filhantering$'
    position: 1
---
Den här veckan (vecka 45) handlar om *filer*: hur programmet läser data
från en fil i stället för att fråga användaren om allt, och hur det sparar
data så att den finns kvar nästa gång programmet körs. Hittills har allt
programmet vet försvunnit när det avslutas. Med filer kan programmet
hantera stora datamängder och behålla dem mellan körningarna, vilket är
vad nästan alla nyttiga program gör. Vi tittar också på vad ett filformat
är, från egna enkla format till standarder som CSV och JSON.

Innan du börjar bör du vara bekväm med strängar och strängmetoder,
behållare (listor och uppslagslistor), for-slingor samt felhantering med
`try` och `except`; att öppna en fil som inte finns är ett typiskt fel som
programmet måste hantera.

## Efter veckan ska du kunna

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

## Gör så här, i ordning

1. **Förbered dig före föreläsningen.** Gör *Unit 6 Vecka 7 i Torus* (den
   kan möjligen heta vecka 8, men den handlar om filer) och se videorna
   här i modulen.
2. **Gå på föreläsningen.** Den går igenom samma innehåll som videon och
   texten, men live och med utrymme för dina frågor.
3. **Gå på övningen för din grupp:** *Övning filer och filhantering*. Vi
   löser problem tillsammans i mindre grupper och går igenom lösningarna.
   Vi hinner bara ett urval av problemen; resten finns med lösningar på
   övningens sida så att du kan fortsätta på egen hand.
4. **Arbeta med** *Laboration (6) filhantering* i par. På labbpassen finns
   lärare och assistenter för att hjälpa er när ni fastnar; det mesta av
   arbetet gör ni på egen tid. Det här är den sista obligatoriska
   laborationen före datorprovet.
5. **Vill du fördjupa dig?** Gör *Fördjupande övning filer och
   filhantering*.

## Schema

<!-- schema:start -->
- **Tis 3/11**
  - 10:00–12:00 Föreläsning (helklass) — D3, Zoom — Grundläggande lärarledd undervisning, hybrid
  - 15:00–17:00 Övning (grupp A–F) — D37, Zoom, E32 — Lärarledd undervisning, genomgång och problemlösning
- **Ons 4/11**
  - 08:00–10:00 Övning (grupp G–L) — D37, Zoom, E32 — Lärarledd undervisning, genomgång och problemlösning
- **Tor 5/11**
  - 08:00–10:00 Labb (grupp A–F) — 4V4Gul (Gul), 4V6 Bru (Brun), D41 — Hjälpsession
- **Fre 6/11**
  - 13:00–15:00 Labb (grupp G–L) — 4V2Röd (Röd), 4V3Ora (Orange), E53 — Hjälpsession
<!-- schema:end -->

Du går bara på övnings- och labbpassen för din grupp (A–F eller G–L);
föreläsningen är gemensam för hela klassen. Tiderna anges som i TimeEdit,
utan akademisk kvart: föreläsningar och övningar börjar kvart över.

## Deadlines och hjälp

Laboration 6 redovisas vecka 47: tisdag 17/11 för grupp A–F och torsdag
19/11 för grupp G–L, boka tid i kalendern i Canvas. Datum för inlämningar
står på respektive uppgift i Canvas; se sidan *Deadlines, examination av
olika moment, betyg och fusk* för hur momenten examineras. Fastnar du
mellan passen, se sidan *Få hjälp*.

## Nästa vecka

Vecka 46 är modulen *Grafiskt gränssnitt*. Den är frivillig och behövs
bara om du siktar på högsta betyg på projektet; annars kan du använda
veckan till repetition inför datorprovet.
