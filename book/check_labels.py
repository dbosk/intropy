#!/usr/bin/env python3
"""Fail when two decks bound into the book define the same label.

Every deck builds standalone, where its labels only have to be unique within
the deck.  The book puts all decks into one document, so a label such as
`app:verifiera` defined in two decks makes every `\\cref` to it resolve to
whichever definition LaTeX saw last.  LaTeX only warns about that, so this
script turns it into a build failure, and says which decks collide.

It reads the decks from `book-body.tex` (the `\\deck{<dir>}{<title>}` lines),
then scans each deck's sources for

- `\\label{...}` and `\\label[type]{...}`;
- the names of `restatable` environments, which define a macro each
  (`\\begin{restatable}{lo}{HelloLOProgram}` defines `\\HelloLOProgram`);
- noweb's chunk labels in the woven `contents.tex` (`NW<prefix>-...`), which
  collide when two decks are woven under the same file name.

Usage: check_labels.py [book-body.tex]
"""

import pathlib
import re
import sys
from collections import defaultdict

DECK = re.compile(r"^\s*\\deck(?:\[[^\]]*\])?\{([^}]*)\}", re.MULTILINE)
LABEL = re.compile(r"\\label(?:\[[^\]]*\])?\{([^}]*)\}")
RESTATABLE = re.compile(r"\\begin\{restatable\}(?:\[[^\]]*\])?\{[^}]*\}\{([^}]*)\}")
NOWEB = re.compile(r"\\sublabel\{([^}]*)\}")
# The deck's sources as the book reads them.  contents.tex is woven from
# contents.nw, so it carries the deck's own labels and noweb's.
SOURCES = ["abstract.tex", "contents.tex", "sokprotokoll.tex"]


def strip_comments(text):
    """Drop TeX comments, so a commented-out label does not count."""
    return re.sub(r"(?<!\\)%.*", "", text)


def deck_labels(deck):
    """Return {label: kind} for one deck directory."""
    found = {}
    for name in SOURCES:
        path = deck / name
        if not path.exists():
            if name == "contents.tex":
                sys.exit(f"{path}: not woven yet; run make -C {deck} first")
            continue
        text = strip_comments(path.read_text(encoding="utf-8"))
        for label in LABEL.findall(text):
            found[label] = "label"
        for label in RESTATABLE.findall(text):
            found["\\" + label] = "restatable"
        for label in NOWEB.findall(text):
            found[label] = "noweb chunk"
    return found


def modules_dir(body):
    """The decks' paths in book-body.tex are relative to modules/."""
    return body.parent / ".." / "modules"


def main():
    body = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "book-body.tex")
    decks = DECK.findall(strip_comments(body.read_text(encoding="utf-8")))
    owners = defaultdict(list)
    kinds = {}
    for deck in decks:
        for label, kind in deck_labels(modules_dir(body) / deck).items():
            owners[label].append(deck)
            kinds[label] = kind
    clashes = {label: where for label, where in owners.items()
               if len(where) > 1}
    for label in sorted(clashes):
        print(f"{kinds[label]} {label}: {', '.join(clashes[label])}")
    print(f"{len(decks)} decks, {len(owners)} labels, "
          f"{len(clashes)} defined in more than one deck")
    return 1 if clashes else 0


if __name__ == "__main__":
    sys.exit(main())
