# Learning Objectives & Variation Theory Review

Date: 2025-11-11
Section: Shopping List Item Representation (lines 107-313)

---

## Executive Summary

All didactic notes now explicitly document learning objectives and show how variation patterns support achieving those objectives. This creates a clear pedagogical chain: objectives → variation patterns → activities → assessment.

---

## Learning Objectives Documented

### Section: "Att representera varor: Uppslagslistor eller klass?"

**Three learning objectives identified** (lines 113-121):

1. **LO1**: Students should discern when to use dictionaries vs classes for data representation
2. **LO2**: Students should identify the trade-off between flexibility/simplicity and structure/safety
3. **LO3**: Students should be able to justify their design choice based on context (program size, complexity, team size)

---

## Mapping: Objectives → Variation → Activities

### Opening Note (lines 112-138)

**Objectives stated**: All three LOs listed at top of section

**Pedagogical strategy**:
- Contrast pattern (variation theory)
- Try-first pedagogy

**Connection to objectives**:
- Contrast pattern supports LO1 and LO2 (by making differences visible)
- Try-first question activates thinking about trade-offs (supports LO3)

**Structure**:
```latex
\ltnote{%
  \textbf{Learning Objectives:}
  [Enumerated list of 3 objectives]

  \textbf{Pedagogical Strategy:}
  [Description of approach]

  \textbf{Connection to Learning Objectives:}
  [How strategy supports which objectives]
}
```

### Comparison Note (lines 225-261)

**Objectives addressed**: LO1, LO2, LO3

**Variation pattern analysis**:
- What varies: Implementation approach (dict vs class)
- What remains invariant: Functionality and information
- Critical aspects to discern: Explicitly mapped to each LO

**Mapping structure**:
```latex
\ltnote{%
  \textbf{Relation to Learning Objectives:}

  This comparison directly addresses:
  - LO1: pros/cons provide concrete criteria
  - LO2: contrast makes trade-off visible

  \textbf{Variation Pattern: Contrast}
  [Standard variation theory documentation]

  \textbf{Critical aspects to discern (mapped to LOs):}
  1. Trade-off structure (LO2)
  2. Criteria for choosing (LO1)
  3. Context matters (LO3)

  \textbf{Why this variation works:}
  [Explanation connecting Marton's theory to objectives]
}
```

**Key insight documented**: "Without this contrast, students might think 'classes are always better' or 'use whatever is easiest.' The side-by-side comparison forces attention to the nuanced trade-offs that govern real design decisions."

### Reflection Note (lines 273-303)

**Objective addressed**: Primarily LO3 (justify design choice based on context)

**Mechanism**: Three guiding questions operationalize the abstract trade-off into concrete decision criteria:

| Question | Maps to | Reasoning |
|----------|---------|-----------|
| "Hur ofta används...?" | Maintenance burden | More usage → higher value of structure |
| "Behövs metoder...?" | Behavior vs data | Need for methods → classes appropriate |
| "Kommer den växa?" | Future complexity | Expected growth → classes handle change better |

**Assessment opportunity documented**: "Listen for students mentioning contextual factors (not just 'classes are better'). If they say 'always use classes' or 'always use dicts,' probe with counter-examples..."

---

## Pedagogical Chain

The section now demonstrates a complete pedagogical chain:

```
Learning Objectives (stated)
    ↓
Variation Pattern (contrast)
    ↓ (supports objectives by making differences visible)
Activities (exercises, comparisons)
    ↓ (students engage with contrasts)
Critical Aspects Discerned
    ↓ (students achieve objectives)
Assessment (documented probes)
```

Each link is explicitly documented in `\ltnote` commands.

---

## Variation Theory Principle Applied

**Marton's Core Principle**: "To learn something, the learner must discern what is to be learned. Discerning the object of learning amounts to discerning its critical aspects." (Marton & Pang, 2006)

**Our Application**:

1. **Object of learning**: When to use dictionaries vs classes
2. **Critical aspects** (explicitly listed in notes):
   - Trade-off structure (flexibility/simplicity ↔ structure/safety)
   - Decision criteria (error detection, IDE support, extensibility, effort)
   - Context-dependence (no universal "better" choice)
3. **Variation pattern**: Contrast (implementation varies, functionality invariant)
4. **Result**: Critical aspects become discernible through comparison

**Connection to objectives**: Each critical aspect maps to a specific learning objective, ensuring the variation serves the learning goals.

---

## Comparison: Before vs After

### Before (No Explicit Objectives)

```latex
\ltnote{%
  Vi introducerar här en viktig designfråga...
  Detta följer variation theory's contrast pattern...
}
```

**Missing**:
- What should students learn?
- How does the variation support specific learning goals?
- What critical aspects map to which objectives?

### After (Objectives-Centered)

```latex
\ltnote{%
  \textbf{Learning Objectives:}
  1. Students should discern when to use dicts vs classes
  2. Students should identify the trade-off...
  3. Students should justify their choice...

  \textbf{Pedagogical Strategy:}
  [How we teach]

  \textbf{Connection to Learning Objectives:}
  Contrast pattern supports LO1 and LO2 by...
}
```

**Improvement**:
- Clear learning goals stated upfront
- Explicit mapping: pattern → objectives
- Rationale for each design choice
- Assessment guidance provided

---

## Benefits of This Approach

### For Instructors

1. **Clear targets**: Know exactly what students should achieve
2. **Justified methods**: Understand why each activity is included
3. **Assessment guidance**: Know what to listen for and probe
4. **Adaptation ease**: Can modify while maintaining pedagogical integrity

