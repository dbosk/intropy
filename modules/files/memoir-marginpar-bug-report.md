# memoir: `\mem@doclearpage` drops `\marginpar`s on the no-footnote fast path (“Float(s) lost”)

## Summary

When a `\clearpage` (or the implicit one at `\end{document}`) is processed on a
page that has **no footnotes**, memoir’s `\mem@doclearpage` takes a fast path
that splits the page with `\vsplit` instead of running `\@makecol`/`\@opcol`.
That fast path never drains pending margin notes from `\@currlist`; it only
*checks* the list and, if it is non-empty, raises

```
! LaTeX Error: Float(s) lost.
```

and silently discards the note (`\global\let\@currlist\@empty`).  Any
`\marginpar` that is still held on `\@currlist` at that moment is therefore
lost.  The stock LaTeX `\@doclearpage` does not exhibit this, because it
disposes of the page through `\@opcol`/`\@makecol`, which *does* process
marginpars.

This affects plain `\marginpar` as well as packages built on it (e.g.
`marginfix`); the note is lost before any such package’s `\@addmarginpar`
hook runs.

## Environment

- LaTeX2e `<2025-06-01>` patch level 1 (TeX Live 2025, format 2025.10.27)
- memoir `2025/10/02 v3.8.4`
- engine: pdfTeX 3.141592653-2.6-1.40.28
- also observed with `marginfix 2020/05/06 v1.2` loaded (via `didactic`)
  and with `beamerarticle`

## Symptom

A document compiles with one (or more) margin notes silently missing from the
output, and the log contains `! LaTeX Error: Float(s) lost.` The traceback
points at memoir’s clearpage routine:

```
\mem@doclearpage ...latexerr {Float(s) lost}\@ehb
                                              \global \let \@currlist \@...
\@specialoutput ...tpenalty >-\@Mii \@doclearpage
```

## Root cause

In `memoir.cls` (v3.8.4):

```latex
\newcommand{\mem@doclearpage}{%
  \@mem@testifnofoot
  \if@mem@nofoot
    \setbox\@tempboxa\vsplit\@cclv to\z@ \unvbox\@tempboxa   % fast path:
    \setbox\@tempboxa\box\@cclv                              %   \vsplit,
    \xdef\@deferlist{\@toplist\@botlist\@deferlist}%         %   not \@makecol
    \global \let \@toplist \@empty
    \global \let \@botlist \@empty
    \global \@colroom \@colht
    \ifx \@currlist\@empty
    \else
       \@latexerr{Float(s) lost}\@ehb        % <-- marginpar on \@currlist lost
       \global \let \@currlist \@empty
    \fi
    ...
  \else
    \setbox\@cclv\vbox{\box\@cclv\vfil}%
    \@makecol\@opcol                          % <-- this path DOES drain marginpars
    \clearpage
  \fi
}
\gdef\@doclearpage{\mem@doclearpage}
```

The `\if@mem@nofoot` branch is taken whenever the page being cleared has no
footnotes (`\footins`, `\footinsv@r`, `\sideins`, `\sidefootins` all void —
see `\@mem@testifnofoot`).  On that branch the page is disposed of with
`\vsplit`, which does **not** call `\@addmarginpar`.  A `\marginpar` that the
output routine has deferred onto `\@currlist` (e.g. because it was anchored
low on a page whose margin was already occupied) is therefore never placed;
the `\ifx\@currlist\@empty\else …\fi` block reports `Float(s) lost` and drops
it.

The `\else` (has-footnotes) branch does not have the problem because it runs
`\@makecol\@opcol`, which processes pending marginpars normally.

## Reproduction

This is pagination-sensitive: it requires a `\marginpar` to be *held* on
`\@currlist` at a footnote-free `\clearpage`.  We reproduce it reliably in a
real document (memoir + `beamerarticle`, several `\marginpar`-based notes per
page, a note anchored near the bottom of a page that is followed by a chapter
/ `\printbibliography`).  We were **not** able to reduce it to a small MWE —
in isolation the output routine drains the marginpars before the clearpage —
which is consistent with the fault being a missing drain only on the
no-footnote fast path under specific fill conditions.

Diagnostic confirmation (via a debug build of `marginfix`): on the failing
page, `marginfix`’s `\@addmarginpar` correctly captured and placed one margin
note, and `\mem@doclearpage` then lost a *second* note that was still on
`\@currlist` — i.e. the loss happens inside memoir’s clearpage routine, not in
the margin-note package.

## A fix that does NOT work (please avoid)

The obvious idea — divert to the `\@makecol` branch when `\@currlist` is
non-empty, e.g.

```latex
\renewcommand*{\@mem@extranofeet}{\ifx\@currlist\@empty\else\@mem@nofootfalse\fi}
```

**causes an infinite loop.**  The `\else` branch ends in `\clearpage`, which
re-enters `\mem@doclearpage`; `\@makecol\@opcol` on the (now essentially empty)
page does not place the stuck marginpar, so `\@currlist` stays non-empty and
the document re-clears forever (we observed 13000+ pages before aborting).
So the fast path needs to actually *drain* the marginpars, not merely be
bypassed.

## Suggested fix direction

On the no-footnote fast path, dispose of pending marginpars the same way the
normal path does — i.e. ensure `\@currlist` marginpars are run through the
marginpar-placement machinery (`\@addmarginpar`) before the
`\ifx\@currlist\@empty` check, rather than erroring and discarding them.  The
goal is that a held marginpar is carried to a subsequent page (as it would be
under the stock `\@doclearpage`) instead of being lost.

## Workarounds (for users)

- Reduce margin-note pressure so no note is held across the clearpage (move or
  shorten notes), or add content so the offending note is not anchored at the
  very bottom of a page.
- Build with a margin-note manager (e.g. `marginfix`) *and* avoid the
  no-footnote fast path on the relevant page — but note the infinite-loop trap
  above; bypassing the fast path is not sufficient on its own.
- Treat the `Float(s) lost` as non-fatal in the build (the PDF is still
  produced; one margin note is dropped and the error is logged).
