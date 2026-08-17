```approach
idea: Positive-correlation (FKG / Ahlswede–Daykin four-functions) engine applied
  NOT to a second moment (that sibling is explicitly refuted by Ellis's small-AOD
  construction) but to a *monotone functional comparison on the family's own
  order*. Work in the dual intersection-closed form G containing ∅ and V, where
  UC says some element is rare (in ≤ |G|/2 sets). The Ahlswede–Daykin four
  functions theorem states: if f1(A)f2(B) ≤ f3(A∪B) f4(A∩B) for all A,B, then
  (Σ f1)(Σ f2) ≤ (Σ f3)(Σ f4) — a genuine tensoring correlation inequality.
  Choose four monotone functions on G (very explicitly: the ∩-closed indicator,
  its shifting partners) satisfying the inequality, and read the forced relation
  between "the total presence of element x" and "the total", i.e. between δ(x)
  and |G|. The engine is correlation/positivity, distinct from entropy (capped),
  distinct from moments (refuted), distinct from averaging (the linear-average
  CMS failure): AD is a nonlinear multiplicative pair inequality whose
  hypotheses can be *checked by exact query* on every small family.

mechanism: For a rare-counting set-up, abundance of x = |G| − #{A∈G: x∉A}; the
  sets avoiding x form an ∩-closed subfamily G_x^c. AD-type pairs give a bound on
  Σ_{A∈G} (weighted membership of x) versus |G|. The decisive distinction from
  the closed second-moment route: that route sums a *pair/overlap moment* that
  Ellis shows can be tiny; this one compares *monotone functions pointwise* (a
  four-function inequality, checked per pair), which moment data does not encode
  and which Ellis's Θ(loglog/log) families do not obviously respect. Marked
  speculative: the literature string "Ahlswede-Daykin / FKG union-closed Frankl
  abundance four-functions" has (to this run's knowledge) no application, so the
  first job is to *measure* whether any AD-consistent choice of the four
  functions forces the abundance comparison on n ≤ 5 — if none does, that is a
  documented negative.

status: proposed

first-step: With the canonical oracle, for each ∩-closed G on n ≤ 5 with ∅,V∈G,
  enumerate candidate monotone f1..f4 (indicators of {A: x∈A}, {A: x∉A}, {A: A⊇S}
  for S∈G, and the constant-on-filters), and decide by exact integer check
  whether the four-functions inequality holds for that choice; for each choice
  that does, verify the AD conclusion and test whether it forces δ(x) ≤ |G|/2
  for some x. Report per family the set of AD-cores that certify a rare element
  vs. the true rare set. Three controls: 2^[n] (every x has δ(x)=|G|/2, so AD
  must certify *all* x simultaneously or none strictly); the non-union-closed
  negative control family must break at least one four-functions inequality on
  every candidate choice (closure is genuinely used); finiteness via |G| ≤ 2^n.
  If no AD-consistent choice separates rare from abundant for n ≤ 5, close with
  that negative evidence.
```
