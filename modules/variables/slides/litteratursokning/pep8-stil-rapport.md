# PEP 8 and coding style: a two-sided literature search

For `modules/variables/slides` (*Variabler och utskrifter*), the passage at
`contents.nw:1038-1044`.

**Search date:** 2026-09-06. **Scholar session:** `variables-pep8`.
**Classification model:** `github_copilot/gpt-5.4` (via `scholar llm
classify --no-examples`).

---

## 1. The research question the appendix chapter should answer

The author's handwritten question was: *is adhering to PEP 8 really
beneficial, or can we skip it without negative effects?* That is one
question about a bundle of rules, so the chapter needs one title question
and five sub-questions.

**Chapter title (Swedish), suggested:**

> Hjälper det läsaren att koden följer en stilguide som PEP 8?

**Chapter title (English, for your notes):** *Does following a coding
style guide such as PEP 8 measurably help the reader?*

**Sub-questions as the Resultat sections are organised:**

- (a) Does the choice of *identifier names* affect comprehension?
- (b) Does *layout* (indentation, spacing, line length) affect
  comprehension?
- (c) Does *adherence to a convention as such* affect readability?
- (d) Is there evidence about *PEP 8 itself*, and about style in
  introductory programming?
- (e) The counter side: null results, failed replications, and criticism.

---

## 2. `scholar providers check`, verbatim

Run 2026-09-06 before any search.

```
WARNING: Failed to load cache for biorxiv: Ran out of input
WARNING: Failed to load cache for medrxiv: Ran out of input
WARNING: Failed to load cache for chemrxiv: Ran out of input
WARNING: Failed to load cache for researchsquare: Ran out of input
WARNING: Failed to load cache for preprintsorg: Ran out of input
WARNING: Failed to load cache for iacr: Ran out of input
                                Provider Health
 ──────────────────────────────────────────────────────────────────────────────
  Provider         Configured   Status         Detail
 ──────────────────────────────────────────────────────────────────────────────
  s2               Yes          key rejected   HTTP 403 -- check or replace
                                               S2_API_KEY
  openalex         Yes          ok             API key configured; $0.999 of
                                               $1.00 daily budget left; resets
                                               02:00 (in 12h05m)
  dblp             Yes          ok
  wos              Yes          ok
  ieee             Yes          ok
  arxiv            Yes          ok
  ssrn             Yes          ok             shares the openalex key and
                                               budget
  biorxiv          Yes          ok             shares the openalex key and
                                               budget
  medrxiv          Yes          ok             shares the openalex key and
                                               budget
  chemrxiv         Yes          ok             shares the openalex key and
                                               budget
  researchsquare   Yes          ok             shares the openalex key and
                                               budget
  preprintsorg     Yes          ok             shares the openalex key and
                                               budget
  iacr             Yes          ok             shares the openalex key and
                                               budget
  hal              Yes          ok
  scopus           Yes          ok
 ──────────────────────────────────────────────────────────────────────────────

s2: key rejected HTTP 403 -- check or replace S2_API_KEY
```

**Provider health as it affects this search.**

- **Semantic Scholar was dead** the whole time (HTTP 403). Every query
  therefore missed whatever only S2 indexes.
- **Scopus was alive**, contrary to the note in my instructions that
  Elsevier had been refusing since 2026-09-02. It answered all 34
  queries and was the second-richest provider.
- **IEEE Xplore's daily quota ran out partway through**, after the 26
  long queries and before the 8 short ones. All eight IEEE cells in the
  T-rows of the matrix below are therefore zeros *for quota reasons, not
  because IEEE holds nothing*. Verified afterwards by re-running one
  query: `WARNING: ieee: daily quota exhausted (IEEE); resets 02:00`.
- **DBLP searches publication titles only, and its API strips quotes and
  boolean operators**, so a multi-concept query becomes a conjunction of
  every word in the query and returns nothing. That is why the DBLP
  column is zero for all 26 long queries. The second pass (T1--T8) exists
  precisely to give DBLP a fair chance with short, operator-free queries;
  it still returned only 14 hits in total, because the negative
  vocabulary of a counter-query ("no effect", "null result") almost never
  appears in a title.

---

## 3. Query x provider x hits matrix

Every query was run on every live provider, with the same keyword set
translated into each provider's syntax: OpenAlex, IEEE and arXiv take the
plain form shown; WoS takes `TS=(...)` around it; Scopus takes
`TITLE-ABS-KEY(...)` around it; DBLP receives the plain form and strips
the operators itself. Every query was run under session `variables-pep8`
with `--limit 25`, so a cell of 25 means "25 or more".

Command form:

```
scholar search '<query>' -n variables-pep8 -p <provider> -f csv -l 25
```


### Support queries

| ID | Sub | Query (plain form; WoS TS=(...), Scopus TITLE-ABS-KEY(...)) | OPENALEX | DBLP | IEEE | ARXIV | WOS | SCOPUS |
|---|---|---|---|---|---|---|---|---|
| S1 | (a) | `"identifier naming" AND ("program comprehension" OR readability)` | 25 | 0 | 15 | 16 | 20 | 25 |
| S2 | (a) | `("camelCase" OR "under_score" OR "identifier style") AND (comprehension OR readability OR "eye tracking")` | 25 | 0 | 5 | 1 | 7 | 9 |
| S3 | (a) | `("identifier names" OR "variable names") AND "controlled experiment" AND comprehension` | 23 | 0 | 2 | 0 | 5 | 4 |
| S4 | (a) | `(abbreviations OR abbreviated OR "full words") AND identifiers AND (comprehension OR readability OR memory)` | 25 | 0 | 21 | 25 | 25 | 25 |
| S5 | (a) | `("naming conventions" OR "identifier quality") AND (defects OR faults OR "maintenance effort" OR maintainability)` | 25 | 0 | 12 | 14 | 19 | 25 |
| S6 | (b) | `indentation AND ("program comprehension" OR "source code" OR "computer program") AND (comprehension OR readability)` | 25 | 0 | 5 | 4 | 15 | 17 |
| S7 | (b) | `("source code formatting" OR "program layout" OR "pretty printing" OR "code layout") AND (comprehension OR readability OR maintenance)` | 25 | 0 | 8 | 4 | 16 | 25 |
| S8 | (b) | `"code readability" AND (model OR metric OR "human judgement" OR "human judgment") AND "source code"` | 25 | 0 | 25 | 6 | 25 | 25 |
| S9 | (b) | `(whitespace OR "blank lines" OR "line length" OR "visual structure") AND "source code" AND (comprehension OR readability)` | 25 | 0 | 8 | 1 | 5 | 11 |
| S10 | (c) | `("coding conventions" OR "coding standards" OR "code conventions") AND (readability OR comprehension OR maintainability)` | 25 | 0 | 25 | 25 | 25 | 25 |
| S11 | (c) | `("coding style" OR "programming style" OR "code style") AND (consistency OR convention OR violation) AND (comprehension OR readability OR quality)` | 25 | 0 | 23 | 18 | 25 | 25 |
| S12 | (c) | `("code smell" OR "convention violation" OR "style violation") AND ("program comprehension" OR readability OR "developer perception")` | 25 | 0 | 25 | 21 | 25 | 25 |
| S13 | (d) | `"PEP 8" OR "PEP8" OR ("Python" AND "style guide" AND "source code")` | 25 | 0 | 7 | 7 | 25 | 25 |
| S14 | (d) | `(linter OR "static analysis" OR "style checker" OR pycodestyle OR checkstyle) AND ("introductory programming" OR CS1 OR novice OR students) AND (style OR feedback)` | 25 | 0 | 25 | 11 | 25 | 25 |
| S15 | (d) | `(automated OR automatic) AND (assessment OR grading OR feedback) AND ("programming style" OR "code style" OR "code quality") AND (students OR novice)` | 25 | 0 | 25 | 15 | 25 | 25 |
| S16 | (d) | `(novice OR "introductory programming" OR CS1) AND "code quality" AND (style OR readability OR conventions)` | 25 | 0 | 23 | 6 | 23 | 25 |
| T1 | (a) | `identifier names comprehension` | 25 | 2 | 0 | 25 | 25 | 25 |
| T2 | (a) | `identifier style eye tracking` | 25 | 1 | 0 | 25 | 3 | 4 |
| T3 | (b) | `indentation comprehension` | 25 | 4 | 0 | 25 | 25 | 25 |
| T4 | (b) | `code readability metric` | 25 | 5 | 0 | 25 | 25 | 25 |
| T5 | (c) | `coding conventions readability` | 25 | 0 | 0 | 25 | 25 | 25 |
| T6 | (d) | `programming style automated feedback students` | 25 | 0 | 0 | 25 | 25 | 24 |

