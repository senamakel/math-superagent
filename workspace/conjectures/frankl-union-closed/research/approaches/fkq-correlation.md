# fkq-correlation — Ahlswede–Daykin / four-functions engine

## Verdict: refuted — AD's conclusion is an aggregate Σ-product (correlation) bound, not a per-element forcing, and the only UC application of it in the literature (the average-size/Reimer direction via Balla–Bollobás–Eccles) is known not to force the abundance ≥ 1/2 conclusion (Raz; Lu–Raz); the collapse is to the already-refuted overlap method (Ellis).

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
status: refuted
killed-by: ad-conclusion-is-aggregate-and-the-uc-app-collapses-to-the-refuted-overlap-route —
  (a) Ahlswede–Daykin's theorem is real and its hypotheses hold on P(n) (if
  α(A)β(B) ≤ γ(A∪B)δ(A∩B) for all A,B then (Σα)(Σβ) ≤ (Σγ)(Σδ)); source:
  The Probabilistic Method ch.6, and Christofides' q-analogue arXiv:0909.5137.
  BUT its conclusion is an AGGREGATE Σ-product (correlation/overlap) inequality
  — it bounds the product of total masses, i.e. a correlation/overlap-type
  quantity, NOT a per-element membership count δ(x). A four-functions choice
  whose conclusion is "δ(x) ≤ |G|/2 for some x" would have to convert the
  aggregate product into a per-element forcing, and no such conversion exists
  in the literature. (b) The ONLY application of AD/FKG to union-closed sets in
  the literature is through the average-size/Reimer direction: Balla–Bollobás–
  Eccles (JCTA 2013, doi:10.1016/j.jcta.2012.10.005) determine the minimum
  average size of a union-closed family (confirming Czédli–Maróti–Schmidt) by an
  up-compression/averaging argument and deduce UC for m ≥ (2/3)2^n. That exact
  route is known NOT to force abundance in general: Raz (doi:10.37236/6989) and
  Lu–Raz (arXiv:2405.10639) show Reimer's average-size conditions (which
  AD/averaging feed) do not imply the ≥1/2-abundance conclusion. (c) Reading
  the AD conclusion as a correlation/overlap bound reunites it with the
  second-moment/overlap machinery, which Ellis (doi:10.37236/10121, small-AOD
  families Θ(loglog/log)) refutes: no overlap-type quantity separates rare from
  abundant. So the candidate's would-be novelty — "the first job is to measure
  whether ANY AD-consistent four-function choice separates rare from abundant" —
  is answered in the negative by the shape of AD itself (aggregate, not
  per-element) plus the collapse to the already-refuted overlap method; no
  AD-consistent per-element forcing is found in the literature.
precedent: ahslwede-daykin-four-functions (The Probabilistic Method, 2nd ed., ch.6
  "Correlation Inequalities");
  christofides-q-four-functions (Christofides, arXiv:0909.5137 — q-analogue of the
  four-functions theorem, hypotheses and statement on P(n));
  balla-bollobas-eccles-min-avg-size (JCTA 2013, doi:10.1016/j.jcta.2012.10.005 —
  the only UC application of the AD/averaging engine, via average set size);
  raz-reimer-conditions-dont-force-abundance (Raz, EJC 2017, doi:10.37236/6989);
  lu-raz-reimer-counterexamples (Lu–Raz, arXiv:2405.10639);
  ellis-small-aod (Ellis, EJC 2022, doi:10.37236/10121 — refutes the overlap-type
  second-moment route this would collapse to).
first-step: (refuted as a route to UC — AD's aggregate conclusion cannot force
  the per-element abundance bound, and its UC application collapses to the
  refuted overlap method. A residual measurement (does any AD-consistent
  four-function choice separate rare from abundant on n ≤ 5) is cheap and
  worth running FOR THE RECORD on the ∩-closed oracle families, but the
  literature answer predicts a negative, and a negative there is not a result
  — it is the refutation above re-observed at small size.)
```

## What the literature establishes

**The theorem is real; its hypotheses hold here.** Ahlswede–Daykin's four-functions theorem: for non-negative functions α,β,γ,δ on the power set P(n) satisfying α(A)β(B) ≤ γ(A∪B)δ(A∩B) for all A,B ∈ P(n), one has (Σ_A α(A))(Σ_B β(B)) ≤ (Σ_C γ(C))(Σ_D δ(D)). It is in The Probabilistic Method (ch. 6, "Correlation Inequalities") alongside FKG, and Christofides (arXiv:0909.5137) proves a q-analogue, confirming the hypotheses on P(n) (a distributive lattice). So the engine the candidate names is sound and applicable to the ∩-closed dual G.

**But its conclusion is the wrong shape.** AD is a *tensoring correlation* inequality: it bounds the product of total masses, i.e. a correlation / overlap-type quantity, not a per-element membership count δ(x). The candidate's goal — "force δ(x) ≤ |G|/2 for some x" — requires turning an aggregate Σ-product into a per-element statement. There is no such conversion in the literature, and the aggregate shape is exactly why AD lives in the same family as the overlap/second-moment machinery.

**The only UC application of AD in the literature is the average-size route, and it is known not to force abundance.** Balla–Bollobás–Eccles (JCTA 2013) use the AD/averaging engine to determine the minimum average size of a union-closed family and deduce UC for large families (m ≥ (2/3)2^n). Raz (2017, doi:10.37236/6989) then showed the Reimer average-size conditions this route feeds do NOT imply the ≥ 1/2-abundance conclusion, and Lu–Raz (arXiv:2405.10639) extended to infinitely many such counterexamples. So the specific "four-functions → abundance" direction the candidate proposes has been implicitly tried (as an AD/averaging argument) and shown to stop short.

**The collapse is to the already-refuted overlap method.** Reading AD's conclusion as a correlation/overlap bound, the candidate's would-be novelty — "compare monotone functions pointwise, which overlap-moment data does not encode" — is not supported: AD's *conclusion* is still an aggregate correlation inequality, and Ellis's small-AOD families (doi:10.37236/10121) show such second-moment/overlap quantities cannot separate rare from abundant. This is the same obstruction that already killed the `second-moment-cooccurrence` approach — the candidate's own "sibling" it explicitly tried to avoid, but the two collapse onto the same aggregate-overlap shape.

## What was actually searched / the honest gap

No application of Ahlswede–Daykin *specifically* to the per-element abundance ≥ 1/2 question was found (searched "Ahlswede-Daykin FKG union-closed Frankl abundance four-functions", and the q-analogue / The Probabilistic Method corpus). The refutation rests on (i) the shape of AD's conclusion (aggregate Σ-product, none of a per-element forcing; a structural fact about the theorem, not a search-absence) and (ii) the only UC application of the engine being the average-size route, which is published and known to stop short (Raz; Lu–Raz), together with (iii) the collapse to the refuted overlap method (Ellis). If someone finds a four-function choice whose conclusion is genuinely per-element (not a correlation/overlap aggregate), that would escape this refutation — but no source offers one.

## Negative controls

2^[n]: every x has δ(x) = |G|/2, so AD must certify all x simultaneously or none strictly — as an aggregate bound it gives no strict per-element separation. A non-union-closed family must break every candidate four-functions inequality (closure genuinely used — this is the one clean positive remaining test). Finiteness via |G| ≤ 2^n.
