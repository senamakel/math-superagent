# Audit: does any automorphism source use the (refuted) "fixed set is a coclique or a smaller srg" lemma?

Directive 28 audit. The folklore lemma — *under an automorphism of an
srg(v,k,1,2), the fixed-point set is a coclique or a smaller strongly regular
graph* — is REFUTED on the BvLS control: `srg(243,22,1,2)` has an order-2
automorphism fixing exactly 27 vertices inducing a 6-regular graph with
constant λ=1 but non-constant μ ∈ {0:216, 2:324}, neither a coclique nor an
SRG (claim `fixed-set-lemma-fails-on-bvls`; verified in
`code/out/fixed_set_lemma*.captured.txt`; holds on rook(3)).

The audit question: does ANY published automorphism result this run cites for
(99,14,1,2) depend on that lemma (or a variant) as a load-bearing step?

## The central distinction that resolves the audit

The refuted folklore lemma and the real result the four sources use are
DIFFERENT claims — this is the key finding.

- **Folklore lemma (refuted):** a *general* assertion for every srg(v,k,1,2)
  that Fix(g) is a coclique or a smaller srg. False on BvLS. It originated in
  this run's own approach note (`research/approaches/orbit-matrix-residual-group.md`,
  first-step (4)); it is not in any of the four sources as a stated assumption.
- **Makhnev–Minakova dichotomy (valid, what the sources actually use):** for
  THE SPECIFIC (99,14,1,2), the character theory of the Bose-Mesner algebra
  (Higman method) proves Fix(g) of a prime-order automorphism is one of a
  finite character-theoretically-determined list — singleton (p=2,7), empty
  (p=3,11), or triangle (p=3) (Thm 1 / Thm 1.6); for involutions, one of seven
  listed subgraphs including the n-coclique and the 3×3 grid (= srg(9,4,1,2))
  (Prop 2). These are CONSEQUENCES of the character computation, specific to
  the parameters (99,14,1,2), not an assumption of the folklore lemma.

The sources do not ASSUME "Fix is a coclique or smaller srg"; they PROVE, case
by case, what Fix is from the eigen-character arithmetic and then check
integrality of χ2(g) = (4α0(g) + α1(g) − 18)/7, and the orbit-matrix refinements.
The refuted folklore lemma therefore does **not** appear as a load-bearing step
in any of the four sources.

## Per-source verdicts

### Makhnev–Minakova 2004 — NO uses it
- Conclusion audited: **|G| divides 2·3³·7·11**; if 2|G| then |G| divides 42.
- Method (reproduced in the Makhnev lecture `makhnev-symmetric-graphs-automorphisms-lecture.full.md`,
  lines 179–301, which is Makhnev's own account of his [3] = Makhnev–Minakova):
  Higman character theory of the Bose-Mesner algebra. The fixed-subgraph step
  is the parameter-specific dichotomy (Prop 2 list of 7 possible Fix(t) for an
  involution; Thm 1 for prime order), pruned by integrality of the projected
  character χ2(g). No use of a general "coclique-or-smaller-srg" lemma.
- Note: the character formula is exactly
  χ2(g) = (4α0(g) + α1(g) − 18)/7 with spectrum 14¹, 3⁵⁴, −4⁴⁴ (confirmed in
  the lecture). The fixed-subgraph analysis is fully dependent on these
  parameter-specific values.

### Behbahani–Lam 2011 / Behbahani 2009 thesis — NO uses it
- Conclusion audited: **only primes 2 and 3 can divide |Aut Γ|**; order-3
  automorphisms are **fixed-point-free**.
- Method (primary text `behbahani-2009-phd-thesis-pdf.full.md`): the
  orbit-matrix method (genOrbit + SRG backtrack program) fed by the
  Makhnev–Minakova fixed-point dichotomy (Thm 1.6 quoted in full at lines
  913–959: "the subgraph induced by the fixed points of p" is singleton/empty/
  triangle). The primes are pruned by orbit-length arithmetic and integer
  character conditions (upper bound on number of fixed points, §3.5, built by
  algebraic/eigenvalue techniques). No use of the folklore lemma.
- Note (gap): the 2011 paper's primary text could not be placed (paywalled);
  the thesis is the primary source for the "only primes 2,3; order-3
  fixed-point-free" claim. Both derive from the Makhnev–Minakova dichotomy,
  not the refuted folklore lemma.

### Cesarz–Woldar 2025 — CANNOT CONFIRM FROM LIBRARY; NO EVIDENCE IT USES IT
- Conclusion audited: if 7 | |G| then G ≅ Z₇; consequently if 2 | |G| then
  |G| divides 6. Plus no order-14 automorphism (Stage 1).
- Method as documented in the abstract/landing pages and the run's notes:
  described as re-proving the predecessor results **computer-free**, via the
  Higman character / fixed-point-subgraph (construction-of-fixed-subgraphs)
  method.
- **Caveat (a finding about the library):** the Cesarz–Woldar proof body is
  NOT on disk. `automorph-putative-conway-99-graph.full.md` and
  `cesarz-woldar-automorph-conway99.full.md` are both abstract/landing pages
  (no §s, no lemmas). The run's consolidated understanding of their 2|6 and
  7⟹Z₇ proofs rests on the abstract + the run's own character-theoretic
  reconstruction. On the evidence in the library, nothing indicates they use
  the folklore lemma — but an absolute "NO, they don't, with proof-level
  certainty" cannot be given without the proof body. Verdict: **no evidence it
  uses the lemma; proof body absent, so flagged, not guaranteed.**
- The Frob(21) computer-assistance nuance (arXiv vs ALCO) is unrelated to the
  fixed-set lemma and remains the only flagged caveat on this source.

### Crnković–Maksimović 2020 — NO uses it
- Conclusion audited: **no automorphism group is isomorphic to Z₆, S₃, Z₉, or
  E₉**; order 2^a·3^b with b ∈ {0,1}; order-3 automorphisms fixed-point-free.
- Method (full text `crnkovic-maksimovic-full-pdf.full.md`, §7): computer-
  assisted orbit-matrix method. It takes Behbahani–Lam's Thm 7.1 (order-3
  fixed-point-free) as given, enumerates orbit-length distributions
  (for Z6/S3: (0,0,1,16), (0,0,3,15), (0,0,5,14); for E9/Z9: (0,0,11)), computes
  the orbit matrices, and checks refinement to the normal Z₃. The fixed-point
  facts come from the Makhnev–Minakova/Behbahani–Lam dichotomy. No use of the
  folklore lemma.

