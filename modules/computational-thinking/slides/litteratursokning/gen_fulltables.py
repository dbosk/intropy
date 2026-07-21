#!/usr/bin/env python3
"""Generate auditable full-candidate longtables from scholar session CSVs.

Every candidate is listed with the reason it was included or excluded.  The
reason comes from the decision tag recorded in the scholar session:

  * kept papers carry a *theme* tag (why they were selected);
  * discarded papers carry one of two *screening* tags, assigned by reading
    each candidate's title and venue:
      - off-topic-false-hit   -> another subject, returned on keyword overlap
      - on-topic-not-selected -> genuinely on topic, but not cited
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

# Screening / theme tag -> readable Swedish reason for the "Skäl" column.
DISCARD_REASON = {
    "off-topic-false-hit": "annat ämne (felträff)",
    "on-topic-not-selected": "på ämnet, ej vald",
}
THEME_REASON = {
    "structured-programming-theorem": "struktureringsteoremet",
    "misconceptions-review": "översikt över missuppfattningar",
    "CT-definition": "definition av beräkningstänkande",
    "CT-facets-concepts-vs-practices": "facetter: begrepp mot färdigheter",
    "systematic-review": "systematisk översikt",
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


def reason_for(status, tags):
    """Human-readable Swedish reason from a paper's status and decision tag."""
    tag = (tags or "").split("|")[0].strip()
    if status == "kept":
        return "\\emph{vald}: " + tex(THEME_REASON.get(tag, tag or "vald"))
    return tex(DISCARD_REASON.get(tag, tag or "ej vald"))


def rows_for(csv_path):
    seen = {}
    with open(csv_path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            title = tex(r["title"])[:180]
            year = tex(r.get("year", ""))
            prov = short_provider(r.get("provider", ""))
            status = r.get("status", "").strip().lower()
            reason = reason_for(status, r.get("tags", ""))
            key = (r["title"].strip().lower(), year)
            if key in seen:                       # merge provider dups
                if prov and prov not in seen[key][2]:
                    seen[key][2] += ", " + prov
                if status == "kept":              # a kept dup wins the reason
                    seen[key][3] = "kept"
                    seen[key][4] = reason
            else:
                seen[key] = [title, year, prov, status, reason]
    return list(seen.values())


TABLE = r"""\begingroup\footnotesize
\begin{longtable}{@{}%%
  >{\raggedright\arraybackslash}p{0.44\textwidth}c%%
  >{\raggedright\arraybackslash}p{0.13\textwidth}%%
  >{\raggedright\arraybackslash}p{0.26\textwidth}@{}}
\caption{Fullständig träfflista, sökspår %(track)s (session \texttt{%(sess)s};
%(n)d unika träffar, %(kept)d behållna, %(off)d felträffar, %(nots)d på ämnet
men ej valda).  Skälet till varje in- eller uteslutning står i sista
kolumnen.}\label{tab:sok-%(track)s}\\
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

for track, sess in [("A", "sprak-A"), ("B", "sprak-B"), ("C", "sprak-C")]:
    rows = rows_for(BASE / f"{sess}.csv")
    # kept first, then on-topic-not-selected, then off-topic; title within group
    rows.sort(key=lambda r: (r[3] != "kept",
                             "på ämnet" not in r[4],   # on-topic before off
                             r[0].lower()))
    kept = sum(1 for r in rows if r[3] == "kept")
    off = sum(1 for r in rows if "felträff" in r[4])
    nots = sum(1 for r in rows if "på ämnet" in r[4])
    body = "\n".join(
        "%s & %s & %s & %s \\\\" % (t, y, p, reason)
        for (t, y, p, s, reason) in rows)
    (BASE / f"{sess}-full.tex").write_text(
        TABLE % {"track": track, "sess": sess, "n": len(rows),
                 "kept": kept, "off": off, "nots": nots, "body": body},
        encoding="utf-8")
    print(f"track {track}: {len(rows)} unique rows, {kept} kept, "
          f"{off} felträff, {nots} på ämnet -> {sess}-full.tex")
