# Brown — Descriptions of the Characteristic Sequence of an Irrational (Canad. Math. Bull. 36, 1993)

**Source:** Tom C. Brown, "Descriptions of the Characteristic Sequence of an
Irrational", Canadian Mathematical Bulletin 36(1) (1993) 15–21,
DOI 10.4153/CMB-1993-003-6, Cambridge University Press.
Full text: `research/sources/cmb-1993-descriptions-characteristic-sequence.full.md`
(from https://doi.org/10.4153/cmb-1993-003-6).

## What this source is

A short primary paper surveying the various descriptions in the literature of
the **characteristic sequence** of an irrational α ∈ (0,1):

> f(α) = f_1 f_2 ⋯ with **f_n = [(n+1)α] − [nα]**.

That is exactly the lower mechanical word of slope α with intercept 0 (the
digit rule `mechanical-word-digit-rule` uses, and the rule that defines the
problem's word S_n limit at α = (3−√5)/2 = 1/φ²). The paper:

- collects the historical descriptions of characteristic sequences that have
  appeared in the literature (Bernoulli, Christoffel, Markoff, Morse–Hedlund,
  Ostrowski, Fraenkel–Levitt–Shimshoni, Ito–Yasutomi, Shallit, … — the
  reference list is itself a history of the subject, including Christoffel
  1875, Morse–Hedlund 1940, Ostrowski 1922, Fraenkel–Levitt–Shimshoni 1972);
- refines one description to give a simple derivation of an arithmetic
  expression for [nα] (Fraenkel–Levitt–Shimshoni);
- gives conditions on n equivalent to f_n = 1 (i.e. where the 1's occur).

## Why the library holds it (and its limitation)

Held as a primary anchor for the *definition* of the characteristic sequence as
a floor-difference mechanical word, and for its literature history. **Limitation
(recorded honestly):** the conversion at hand contains only the abstract,
keywords, references, and the "cited by" list — the article body and proofs are
behind CUP's paywall (no open full text). The abstract's definition
`f_n = [(n+1)α] − [nα]` is verbatim and is the one load-bearing statement
extracted from it. The derivations it contains are already covered on disk by
Perrin's lecture (`perrin-sturmian-words-lecture2-mechanical.full.md`), the
Berstel DLT'95 survey, and the characteristic-word slope confirmation in
Richomme–Saari–Zamboni — all open full texts. So this source is a definitional
and historical anchor, not the proof carrier.

## Statements extracted

1. (Abstract, verbatim) Let α be a positive irrational. The characteristic
   sequence of α is f(α) = f_1 f_2 ⋯ with f_n = [(n+1)α] − [nα].
2. (References) The classical literature on characteristic/Sturmian sequences:
   Christoffel 1875; Smith 1876; Markoff 1882; Morse–Hedlund 1940
   ("Symbolic dynamics II. Sturmian trajectories", Amer. J. Math. 62, 1–42);
   Ostrowski 1922 (diophantine approximation); Fraenkel–Levitt–Shimshoni 1972;
   Lekkerkerker 1952 (Zeckendorf); Zeckendorf 1972; Shallit 1991
   ("Characteristic words as fixed points of homomorphisms"); Ito–Yasutomi 1990
   (continued fractions, substitutions, characteristic sequences) — many already
   in the frontier as the field's citation spine.

```claim
id: characteristic-sequence-floor-difference-def
statement: The characteristic sequence of an irrational alpha in (0,1) is the
lower mechanical word f(alpha) = f_1 f_2 ... with f_n = floor((n+1)alpha) -
floor(n alpha). The Fibonacci word (PE1006's S_n limit) is the characteristic
sequence of alpha = (3-sqrt(5))/2 = 1/phi^2, whose partial quotients are all 1.
The literature on this object runs from Christoffel 1875 and Markov 1882 through
Morse-Hedlund 1940, Ostrowski 1922, Fraenkel-Levitt-Shimshoni 1972, Ito-Yasutomi
1990 and Shallit 1991 (fixed points of homomorphisms).
hypotheses: alpha irrational in (0,1).
holds-here: yes — the problem word is exactly this object at alpha = 1/phi^2
(see governing-sturmian, + Richomme-Saari-Zamboni Example 3.3).
status: sourced
bearing: Fixes the definition of the word whose length-k factors are summed; the
floor-difference form is the digit rule the mechanical construction evaluates.
anchor: research/sources/cmb-1993-descriptions-characteristic-sequence.full.md
(https://doi.org/10.4153/cmb-1993-003-6, abstract page; body paywalled)
```

## Obtained / not obtained

- Abstract + references + cited-by list: obtained (this is what the .full.md
  holds). The article body and proofs are paywalled at CUP; the load-bearing
  definitional content is in the abstract and is independently covered by the
  open sources above. Non-blocking.