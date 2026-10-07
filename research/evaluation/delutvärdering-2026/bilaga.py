#!/usr/bin/env python3
"""Turn canvaslms's LaTeX export of the survey into Bilaga B.

Reads svar-canvas.tex (`canvaslms quizzes analyse --format latex`) and
writes bilaga.tex: Swedish headings, Canvas's escaped commas restored, and
the two meaningless "n correct"/"n incorrect" fields of a survey dropped.
"""
import re

s = open("svar-canvas.tex", encoding="utf-8").read()
s = s.replace("\\textbackslash{},", ",")
s = re.sub(
    r"\\subsection\{n correct\}.*?(?=\\section\{Qualitative Summary\})",
    "",
    s,
    flags=re.S,
)
for old, new in [
    ("\\section{Quantitative Summary}", "\\section{Flervalsfrågorna}"),
    ("\\section{Qualitative Summary}", "\\section{Fritextsvaren}"),
    ("Total responses:", "Antal svar:"),
    ("Total selections:", "Antal markeringar:"),
    ("\\textbf{Response distribution:}", ""),
    ("\\textbf{Option distribution:}", ""),
    ("\\textit{Full question:}", "\\textit{Hela frågan:}"),
]:
    s = s.replace(old, new)
s = re.sub(
    r"\\textbf\{Individual Responses \((\d+) total\):\}", r"\\textbf{\1 svar:}", s
)
open("bilaga.tex", "w", encoding="utf-8").write(s)
