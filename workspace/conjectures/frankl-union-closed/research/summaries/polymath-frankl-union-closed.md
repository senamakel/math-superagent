# Polymath project — "Frankl's union-closed conjecture" (project page)

**Source URL:** https://www.michaelnielsen.org/polymath/index.php?title=Frankl%27s_union-closed_conjecture · **Full text:** [[polymath-frankl-union-closed.full]]

## What it is

The collaborative Polymath run on the conjecture led by Tim Gowers (2016). A
canonical problem-collection page that gathers: the partial results known at the
time, several proposed **strengthenings of FUNC**, the disproved ones, the
structural theory (Horn clause, lattice), and important constructions/examples
(power sets, total orders, Duffus–Sands, Renaud–Sarvate, Steiner systems, fibre
bundles, Hom-lattices). Much of the *quantitative* content (m ≤ 12, the record
constant) is now superseded by the entropy era, but the **strengthening
landscape is permanently useful**: it is the map of "if you prove X you get FUNC",
and most of the X have been ruled out.

## What it establishes that the library did not previously hold

### Partial results (as of the page) — superseded-but-confirming

`m ≤ 12`, `n ≤ 50`, `n ≥ (2/3)2^m`, `n ≤ 4m−2` for separating, `|A| ∈ {1,2}`
for some A, and "contains three 3-sets all subsets of the same 5-set". Also the
log-bound `|A_x| ≥ (n−1)/log₂n` and its `2.4n/log₂n` improvement. These all
match primary sources already in the library; the page corroborates them.

### Disproved strengthenings of FUNC (RULED-OUT routes, highest value)

1. **Injection-to-superset**: is there always `x` and an injection
   `φ : A_¬x → A_x` with `A ⊂ φ(A)`? **Answered in the negative.**
2. **Uniform weighted FUNC**: is there always `x` with
   `Σ_{x∈A} f(A) ≥ Σ_{x∉A} f(A)` for *every* monotone `f`? (equivalent to:
   some `x` abundant in every upper set of `A`). **Is false.**

These two are specifically flagged as false on the Polymath page. They are
exactly the kind of "natural strengthening" a fresh attack on the conjecture
proposes, and the run must not re-derive them as open.

### Strengthening implication relationships

`injection-to-superset ⟹ uniform weighted FUNC ⟹ weighted FUNC ⟹ injection-to-larger`.
Since the top two are disproved, the useful open ones among the strengthenings
are the *weaker* tail (ordinary weighted FUNC, injection-to-larger) — but even
these should be treated as folklore/conjectural, not established.

```claim
id: polymath-injection-to-superset-false
statement: The "injection-to-superset" strengthening of FUNC is FALSE: it is not
  true that for every union-closed family there is an element x and an injection
  φ : A_¬x → A_x with A ⊂ φ(A) for all A.
hypotheses: A union-closed family; A_x = {A : x∈A}; the stated injection must
  exist for some x.
holds-here: no — this is a *strengthening* whose falsehood means it cannot be
  the route to UC; recorded so the run does not re-propose it.
status: asserted-by-source (Polymath page flags it "answered in the negative";
  the run has not located the original counterexample paper).
bearing: RULED OUT as a path to UC. A proof that this injection exists would
  have implied UC; since it is false, nothing of the sort is available.
anchor: research/sources/polymath-frankl-union-closed.full.md
```

```claim
id: polymath-uniform-weighted-func-false
statement: The "uniform weighted FUNC" strengthening of FUNC is FALSE: it is not
  true that for every union-closed family some element x has
  Σ_{x∈A} f(A) ≥ Σ_{x∉A} f(A) for every monotone nonnegative f.
hypotheses: A union-closed; f monotone (A⊆B ⟹ f(A)≤f(B)), nonnegative.
holds-here: no — a strengthening whose falsehood RULES OUT that route to UC.
status: asserted-by-source (Polymath page: "This conjecture is false"; the run
  has not located the original counterexample).
bearing: RULED OUT. This is why the ordinary "weighted FUNC" (the FC-families /
  Poonen-weight machinery) is the surviving version — and matches the library's
  FC-families line.
anchor: research/sources/polymath-frankl-union-closed.full.md
```

## Why it matters for this run

The run's GOAL item 4 is a proved *barrier* or a structural claim about a
minimal counterexample. The Polymath page is the canonical record of which
"just prove this stronger thing" statements are already dead. Both the
injection-to-superset and uniform-weighted-FUNC strengthenings are false, so the
surviving strengthening routes are weighted FUNC and the entropy/coupling line —
and the latter is already pursued in the library. This page also supplies the
explicit constructions (Renaud–Sarvate example, Duffus–Sands) that the run's
oracle can use as test families.
