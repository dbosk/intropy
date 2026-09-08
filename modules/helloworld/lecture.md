---
title: 'Föreläsning: Hello, World!'
regex: '^Föreläsning: Hello, World!$'
published: true
front_page: false
editing_roles: teachers
modules:
  - module: '^Terminalen, programmeringens grunder och "Hello World!"$'
    position: 4
---
Föreläsningen ges live; tid och plats står i veckoöversikten överst i
modulen. Den har två delar med var sin sida här i modulen: den här sidan
gäller den andra delen, *Hello, World!*; den första delen är *Algoritmiskt
tänkande*. Bilderna visas under föreläsningen. Anteckningarna till den här
delen finns som ett interaktivt dokument (FeedbackFruits) här i modulen:
läs dem efter föreläsningen, eller i stället för den om du inte kan komma,
och svara på frågorna i dokumentet.

## Översikt

Den här delen av föreläsningen fortsätter där *Algoritmiskt tänkande*
slutade. Där förfinade vi en vardagsalgoritm ända ner till ett
pythonprogram, men vi körde det aldrig. Här tar vi steget: vad *är* ett
program, vad *är* ett programmeringsspråk, och vad händer i datorn när du
skriver `python3 hello.py` i terminalen? Vi går från processorn, som bara
kan exekvera maskinkod, till samma lilla hälsning skriven i flera språk,
från assembler till Lean 4, och urskiljer ur kontrasten vad ett
programmeringsspråk är och varför något alltid måste översätta mellan din
text och processorn. Sedan kör vi Python på två sätt, interaktivt och som
en sparad fil, för att skilja *filen* från det *körande programmet* och
redigeraren från språket. Föreläsningen slutar vid det första
felmeddelandet.

## Lärandemål

Efter föreläsningen ska du kunna

- förklara vad ett program och ett programmeringsspråk är, och varför
  något alltid måste översätta mellan det du skriver och processorn,
- förklara vad som händer när Python kör en fil,
- skilja på textredigeraren, filen på disken och det körande programmet,
  och köra samma pythonprogram på båda sätten: interaktivt och som en
  sparad fil startad från terminalen,
- skriva, spara och köra ett litet pythonprogram som skriver ut text, och
  byta ut det utskrivna mot en variabel och mot en funktion,
- läsa Pythons felmeddelande: hitta filen och raden det pekar på, avgöra
  vad som hann köras innan felet, och rätta felet.

## Förkunskaper

Föreläsningen förutsätter inga tidigare programmeringskunskaper. Den
bygger på *Algoritmiskt tänkande*: programmet `pannkakor.py` därifrån är
det program vi kör här, och notationen med namngivna steg införs där.
Terminalen och filsystemet lär du dig i modulen *The terminal* (från
*Briefly on interfaces* till *Choosing an editor*); länken *Gör
terminaldelen i DD1301* här i modulen leder dit.

## Efter föreläsningen

Gör *Laboration (0) kom igång med Hello World* på egen hand; föreläsningen
är dess underlag, och på labbpasset direkt efter får du hjälp att få igång
din arbetsmiljö. Fortsätt sedan enligt veckoöversikten med *Övning:
Terminalen och köra kod*, som den här veckan också fortsätter där
föreläsningen slutade om allt inte hann med.