## Overall safety verdict

**No published automorphism result this run cites for (99,14,1,2) uses the
refuted folklore fixed-set lemma as a load-bearing step.** The four cited
conclusions — |G| divides 2·3³·7·11; if 7|G| then G ≅ Z₇; if 2|G| then |G|
divides 6; only primes 2,3; no Z₆/S₃/Z₉/E₉; order-3 fixed-point-free — all
stand on the parameter-specific Makhnev–Minakova character dichotomy and the
orbit-matrix method, NOT on the false general lemma. The refutation of the
folklore lemma (claim `fixed-set-lemma-fails-on-bvls`) removes only the run's
own approach-note assumption; it does not touch any cited automorphism result.

The one honest caveat: **Cesarz–Woldar's proof body is not in the library**,
so that source is "no evidence it uses the lemma (and its method as described
is the character method)" rather than a fully-checked "NO". If the run ever
needs to cite CW's results as the strongest form, fetching the proof body
(when the library re-opens) would close this; as it stands, the run's
automorphism constraints are safe to rely on either way, because the same
conclusions are independently reached by Behbahani–Lam and Makhnev–Minakova.

## Files
- Sources: `research/sources/makhnev-symmetric-graphs-automorphisms-lecture.full.md`,
  `research/sources/behbahani-2009-phd-thesis-pdf.full.md`,
  `research/sources/crnkovic-maksimovic-full-pdf.full.md`,
  `research/sources/automorph-putative-conway-99-graph.full.md`,
  `research/sources/cesarz-woldar-automorph-conway99.full.md`.
- Summaries: `research/summaries/makhnev-symmetric-graphs-automorphisms-lecture.md`,
  `research/summaries/behbahani-2009-phd-thesis.md`, `research/summaries/crnkovic-maksimovic-full-pdf.md`,
  `research/summaries/automorph-putative-conway-99-graph.md`.
- Related note: `research/notes/fixed-set-lemma-fails-on-bvls.md`, `research/notes/automorphism-orders-consolidated.md`,
  `research/notes/wilbrink-order11-makhnev.md`.

```claim
id: audit-fixed-set-lemma-no-source-uses-it
statement: None of the four automorphism sources cited for (99,14,1,2) —
  Makhnev–Minakova 2004, Behbahani–Lam 2011, Cesarz–Woldar 2025,
  Crnković–Maksimović 2020 — uses the (refuted) folklore lemma "the fixed set
  of an automorphism is a coclique or a smaller srg" as a load-bearing step.
  All four rest instead on the parameter-specific Makhnev–Minakova character
  dichotomy for (99,14,1,2) (Fix of prime-order g is singleton/empty/triangle;
  for involutions one of seven listed subgraphs) pruned by integrality of
  chi2(g)=(4*alpha0+alpha1-18)/7, plus the orbit-matrix method. Hence the
  refutation of the folklore lemma on BvLS (claim fixed-set-lemma-fails-on-bvls)
  does not undermine any cited automorphism conclusion.
hypotheses: the four sources as they exist in the library; Cesarz–Woldar's
  proof body is absent (only abstract/landing pages), so its verdict is
  "no evidence uses it, not guaranteed" per the evidence on disk.
holds-here: yes — directly answers directive 28's audit question for exactly
  the four named sources.
status: sourced/read (primary full texts of Makhnev lecture, Behbahani thesis,
  Crnković–Maksimović §7 read directly; Cesarz–Woldar abstract-only).
bearing: the automorphism-constraint conclusions (|G| divides 2.3^3.7.11;
  7||G| => Z7; 2||G| => |G||6; primes {2,3}; no Z6/S3/Z9/E9; order-3
  fixed-point-free) remain safe to cite. The refutation of the folklore
  fixed-set lemma only removes the run's own approach assumption; it is not a
  finding against the literature.
anchor: research/notes/audit-fixed-set-lemma-automorphism-sources.md
contradicts: none — the refuted lemma was never load-bearing in these sources;
  it resolves the concern by showing the sources use a different, valid lemma.
```

## What the audit leaves open
- The Cesarz–Woldar proof body (whether their computer-free 2|6 and 7⟹Z₇
  proofs internally use any fixed-set structural claim akin to the folklore
  lemma). Library-closed forbids acquisition now; the conclusion is
  independently reached by Behbahani–Lam/Makhnev–Minakova, so no citable
  result is at risk.
