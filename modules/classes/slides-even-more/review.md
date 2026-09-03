# Review of slides-even-more Notes
## Focus: Variation Theory and pQBL Analysis

Date: 2025-11-04
Reviewer: Claude (Sonnet 4.5)

---

## Executive Summary

The `slides-even-more/` notes present excellent practical examples (shopping lists, bank system) with strong design principles coverage. However, they underutilize variation theory patterns and don't fully implement pQBL principles. The material would benefit from:

1. Adding strong **contrast** sections (showing with/without classes)
2. Making **variation and invariance explicit** throughout
3. Restructuring exercises as proper **question-feedback pairs**
4. Systematically sequencing by **variation patterns** (contrast → separation → generalization → fusion)

---

## Variation Theory Analysis

### Object of Learning
Practical applications of classes, including:
- Composition (has-a relationships)
- Inheritance (is-a relationships)
- Design principles for OOP

### Critical Aspects Identified

The material addresses these critical aspects that learners must discern:

1. **Classes as organizational structures** - Grouping related data and behavior
2. **Composition** - Objects containing other objects (has-a)
3. **Inheritance** - Classes extending other classes (is-a)
4. **Encapsulation** - Controlling access to data
5. **Design principles** - When to use classes vs simpler structures

### Variation Patterns - Current Usage

#### ✅ Generalization (Strong)
- Two diverse examples (shopping lists, bank system) demonstrate same principles
- Shows patterns across different domains effectively
- Lines 3-106: Shopping list example
- Lines 107-313: Bank system example
- Both illustrate composition, methods, and data organization

#### ✅ Fusion (Present)
- Bank example combines multiple concepts simultaneously
- Lines 107-313: Integrates composition (Person has Address, BankAccount has Person) + inheritance (Citizen extends Person)
- Lines 328-336: Explicit summary of integrated concepts
- This enables learners to see how aspects interrelate

#### ⚠️ Separation (Moderate)
- Concepts introduced sequentially
- Could be more systematically isolated
- Example: Composition introduced (lines 142-180) before inheritance (lines 255-312)
- However, could better isolate **why** each pattern by varying it independently

#### ❌ Contrast (Weak)
- **Major weakness**: Missing strong "with vs without classes" comparison
- Compare to `slides/contents.tex` lines 10-88: Excellent phonebook example showing dictionary approach first, then class approach
- Current version starts directly with class solution (line 28)
- **Impact**: Learners may not discern WHY classes help if they never experience the alternative

### Making Variation/Invariance Explicit

**Critical Gap**: The material doesn't explicitly state what varies and what remains invariant.

Marton's principle: "When some aspect of a phenomenon varies while another aspect remains invariant, the varying aspect will be discerned."

**Examples where this could be added**:

- **Line 28-33**: When introducing ShoppingList class
  - *What varies*: Implementation approach (dict → class)
  - *What's invariant*: Functionality (add, list, check items)
  - Currently implicit, should be explicit

- **Line 170-180**: Composition advantages
  - *What varies*: Context where Address is used (Person, Company, School)
  - *What's invariant*: Address structure itself
  - Should explicitly state: "Notice how Address structure remains invariant while usage context varies"

- **Line 382-432**: Composition vs Inheritance
  - *What varies*: Relationship type (has-a vs is-a)
  - *What's invariant*: Both reuse code
  - Could make the critical distinction more explicit through variation pattern

---

## pQBL Analysis

### Strengths

✅ **Extensive use of exercises**: Many `\begin{exercise}` blocks throughout
- Lines 11-21, 23-26, 47-50, 67-70, 81-84, 97-105, etc.
- Good question-first approach

✅ **Questions often precede content**: Follows pQBL principle
- Line 24: "Hur skulle du representera en inköpslista?" (before solution)
- Line 115: "Vilka attribut och metoder behöver en person?" (before Person class)
- Line 184: "Vilka attribut och metoder behöver ett bankkonto?" (before BankAccount)

✅ **Reflective questions**: Encourage thinking
- Line 339: "Reflektera över de exempel vi har sett"
- Line 361: "När är det lämpligt att skapa en klass?"
- Line 387: "Varför använde vi komposition för Address och Person, men arv för Citizen?"

### Critical Weaknesses

#### 1. Feedback Not Structured as Feedback

**Issue**: Exercises ask questions, but answers appear as continuous narrative rather than structured feedback.

**Example - Lines 11-33**:
```latex
\begin{exercise}
  Skriv ett program som hanterar en inköpslista...
\end{exercise}

\begin{exercise}
  Innan du fortsätter läsa: Hur skulle du representera en inköpslista?
\end{exercise}

\subsection{Design och implementation}

Vi kan använda en klass...
```

**What's missing**:
- No explicit feedback block
- No verification of common answers
- No explanation of why certain approaches work/don't work
- No explicit variation/invariance identification

**Better structure**:
```latex
\begin{question}
  ...
\end{question}

\begin{feedback}
  \textbf{Verification:} [Common answers]
  \textbf{Explanation:} [Why each works/doesn't]
  \textbf{Variation/Invariance:} [What varied? What stayed same?]
  \textbf{Content:} [The learning material]
\end{feedback}
```

