# LeanPool ErdosTuzaValtr CapCup.lean — a Lean formalisation of a cups-and-caps dichotomy

Source: https://raw.githubusercontent.com/Vilin97/lean-pool/main/LeanPool/ErdosTuzaValtr/Main/CapCup.lean
Full text: [[leanpool-erdostuzavaltr-capcup.lean.full]]
Authors: Jineon Baek, copyright 2026. Verified: downloaded and read this run.

## What it establishes

A Lean 4 formalisation (against Mathlib), in the namespace `Config` over a `LinearOrder`:
- `has_cap2_cup2 {S} (hS : 1 < S.card) : C.HasNCap 2 S ∧ C.HasNCup 2 S` — a 2-cup and 2-cap exist in any set of ≥2 elements.
- `cap_cup (a b) (S) (hS : Nat.choose (a+b) a < S.card) : C.HasNCap (a+2) S ∨ C.HasNCup (b+2) S` — the cap/cup dichotomy: a set larger than C(a+b,a) contains an (a+2)-cap or a (b+2)-cup. Proved by `pincerRecursion` (diagonal induction on (a,b)), using `binom_eq` (Pascal) and a filter/subset argument on the cap-start points.

This is the cups-and-caps counting dichotomy in the **Erdős–Tuza–Valtr configuration** setting (a `Config α` abstraction), i.e. the monotone-subsequence / ordered-set flavour of cups and caps, NOT the planar convex-polygon Erdős–Szekeres conjecture. The `C(a+b,a)` threshold is exactly the combinatorial core of the classical cups-and-caps lemma f(k,ℓ).

## Implication for this run

Three distinct things:
1. **Name hygiene (GOAL 5).** The planar convex-polygon ES(n) is a *different* theorem from this monotone/ordered-set cups-and-caps result, and both are distinct from Mathlib's monotone-subsequence `erdos_szekeres`. All three live under the name "Erdős–Szekeres". A Lean file for THIS run must state the planar convex-position version explicitly.
2. **Formalisation model.** `cap_cup` is a complete, kernel-checked example of the cups-and-caps counting argument written in Lean. The run's Lean arm wants to formalise the ES lower-bound construction and the exact-small-case facts; this file shows the idiom (Finset, `HasNCap`/`HasNCup` predicates, diagonal induction).
3. **The planar lemma is a different statement.** The classical planar cups-and-caps lemma is f(k,ℓ)=C(k+ℓ−4,k−2)+1 (Morris–Soltan Thm 2.5). The LeanPool result is the ordered/ETV version at threshold C(a+b,a). Do not cite it as the planar lemma; use it as proof that the cups-and-caps induction is Lean-formalisable.

```claim
id: leanpool-capcup-ordinal-dichotomy
statement: LeanPool/ErdosTuzaValtr/Main/CapCup.lean formalises (in Lean 4, no sorry) the caps-and-cups dichotomy over an ErdosTuzaValtr Config: |S| > C(a+b,a) forces an (a+2)-cap or a (b+2)-cup, via the pincer/diagonal induction. This is the ordered-set (ETV) flavour, threshold C(a+b,a), NOT the planar convex-polygon lemma f(k,l)=C(k+l-4,k-2)+1.
hypotheses: S a finite set in a linear order; C a Config; the HasNCap/HasNCup predicates as defined in LeanPool.ErdosTuzaValtr.
holds-here: yes
status: checked (directly read the Lean source file this run — confirms the ETV/monotone flavour and its C(a+b,a) threshold)
bearing: GOAL 5 — a formalisation model for the cups-and-caps counting arm; a name-hygiene marker separating the ETV/monotone flavour from the planar ES(n).
anchor: research/summaries/leanpool-erdostuzavaltr-capcup.md
```
