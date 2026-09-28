#!/usr/bin/env python3
"""Fail when two decks bound into the book define a bib key differently.

The book merges the decks' ltnotes.bib into one file with bibtool, which
keeps one entry per key and drops the rest without looking at them.  So a
key must mean the same in every deck, or a chapter cites the other deck's
version of the source.  This script compares the entries field by field
(whitespace aside, provenance comments ignored) and lists every key whose
entries differ, with the decks and the fields.  Make the entries identical
at the source: the fuller, verified entry wins.

Usage: check_bib.py [book-body.tex]
"""

import pathlib
import re
import sys

DECK = re.compile(r"^\s*\\deck(?:\[[^\]]*\])?\{([^}]*)\}", re.MULTILINE)


def strip_comments(text):
    """Drop TeX and bib comments."""
    return re.sub(r"(?<!\\)%.*", "", text)


def braced(text, i):
    """Return the index just after the brace group that opens at text[i]."""
    depth = 1
    i += 1
    while depth:
        depth += (text[i] == "{") - (text[i] == "}")
        i += 1
    return i


def fields(body):
    """Return {field: normalised value} of an entry's body."""
    out, j = {}, 0
    for m in re.finditer(r"(\w+)\s*=\s*", body):
        if m.start() < j:
            continue
        k = m.end()
        if body[k] == "{":
            end = braced(body, k)
            value = body[k + 1:end - 1]
        else:
            end = body.find(",", k)
            end = len(body) if end < 0 else end
            value = body[k:end]
        j = end
        out[m.group(1).lower()] = re.sub(r"\s+", " ", value).strip()
    return out


def entries(path):
    """Return {key: (type, fields)} of a bib file."""
    text = re.sub(r"(?m)^\s*%.*$", "", path.read_text(encoding="utf-8"))
    out = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        end = braced(text, text.index("{", m.start()))
        out[m.group(2)] = (m.group(1).lower(), fields(text[m.end():end - 1]))
    return out


def main():
    body = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "book-body.tex")
    decks = DECK.findall(strip_comments(body.read_text(encoding="utf-8")))
    modules = body.parent / ".." / "modules"
    bibs = {d: entries(modules / d / "ltnotes.bib") for d in decks}
    keys = set().union(*bibs.values())
    differing = 0
    for key in sorted(keys):
        have = [d for d in decks if key in bibs[d]]
        if len({repr(bibs[d][key]) for d in have}) < 2:
            continue
        differing += 1
        print(f"{key}: differs between {', '.join(have)}")
        names = sorted(set().union(*(bibs[d][key][1] for d in have)))
        for name in names:
            values = {d: bibs[d][key][1].get(name) for d in have}
            if len(set(values.values())) > 1:
                print(f"  {name}: " + "; ".join(
                    f"{d}: {v}" for d, v in values.items()))
    print(f"{len(decks)} decks, {len(keys)} keys, "
          f"{differing} defined differently")
    return 1 if differing else 0


if __name__ == "__main__":
    sys.exit(main())
