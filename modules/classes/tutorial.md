---
title: 'Övning: Klasser och objekt'
regex: '^Övning: Klasser och objekt$'
published: false
front_page: false
editing_roles: teachers
modules:
  - module: '^Klasser och objekt$'
    position: 3
---
Övningen ges live i din grupp; tid och plats står i veckoöversikten
överst i modulen. Vi löser uppgifter tillsammans i mindre grupper.
Uppgifterna och deras lösningsförslag finns i det interaktiva dokumentet
(FeedbackFruits) här i modulen, *Övning: Klasser och objekt
(övningsanteckningar)*: pröva varje uppgift innan du läser lösningen.

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Vad vi går igenom på övningen

Vi hinner bara ett urval av övningens uppgifter under passet. De här tar
vi tillsammans, i den här ordningen:

1. **Uppgift 1: Boken.** Skriva klassen `Book` med privata attribut och
   en dundermetod som ger en läsbar utskrift.
2. **Uppgift 2: Sista sidan.** Lägga till en metod som flyttar ett
   bokmärke och skyddar det mot att gå längre än bokens sista sida.
3. **Uppgift 4: Kortast först.** Implementera `__lt__` så att en lista av
   böcker går att sortera med `sort`.
4. **Uppgift 5: Två exemplar.** Implementera `__eq__` så att `==`
   jämför böckernas innehåll i stället för deras identitet.
5. **Uppgift 6: En bråkig klass.** Skriva en klass för bråk som går att
   jämföra, skriva ut, räkna med, omvandla till flyttal och förkorta.
6. **Uppgift 7: Metoderna som redan fanns.** Ta reda på varifrån `print`
   och `==` fick sina svar innan klassen hade dundermetoder, och skriva
   en underklass för en lånad bok som överlagrar en metod med hjälp av
   `super()`.

## På egen hand

Resten av uppgifterna finns kvar att göra på egen tid; lösningsförslagen
i dokumentet låter dig kontrollera dina egna svar.

1. **Uppgift 3: Två böcker.** Förutsäga utskriften från två nästan
   identiska program, för att se att metodanrop gäller ett bestämt
   objekt.
2. **Uppgift 8: Klass eller uppslagslista.** Välja mellan att
   representera samma data som en klass eller som en uppslagslista,
   beroende på vad programmet behöver.
3. **Uppgift 9: Någon annans klass.** Granska och skriva om en illa
   skriven klass: inkapsling, namn, kodupprepning och dundermetoder.
4. **Fördjupning: Uppgift 10: Författaren.** Välja mellan arv och
   komposition (is-a mot has-a) för en ny klass `Author`.

## Förberedelser

Innan övningen bör du ha tagit del av föreläsningen *Föreläsning: Klasser
och objekt* här i modulen.

## Efter övningen

Fortsätt enligt veckoöversikten: arbeta i par med *Laboration (4) klasser
och objekt (kamratgranskning)*.