### Counter queries

| ID | Sub | Query (plain form; WoS TS=(...), Scopus TITLE-ABS-KEY(...)) | OPENALEX | DBLP | IEEE | ARXIV | WOS | SCOPUS |
|---|---|---|---|---|---|---|---|---|
| C1 | (e) | `("identifier naming" OR "identifier style" OR "variable names") AND ("no significant difference" OR "no effect" OR "null result")` | 25 | 0 | 1 | 25 | 2 | 4 |
| C2 | (e) | `("camelCase" OR "under_score" OR "identifier style") AND (replication OR "conflicting results" OR "no significant")` | 24 | 0 | 0 | 3 | 5 | 4 |
| C3 | (e) | `indentation AND ("source code" OR "computer program") AND ("no significant" OR "no effect" OR replication OR contradictory)` | 25 | 0 | 1 | 5 | 3 | 6 |
| C4 | (e) | `("coding conventions" OR "coding standards" OR "code conventions") AND (criticism OR limitations OR "lack of evidence" OR "no effect")` | 25 | 0 | 25 | 25 | 25 | 25 |
| C5 | (e) | `("code readability" OR "program comprehension") AND ("negative results" OR "failed replication" OR "does not improve" OR "no difference")` | 25 | 0 | 7 | 25 | 4 | 11 |
| C6 | (e) | `("programming style" OR "code style" OR "coding style") AND (novice OR students) AND ("no effect" OR "no improvement" OR "not associated")` | 25 | 0 | 0 | 10 | 0 | 1 |
| C7 | (e) | `("source code formatting" OR "program layout" OR "code layout") AND "controlled experiment" AND ("no difference" OR "not significant" OR inconclusive)` | 23 | 0 | 0 | 0 | 0 | 1 |
| C8 | (e) | `(linter OR "static analysis" OR "style checker") AND (students OR novice) AND ("no effect" OR "did not improve" OR limitations OR "false positives")` | 25 | 0 | 25 | 15 | 18 | 25 |
| C9 | (e) | `"empirical evidence" AND ("coding conventions" OR "coding style" OR "software engineering practices") AND (weak OR lacking OR inconclusive OR "little evidence")` | 25 | 0 | 0 | 2 | 1 | 1 |
| C10 | (e) | `"program comprehension" AND "controlled experiment" AND (replication AND ("failed" OR "contrary" OR "could not"))` | 25 | 0 | 0 | 0 | 0 | 1 |
| T7 | (e) | `coding style experiment negative results` | 25 | 0 | 0 | 25 | 19 | 11 |
| T8 | (e) | `program comprehension replication experiment` | 24 | 2 | 0 | 25 | 23 | 21 |

Total hits returned per provider (capped at 25 per query):
  openalex: 844
  dblp: 14
  ieee: 313
  arxiv: 484
  wos: 538
  scopus: 580

Queries per provider: 34


---

## 3b. Classification of the whole session

The 1858 unique records the 34 queries produced were classified in one
pass over the whole session:

```
scholar llm context variables-pep8 "<the research context, below>"
scholar llm classify variables-pep8 --no-examples --no-enrich -n 200 \
  -t supports-claim -t qualifies-claim -t adjacent-subtopic \
  -t off-topic-false-hit          # repeated until Pending: 0
```

Model: `github_copilot/gpt-5.4`, zero-shot from the research context only.
Outcome after the machine pass: 169 kept, 1689 discarded.

**What I changed by hand.** I read every row the model tagged
`qualifies-claim` (70 of them) and every discard it made with confidence
below 0.72 (19 of them), then:

- marked the 18 cited sources as reviewed keeps with a theme tag each, so
  they print as `\emph{citerad}` rows in the audit table;
- **overrode one discard**: Avidan and Feitelson's *From Obfuscation to
  Comprehension* (ICPC 2015, DOI `10.1109/ICPC.2015.27`) was tagged
  `adjacent-subtopic` at confidence 0.62 and discarded. It is a study of
  what happens to comprehension when variable names are stripped, which
  bears directly on sub-question (a), so I re-tagged it `supports-claim`
  and kept it. It is not cited, because its full 2017 successor
  (`Avidan2017VariableNames`) is.

The export reports this as: 18 LLM decisions confirmed, 1 changed, 0
kept→discarded, 1 discarded→kept.

**Two classifier calls I checked and let stand**, in case the author
disagrees: *The effect of semantic complexity on the comprehension of
program modules* (1984) was discarded as an off-topic false hit — it
varies semantic complexity, not style — and *A Large Scale Empirical Study
of the Impact of Spaghetti Code and Blob Anti-patterns on Program
Comprehension* (2020) was discarded as well, because anti-patterns are
structure rather than the formatting and naming this claim is about.

**A caveat on the classification.** 589 of the 1858 records had no
abstract, so the model saw only their titles. Enrichment could not fix
this: Semantic Scholar's key is rejected, IEEE's daily quota was spent,
and OpenAlex was deliberately left unused to stay inside its metered daily
budget, which left only arXiv and Web of Science, and they added nothing.

The research context given to the classifier is reproduced here so the
appendix's method section can state the inclusion criteria:

