---
title: Laboration: Kom igång med Hello world
authors:
  - Celina Soori <celinah@kth.se>
  - Daniel Bosk <dbosk@kth.se>
---
# Laboration: Kom igång med Hello world

Det här är en frivillig laboration för att hjälpa dig att komma igång med kodandet. 
Du behöver inte lämna in något för denna laboration.

Målet med laborationen är att:

1. Installera Python.
2. Välj, installera och förstå en textredigerare.
3. Skriva ett enkelt program "Hello World".

## Ladda ner Python

Första steget vi ska göra är att installera Python. Det gör du enklast genom 
att gå till [Pythons nedladdningssida](https://www.python.org/downloads/).

När du installerar Python, missa inte att klicka i boxen musen pekar på
i bilden nedan (bilden är från Windows-versionen):

![download_python](https://user-images.githubusercontent.com/105818197/186904393-23505d95-c172-4c9e-a949-952a4b8ded18.PNG)

## Välj textredigerare

Det finns många textredigerare därute, i den här kursen får du välja själv
vilken textredigerare du känner dig mest bekväm vid. Nedan kommer några
av de textredigerare vi rekommenderar. Under varje textredigerare finns en 
länk till en tutorial som hjälper dig att skriva ditt första python-program.

Hur din textredigerare ser ut på din dator stämmer inte alltid överens med 
hur den ser ut i den tutorial du tittar på. Om du stöter på problem är du 
välkommen till ett laborationstillfälle för att få hjälp!

### PyCharm

Installera PyCharm Community från [PyCharms nedladdningssida](https://www.jetbrains.com/pycharm/download/#section=windows).

Läs genomgången [Create and run your first Python project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#summary) 
för att skapa ditt första program i PyCharm. Koden som används i genomgången 
behöver du inte förstå, utan viktiga är att du förstår hur du öppnar PyCharm, 
skapar ett program, skriver in kod i programmet och kör programmet.

### IDLE 

IDLE är en textredigerare som installeras automatiskt när du installerar Python 
(på de flesta system, på vissa Linux-system måste den installeras separat).

Gå till sökbaren på din dator. Skriv in "IDLE" och öppna programmet IDLE 
(Python GUI). Nu borde du se detta fönster:

![idle_part1](https://user-images.githubusercontent.com/105818197/186905321-49a6c171-0786-4342-b0c9-0a4eb77ff16e.PNG)

Följ nu [Writing, Saving and Running Python Programs with IDLE](https://thehelloworldprogram.com/python/python-program-idle/) för att 
skapa ditt första program i IDLE.


### VSCode

Installera VSCode från [VSCodes nedladdningssida](https://code.visualstudio.com/download).
När du installerat VSCode och startat det borde det se ut ungefär så här:

![vscode_part1](https://user-images.githubusercontent.com/105818197/186906373-e111faad-a7bc-4900-a5a1-c98913098fe2.PNG)

Följ nu de första 5 minuterna av [videon Visual Studio Code Python for Beginners: Hello World & Beyond](https://www.youtube.com/watch?v=dGeUH_bqNpA) 
för att skriva ditt första Python-program!


## Skriv ett enkelt program

Nu har du förhoppningsvis installerat Python och en textredigerare. Dags att skriva
ditt första egna program!

Skapa en fil i din textredigerare och döp den till helloworld.py (eller något 
annat skoj). Skriv in:
```python
message = "Hello World!"

print(message)
```
Kör din fil helloworld.py i din textredigerare. Utskriften i terminalen ska nu 
se ut så här:
```
Hello World!
```

## Remixa program

Ladda hem programmen

  - [frågesport.py](https://github.com/dbosk/intropy/raw/v2023/modules/helloworld/frågesport.py)
  - [rövarspråket.py](https://github.com/dbosk/intropy/raw/v2023/modules/helloworld/rövarspråket.py)
Provkör programmen. Prova att ändra på programmen.

När du är nöjd med dina ändringar kan du lämna in programmet här. Efter 
deadline kommer du att få två program som dina klasskamrater har skrivit. Ge 
dem återkoppling. Detta låter dig öva på att använda Canvas såsom vi kommer att 
använda det på kommande labbar. Se Canvas sida
[How do I submit a peer review to an assignment?](https://community.canvaslms.com/t5/Student-Guide/How-do-I-submit-a-peer-review-to-an-assignment/ta-p/293) 
om hur du går tillväga.
