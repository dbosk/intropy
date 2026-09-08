# csquotes Package Usage Review

Date: 2025-11-11
Reviewer: Claude (with latex-writing skill)

---

## Summary

Updated all manual quotation marks to use the `\enquote{...}` command from the csquotes package, following LaTeX semantic markup best practices.

---

## Changes Made

### 1. Updated latex-writing Skill

Added new section: **Quotations (csquotes package)**

**Key principles**:
- Always use `\enquote{...}` for quotes, never manual quote marks
- Handles nested quotes automatically
- Language-aware (adapts to Swedish vs English)
- For block quotes, use `\begin{displayquote}...\end{displayquote}`

**Anti-patterns documented**:
```latex
% INCORRECT
"This is a quote"
``This is a quote''
'single quotes'
```

**Correct usage**:
```latex
% CORRECT
\enquote{This is a quote}
\enquote{outer \enquote{inner} quote}
```

**Added to checklist**: Manual quotes check

---

## Quotes Fixed in contents.tex

### Line 249
**Before**: `Inget universellt "bättre" val`
**After**: `Inget universellt \enquote{bättre} val`

### Lines 258-259
**Before**:
```latex
kan studenter tänka att "klasser är alltid bättre" eller
"använd det som är enklast".
```
**After**:
```latex
kan studenter tänka att \enquote{klasser är alltid bättre} eller
\enquote{använd det som är enklast}.
```

### Line 283
**Before**: `Kopplar till "beteende vs data"-distinktionen`
**After**: `Kopplar till \enquote{beteende vs data}-distinktionen`

### Lines 300-303
**Before**:
```latex
faktorer (inte bara "klasser är bättre"). Om de säger "använd alltid klasser"
eller "använd alltid uppslagslistor", undersök med motexempel: "Vad sägs om
konfigurationsdata från JSON?" eller "Vad sägs om ett komplext
användarprofilsystem?"
```

**After**:
```latex
faktorer (inte bara \enquote{klasser är bättre}). Om de säger \enquote{använd alltid klasser}
eller \enquote{använd alltid uppslagslistor}, undersök med motexempel: \enquote{Vad sägs om
konfigurationsdata från JSON?} eller \enquote{Vad sägs om ett komplext
användarprofilsystem?}
```

---

## Quotes NOT Changed (Correctly Left as-is)

**Python code in `\mintinline{python}{...}` blocks**: Properly kept as Python string syntax:
- Line 44: `\mintinline{python}{"name"}`
- Line 45: `\mintinline{python}{"checked"}`
- Line 142: `\mintinline{python}{{"name": "mjölk", "checked": False}}`
- Lines 156, 160, 161, 196, 201: Similar Python dictionary syntax
- Line 443: Python f-string in example file

**Rationale**: Code examples should preserve the language's native syntax.

---

## Why This Matters

### Typographical Correctness
- Swedish typically uses »...« or "..." (different from English "...")
- `\enquote` automatically adapts to document language settings
- Consistent quotation style throughout document

### Semantic Markup
- Explicit markup for quotations (not just visual formatting)
- Enables alternative renderings (e.g., accessibility tools)
- Easier to change quotation style globally

### Nested Quotes
Manual approach fails with nested quotes:
```latex
% INCORRECT - ambiguous nesting
"outer 'inner' quote"
```

csquotes handles automatically:
```latex
% CORRECT - clear nesting
\enquote{outer \enquote{inner} quote}
```

### Professional Standards
- LaTeX best practice for 20+ years
- Used in all major academic publishers
- Expected in professional LaTeX documents

---

## Compilation Status

✅ **notes.pdf**: Compiles successfully (90263 bytes, 14 pages)
✅ **All `\enquote` commands** render correctly
✅ **No warnings** related to quotation marks

---

## latex-writing Skill Enhancements

### Added Section
**Quotations (csquotes package)** - Complete guidance on quote usage

### Updated Checklist
Now includes:
```markdown
- [ ] Manual quotes (`"..."`, `'...'`, `` `...` ``) instead of `\enquote{...}`
```

### Documentation
- Clear anti-patterns identified
- Correct usage examples
- Rationale explained (language-aware, nested quotes, semantic markup)

---

## Recommendation

Apply this pattern throughout all course materials:

1. **Search for manual quotes**: `grep -n '"' *.tex`
2. **Distinguish code from text**: Keep quotes in `\mintinline` and code blocks
3. **Replace text quotes**: Use `\enquote{...}` for all natural language quotes
4. **Verify compilation**: Ensure csquotes package is loaded

**Pattern for checking**:
```bash
# Find quotes not in Python code
grep '"' file.tex | grep -v 'mintinline{python}'
```

---

## Integration with Other Skills

This csquotes usage integrates with:

1. **latex-writing**: Semantic markup principle
2. **didactic-notes**: Professional documentation standards
3. **variation-theory**: Clear, unambiguous presentation of examples

All three benefit from proper typographical conventions.

---

## Conclusion

The document now follows LaTeX best practices for quotation marks:
- Semantic markup with `\enquote{...}`
- Language-aware rendering
- Consistent style throughout
- Professional typographical quality

This is a small but important detail that contributes to overall document quality and professionalism.