> A paper BEARS ON the claim if it reports human-centric empirical
> evidence (controlled experiment, eye tracking, survey of perceived
> readability, replication, systematic review, or large-scale study of
> real or student code) about how identifier naming, identifier style
> (camelCase vs snake_case), abbreviations, indentation, spacing, blank
> lines, line length, source-code formatting, coding conventions, coding
> standards, style violations, style checkers/linters, or style guides
> such as PEP 8 affect code readability, program comprehension, fault
> fixing, maintainability, or novice programmers' learning and code
> quality.

---

## 4. Results

Eighteen sources were verified and are cited. Twelve were read in full
text (six of them from an author's or a repository's copy, because the
publisher's PDF was paywalled or refused the fetcher). Six --
`Scanniello2017Abbreviated`, `Kirk2025DistillingPEP8`,
`Kirk2024StyleNotQuality`, `Hanenberg2024Indentation`,
`vanderWerf2024TeachersNaming` and `BoogerdMoonen2008CodingStandards` --
were verified at abstract level only, and every place they appear says so.
Sources that could not be verified at all are in section 7 and are not
cited anywhere.

### (a) Does identifier naming affect comprehension?

**Yes, for descriptiveness, and the effect is measurable — but it was
found in experienced readers, not beginners.** Schankin et al.
(`Schankin2018Names`) ran a web-based experiment with 88 Java developers
who had to locate a semantic defect, with a syntax-error task as a
control:

> "With descriptive identifier names, developers spent more time in the
> lines of code before the actual defect occurred and changed their
> reading direction less often, finding the semantic defect about 14%
> faster than with shorter but less descriptive identifier names. These
> effects disappeared when developers searched for a syntax error, i.e.,
> when no in-depth understanding of the code was required. Interestingly,
> the style of identifier names had a clear impact on program
> comprehension for more experienced developers but not for less
> experienced developers."
> — Abstract

That last sentence is the one that matters most for a beginners' course:
the 14% gain was an experienced-developer effect.

**But a descriptive name that is wrong is worse than no name at all.**
Avidan and Feitelson (`Avidan2017VariableNames`) are the only ones who
varied names in real production code, with nine professional developers
and six methods from utility classes:

> "Replicating previous work on identifier naming reconfirms that names
> have a large impact on the comprehension of code.  Good names can
> effectively serve as the code's documentation, and are instrumental for
> comprehension.  We also showed that method parameter names are typically
> more significant for comprehension than local variable names."
> — §IX Conclusions

> "Surprisingly, three of the six methods we used turned out to have
> problematic names that even led to comprehension errors.  These
> demonstrate that misleading names, or names that clash with their types,
> are worse than meaningless names like consecutive letters of the
> alphabet."
> — §IX Conclusions

That is the strongest single sentence in this whole search for what a
course should actually teach: the rule is not "make names long", it is
"make names true".

**Readers also say they prefer real words.** dos Santos and Gerosa
(`SantosGerosa2018Readability`) put matched pairs of Java snippets to 54
developers and students for the naming practice:

> "P.11 Names using dictionary words 42 12 22.22% ▲ 54 0.0001"
> — §4.2, Table 1 (42 votes for the adhering snippet, 12 against, p = 0.0001)

**Which convention you pick matters less, and the two studies of it
disagree.** Sharif and Maletic (`SharifMaletic2010CamelCase`) tracked the
eyes of readers recognising identifiers:

> "Although, no difference was found between identifier styles with
> respect to accuracy, results indicate a significant improvement in time
> and lower visual effort with the underscore style.  The interaction of
> Experience with Style indicates that novices benefit twice as much with
> respect to time, with the underscore style."
> — §VIII Conclusions and Future Work

This is a small point in PEP 8's favour, because PEP 8 prescribes the
underscore style for variables. But it is contradicted by the other study
of the same contrast, as the systematic review records
(`Oliveira2023FormattingSLR`, §4): "one study found that underscore is the
best alternative for identifier style while another study found that camel
case is better than underscore."

**Counter-evidence, two independent null results.** Beniamini et al.
(`Beniamini2017SingleLetter`):

> "In addition, controlled experiments with different versions of the same
> functions (specifically, different variable names) failed to show
> significant differences in ability to modify the code. [...] The
> conclusion from all this is that single letter variables can indeed be
> used beneficially in certain cases, leading to more concise code."
> — Abstract

And Scanniello et al. (`Scanniello2017Abbreviated`), the largest study of
the abbreviated-vs-full-word contrast — an original experiment plus three
replications, 100 participants:

> "Overall results suggested that there is no difference in terms of
> effort, effectiveness, and efficiency to fix faults, when source code
> contains either only abbreviated or only full-word identifier names."
> — Abstract (verified at abstract level only)

### (b) Does layout affect comprehension?

**Indentation: the classic result is positive, its replication is null.**
Miara, Musselman, Navarro and Shneiderman (`Miara1983Indentation`) tested
one Pascal program at 0, 2, 4 and 6 spaces on novices and experts:

> "In summary, we conclude that some indentation does aid program
> comprehension.  From our results, we suggest that the optimal level of
> indentation is 2--4 spaces.  No indentation produced significantly lower
> mean scores and the subjects found working with this program difficult."
> — §5 Conclusion

The effect of indentation level on comprehension scores was significant at
p = 0.013 (§4), and 2 spaces, not 4, gave the highest mean score.

Bauer, Siegmund, Peitek, Hofmeister and Apel (`Bauer2019Indentation`) set
out explicitly "to provide empirical evidence for the suggested level of
indentation made by many style guides" and could not reproduce it. With 22
participants, Java snippets and levels 0, 2, 4 and 8:

> "Our results did not show any effect of indentation depth on program
> comprehension, perceived difficulty, or visual effort, indicating that
> indentation is indeed simply a matter of task and style, and do not
> provide support for program comprehension."
> — §8 Conclusion

Correctness: Friedman, chi-square(3) = 3.32, p = 0.36. Response time:
repeated-measures ANOVA, F(3,63) = 0.44, p = 0.72. The same section states
the general problem plainly: "most style guides on code layout, yet there
is little empirical evidence on optimal indentation depth."

**A 2024 randomised trial then found a large effect after all.**
Hanenberg, Morzeck and Gruhn (`Hanenberg2024Indentation`) ran a randomised
controlled trial with 27 participants on generated if-statement tasks,
comparing indented against non-indented code:

> "The experiment (again) confirms a strong (p < .001) and large
> (eta_p^2 = .198, M_Non-Indented / M_Indented = 2.13) effect of
> indentation."
> — Abstract (verified at abstract level only; Springer redirects the
> fetcher to its identity provider despite listing the article as hybrid
> open access)

Non-indented code took 2.13 times as long to read. Two caveats from the
same abstract: the authors note that "although the previous statements
holds true for the whole sample in the experiment, this effect could only
be shown for a subset of individual participants", and they open by saying
that "while this technique has been taught and applied for decades,
evidence for its effectiveness is weak". Note also what this trial varied:
indented against non-indented, not one indentation depth against another.
It therefore supports *indenting* without saying anything about four
spaces.

**The systematic review is the decisive source and it is mixed.** Oliveira,
Santos, Madeiral, Masuhara and Castor (`Oliveira2023FormattingSLR`)
screened the whole literature and found only 15 human-centric studies
directly comparing formatting alternatives, giving 27 comparisons of 13
formatting elements, of which 17 were significant and 10 were not:

> "Finally, for four factors (i.e., formatting layout, vertical and
> horizontal spacing, vertical spacing between related instructions, and
> blank space around operators and parameters), no statistically
> significant results were found for their levels."
> — §4 Results

