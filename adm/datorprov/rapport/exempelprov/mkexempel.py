#!/usr/bin/env python3
"""Typeset the two practice exams (New Quizzes exports) as LaTeX.

Usage: mkexempel.py EXPORT.json OUT.tex PREFIX

Every item becomes a subsection: the stem (HTML converted: paragraphs,
lists, emphasis, inline code as \\texttt, code blocks as minted), the
options as a list with the key marked, ordering and matching keys, fill-in
blanks with their accepted answers, and the item's feedback when it has
any (neutral, right, wrong, per option).
"""
import html
import json
import math
import re
import sys

TEXT_SPECIALS = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$",
    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}", '"': r"\textquotedbl{}", "<": r"\textless{}",
    ">": r"\textgreater{}", "|": r"\textbar{}", "\xa0": "~",
}
TT_SPECIALS = dict(TEXT_SPECIALS)
TT_SPECIALS["\xa0"] = " "
TT_SPECIALS["'"] = r"\textquotesingle{}"
TT_SPECIALS["`"] = r"\textasciigrave{}"
TT_SPECIALS["-"] = "-{}"
BREAK_AFTER = "._(,=/|)*?+]"


def esc(text, table=TEXT_SPECIALS):
    out = "".join(table.get(ch, ch) for ch in text)
    while "--" in out:
        out = out.replace("--", "-{}-")
    return out


def tt(code):
    """Inline code: \\texttt with every special escaped; a long literal
    may break after a dot, underscore, parenthesis, comma, = or slash."""
    code = html.unescape(code)
    if len(code) <= 16:
        return r"\texttt{" + esc(code, TT_SPECIALS) + "}"
    out = []
    for ch in code:
        out.append(esc(ch, TT_SPECIALS))
        if ch in BREAK_AFTER:
            out.append(r"\allowbreak{}")
    return r"\texttt{" + "".join(out) + "}"


def pre_to_code(fragment):
    """The text of a <pre> block: <br> and newlines are line breaks."""
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"</?(code|span|p|strong|em)[^>]*>", "", fragment)
    text = html.unescape(fragment).replace("\xa0", " ")
    return text.strip("\n")


def lexer(code):
    if re.search(r"\b(def|print|for|while|if|import|return|class|in)\b|=",
                 code):
        return "python"
    return "text"


def minted(code):
    return ("\\begin{minted}{" + lexer(code) + "}\n" + code
            + "\n\\end{minted}\n")


def inline(fragment):
    """Convert inline HTML (no block elements) to LaTeX."""
    out = []
    pos = 0
    for m in re.finditer(r"<code[^>]*>(.*?)</code>", fragment, re.S):
        out.append(inline_text(fragment[pos:m.start()]))
        out.append(tt(re.sub(r"<[^>]+>", "", m.group(1))))
        pos = m.end()
    out.append(inline_text(fragment[pos:]))
    return "".join(out)


def inline_text(fragment):
    fragment = re.sub(r"<br\s*/?>", "\n\n", fragment)
    parts = re.split(r"(</?(?:em|strong|b|i)>)", fragment)
    out = []
    for part in parts:
        if part in ("<em>", "<i>"):
            out.append(r"\emph{")
        elif part in ("<strong>", "<b>"):
            out.append(r"\textbf{")
        elif part in ("</em>", "</strong>", "</i>", "</b>"):
            out.append("}")
        else:
            part = re.sub(r"<[^>]+>", "", part)
            out.append(esc(html.unescape(part)))
    return "".join(out)


def console(fragment):
    """Canvas pastes terminal output as <p class="jqconsole"> lines: make
    each run of them one <pre> block, and move a closing remark in
    parentheses out of it."""
    fragment = re.sub(r'<p class="jqconsole[^"]*"[^>]*>(.*?)</p>',
                      r"<pre>\1</pre>", fragment, flags=re.S)
    fragment = re.sub(r"</pre>\s*<pre>", "<br>", fragment)

    def remark(m):
        body = m.group(1)
        found = re.search(r"((?:<br\s*/?>)+)\s*(\([^()]*\))\s*"
                          r"(?:<br\s*/?>|</span>|\s)*$", body)
        if not found:
            return m.group(0)
        return ("<pre>" + body[:found.start()] + "</pre><p>"
                + found.group(2) + "</p>")
    return re.sub(r"<pre>(.*?)</pre>", remark, fragment, flags=re.S)


def blocks(fragment):
    """Convert an HTML fragment with blocks to LaTeX paragraphs."""
    fragment = console(fragment or "")
    out = []
    pos = 0
    pattern = re.compile(r"<pre[^>]*>(.*?)</pre>|<ul[^>]*>(.*?)</ul>"
                         r"|<ol[^>]*>(.*?)</ol>", re.S)
    for m in pattern.finditer(fragment):
        out.append(paragraphs(fragment[pos:m.start()]))
        if m.group(1) is not None:
            code = pre_to_code(m.group(1))
            if code.strip():
                out.append(minted(code))
        else:
            body = m.group(2) if m.group(2) is not None else m.group(3)
            env = "itemize" if m.group(2) is not None else "enumerate"
            items = re.findall(r"<li[^>]*>(.*?)</li>", body, re.S)
            out.append("\\begin{" + env + "}\n" + "".join(
                "  \\item " + inline(i).strip() + "\n" for i in items)
                + "\\end{" + env + "}\n")
        pos = m.end()
    out.append(paragraphs(fragment[pos:]))
    return "\n".join(p for p in out if p.strip())