#### 2. Questions Don't Follow Variation Pattern Sequence

**pQBL + Variation Theory Best Practice**: Sequence questions as:
1. **Contrast** (early) - Help notice aspects exist
2. **Separation** (middle) - Isolate individual aspects
3. **Generalization** (middle-late) - Show patterns across contexts
4. **Fusion** (late) - Integrate multiple aspects

**Current state**: Questions present but not systematically labeled or sequenced by pattern type.

**Examples of implicit patterns** (could be made explicit):

- **Contrast** (should add): With/without classes comparison
- **Separation** (present): Line 67-70 (why dicts for each item?), Line 215-218 (why return boolean?)
- **Generalization** (present): Line 387-390 (why composition here, inheritance there?)
- **Fusion** (present): Line 436-459 (extension projects requiring integration)

#### 3. Immediate Answers

Some explanations follow questions too quickly without giving learners time to struggle.

**Example - Lines 47-53**:
```latex
\begin{exercise}
  Varför använder vi en lista av uppslagslistor istället för bara en lista
  av strängar? Vilka fördelar ger det?
\end{exercise}

Genom att använda uppslagslistor kan vi lagra mer information...
```

**Impact**: The answer appears immediately (line 52), potentially preventing productive struggle.

**Better**: Add more space, perhaps another question, or explicitly signal "Think about this before reading..."

#### 4. No Tailored Feedback Paths

Since this is LaTeX slides/notes (not interactive system), it can't provide response-specific feedback. However, it could still structure content as:

```latex
\begin{feedback}
  If you thought A: Here's why that makes sense and where it leads...
  If you thought B: This is a common answer because... but consider...
  If you thought C: Excellent! This captures...
\end{feedback}
```

**Example where this would help - Line 136-140**:
```latex
\begin{exercise}
  Om vi vill lägga till adressinformation, skulle du lägga till attributen
  street, city och zipcode direkt i Person-klassen, eller skulle du skapa
  en separat Address-klass? Motivera ditt val.
\end{exercise}
```

This is excellent multiple-choice structure but needs feedback for BOTH options explaining why each might seem reasonable and why one is better.

---

## Comparison with Other Versions

### `slides/` (Phonebook & Person) - Basic Introduction

**Strengths relative to slides-even-more**:

✅ **Superior contrast** (lines 10-88):
- Shows same problem WITH and WITHOUT classes explicitly
- `phonebook.py` with dicts vs `contacts_class.py` with Person class
- Makes variation/invariance visible: implementation varies, functionality invariant

✅ **Better isolation** of concepts:
- Section 230-308: "Klasser och objekt" defines terms clearly
- Section 309-426: "Metoder och attribut" isolates these concepts
- Section 427-517: "Dundermetoder" dedicated section
- Section 519-656: "Arv" isolated concept
- Each gets focused treatment

✅ **Clearer progression** through critical aspects:
- More systematic building from simple to complex
- Each concept fully explored before next introduced

**Weaknesses relative to slides-even-more**:

⚠️ **Less practical**: Single phonebook example throughout, less variety

⚠️ **Minimal composition**: Focuses more on inheritance than composition

⚠️ **Less design guidance**: Doesn't discuss when to use classes as thoroughly

### `slides-more/` (Fractions Class) - Advanced Techniques

**Strengths relative to slides-even-more**:

✅ **Better separation** of operations:
- Lines 210-298: Addition isolated
- Lines 300-402: Subtraction isolated (builds on negation)
- Lines 404-461: Multiplication isolated
- Lines 463-605: Simplification isolated
- Each operation gets complete treatment before next

✅ **Progressive complexity**:
- Very systematic: constructor → properties → conversion → operations → simplification
- Each builds on previous in clear dependency chain

✅ **Modern Python features**:
- Lines 68-110: Properties with @property decorator
- Lines 160-208: Type conversion dunder methods
- More sophisticated than slides-even-more examples

**Weaknesses relative to slides-even-more**:

⚠️ **More abstract**: Fractions less immediately relatable than shopping/banking

⚠️ **No composition**: Focuses on single-class development

⚠️ **No inheritance**: Doesn't cover class relationships

⚠️ **More advanced**: Requires more mathematical sophistication

### `slides-even-more/` (Shopping Lists & Bank) - Current Version

**Unique strengths**:

✅ **Most practical examples**: Shopping lists (3-106) and banking (107-313) are relatable

✅ **Best composition coverage**:
- Address in Person (142-180)
- Person in BankAccount (182-253)
- Clear has-a relationships

✅ **Design principles**:
- Lines 337-381: Excellent summary of when to use classes
- Lines 382-432: Thoughtful composition vs inheritance discussion
- Most complete treatment of design decisions

✅ **Multiple examples**: Two complete systems showing different applications

**Critical gaps**:

❌ **Weakest contrast**: Doesn't show alternative approaches first

❌ **Less isolation**: Concepts more intertwined (composition + methods + design simultaneously)

❌ **Variation/invariance implicit**: Never explicitly stated

---

## Specific Recommendations

### 1. Add Strong Contrast Section (High Priority)