> "The number of identified papers, some of which are outdated, and the
> many null and contradictory results emphasize the relative lack of work
> in this area and underline the importance of more research.  There is
> much to be understood about how formatting elements influence code
> legibility before the creation of guidelines and automated aids to help
> developers make their code more legible."
> — Abstract, Conclusion

Note which factor is in that null list: *blank space around operators and
parameters* — one of the four PEP 8 rules the deck names. In the same
summary, keeping line lengths within 80 characters is one of only four
factors with a clear best alternative, and indentation is listed among the
factors with divergent results.

**Rule by rule, as readers judge them.** dos Santos and Gerosa
(`SantosGerosa2018Readability`) tested 11 Java practices as matched
snippet pairs and reported a p-value for each (§4.2, Table 1):

| Practice | For | Against | n | p |
|---|---|---|---|---|
| P.4 Line lengths not exceeding 80 chars | 44 | 15 | 59 | 0.0003 |
| P.11 Names using dictionary words | 42 | 12 | 54 | 0.0001 |
| P.5 Indents as 4 spaces | 21 | 29 | 50 | 0.3222 |
| P.3 Blanks separating related instructions | 28 | 28 | 56 | 1.0000 |

The four-space rule is not merely unsupported here: a majority of
respondents preferred the snippet that broke it. The abstract summarises
the whole picture:

> "While some practices promoted an enhancement of readability, others did
> not show statistically significant effects.  Interestingly, one of the
> practices worsened the readability."
> — Abstract

### (c) Does adherence to a convention as such matter?

**One large study says yes, but it measures a model's readability score,
not a human's.** Lee, Lee and In (`Lee2015ConventionViolations`) analysed
210 open-source Java projects against 117 checks from the Sun style guide:

> "It has generally been believed that adherence to coding conventions
> could ensure a good quality of code readability.  However, there were no
> many studies exploring whether this proposition was true or how strongly
> it could be accepted with supporting data. [...] The adherence or
> violation of coding conventions affected the quality of readability of
> post-delivered code (RQ1, Sect. 4.1)."
> — §7 Conclusion

> "violations related to trailing comments, Javadoc, and indentation were
> particularly sensitive ones, so they need to be respected and controlled
> to enhance code readability"
> — §7 Conclusion

The crucial caveat, which I read in §3 of the paper: readability was not
measured on human subjects at all. It was *predicted* with the
Buse–Weimer/Posnett readability model. So this is a correlation between
convention violations and a model's score.

**And the standard-enforcement literature says the evidence is thin.**
Boogerd and Moonen (`BoogerdMoonen2008CodingStandards`) studied MISRA C
2004 on an industrial code base:

> "In spite of the widespread use of coding standards and tools enforcing
> their rules, there is little empirical evidence supporting the intuition
> that they prevent the introduction of faults in software.  Not only can
> compliance with a set of rules having little impact on the number of
> faults be considered wasted effort, but it can actually result in an
> increase in faults, as any modification has a non-zero probability of
> introducing a fault or triggering a previously concealed one."
> — Abstract (verified at abstract level only; the TU Delft green
> open-access record exposes no direct file link and the ResearchGate
> mirror returns HTTP 403)

Their outcome measure is faults, not readability, so this does not settle
the deck's claim. It does settle the weaker one: "a standard exists and is
enforced" is not itself evidence that following it pays.

**A real gap.** Neither the support searches (S10–S12, T5) nor the counter
searches (C4, C9, T7) on any of the six providers turned up a
human-subject study that isolates *consistency with whatever convention
the project uses* from *this particular convention being the better one*.
The rhetorical argument for a shared style — that a reader who knows the
convention reads faster — appears in the introductions of these papers but
was not found tested.

### (d) Is there evidence about PEP 8 itself, and about style in teaching?

**There is exactly one direct study, and it is mixed.** Oliveira, Gheyi,
Costa and Ribeiro (`Oliveira2024PythonStyleGuides`) ran a controlled
eye-tracking experiment with 32 Python novices on four PEP 8 guidelines:

> "We observed that non-adherence to PEP8's proper spacing increases time,
> number of fixations and horizontal regressions.  Moreover, omitting line
> breaks before operators, against PEP8 recommendations, increased
> regressions, validating the importance of these practices for code
> readability.  The analysis of the Multiple Clauses on the Same Line
> pattern showed that following the PEP8 guideline to separate clauses
> onto different lines reduced both the number and duration of fixations,
> enhancing code comprehension due to the clarity provided by this
> separation.  Surprisingly, for the Comparison to True pattern, results
> suggested that direct comparisons with Boolean values (True/False) were
> more effective, indicating that, in certain cases, deviating from PEP8
> recommendations might actually aid in novice programmers' understanding
> of the code."
> — §8 Conclusions

Three of four rules held up, one did not, and the authors close by
recommending "selecting guidelines supported by experimental evaluations"
(§8). Their own framing of the field is blunt:

> "Yet, many guides, including PEP8, lack empirical studies as a
> foundation [31]."
> — §1 Introduction

Note that this study is worth flagging to the author separately: it also
found that PEP 8's *proper spacing* rule did help these novices, which is
in tension with the systematic review's null finding for "blank space
around operators and parameters" in Java. The two used different tasks and
measures.

**And the one paper that looks at PEP 8 as a teaching document says it is
not one.** Kirk, Luxton-Reilly and Tempero (`Kirk2025DistillingPEP8`) set
out to build a Python style primer for introductory courses precisely
because the guide itself will not serve:

> "Professional style guides such as PEP 8 exist, but they are not
> designed for teaching as they contain content that is not suitable for
> introductory programming courses and often present advice without
> explaining why it should be adopted."
> — Abstract (verified at abstract level only; the ACM PDF returns HTTP
> 403 although OpenAlex reports the paper as gold open access)

This is a contribution paper, not an experiment, so it is cited only for
that characterisation of PEP 8, not as evidence about readers. It happens
to endorse the deck's own line — students should know the guide exists and
follow it, not memorise it — and the author may want to read it in full.

**The same group argues that style and quality should not be equated at
all.** Kirk, Luxton-Reilly and Tempero (`Kirk2024StyleNotQuality`):

> "Different sets of style guides contain conflicting advice, have rules
> that do not obviously relate to quality, and specify requirements that
> cannot be objectively confirmed.  Conflating style with quality risks
> students believing that meeting guides will 'improve' their code, when
> in fact it may not, and so they may not appreciate what good quality
> really means."
> — Abstract (verified at abstract level only; ACM returns HTTP 403
> although OpenAlex lists the paper as gold open access)

