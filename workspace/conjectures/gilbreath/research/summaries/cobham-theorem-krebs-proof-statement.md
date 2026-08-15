# Cobham's theorem — grounded statement (fill of a named gap)

**Krebs, Thijmen J. P., "A more reasonable proof of Cobham's theorem",**
arXiv:1801.06704 [cs.FL], 20 Jan 2018, 3 pp. Full text:
`research/sources/cobham-theorem-krebs-proof-statement.full.md`.

**Why this was fetched.** The two *adopted* approaches
`christol-cobham-fold-inverse-automaticity` and `dyadic-linear-complexity-supply`
both named **Cobham's theorem** as the load-bearing tool for their
automatic-subclass lemma ("a 2-automatic h is rigid iff its σ-action is
nilpotent: finite 2-kernel + Cobham"), yet no readable statement of it was on
disk — `search_documents` and memory returned nothing for it. This file closes
that gap so the run reasons from a quotable source instead of recall.

## The theorem, verbatim (Krebs Theorem 1)

> **Theorem 1 (Cobham).** Let `a, b ≥ 2` be multiplicatively independent
> (i.e. `a^m ≠ b^n` for all `m, n > 0`). A sequence `(f_x)_{x∈ℕ}` is both
> `a`-automatic and `b`-automatic **if and only if** it is ultimately periodic.

Equivalently (the set form): if `X ⊆ ℕ` is both `a`-recognizable and
`b`-recognizable with `a,b` multiplicatively independent, then `X` is
ultimately periodic (a finite union of arithmetic progressions). The condition
`a^m ≠ b^n` for all positive `m,n` is another way to say `log a / log b` is
irrational; the paradigm example is `2` and `3` (independent), vs `2` and `4`
or `8` and `16` (dependent, since `8^4 = 16^3`).

## Why it matters here — the extraction the approaches need

The automatic-subclass lemma of both adopted approaches runs: *a 2-automatic
string h is rigid (ν₂ = o(n)) only under an extra condition; by Christol h is
2-automatic iff its F₂-generating function is algebraic; the subset-zeta
transform acts by the rational substitution `t ↦ t/(1+t)`, preserving
algebraicity and hence 2-automaticity; and **Cobham** gives the rigidity tool
for the 2-automatic subclass.* The precise role Cobham plays: once the 2-kernel
is finite (equivalently 2-automatic, Christol) and one has a *second*
independent base of automaticity, Cobham yields ultimate periodicity — which is
the collapse side. Note the scope discipline the approaches themselves record:
Cobham's theorem is a *finite-state rigidity* tool; it says nothing alone about
a single-base (2-automatic-only) string. Both witnesses pin that down:
Thue–Morse is 2-automatic and aperiodic (so not governed toward periodicity by
Cobham alone), and period-3 is 2-automatic yet non-rigid (positive density). So
Cobham alone does **not** force rigidity on 2-automatic strings — this source
does not overclaim; the dichotomy rests on the σ = I+S spectral structure, not
on Cobham.

Krebs's note is a proof-of-theorem paper, not a survey; its value to this run is
the **canonical statement and citation chain** (Cobham 1969 = Math. Systems
Theory 3:186–192; Allouche–Shallit 2003; Hansel 1982; Durand–Rigo; Semenov
1977 = the Cobham–Semenov extension cited in the run's "coverse
DPC-kernel-classification"). The 42 citations it added to `research/FRONTIER.md`
are leads, not yet assessed.

## Status

Sourced statement of a named theorem; the library's claim ledger holds the
*use* of it (adopted approaches), which is now backed by a readable primary
statement. Not a proof re-derived here (Krebs's short proof is on disk for that).