**Location**: Beginning of shopping list example (before line 11)

**Current**: Starts directly with the problem and solution

**Recommended**: Add contrast like `slides/` does

```latex
\subsection{Utan klasser: Försök med uppslagslistor}

\begin{exercise}
  Innan vi använder klasser, hur skulle du implementera en inköpslista
  med bara listor och uppslagslistor?
\end{exercise}

\begin{frame}[fragile]
  shopping\_dict.py \hrulefill
  \inputminted[linenos]{python}{examples/shopping_dict.py}
\end{frame}

\begin{example}[Användning utan klasser]
  \inputminted[linenos]{python}{examples/shopping_dict_usage.py}
\end{example}

\begin{exercise}
  Prova att utöka programmet ovan:
  \begin{itemize}
    \item Lägg till prioritet för varje vara
    \item Lägg till kategori för varje vara
    \item Hantera flera olika listor
  \end{itemize}
  Vilka problem uppstår när programmet växer?
\end{exercise}

\begin{feedback}
  \textbf{Problem som uppstår}:
  \begin{itemize}
    \item Måste komma ihåg alla nyckelnamn ("name"? "namn"? "item"?)
    \item Lätt att stavfel i nyckelnamn → KeyError
    \item Ingen validering av data
    \item Logiken (add, check, remove) är spridd i programmet
    \item Svårt att återanvända koden
  \end{itemize}

  \textbf{Variation Pattern - Contrast}: Vi har sett implementationen med
  uppslagslistor. Nu ska vi se SAMMA funktionalitet implementerad med klasser.
  Genom att jämföra dessa två approacher, där IMPLEMENTATIONEN varierar men
  FUNKTIONALITETEN förblir invariant, kan vi discernera fördelarna med klasser.
\end{feedback}

\subsection{Med klasser: En bättre lösning}

[Current content starting line 11...]
```

**Rationale** (Variation Theory):
- Learners must experience **contrast** to discern that an aspect (organizational approach) exists
- Seeing what classes ARE versus what they ARE NOT makes the critical aspect visible
- Currently this variation is missing

**Code to create**: `examples/shopping_dict.py` and `examples/shopping_dict_usage.py`

### 2. Make Variation/Invariance Explicit Throughout

Add explicit statements about what varies and what remains invariant. This is crucial for variation theory.

#### Example A: Line 170-180 (Composition advantages)

**Currently**:
```latex
Fördelarna med komposition inkluderar:
\begin{itemize}
  \item \textbf{Återanvändbarhet}: Address-klassen kan användas i andra
    sammanhang (företag, skolor, etc.).
  \item \textbf{Modularitet}: Adresslogik kan ändras utan att påverka
    Person-klassen.
  ...
\end{itemize}
```

**Better with explicit variation**:
```latex
Fördelarna med komposition inkluderar:
\begin{itemize}
  \item \textbf{Återanvändbarhet}: Address-klassen kan användas i andra
    sammanhang (företag, skolor, etc.).
    \textit{Variation: Användningskontexten (Person, Company, School) varierar.
    Invariant: Address-strukturen förblir densamma. Detta gör klassen återanvändbar.}

  \item \textbf{Modularitet}: Adresslogik kan ändras utan att påverka
    Person-klassen.
    \textit{Variation: Address-implementationen kan ändras.
    Invariant: Person-klassens interface förblir oförändrat. Detta ger flexibilitet.}
  ...
\end{itemize}
```

#### Example B: Line 28-33 (Introducing ShoppingList class)

**Currently**:
```latex
Vi kan använda en klass \mintinline{python}{ShoppingList} som lagrar varor
i en lämplig datastruktur, har metoder för att lägga till, visa och ta bort
varor, och håller koll på vilka varor som är avbockade.
```

**Better with explicit variation**:
```latex
Vi kan använda en klass \mintinline{python}{ShoppingList} som lagrar varor
i en lämplig datastruktur, har metoder för att lägga till, visa och ta bort
varor, och håller koll på vilka varor som är avbockade.

\begin{variation}
  \textbf{Vad varierar}: Implementationsapproach (från uppslagslistor till klass)

  \textbf{Vad förblir invariant}: Funktionaliteten (lägga till, visa, bocka av, ta bort)

  \textbf{Vad vi kan discernera}: Genom att hålla funktionaliteten konstant medan
  vi varierar implementationen kan vi se exakt vad klasser tillför: inkapsling
  av data och metoder, tydligt interface, återanvändbarhet.
\end{variation}
```

#### Example C: Lines 382-432 (Composition vs Inheritance)

**Currently** (line 392-406):
```latex
\begin{frame}[fragile]
  \begin{block}{Komposition (has-a)}
    En klass \emph{innehåller} ett objekt av en annan klass.
    ...
  \end{block}
\end{frame}
```