This is a position paper — its abstract says "Our position is" — so it is
an argument, not evidence. It is worth quoting in the appendix precisely
because it names the trap the deck's own sentence could fall into.

**Teachers do not agree on what a meaningful name is.** van der Werf,
Swidan, Hermans, Specht and Aivaloglou (`vanderWerf2024TeachersNaming`)
interviewed ten teachers of introductory Python courses:

> "Among various opinions and practices, we found that teachers agree on
> using meaningful names, but have conflicting beliefs about what is
> meaningful.  Moreover, the described teaching practices do not always
> match teacher's views on meaningful names, and teachers rarely encourage
> students to use them."
> — Abstract (verified at abstract level only; ACM returns HTTP 403)

> "Naming practices do not seem to be deliberately taught, even though
> they influence program understanding and code quality."
> — Abstract

**The education literature studies tools, not learning outcomes.** Keuning,
Jeuring and Heeren (`Keuning2023CodeQualityMapping`) mapped 195
publications on code quality in education from 1976 to 2022:

> "Its main focus has been on developing and evaluating tools for feedback
> on code smells, and suggestions for improvements and refactorings. [...]
> Another major area is quality analysis of student code."
> — §5 Conclusion

> "The majority of program quality studies employ quantitative,
> descriptive methods, but others take a qualitative approach."
> — §4.2

**And style tooling does not by itself change what students write.** The
same group (`Keuning2017StudentCodeQuality`) analysed 2.6 million code
snapshots from novices in the Blackbox database:

> "We found that students hardly fix issues, in particular issues related
> to modularization, and that the use of tooling does not have much effect
> on the occurrence of issues."
> — Abstract

> "We found that many of the checks PMD can perform are not suitable for
> novice programmers, and may cause confusion with students that might
> result in neglecting the tool.  We advise educators to customize the
> tool by selecting a small set of relevant checks and adjusting threshold
> values."
> — §6 Conclusion

That last sentence is the practical lesson for the course: if a style
checker is used, point it at a small chosen set of rules rather than at
everything `pycodestyle` can complain about.

### (e) The counter side, and how it was found

The counter-queries C1–C10 and T7–T8 used every concept term of the
support queries plus the negative vocabulary ("no significant difference",
"no effect", "null result", "replication", "criticism", "limitations",
"lack of evidence", "does not improve", "inconclusive", "negative
results", "contrary"). Run on all six providers, they returned 728 hits (of 2773 in total),
and almost all of them were false matches: the phrase "no effect" is not
how this field titles or abstracts its null results.

The substantive counter-evidence came instead from the *same topical
searches as the support side*, because in this literature the null results
are inside papers with neutral or positive-sounding titles: Bauer et al.'s
failed replication is titled as a question, Beniamini et al.'s null result
sits inside a paper about single-letter variables, and Scanniello et al.'s
four experiments are titled after the task, not the outcome. This is worth
stating in the appendix as a methodological observation: a counter-search
by negative vocabulary is close to useless here, and the two-sidedness had
to come from reading the topical hits.


---

## 5. Discussion and limitations

**What the evidence does not cover.**

1. **PEP 8 itself is nearly untested.** One study, `Oliveira2024PythonStyleGuides`,
   tests four of its rules on 32 novices. Nothing else in 2773 hits across
   six databases tests PEP 8 empirically; the only other PEP 8 paper found,
   `Kirk2025DistillingPEP8`, adapts the guide for teaching rather than
   testing it. The style guide's own justifications are, as both papers
   say, not backed by studies.
2. **The evidence is rule by rule, not guide by guide.** No study tests
   "following a style guide" as a package against "not following one".
   Every result is about one formatting element or one naming contrast at
   a time, and the results point in different directions for different
   elements. The closest thing to a package-level test,
   `BoogerdMoonen2008CodingStandards`, measures faults rather than
   readability, and its headline is that the evidence is thin.
3. **Consistency as such is untested.** The strongest argument in the
   deck's prose — that a shared convention helps because the reader knows
   what to expect — was not found tested against a control in either
   direction. `Lee2015ConventionViolations` comes closest but predicts
   readability with a model instead of measuring it on people.
4. **Almost none of it is Python.** Miara et al. used Pascal; Bauer et al.,
   Schankin et al., dos Santos and Gerosa, Lee et al. and Keuning et al.
   used Java; Scanniello et al. used C and Java. Only
   `Oliveira2024PythonStyleGuides` used Python.
5. **Almost none of it is beginners.** Where experience was analysed, the
   effect often depended on it, and not always in the direction a course
   would want: Schankin et al. found the naming effect only in
   *experienced* developers, while Sharif and Maletic found novices
   benefited *more* from the underscore style. `Oliveira2024PythonStyleGuides`
   and `Keuning2017StudentCodeQuality` are the only novice studies here.
6. **The indentation evidence has swung three times.** Positive in 1983 on
   one Pascal program, null in the 2019 replication on short Java
   snippets, and strongly positive in the 2024 randomised trial on
   generated if-statements. What the 2024 trial supports is *indenting at
   all*; no study since 1983 has found a defensible answer for *how deep*,
   and the two that asked (Miara et al., Bauer et al.) point at 2 spaces
   and at nothing respectively.
7. **The measures differ, so the studies are not directly comparable.**
   Time to find a defect, eye-fixation counts, correctness scores,
   preference votes and a model-predicted readability score are five
   different things, and a rule can win on one and lose on another. The
   clearest case is spacing around operators: null in the review's Java
   comparisons, positive in the Python eye-tracking study.
8. **Search coverage.** Semantic Scholar was down (HTTP 403) for the whole
   session; IEEE Xplore's quota ran out before the eight short queries;
   DBLP's title-only, operator-stripping search contributed almost
   nothing; and 589 of the 1858 unique records had no abstract for the
   classifier to read, because enrichment could only use arXiv and WoS
   (Semantic Scholar's key is rejected, IEEE's quota was spent, and
   OpenAlex was left unused to stay inside its daily budget). Results are
   capped at 25 per query per provider, so a cell showing 25 means "25 or
   more" and deeper hits were not screened.
9. **Grey literature and books were not searched.** Style guides
   themselves, Kernighan and Pike, Martin's *Clean Code* and the like are
   normative sources, not evidence, and were deliberately excluded.

**What is solid despite all of that.** Four findings survived
counter-search: names have a large effect on comprehension, provided they
are accurate (`Schankin2018Names`, `Avidan2017VariableNames`); indenting
code beats not indenting it (`Miara1983Indentation`,
`Hanenberg2024Indentation`); lines within 80 characters are judged more
readable (`SantosGerosa2018Readability`, `Oliveira2023FormattingSLR`); and
separating clauses onto their own lines helps Python novices
(`Oliveira2024PythonStyleGuides`). Two of the deck's four named PEP 8
rules did *not* survive as stated: **four spaces specifically** (the
depth, as opposed to indenting at all) is contradicted by a preference
survey and unsupported by the replication, and **spaces around operators**
sits in the systematic review's explicit null list, although the Python
eye-tracking study found PEP 8's spacing helped its novices.

---

## 6. Conclusion

**The honest answer to the author's question: the general principle is
supported — names that carry meaning, code that is indented, lines that
are short all measurably help the reader — but the specific numbers PEP 8
prescribes are not, PEP 8 as a document has almost no empirical foundation
of its own, and at least two of the four rules the deck names as examples
are either contested or backed by nothing.**

Skipping the guide entirely is not what the evidence recommends either.
Nothing found in either direction supports "style does not matter"; what
the evidence shows is that the *size and even the existence* of the effect
varies rule by rule, that it is often smaller than practitioners assume,
and that in at least two documented cases (four-space indentation as
judged by developers, and `== True` comparisons as read by Python novices)
the rule was worse than its violation. The best-evidenced reason to teach
a style guide is not that each rule is proven but that names carry meaning
to the reader, indented code is faster to read, and short lines are easier
to scan.

Three practical points the appendix can carry, each cited: give names that
are *accurate*, not merely long, because a misleading name is worse than a
single letter (`Avidan2017VariableNames`); if a style checker is pointed at
students, point it at a small chosen set of rules, because tooling by
itself does not change what novices write (`Keuning2017StudentCodeQuality`);
and do not let "follows PEP 8" stand in for "is good code", which is
exactly the confusion `Kirk2024StyleNotQuality` warns about.

**The one sentence to paste:** *Att koden skrivs för en läsare --- namn
som stämmer, indrag och korta rader --- har vetenskapligt stöd; att just
PEP 8:s siffror skulle vara de rätta har det inte, och för fyra blanksteg
och mellanslag runt operatorer är underlaget svagt eller motsägelsefullt.*

**And the honest strength of the claim, in one sentence:** "consistent,
readable code helps the reader" is supported by controlled experiments,
while "PEP 8 specifically" is supported by a single study of four of its
rules, one of which came out against the guide.

---

## 7. Dropped sources

Not cited anywhere, because they could not be verified. Ordered
load-bearing first; the first two would materially strengthen the
chapter if the author can get them through the KTH library.

1. **Binkley, Davis, Lawrie, Maletic, Morrell and Sharif (2013), "The
   impact of identifier style on effort and comprehension", *Empirical
   Software Engineering* 18(2), DOI `10.1007/s10664-012-9201-4`.** This is
   the study that contradicts Sharif and Maletic on camelCase vs
   snake_case, so the appendix currently reports it second-hand through
   `Oliveira2023FormattingSLR`. Paywalled; `fetch_pdf.py` found no
   open-access copy; neither Crossref nor OpenAlex holds an abstract.
2. **Hofmeister, Siegmund and Holt (2017/2019), "Shorter identifier names
   take longer to comprehend", SANER 2017 / *EMSE* 24, DOI
   `10.1109/SANER.2017.7884623` and `10.1007/s10664-018-9621-x`.** The
   companion result to Schankin et al., with 72 professional C#
   developers; it would corroborate the naming finding in a second
   population. Paywalled on both IEEE and Springer; the Springer page
   redirects to an identity provider; no abstract in Crossref or OpenAlex.
3. **Ribeiro and Travassos (2018), "Attributes Influencing the Reading and
   Comprehension of Source Code – Discussing Contradictory Evidence",
   *CLEI Electronic Journal* 21(1), DOI `10.19153/cleiej.21.1.5`, and its
   journal extension (2023), "On the Investigation of Empirical
   Contradictions", *EMSE*, DOI `10.1007/s10664-023-10360-5`.** These are
   directly about the contradictions this chapter documents, and the
   landing page (read with WebFetch) says the study found four-space
   indentation dominated reader preference — which would qualify the dos
   Santos and Gerosa result. The CLEI journal is open access but its OJS
   server returns HTTP 406 to both `fetch_pdf.py` and WebFetch for the
   PDF; the EMSE extension is paywalled. **The most worthwhile one to
   chase.**
4. **Lawrie, Morrell, Feild and Binkley (2006/2007), "What's in a Name? A
   Study of Identifiers" (ICPC, DOI `10.1109/ICPC.2006.51`) and "Effective
   identifier names for comprehension and memory" (*ISSE* 3, DOI
   `10.1007/s11334-007-0031-2`).** The earliest controlled work on
   full words vs abbreviations vs single letters. Paywalled, no
   open-access copy found.