### For Course Design

1. **Alignment**: Activities clearly support stated objectives
2. **Coherence**: Variation patterns serve learning goals, not just theoretical frameworks
3. **Assessment**: Clear criteria for evaluating student learning
4. **Research**: Can study effectiveness of specific pattern-objective pairings

### For Learning Science

1. **Testable**: Can empirically verify if variation achieves objectives
2. **Replicable**: Other instructors can implement with same rationale
3. **Improvable**: Clear metrics for what success looks like
4. **Theoretical**: Connects variation theory to concrete learning outcomes

---

## Skill Integration Update

### didactic-notes Skill Enhanced

Added section: "CRITICAL: Connect to Learning Objectives"

**New guidance**:
1. State learning objectives explicitly at section beginning
2. Map variation patterns to objectives (show HOW variation helps)
3. Explain why the variation works (connect theory to objectives)

**Template provided**:
```latex
\ltnote{%
  \textbf{Learning Objectives:}
  [Enumerated list]

  \textbf{Relation to Learning Objectives:}
  This [pattern] addresses:
  - LO1: by varying [X]...
  - LO2: by making [Y] visible...

  \textbf{Variation Pattern: [Name]}
  [Standard documentation]

  \textbf{Critical aspects to discern (mapped to LOs)}:
  [Explicit mapping]
}
```

---

## Example: Complete Note with Objectives

From lines 225-261 (comparison note):

```latex
\ltnote{%
  \textbf{Relation to Learning Objectives:}

  This comparison directly addresses:
  \begin{itemize}
    \item \textbf{LO1} (when to use dicts vs classes): The pros/cons list
      provides concrete criteria for decision-making
    \item \textbf{LO2} (identify trade-offs): The contrast makes the
      flexibility/simplicity vs structure/safety trade-off explicit and visible
  \end{itemize}

  \textbf{Variation Pattern: Contrast}

  \textbf{Vad varierar:} Hur vi representerar varor (uppslagslista vs klass)

  \textbf{Vad förblir invariant:} Vilken information vi lagrar (namn och
  avbockningsstatus) och vilken funktionalitet vi behöver

  \textbf{Critical aspects students should discern (mapped to LOs):}
  \begin{enumerate}
    \item The trade-off structure: flexibility/simplicity vs structure/safety
      (LO2)
    \item Criteria for choosing: error detection timing, IDE support,
      extensibility, initial effort (LO1)
    \item No universally "better" choice---context matters (LO3)
  \end{enumerate}

  \textbf{Why this variation works:} Following Marton \& Pang (2006), we vary
  implementation approach while keeping functionality invariant. This makes
  the critical distinguishing features (the trade-offs) discernible because
  students can see EXACTLY what changes when switching representations while
  everything else stays the same.

  Without this contrast, students might think "classes are always better" or
  "use whatever is easiest." The side-by-side comparison forces attention to
  the nuanced trade-offs that govern real design decisions.
}
```

**This note demonstrates**:
- ✅ Learning objectives explicitly referenced
- ✅ Variation pattern documented
- ✅ Clear mapping: pattern elements → objectives
- ✅ Rationale for why variation works
- ✅ What happens without this pedagogical choice

---

## Assessment Implications

With objectives explicit, we can now assess:

1. **Did students achieve LO1?**
   - Can they articulate when each approach is appropriate?
   - Assessment: Listen for contextual reasoning in discussions

2. **Did students achieve LO2?**
   - Can they identify and explain the trade-off structure?
   - Assessment: Check if they mention both sides (not just "classes are better")

3. **Did students achieve LO3?**
   - Can they justify a design choice with contextual factors?
   - Assessment: Probe with edge cases; see if they consider program size, complexity, etc.

**Documented in notes**: Specific probes to use if students show absolutist thinking

---

## Compilation Status

✅ **notes.pdf**: Compiles successfully (91443 bytes, 14 pages)
✅ **All `\ltnote` commands** parse correctly
✅ **Learning objectives** render properly in margins

---

## Recommendation: Apply Pattern Everywhere

This objectives-centered approach should be applied to:

1. **All sections of slides-even-more**
   - Banking system section
   - Design principles section
   - Summary sections

2. **Other course materials**
   - slides/ (basic introduction)
   - slides-more/ (fractions)

3. **Future materials**
   - Use as template for new content

**Template checklist for each section**:
- [ ] Learning objectives stated explicitly
- [ ] Variation pattern documented
- [ ] Mapping: pattern → objectives
- [ ] Critical aspects identified
- [ ] Why the variation works explained
- [ ] Assessment guidance provided

---

## Theoretical Grounding

This approach aligns with:

1. **Constructive alignment** (Biggs & Tang, 2011): Learning objectives, teaching activities, and assessment all aligned

2. **Variation theory** (Marton & Pang, 2006): Critical aspects made discernible through patterns of variation

3. **Backward design** (Wiggins & McTighe, 2005): Start with objectives, design activities to achieve them

The integration is coherent and research-based.

---

## Conclusion

The section now demonstrates exemplary practice in educational design:

- **Clear objectives**: Students and instructors know the learning goals
- **Theory-grounded**: Variation patterns serve explicit pedagogical purposes
- **Assessable**: Clear criteria for evaluating success
- **Documented**: Future instructors can understand and adapt
- **Aligned**: Activities support objectives, assessment measures objectives

This is literate pedagogy at its best: making pedagogical reasoning explicit, connecting theory to practice, and providing guidance for effective teaching and continuous improvement.