**Better with explicit variation**:
```latex
\begin{frame}[fragile]
  \begin{block}{Komposition (has-a)}
    En klass \emph{innehåller} ett objekt av en annan klass.
    \begin{itemize}
      \item Person \emph{har} en Address
      \item BankAccount \emph{har} en Person
    \end{itemize}

    \textbf{Variation Pattern - Separation}:
    \begin{itemize}
      \item \textit{Vad varierar här}: Vilken klass som innehåller vilken
      \item \textit{Vad är invariant}: Båda är separata, oberoende klasser
      \item \textit{Discernment}: Komposition = löst kopplad ägarrelation
    \end{itemize}
  \end{block}
\end{frame}

\begin{frame}[fragile]
  \begin{block}{Arv (is-a)}
    En klass \emph{är en specialisering} av en annan klass.
    \begin{itemize}
      \item Citizen \emph{är en} Person (med extra information)
    \end{itemize}

    \textbf{Variation Pattern - Separation}:
    \begin{itemize}
      \item \textit{Vad varierar här}: Mängden funktionalitet (Person → Citizen)
      \item \textit{Vad är invariant}: Grundfunktionaliteten från Person
      \item \textit{Discernment}: Arv = strikt hierarkisk relation med kodåteranvändning
    \end{itemize}
  \end{block}
\end{frame}

\begin{frame}[fragile]
  \begin{block}{Jämförelse genom Variation}
    Genom att presentera komposition och arv sida vid sida, där
    RELATIONSTYPEN varierar (has-a vs is-a) men MÅLET (kodåteranvändning)
    förblir invariant, kan vi discernera den kritiska skillnaden:

    \begin{itemize}
      \item \textbf{Komposition}: Flexibel, lös koppling, kan ändras vid körtid
      \item \textbf{Arv}: Hierarkisk, polymorfism, fast vid kompilering
    \end{itemize}
  \end{block}
\end{frame}
```

### 3. Restructure as True pQBL Questions

Transform exercises into proper question-feedback pairs following pQBL principles.

#### Example A: Lines 11-33 (Shopping List Introduction)

**Currently**:
```latex
\begin{exercise}
  Skriv ett program som hanterar en inköpslista. Programmet ska kunna:
  \begin{itemize}
    \item Lägga till saker på listan
    \item Lista alla varor
    \item Bocka av enskilda saker
    \item Ta bort alla avbockade saker
  \end{itemize}
\end{exercise}

\begin{exercise}
  Innan du fortsätter läsa: Hur skulle du representera en inköpslista?
\end{exercise}

\subsection{Design och implementation}

Vi kan använda en klass \mintinline{python}{ShoppingList}...
```

**Restructured as pQBL**:
```latex
\begin{question}[Contrast: Datastruktur för inköpslista]
  Vi ska bygga ett program för inköpslistor med följande funktioner:
  \begin{itemize}
    \item Lägga till varor
    \item Lista alla varor
    \item Bocka av enskilda varor
    \item Ta bort avbockade varor
    \item Hantera flera olika listor (mat, hushåll, etc.)
  \end{itemize}

  Vilket approach skulle fungera bäst?
  \begin{enumerate}[a)]
    \item En lista av strängar: \mintinline{python}{["mjölk", "bröd"]}
    \item En lista av uppslagslistor: \mintinline{python}{[{"name": "mjölk", "checked": False}]}
    \item En klass \mintinline{python}{ShoppingList} med metoder
  \end{enumerate}

  \textbf{Tänk igenom fördelar och nackdelar innan du läser vidare.}
\end{question}

\begin{feedback}
  \textbf{Verification}: Alla tre alternativ KAN tekniskt fungera, men de
  varierar dramatiskt i underhållbarhet och användbarhet.

  \textbf{Explanation}:

  \textit{Alternativ a - Lista av strängar}:
  \begin{itemize}
    \item[+] Enklast att implementera initialt
    \item[−] Hur representerar vi avbockade varor? Behöver separat lista
    \item[−] Svårt att lägga till mer information (prioritet, kategori)
    \item[−] Logiken finns utspridd i programmet
  \end{itemize}

  \textit{Alternativ b - Lista av uppslagslistor}:
  \begin{itemize}
    \item[+] Kan lagra flera attribut per vara
    \item[+] Flexibelt att lägga till fält
    \item[−] Måste komma ihåg exakta nyckelnamn ("name"? "namn"? "item"?)
    \item[−] Stavfel i nycklar → KeyError vid körtid
    \item[−] Ingen validering av data
    \item[−] Logiken (add, check, remove) är fortfarande utspridd
  \end{itemize}

  \textit{Alternativ c - ShoppingList klass}:
  \begin{itemize}
    \item[+] Data OCH metoder tillsammans (inkapsling)
    \item[+] Tydligt interface: \mintinline{python}{add_item()}, \mintinline{python}{check_item()}
    \item[+] Kan lägga till validering i metoderna
    \item[+] Återanvändbar struktur
    \item[+] IDE kan ge autocomplete och typkontroll
    \item[−] Mer initial kod att skriva
  \end{itemize}

  \textbf{Variation och Invariance}:
  \begin{itemize}
    \item \textit{Vad varierar}: Datastrukturen och hur funktionaliteten organiseras
    \item \textit{Vad är invariant}: Funktionaliteten som behövs (add, list, check, remove)
    \item \textit{Discernment}: Genom att se tre olika implementationer av SAMMA
    funktionalitet kan vi discernera att klasser erbjuder bäst kombination av
    struktur och flexibilitet
  \end{itemize}

  \textbf{Connection}: Detta är ett exempel på \textit{inkapsling} - att samla
  relaterad data och funktionalitet i en enhet. Vi kommer se fler exempel på
  detta designprincip.

  \textbf{Implementation}:

  Vi väljer alternativ c. Här är hur en \mintinline{python}{ShoppingList}-klass
  kan struktureras:

  [Current content from line 34...]
\end{feedback}
```

