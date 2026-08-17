> **Note — duplicate; the owning note holds the claim.**

This file is a duplicate digest of **LeanPool ErdosTuzaValtr `Main/CapCup.lean`**
(Jineon Baek, 2026). The owning note holds the full digest and the claim:

→ [[leanpool-erdostuzavaltr-capcup]] (claim `leanpool-capcup-ordinal-dichotomy`,
status checked — the Lean source was read this run).

**Bottom line.** A Lean-4 (Mathlib) formalisation, no sorry, of the
caps-and-cups dichotomy over an ErdosTuzaValtr `Config`: $|S| > \binom{a+b}{a}$
forces an $(a+2)$-cap or a $(b+2)$-cup, via the pincer/diagonal induction. This is
the **ordered-set (ETV/monotone)** flavour with threshold $\binom{a+b}{a}$ — the
combinatorial core of the classical cups-and-caps lemma — and is a
name-hygiene marker: it is NOT the planar convex-polygon lemma
$f(k,\ell)=\binom{k+\ell-4}{k-2}+1$, and neither is the (already-in-Mathlib)
monotone-subsequence ES theorem. Its value is as a formalisation model and a proof
that the cups-and-caps induction is Lean-formalisable (GOAL criterion 7).