5. **Sharafi, Soh, Guéhéneuc and Antoniol (2012), "Women and men —
   Different but equal: On the impact of identifier style on source code
   reading", ICPC, DOI `10.1109/ICPC.2012.6240505`.** A third data point
   on the camelCase/snake_case contrast. Surfaced in the session but not
   fetched.
6. **Prause and Jarke (2015), "Gamification for Enforcing Coding
   Conventions", ESEC/FSE, DOI `10.1145/2786805.2786806`; Chen, Chen and
   Lee (2018), "An Automated Assessment System for Analysis of Coding
   Convention Violations in Java Programming Assignments", DOI
   `10.6688/JISE.201809_34(5).0006`.** Both about enforcing conventions
   rather than about whether they help the reader; not fetched.
7. **Saliba, Shioji, Oliveira, Cohney and Qi (2024), "Learning with
   Style: Improving Student Code-Style Through Better Automated Feedback",
   SIGCSE, DOI `10.1145/3626252.3630889`.** The nearest thing found to a
   classroom intervention study measuring whether style feedback improves
   student style. Closed access; no open-access copy found. **Worth
   chasing second, after the contradictions paper**, because it is the
   study that could fill sub-question (d)'s biggest gap.
8. **"Human vs. Automated Coding Style Grading in Computing Education"
   (ASEE 2020, DOI `10.18260/1-2--32906`) and "Teaching Students to
   Recognize and Implement Good Coding Style" (L@S 2017, DOI
   `10.1145/3051457.3051469`).** Two more classroom studies on style.
   Both paywalled; `fetch_pdf.py` found no open-access copy for either.
9. **Three papers whose PDFs are listed as open access but whose
   publishers refuse the fetcher, and which are therefore cited at
   abstract level rather than dropped:** `Kirk2025DistillingPEP8`,
   `Kirk2024StyleNotQuality` and `vanderWerf2024TeachersNaming` (ACM
   returns HTTP 403 to all clients tried), and `Hanenberg2024Indentation`
   (Springer redirects to `idp.springer.com`). If the author can open
   these through KTH, the Hanenberg trial in particular deserves a full
   read: it is the strongest indentation result in the chapter and the
   appendix currently quotes only its abstract.

---

## 8. Search protocol: every non-`scholar` query, verbatim

All on 2026-09-06. `fetch_pdf.py` is
`~/.claude/skills/backing-claims/scripts/fetch_pdf.py`, which fetches into
scholar's PDF cache.

### WebSearch