**Note the pQBL components**:
- ✅ Question first with multiple-choice structure
- ✅ Explicit instruction to think before reading
- ✅ Verification acknowledges all options
- ✅ Explanation covers why each works/doesn't
- ✅ Variation/invariance explicitly stated
- ✅ Connection to broader concepts
- ✅ Content (implementation) within feedback

#### Example B: Lines 115-140 (Person Class Introduction)

**Currently**:
```latex
\begin{exercise}
  Vi ska bygga ett banksystem. Ett bankkonto behöver information om sin
  ägare. Vilka attribut och metoder behöver en klass för att representera
  en person ha?
\end{exercise}

Vi börjar med att skapa en klass för att representera en person...

[Code example]

\begin{exercise}
  Om vi vill lägga till adressinformation, skulle du lägga till attributen
  \mintinline{python}{street}, \mintinline{python}{city} och
  \mintinline{python}{zipcode} direkt i Person-klassen, eller skulle du skapa
  en separat Address-klass? Motivera ditt val.
\end{exercise}
```

**Restructured as pQBL**:
```latex
\begin{question}[Separation: Attribut för Person]
  Vi ska bygga ett banksystem. Ett bankkonto behöver information om sin ägare.

  Vilka attribut är NÖDVÄNDIGA för en grundläggande Person-klass?

  Markera alla som du tycker hör till en persons grundläggande identitet:
  \begin{itemize}
    \item[$\square$] Namn (för- och efternamn)
    \item[$\square$] Ålder/födelsedatum
    \item[$\square$] Adress (gata, stad, postnummer)
    \item[$\square$] Telefonnummer
    \item[$\square$] E-postadress
    \item[$\square$] Kontonummer
    \item[$\square$] Saldo
  \end{itemize}

  Tänk: Vilka attribut beskriver PERSONEN vs vilka beskriver personens
  RELATIONER till andra saker?
\end{question}

\begin{feedback}
  \textbf{Verification}: Det finns inget entydigt "rätt" svar, men vissa val
  är mer motiverade än andra baserat på designprinciper.

  \textbf{Explanation}:

  \textit{Grundläggande identitet} (passar i Person):
  \begin{itemize}
    \item Namn - definitivt grundläggande
    \item Ålder/födelsedatum - del av personens identitet
  \end{itemize}

  \textit{Kontaktinformation} (kan argumenteras):
  \begin{itemize}
    \item Adress - personen har en adress, men se diskussion nedan om komposition
    \item Telefon/e-post - liknande, personer har detta men det kan ändras
  \end{itemize}

  \textit{Relationsdata} (hör INTE till Person):
  \begin{itemize}
    \item Kontonummer - detta beskriver ett BANKKONTO, inte personen
    \item Saldo - likaså, detta är kontots attribut
  \end{itemize}

  \textbf{Key Insight}: En person KAN ha bankkonton, men bankkontoinformation
  är inte del av personens grundläggande identitet. Samma person kan ha
  flera konton, inga konton, eller byta konton. Detta antyder att BankAccount
  bör vara en SEPARAT klass.

  \textbf{Variation Pattern - Separation}:
  \begin{itemize}
    \item \textit{Vad varierar}: Vilka attribut vi inkluderar
    \item \textit{Vad är invariant}: Alla beskriver aspekter av "person"-konceptet
    \item \textit{Discernment}: Genom att systematiskt överväga olika attribut
    kan vi discernera skillnaden mellan:
    \begin{itemize}
      \item Attribut som är INNEBOENDE i objektet (namn, ålder)
      \item Attribut som beskriver RELATIONER till andra objekt (kontonummer)
    \end{itemize}
  \end{itemize}

  \textbf{Implementation}:

  Vi börjar med en minimal Person-klass:

  [Code from lines 125-130]

  Detta är en enkel början. Nu kommer en viktig designfråga...
\end{feedback}

\begin{question}[Separation: Komposition för Address]
  Vi vill lägga till adressinformation till Person. Vilket approach är bäst?

  \begin{enumerate}[a)]
    \item Lägg till attribut direkt i Person:
    \begin{minted}{python}
    def __init__(self, name, age, street, city, zipcode):
        self.__name = name
        self.__age = age
        self.__street = street
        self.__city = city
        self.__zipcode = zipcode
    \end{minted}

    \item Skapa en separat Address-klass och använd komposition:
    \begin{minted}{python}
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address  # Ett Address-objekt
    \end{minted}
  \end{enumerate}

  Vilket är bättre och varför?
\end{question}

\begin{feedback}
  \textbf{Verification}: Båda fungerar tekniskt, men alternativ b (komposition)
  är ofta bättre design.

  \textbf{Explanation}:

  \textit{Alternativ a - Direkt i Person}:
  \begin{itemize}
    \item[+] Enklare initialt (färre klasser)
    \item[+] Direkt åtkomst till adressfält
    \item[−] Person-klassen blir större och mer komplex
    \item[−] Address-logik (validering, formattering) sprids
    \item[−] Kan inte återanvända Address-struktur för Company, School, etc.
    \item[−] Svårt att ändra hur adresser hanteras senare
  \end{itemize}

  \textit{Alternativ b - Separat Address-klass}:
  \begin{itemize}
    \item[+] \textbf{Återanvändbarhet}: Address kan användas av Person, Company,
    School, etc.
    \item[+] \textbf{Modularitet}: Address-logik inkapslas i Address-klassen
    \item[+] \textbf{Enkelhet}: Person-klassen förblir enkel och fokuserad
    \item[+] \textbf{Flexibilitet}: Kan ändra Address-implementation utan att
    röra Person
    \item[+] \textbf{Testbarhet}: Kan testa Address separat
    \item[−] Lite mer initial kod (måste skapa Address-klass först)
  \end{itemize}

  \textbf{Design Principle - Komposition}:

  Detta är ett exempel på \textit{komposition}: en klass innehåller ett objekt
  av en annan klass. Vi säger att Person "har en" Address (has-a relationship).

  Komposition är att föredra när:
  \begin{itemize}
    \item En grupp attribut hör naturligt ihop (street, city, zipcode = address)
    \item Samma gruppering kan användas i flera sammanhang
    \item Du vill inkapsla logik för den gruppen
  \end{itemize}

  \textbf{Variation Pattern - Contrast}:
  \begin{itemize}
    \item \textit{Vad varierar}: Organisationsstruktur (flat vs composited)
    \item \textit{Vad är invariant}: Information som lagras (samma adressfält)
    \item \textit{Discernment}: Genom att se båda approacherna kan vi discernera
    att komposition ger bättre modularitet och återanvändbarhet
  \end{itemize}

  \textbf{Implementation}:

  [Code from lines 148-162 showing Address and updated Person]
\end{feedback}
```