def paragraphs(fragment):
    paras = re.split(r"</p>|<p[^>]*>", fragment)
    out = []
    for para in paras:
        text = inline(para).strip()
        text = re.sub(r"(\n\s*)+\n", "\n\n", text)
        if text.replace("~", "").strip():
            out.append(text + "\n")
    return "\n".join(out)


def option_body(fragment):
    """An option: inline text, or a code block."""
    if "<pre" in fragment:
        body = blocks(fragment)
        if body.lstrip().startswith("\\begin{minted}"):
            # a code block must not start on the label's line
            body = "\\leavevmode\\par\n" + body
        return body
    return paragraphs(fragment).strip()


def letter(i):
    return "ABCDEFGHIJ"[i]


def choices_list(entry, keys, feedback):
    choices = entry["interaction_data"]["choices"]
    if isinstance(choices, dict):
        choices = list(choices.values())
    choices = sorted(choices, key=lambda c: c.get("position", 0))
    lines = ["\\begin{description}"]
    for i, choice in enumerate(choices):
        mark = r" \textit{(key)}" if choice["id"] in keys else ""
        lines.append(f"  \\item[{{{letter(i)}{mark}}}] "
                     + option_body(choice["item_body"]))
        fb = feedback.get(choice["id"])
        if fb:
            lines.append("\n    \\emph{Feedback:} " + blocks(fb).strip())
    lines.append("\\end{description}")
    return "\n".join(lines) + "\n"


def render_item(item, prefix):
    entry = item["entry"]
    kind = entry["interaction_type_slug"]
    lo = round(math.log10(item["points_possible"])) + 1
    points = f"{int(item['points_possible']):,}".replace(",", "\\,")
    out = [f"\\subsection{{Question {item['position']}}}",
           f"\\label{{{prefix}:q{item['position']}}}",
           f"\\emph{{Learning objective {lo}, {points} "
           f"point{'s' if points != '1' else ''}, {kind}"
           + (f", drawn from bank {esc(entry['title'].split()[0])}"
              if re.match(r"\d\.\d ", entry.get("title") or "") else "")
           + ".}\n"]
    body = entry["item_body"]
    if kind == "rich-fill-blank":
        for n, blank in enumerate(entry["interaction_data"]["blanks"], 1):
            body = re.sub(r'<span id="blank_' + re.escape(blank["id"])
                          + r'"></span>', f"[[BLANK{n}]]", body)
    stem = blocks(body)
    stem = re.sub(r"\[\[BLANK(\d+)\]\]",
                  r"\\fbox{\\strut\\enspace(\1)\\enspace}", stem)
    out.append(stem)
    scoring = entry["scoring_data"]
    feedback = entry.get("answer_feedback") or {}
    if kind == "choice":
        out.append("The options; the key is marked:")
        out.append(choices_list(entry, {scoring["value"]}, feedback))
    elif kind == "multi-answer":
        out.append("The options; every correct option is marked:")
        out.append(choices_list(entry, set(scoring["value"]), feedback))
    elif kind == "ordering":
        choices = entry["interaction_data"]["choices"]
        ids = list(choices)
        out.append("The lines to order, as the item lists them:")
        out.append("\\begin{description}")
        for i, cid in enumerate(ids):
            out.append(f"  \\item[{{{letter(i)}}}] "
                       + option_body(choices[cid]["item_body"]))
        out.append("\\end{description}")
        order = ", ".join(letter(ids.index(c)) for c in scoring["value"])
        out.append(f"The key: the order {order}.\n")
    elif kind == "matching":
        data = entry["interaction_data"]
        out.append("Match each name with a description; the key:")
        out.append("\\begin{description}")
        for q in data["questions"]:
            out.append("  \\item[{" + tt(q["item_body"]) + "}] "
                       + esc(scoring["value"][q["id"]]))
        out.append("\\end{description}")
        extra = [a for a in data["answers"]
                 if a not in scoring["value"].values()]
        if extra:
            out.append("Descriptions that match nothing: "
                       + "; ".join(esc(a) for a in extra) + ".\n")
    elif kind == "rich-fill-blank":
        out.append("The key for each blank:")
        out.append("\\begin{description}")
        for n, blank in enumerate(scoring["value"], 1):
            data = blank["scoring_data"]
            text = data.get("blank_text") or data.get("value")
            line = f"  \\item[({n})] " + tt(str(text))
            if blank.get("scoring_algorithm") == "TextRegex":
                line += (", accepted as the regular expression "
                         + tt(str(data["value"])))
            out.append(line)
        out.append("\\end{description}")
    else:
        out.append(f"(Item type {esc(kind)} not shown.)\n")
    general = entry.get("feedback") or {}
    names = [("neutral", "General feedback"),
             ("correct", "Feedback on a right answer"),
             ("incorrect", "Feedback on a wrong answer")]
    present = [(k, n) for k, n in names if general.get(k)]
    if present:
        out.append("The item's feedback:")
        out.append("\\begin{description}")
        for k, n in present:
            out.append(f"  \\item[{n}] " + blocks(general[k]).strip())
        out.append("\\end{description}")
    return "\n".join(out) + "\n"


def main():
    export, target, prefix = sys.argv[1:4]
    with open(export, encoding="utf-8") as file:
        quiz = json.load(file)
    items = sorted(quiz["items"], key=lambda i: i["position"])
    text = ("% Generated from a `canvaslms quizzes export` of the practice\n"
            "% exam by mkexempel.py; do not edit by hand.\n"
            "\\begin{otherlanguage}{swedish}\n"
            + "\n".join(render_item(i, prefix) for i in items)
            + "\\end{otherlanguage}\n")
    with open(target, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    main()
