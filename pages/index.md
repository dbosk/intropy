---
title: En inledande kurs i pythonprogrammering
permalink: /
lang: sv
---
# En introduktion till programmering i Python

Denna kurs introducerar programmering i Python. Mer specifikt är lärandemålen 
att studenten ska kunna

- dela upp ett större problem i hanterliga delar,
- konstruera program utan kodupprepningar,
- tillämpa styrstrukturer,
- utforma och presentera användarvänliga utdata,
- skapa flexibla applikationer,
- välja lämpliga identifierarnamn,
- konstruera interaktiva program,
- överföra data mellan fil och program,
- använda och konstruera sammansatta datatyper (klasser).


## Ingående moduler

Vi har följande moduler:
{% for module in site.data.navigation.modules %}
- [{{ module[1].title }}]({{ module[0] }}) 
{% if module[0] == "/" %}(denna sida){% endif %}
{% endfor %}