### 4. Systematically Label and Sequence Questions by Variation Pattern

Add explicit labels to questions indicating which variation pattern they employ.

**Recommended structure**:

```latex
% At beginning of document, define question types
\newcommand{\questioncontrast}[1]{\textbf{[Contrast Question]} #1}
\newcommand{\questionseparation}[1]{\textbf{[Separation Question]} #1}
\newcommand{\questiongeneralization}[1]{\textbf{[Generalization Question]} #1}
\newcommand{\questionfusion}[1]{\textbf{[Fusion Question]} #1}
```

Then systematically organize content:

**Phase 1: Contrast Questions** (Beginning)
- With/without classes for shopping list
- Flat vs composed Person structure
- List of dicts vs ShoppingList objects

**Phase 2: Separation Questions** (Middle)
- Why return boolean from deposit()? (lines 215-222)
- Why use private attributes? (throughout)
- Why separate Address from Person? (lines 136-140)

**Phase 3: Generalization Questions** (Middle-Late)
- Does composition work for other domains? (implicitly line 172)
- When to use classes vs simpler structures? (lines 361-380)
- When composition vs inheritance? (lines 387-390)

**Phase 4: Fusion Questions** (End)
- Extension projects (lines 436-459) - perfect fusion!
- Design new system incorporating all principles

#### Concrete Example: Reorganizing Shopping List Section

**Current order** (lines 3-106):
1. Problem statement
2. Design question
3. Implementation
4. Methods
5. Usage
6. Multiple lists

**Better order with patterns**:

```latex
\section{Inköpslistor med klasser}

%% CONTRAST PHASE
\subsection{Att observera behovet av struktur}

\begin{question}[Contrast]
  [Show dict approach vs class approach side-by-side]
\end{question}

%% SEPARATION PHASE
\subsection{Att isolera olika aspekter av inköpslistor}

\begin{question}[Separation: Data representation]
  Varför använder vi uppslagslistor för varje vara?
  [Vary: representation of item / Invariant: list of items]
\end{question}

\begin{question}[Separation: Method return values]
  Varför returnerar check_item() och remove_checked() boolean/None?
  [Vary: return type / Invariant: operation performed]
\end{question}

%% GENERALIZATION PHASE
\subsection{Att se mönstret i olika sammanhang}

\begin{question}[Generalization: Multiple lists]
  Hur hanterar vi flera olika inköpslistor?
  [Same pattern: list-of-objects applies to shopping lists themselves]
\end{question}

\begin{question}[Generalization: Improvements]
  Hur skulle du förbättra ShoppingList? (prioriteter, kategorier, osv)
  [Same principles apply to extended features]
\end{question}

%% FUSION PHASE (comes later after bank example)
\subsection{Integration av alla principer}

\begin{question}[Fusion: Complete system]
  Designa ett system som hanterar:
  - Flera inköpslistor
  - Användare med olika preferenser
  - Delade listor mellan användare
  - Historik av inköp

  Vilka klasser behövs? Hur relaterar de till varandra?
\end{question}
```

