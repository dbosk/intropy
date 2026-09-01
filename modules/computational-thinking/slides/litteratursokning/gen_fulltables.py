#!/usr/bin/env python3
"""Generate auditable full-candidate longtables from scholar session CSVs.

Every candidate is listed with the reason it was included or excluded, drawn
from the decision recorded in the scholar session.  Candidates were screened
by LLM classification (scholar llm classify) against a stated research context,
grounded in each paper's abstract:

  * citerad            -- the primary source actually cited (human decision);
  * stöder påståendet  -- LLM-judged to bear on the module's decomposition
                          claim (a corroborating source strengthens the claim);
  * angränsande delämne-- within computing, but does not bear on the claim;
  * annat ämne (felträff) -- another field, returned only on keyword overlap.

For LLM-decided rows the model's confidence is shown in parentheses.
"""
import csv
import pathlib

BASE = pathlib.Path(__file__).resolve().parent

# Unicode punctuation -> pdflatex-safe ASCII/TeX (inputenc handles Latin accents).
PUNCT = {
    "“": "``", "”": "''", "‘": "`", "’": "'",
    "–": "--", "—": "---", "…": r"\dots{}",
    " ": " ", " ": " ", "​": "", "﻿": "",
    "ʼ": "'", "′": "'", "­": "",
}
SPECIAL = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
           "^": r"\textasciicircum{}", "\\": r"\textbackslash{}"}

# Theme tag (kept, human-cited) -> readable Swedish name of the strand.
THEME_REASON = {
    "structured-programming-theorem": "struktureringsteoremet",
    "misconceptions-review": "översikt över missuppfattningar",
    "CT-definition": "definition av beräkningstänkande",
    "CT-facets-concepts-vs-practices": "facetter: begrepp mot färdigheter",
    "systematic-review": "systematisk översikt",
}
# Decision tag -> (Swedish reason label, sort order).  Kept-cited is 0.
CATEGORY = {
    "supports-claim": ("stöder påståendet", 1),
    "adjacent-subtopic": ("angränsande delämne", 2),
    "off-topic-false-hit": ("annat ämne (felträff)", 3),
}


def tex(s):
    s = s or ""
    for k, v in PUNCT.items():
        s = s.replace(k, v)
    out = []
    for ch in s:
        if ch in SPECIAL:
            out.append(SPECIAL[ch])
        elif ord(ch) > 0x2100:            # drop exotic symbols pdflatex lacks
            out.append("")
        else:
            out.append(ch)
    return "".join(out).strip()


def short_provider(p):
    return (p or "").replace("openalex", "OA").replace("dblp", "DBLP") \
        .replace("scopus", "Scopus").replace("wos", "WoS").replace("ieee", "IEEE")


def reason_for(row):
    """(reason label, sort order) from a paper's status, tag, and confidence."""
    status = (row.get("status") or "").strip().lower()
    tag = (row.get("tags") or "").split("|")[0].strip()
    conf = (row.get("llm_confidence") or "").strip()
    src = (row.get("decision_source") or "").strip().lower()
    if status == "kept" and tag != "supports-claim":     # human-cited source
        return "\\emph{citerad}: " + tex(THEME_REASON.get(tag, tag)), 0
    label, order = CATEGORY.get(tag, (tex(tag or "?"), 4))
    if src == "llm" and conf:                            # show model confidence
        try:
            label += " (%.2f)" % float(conf)
        except ValueError:
            pass
    return label, order


def rows_for(csv_path):
    seen = {}
    with open(csv_path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            title = tex(r["title"])[:180]
            year = tex(r.get("year", ""))
            prov = short_provider(r.get("provider", ""))
            status = (r.get("status") or "").strip().lower()
            reason, order = reason_for(r)
            key = (r["title"].strip().lower(), year)
            if key in seen:                       # merge provider dups
                if prov and prov not in seen[key][2]:
                    seen[key][2] += ", " + prov
                if status == "kept":              # a kept dup wins the reason
                    seen[key][3] = "kept"
                    seen[key][4] = reason
                    seen[key][5] = order
            else:
                seen[key] = [title, year, prov, status, reason, order]
    return list(seen.values())


TABLE = r"""\begingroup\footnotesize
\begin{longtable}{@{}%%
  >{\raggedright\arraybackslash}p{0.44\textwidth}c%%
  >{\raggedright\arraybackslash}p{0.13\textwidth}%%
  >{\raggedright\arraybackslash}p{0.26\textwidth}@{}}
\caption{Fullständig träfflista, sökspår %(num)s (session \texttt{%(sess)s};
%(n)d unika träffar: %(cit)d citerade, %(sup)d stöder påståendet,
%(adj)d angränsande, %(off)d felträffar).  Skälet till varje in- eller
uteslutning står i sista kolumnen; för maskinklassade rader anges modellens
konfidens.}\label{tab:sok-%(track)s}\\
\toprule
Titel & År & Leverantör & Skäl \\
\midrule
\endfirsthead
\multicolumn{4}{@{}l}{\emph{\tablename~\thetable{} (forts.)}}\\
\toprule Titel & År & Leverantör & Skäl \\ \midrule
\endhead
\midrule \multicolumn{4}{r@{}}{\emph{forts.\ på nästa sida}}\\
\endfoot
\bottomrule
\endlastfoot
%(body)s
\end{longtable}
\endgroup
"""

for track, sess, num in [("A", "sprak-A", "1"), ("B", "sprak-B", "2"),
                         ("C", "sprak-C", "3")]:
    rows = rows_for(BASE / f"{sess}.csv")
    # kept-cited -> supports -> adjacent -> felträff; title within each group
    rows.sort(key=lambda r: (r[5], r[0].lower()))
    cit = sum(1 for r in rows if r[5] == 0)
    sup = sum(1 for r in rows if r[5] == 1)
    adj = sum(1 for r in rows if r[5] == 2)
    off = sum(1 for r in rows if r[5] == 3)
    body = "\n".join(
        "%s & %s & %s & %s \\\\" % (t, y, p, reason)
        for (t, y, p, _st, reason, _o) in rows)
    (BASE / f"{sess}-full.tex").write_text(
        TABLE % {"track": track, "num": num, "sess": sess, "n": len(rows),
                 "cit": cit, "sup": sup, "adj": adj, "off": off, "body": body},
        encoding="utf-8")
    print(f"track {track}: {len(rows)} rows | {cit} citerade, {sup} stöder, "
          f"{adj} angränsande, {off} felträff -> {sess}-full.tex")