| # | Query | Outcome |
|---|---|---|
| W1 | `"An Eye Tracking Study on camelCase and under_score Identifier Styles" Sharif Maletic pdf` | Retained. Gave the author's copy at `cs.kent.edu/~jmaletic`, fetched with `fetch_pdf.py`. |
| W2 | `Miara Musselman Navarro Shneiderman "Program indentation and comprehensibility" 1983 CACM pdf` | Retained, twice over. Gave the copy at `cs.umd.edu/~ben` (ACM's own PDF returns HTTP 403) **and** surfaced Bauer et al.'s open copy at `infosun.fim.uni-passau.de`. |
| W3 | `"Who is right? Evaluating empirical contradictions in the readability and comprehensibility of source code" pdf` | Not retained. Identified the CLEI and EMSE versions; neither could be fetched (see dropped source 3). |
| W4 | `Scanniello "Fixing Faults in C and Java Source Code" "Abbreviated vs. Full-Word Identifier Names" TOSEM pdf` | Abstract level only. No open-access full text; the CORE mirror returns HTTP 403. |
| W5 | `"Impacts of Coding Practices on Readability" dos Santos Gerosa ICPC 2018 pdf preprint` | Retained, three times over. Gave the authors' copy at `ime.usp.br/~gerosa`, **and** surfaced both the formatting systematic review and the Python style-guide eye-tracking study. |
| W6 | `"systematic literature review on the impact of formatting elements on code legibility" arxiv preprint pdf` | Retained. Gave arXiv:2208.12141, the accepted version of the JSS article. |
| W7 | `Hofmeister Siegmund Holt "Shorter identifier names take longer to comprehend" SANER 2017 pdf` | Not retained. Paywalled on IEEE and Springer (dropped source 2). |
| W8 | `Beniamini Gingerich Gutstein Feitelson "Meaningful Identifier Names: The Case of Single-Letter Variables" pdf cs.huji.ac.il` | Retained. Gave the author's copy at `cs.huji.ac.il/w~feit`. |
| W9 | `Schankin Berger Holt Hofmeister Riedel "Descriptive compound identifier names improve source code comprehension" pdf` | Retained. Gave the group's copy at `brains-on-code.github.io`. |
| W10 | `"A Systematic Mapping Study of Code Quality in Education" ITiCSE 2023 pdf open access` | Retained. Gave arXiv:2304.13451. |
| W11 | `Keuning Jeuring Heeren "Code Quality Issues in Student Programs" ITiCSE 2017 pdf` | Retained. Gave Utrecht technical report UU-CS-2017-006, which contains the ITiCSE camera-ready. |
| W12 | `Kirk Luxton-Reilly Tempero "Distilling PEP 8 for Teaching Introductory Programming" ACE 2025 pdf` | Not retained in full. Confirmed the paper and its authors; no copy outside ACM. |
| W13 | `"Distilling PEP 8" Kirk Tempero abstract "Code Style Model" ACE 2025 researchgate` | Not retained in full. Same outcome; the abstract came from OpenAlex instead. |
| W14 | `"Indentation and reading time" "randomized control trial" indented non-indented if-statements Hanenberg pdf` | Not retained in full. Identified authors and venue; Springer blocks the fetcher. |
| W15 | `Avidan Feitelson "Effects of Variable Names on Comprehension" ICPC 2017 pdf cs.huji.ac.il` | Retained via a follow-up fetch of the author's publication list (F6 below). |
| W16 | `Boogerd Moonen "Assessing the value of coding standards" MISRA preprint pdf swerl tudelft TUD-SERG` | Not retained in full. Found the ResearchGate mirror, which returns HTTP 403. |

### WebFetch

| # | URL | Purpose and outcome |
|---|---|---|
| F1 | `https://www.clei.org/cleiej/index.php/cleiej/article/view/82` | Metadata and abstract for Ribeiro and Travassos 2018. Landing page read; the PDF at `.../82/35` and `.../download/82/35` returns HTTP 406 to `fetch_pdf.py`. Not cited. |
| F2 | `https://zenodo.org/record/1202282` | Semantic Scholar pointed here as the "PDF" for dos Santos and Gerosa. The record holds only the dataset zip, not the paper. |
| F3 | `https://core.ac.uk/outputs/141689346/` | Attempt at Scanniello et al. full text. HTTP 403. |
| F4 | `https://link.springer.com/article/10.1007/s10664-018-9621-x` | Attempt at the Hofmeister et al. abstract. HTTP 303 to `idp.springer.com`; not followed. |
| F5 | `https://www.cs.huji.ac.il/w~feit/papers/SingleLetter17ICPC.pdf` | Retrieved the Beniamini et al. PDF. The server sends `Content-Type: text/html` for it, so `fetch_pdf.py` refused it; WebFetch saved the file and it was read with `pdftotext -layout`. |
| F6 | `https://www.cs.huji.ac.il/w~feit/pub.html` | Read the author's publication list to get the file name for the Avidan and Feitelson 2017 paper. |
| F7 | `https://www.cs.huji.ac.il/w~feit/papers/Names17ICPC.pdf` | Retrieved the Avidan and Feitelson 2017 PDF, same Content-Type problem, same workaround. |
| F8 | `https://www.cs.auckland.ac.nz/~andrew/publications.html` | Checked for an author copy of the two ACE papers. The list gives DOIs only. |
| F9 | `https://dl.acm.org/doi/10.1145/3716640.3716644` | HTTP 403. |
| F10 | `https://link.springer.com/content/pdf/10.1007/s10664-024-10531-y.pdf` and `https://link.springer.com/article/10.1007/s10664-024-10531-y` | Both HTTP 303 to `idp.springer.com`; not followed. |
| F11 | `http://resolver.tudelft.nl/uuid:646de5ba-eee8-4ec8-8bbc-2c188e1847ea` then `https://repository.tudelft.nl/record/uuid:646de5ba-...` | Read the TU Delft record for Boogerd and Moonen and confirmed its abstract verbatim against OpenAlex. The record exposes no direct file link. |

### curl against Crossref and OpenAlex

| # | Command | Purpose |
|---|---|---|
| R1 | `curl -s "https://api.crossref.org/works?query.bibliographic=systematic+literature+review+impact+of+formatting+elements+on+code+legibility&rows=3"` | Resolve the formatting review's DOI. |
| R2 | `curl -s "https://api.crossref.org/works?query.bibliographic=Assessing+Python+Style+Guides+An+Eye-Tracking+Study+with+Novice+Developers&rows=3"` | Resolve the SBES 2024 paper's DOI (`10.5753/sbes.2024.3325`). |
| R3 | `curl -s "https://api.openalex.org/works/doi:<doi>"` for `10.1007/s10664-012-9201-4`, `10.1145/3104029`, `10.1109/ICPC.2017.18`, `10.1007/s11334-007-0031-2`, `10.1587/transinf.2014edp7327`, `10.1007/s10664-018-9621-x` | Look for open-access locations and abstracts. Found the J-STAGE open PDF for Lee et al. and the publisher's abstract for Scanniello et al.; the rest have neither. |
| R4 | `curl -s "https://api.openalex.org/works/doi:<doi>"` for `10.1145/3716640.3716644`, `10.1007/s10664-024-10531-y`, `10.1145/3649165.3703621`, `10.1145/3639474.3640069`, `10.1109/icsm.2008.4658076`, `10.1109/ICPC.2017.27` | Read the publisher's abstracts for the six sources whose full texts the publishers refuse. |
| R5 | `curl -s "https://api.crossref.org/works/<doi>"` for all eighteen cited DOIs | Confirm authors, year, volume, issue and pages for the bib entries. |

### Other tools

`~/.claude/skills/backing-claims/scripts/fetch_pdf.py --text <url-or-doi>`
was used for every full text; nothing was fetched with a bare `curl` into a
scratch directory. `scholar pdf quote` was not used; the supporting passages
were located by `grep` over the `pdftotext -layout` extractions in scholar's
cache and read in context. alphaXiv was not used.

---

## 9. Export command, bib keys and files

**Export command actually run:**

```
D=modules/variables/slides/litteratursokning

scholar sessions export variables-pep8 -f table --bearing-only \
  --lang sv --label sok-pep8 --track "PEP 8 och kodstil" \
  --theme "namngivning=namn på variabler och andra identifierare" \
  --theme "layout=layout och formatering" \
  --theme "konvention=att följa en konvention" \
  --theme "pep8=PEP 8 och undervisning" \
  -o "$D/pep8-stil"

scholar sessions export variables-pep8 -f csv -o "$D/pep8-stil"
```

`-f table` writes `pep8-stil.tex`; that file was then post-processed into
`pep8-stil-full.tex` (the name this deck's appendices `\input`) by
stripping scholar's banner comment, renaming the third column heading from
"Leverantör" to "Databas", and wrapping "open access" in
`\foreignlanguage{english}{...}`, so the fragment matches
`modules/helloworld/slides/litteratursokning/sprakhistoria-full.tex`
exactly. The intermediate `pep8-stil.tex` was removed.

`--label sok-pep8` produces `\label{tab:sok-pep8}`, which is the label the
appendix chapter's `\cref` uses. Note that scholar prepends `tab:` itself,
so passing `--label tab:sok-pep8` would yield `\label{tab:tab:sok-pep8}`.

The resulting caption reads: "Träffar som rör påståendet, PEP 8 och
kodstil (18 citerade, 83 som stöder påståendet och 70 som kvalificerar
eller motsäger det, av 1824 unika träffar; de 631 angränsande och 1022
felträffarna listas inte)."

**Before it compiles, the appendix preamble must have `longtable`,
`booktabs` and `array` loaded** (the deck's `didactic` preamble already
does), and the chapter must `\input` the fragment after its Slutsats,
following the helloworld pattern.

**Files written:**

- `modules/variables/slides/litteratursokning/pep8-stil.csv`
- `modules/variables/slides/litteratursokning/pep8-stil-full.tex`
- `/tmp/claude-1000/fix-variables-r3/pep8-stil.bib` (the new entries, for
  you to merge into `ltnotes.bib`)

**Bib keys** (none collides with the deck's existing keys):

| Key | Role |
|---|---|
| `Schankin2018Names` | (a) supports: descriptive names, 14% faster, experienced only |
| `Avidan2017VariableNames` | (a) supports and qualifies: names matter, but wrong names beat none |
| `SantosGerosa2018Readability` | (a) supports naming and line length; (b) null for four-space indent |
| `SharifMaletic2010CamelCase` | (a) qualifies: snake_case faster than camelCase, accuracy null |
| `Beniamini2017SingleLetter` | (a) counter: name changes gave no significant difference |
| `Scanniello2017Abbreviated` | (a) counter: abbreviated vs full-word null, 100 participants |
| `Miara1983Indentation` | (b) supports: indentation aids comprehension, 2–4 spaces |
| `Hanenberg2024Indentation` | (b) supports: RCT, non-indented code 2.13x slower (abstract level) |
| `Bauer2019Indentation` | (b) counter: failed replication, no effect |
| `Oliveira2023FormattingSLR` | (b) survey: mixed; operator spacing null, ≤80 chars positive |
| `Lee2015ConventionViolations` | (c) supports, but readability is model-predicted |
| `BoogerdMoonen2008CodingStandards` | (c) counter: little evidence standards prevent faults (abstract level) |
| `Oliveira2024PythonStyleGuides` | (d) the only direct PEP 8 study; three rules held, one did not |
| `Kirk2025DistillingPEP8` | (d) PEP 8 is not designed for teaching (abstract level) |
| `Kirk2024StyleNotQuality` | (d) counter, position paper: style is not quality (abstract level) |
| `vanderWerf2024TeachersNaming` | (d) Python teachers disagree on "meaningful" (abstract level) |
| `Keuning2023CodeQualityMapping` | (d) the education field is tools and description, not outcomes |
| `Keuning2017StudentCodeQuality` | (d) counter: style tooling barely changes novice code |

**Validation:**

```
$ check_provenance.py /tmp/claude-1000/fix-variables-r3/pep8-stil.bib
============================================================
  /tmp/claude-1000/fix-variables-r3/pep8-stil.bib  (18 entries)
============================================================

  All entries carry complete provenance.

  Result: OK

$ check_metadata.py /tmp/claude-1000/fix-variables-r3/pep8-stil.bib
checked 18 DOI entries across 1 files

no DOI (verify against ground truth by hand):

0 problems:
```

**Author-only note for the appendix's `%` comment block:**

```
% Session: variables-pep8 (scholar), 2026-09-06.
% Providers: OpenAlex, DBLP, IEEE Xplore, arXiv, Web of Science, Scopus.
%   Semantic Scholar unavailable (HTTP 403) the whole session; IEEE
%   Xplore's daily quota was exhausted before queries T1-T8, so those
%   eight IEEE cells are zero for quota reasons; DBLP searches titles
%   only and strips boolean operators.
% 34 queries x 6 providers = 204 cells; 2773 hits, 1858 unique records
%   (1824 after the export's own de-duplication).
% Classification: scholar llm classify --no-examples, model
%   github_copilot/gpt-5.4, whole session; the 18 cited rows and one
%   override were then decided by hand.
% Export: see the command in the report.
% Bib keys: Schankin2018Names, SantosGerosa2018Readability,
%   SharifMaletic2010CamelCase, Beniamini2017SingleLetter,
%   Scanniello2017Abbreviated, Miara1983Indentation, Bauer2019Indentation,
%   Oliveira2023FormattingSLR, Lee2015ConventionViolations,
%   Avidan2017VariableNames, Hanenberg2024Indentation,
%   BoogerdMoonen2008CodingStandards, Oliveira2024PythonStyleGuides,
%   Kirk2025DistillingPEP8, Kirk2024StyleNotQuality,
%   vanderWerf2024TeachersNaming, Keuning2023CodeQualityMapping,
%   Keuning2017StudentCodeQuality.
```