### 5. Add Comprehensive Feedback Components

For each major question, structure feedback using all five components:

#### Template

```latex
\begin{feedback}
  %% 1. VERIFICATION
  \textbf{Verification}: [Acknowledge the response/common responses]

  %% 2. EXPLANATION
  \textbf{Explanation}: [Why answers are correct/incorrect]

  %% 3. VARIATION & INVARIANCE
  \textbf{Variation and Invariance}:
  \begin{itemize}
    \item \textit{What varies}: [The dimension of variation]
    \item \textit{What remains invariant}: [The background]
    \item \textit{What we can discern}: [The critical aspect revealed]
  \end{itemize}

  %% 4. CONNECTIONS
  \textbf{Connections}: [Link to other concepts, prior knowledge, upcoming material]

  %% 5. ELABORATION
  \textbf{Elaboration}: [Examples, code, deeper exploration]
\end{feedback}
```

#### Example Application: Line 243-246

**Currently** (minimal treatment):
```latex
\begin{exercise}
  Vad händer om vi försöker ta ut mer pengar än vad som finns på kontot?
  Kan du tänka dig andra sätt att hantera detta?
\end{exercise}
```

**With comprehensive feedback**:
```latex
\begin{question}[Separation: Error handling]
  Vad händer om vi försöker ta ut mer pengar än vad som finns på kontot?

  Vår nuvarande implementation:
  \begin{minted}{python}
  def withdraw(self, amount):
      if 0 < amount <= self.balance:
          self.balance -= amount
          return True
      return False
  \end{minted}

  Vilka alternativa sätt att hantera detta fel kan du tänka dig?
\end{question}

\begin{feedback}
  \textbf{Verification}: Det finns flera rimliga sätt att hantera ogiltiga uttag.

  \textbf{Explanation}:

  \textit{Alternativ 1 - Returnera boolean (nuvarande)}:
  \begin{minted}{python}
  success = account.withdraw(1000)
  if not success:
      print("Insufficient funds")
  \end{minted}
  \begin{itemize}
    \item[+] Tyst, ingen krasch
    \item[+] Anroparen kan välja hur fel ska hanteras
    \item[−] Lätt att glömma kontrollera returvärdet
    \item[−] Otydligt VAD som gick fel (belopp negativt? saldo otillräckligt?)
  \end{itemize}

  \textit{Alternativ 2 - Kasta exception}:
  \begin{minted}{python}
  def withdraw(self, amount):
      if amount <= 0:
          raise ValueError("Amount must be positive")
      if amount > self.balance:
          raise InsufficientFundsError(f"Balance: {self.balance}, wanted: {amount}")
      self.balance -= amount
  \end{minted}
  \begin{itemize}
    \item[+] Tydligt VAD som är fel
    \item[+] Måste hanteras (programmet kraschar annars)
    \item[+] Kan fånga och hantera specifika fel
    \item[−] Mer verbose för anroparen (try-except)
  \end{itemize}

  \textit{Alternativ 3 - Partiellt uttag}:
  \begin{minted}{python}
  def withdraw(self, amount):
      withdrawn = min(amount, self.balance)
      self.balance -= withdrawn
      return withdrawn
  \end{minted}
  \begin{itemize}
    \item[+] Alltid lyckas (tar ut vad som finns)
    \item[−] Kan ge oväntat beteende
    \item[−] Passar inte för banksystem (vill inte partiella uttag)
  \end{itemize}

  \textbf{Variation and Invariance}:
  \begin{itemize}
    \item \textit{What varies}: Felhanteringsstrategin (boolean, exception, partial)
    \item \textit{What remains invariant}: Kravet att inte göra ogiltiga uttag
    \item \textit{What we discern}: Det finns en trade-off mellan:
    \begin{itemize}
      \item Explicit (exception) vs implicit (boolean) felhantering
      \item Säkerhet (exception) vs bekvämlighet (boolean)
      \item Strikhet (reject) vs flexibilitet (partial)
    \end{itemize}
  \end{itemize}

  \textbf{Connections}:

  Detta exemplifierar en viktig designprincip: \textit{fail-fast vs fail-safe}.
  \begin{itemize}
    \item \textbf{Fail-fast} (exception): Upptäck fel omedelbart
    \item \textbf{Fail-safe} (boolean): Fortsätt trots fel
  \end{itemize}

  För banksystem är fail-fast ofta lämpligare - vi vill INTE göra ogiltiga
  transaktioner tyst. För andra system (t.ex. rendering graphics) kan fail-safe
  vara bättre - visa något även om allt inte är perfekt.

  \textbf{Elaboration}:

  I professionella system används ofta exceptions för detta:

  \begin{minted}{python}
  class InsufficientFundsError(Exception):
      pass

  class BankAccount:
      def withdraw(self, amount):
          if amount <= 0:
              raise ValueError("Amount must be positive")
          if amount > self.balance:
              raise InsufficientFundsError(
                  f"Insufficient funds: balance={self.balance}, "
                  f"requested={amount}"
              )
          self.balance -= amount

  # Användning
  try:
      account.withdraw(1000)
  except InsufficientFundsError as e:
      print(f"Transaction denied: {e}")
  except ValueError as e:
      print(f"Invalid input: {e}")
  \end{minted}

  Detta ger tydlig, explicit felhantering där anroparen \textit{måste} ta
  ställning till vad som ska hända vid fel.
\end{feedback}
```

**Note**: This comprehensive feedback:
- Verifies multiple approaches exist
- Explains pros/cons of each
- Makes variation/invariance explicit
- Connects to broader design principles (fail-fast/fail-safe)
- Elaborates with professional-grade example

### 6. Address Missing Critical Aspect from slides/

The `slides/` version has a powerful moment missing from `slides-even-more/`:

**slides/contents.tex lines 211-222**:
```latex
\begin{frame}[fragile]
  contacts.py \hrulefill
  \inputminted[linenos,firstline=25,lastline=35]{python}{examples/contacts.py}
  \vspace{0.5em}
  contacts\textunderscore{}class.py \hrulefill
  \inputminted[linenos,firstline=23,lastline=25]{python}{examples/contacts_class.py}
\end{frame}

Vilken skillnad! Med klasser behöver vi inte hantera \mintinline{python}{KeyError}
eller kontrollera om fält finns...
```

**Side-by-side comparison**:
```python
# contacts.py (without classes)
try:
    phone = phonebook[name]["phone"]
    print(f"Phone: {phone}")
except KeyError:
    print("Phone: unknown")

try:
    address = phonebook[name]["address"]
    print(f"Address: {address}")
except KeyError:
    print("Address: unknown")

# contacts_class.py (with classes)
print(person)  # Uses __str__() automatically
```

This is a **visceral contrast** that makes encapsulation benefits tangible.

**Recommendation**: Add similar comparison for shopping list:

```latex
\begin{frame}[fragile]
  \textbf{Jämförelse: Att läsa varorna}

  shopping\_dict.py \hrulefill
  \begin{minted}{python}
  for item in shopping_list:
      name = item["name"]
      checked = item.get("checked", False)  # Must handle missing key
      status = "☑" if checked else "☐"
      print(f"{status} {name}")
  \end{minted}

  shopping\_class.py \hrulefill
  \begin{minted}{python}
  shopping_list.display()  # Metoden hanterar allt
  \end{minted}
\end{frame}

\begin{frame}
  \textbf{Observation}:
  \begin{itemize}
    \item Med uppslagslistor: Vi måste komma ihåg nyckelnamn, hantera saknade
    fält, upprepa formatteringslogik överallt
    \item Med klasser: Logiken finns PÅ ETT STÄLLE i metoden
  \end{itemize}

  \textbf{Variation}: Var logiken finns (utspridd vs inkapsklad)

  \textbf{Invariant}: Vad vi vill åstadkomma (visa listan)

  \textbf{Discernment}: Inkapsling = mindre upprepning + färre buggar
\end{frame}
```

---

## Summary of Priorities

### High Priority (Address First)

1. **Add contrast sections** showing with/without classes
   - Most critical missing pattern
   - Foundation for discernment

2. **Make variation/invariance explicit** throughout
   - Core to variation theory
   - Currently completely implicit

3. **Restructure key exercises as question-feedback pairs**
   - Essential for true pQBL
   - Start with 3-5 major questions

### Medium Priority

4. **Label questions by variation pattern**
   - Helps learners understand structure
   - Makes pedagogical intent clear

5. **Add comprehensive feedback components**
   - Enriches learning experience
   - Makes feedback more actionable

### Lower Priority (Enhancement)

6. **Add side-by-side code comparisons** (borrowing from slides/)
   - Powerful but requires more examples
   - Can be added incrementally

---

## Example Files Needed

To implement recommendation #1 (contrast), create:

1. **examples/shopping_dict.py**: Shopping list using only dicts
2. **examples/shopping_dict_usage.py**: Using the dict version
3. These should be intentionally awkward to motivate classes

---

## Pedagogical Strengths to Preserve

While improving, maintain these excellent features:

✅ **Practical, relatable examples**: Shopping and banking are immediately understandable

✅ **Progressive complexity**: Shopping list (simpler) before bank system (more complex)

✅ **Design principles discussion**: Lines 337-432 are excellent and should be enhanced, not replaced

✅ **Multiple examples showing same principles**: Generalization is already strong

✅ **Extensive exercises**: Many opportunities for engagement already present

✅ **Composition emphasis**: Better coverage than other versions

---

## Conclusion

The `slides-even-more/` material has excellent content with practical, engaging examples. The main gaps are:

1. **Pedagogical scaffolding**: Variation patterns not explicit
2. **Contrast pattern**: Missing comparison with alternative approaches
3. **pQBL structure**: Exercises present but not structured as true question-feedback

With targeted improvements following this review, this could become an exemplary application of both variation theory and pQBL principles while maintaining its strengths in practical, design-focused instruction.

The material is closest to being ready for students as-is compared to the other versions, but making these pedagogical improvements would significantly enhance its learning effectiveness.
