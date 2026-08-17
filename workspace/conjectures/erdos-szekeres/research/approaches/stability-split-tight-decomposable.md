```approach
idea: A STABILITY / classification lemma, not a new separator and not a count:
every n-avoiding set X of size 2^{n-2} is "split-tight or decomposable" in the
Baek–Balko sense — it contains a split-n-gon (a cap and a cup sharing the
rightmost point, a+u = n+2) or is recursively decomposable. If this structural
dichotomy held, ES(n) ≤ 2^{n-2}+1 would follow from the exact 2^{k-2}+1 split
threshold (Baek–Balko, Thm 6) PLUS the decomposable theorem (Thm 8), because an
extremal set that is split-tight at the top level contributes its count from the
already-proved exact recurrence. The line-split induction is dead at n=7; the
replacement is NOT a new cutting geometry (that is wedge-split / halfplane-
separator, both about the separator object) but a classification claim about the
configuration's own structure, stated uniformly over all sets rather than on the
construction template.

mechanism: Baek–Balko's exact threshold is ES_split(k) = 2^{k-2}+1, proven by
counting down-sets in [k-2]×[k-2] under the bounding-box constraint r+s ≤ k−1
(the off-band down-sets are exactly the convex-vs-split gap — see the adopted
signotope-downset approach). A "split k-gon" is the relaxation of a convex
k-gon where a cap and a cup (two monotone chains) share only the rightmost
endpoint. The conjecture is exactly the statement that no n-avoiding set of 2^{n-2}
points is "split-free at every level". So, naming the theory first: this is a
stability/uniqueness statement (the problem.md's own diagnosis — "an exact bound
has to be a stability or uniqueness statement"), and the correct formal target
is a DECOMPOSITION certificate: every n-avoiding 2^{n-2}-set has a recursive
binary decomposition X = A ⊔ B, each of size ≤ 2^{n-3} and (n−1)-avoiding, with
A deep below B as in the split/decomposable structure (NOT necessarily separated
by a single line — the n=7 failure kills exactly the line-separated version).
The recursion depth is the new variable: each level at most halves the
"convexity demand", so 2^{n-2} = 2·2^{n-3} is the leaf count of a binary tree of
depth n−2 whose leaves are points, and the n-gon-avoidance is exactly the
absence of a full-depth alternating branch. This is DIFFERENT from the closed
G-split (which required a LINE cut and fails at n=7 on the template): here the
split is by the configuration's own recursive (cup/cap-sharing) structure, the
n=7 template 32-point set is expected to be decomposable/split-tight so it is
NOT a counterexample, and the claim is quantified over every n-avoiding set of
size 2^{n-2} — a structural property, precisely what GOAL criterion 4 asks for.

status: adopted

decision-note (this round's convergence): Adopted as a STRUCTURAL / GOAL-4
certificate, NOT as a route to the bound (the split-tight deductive step is
UNSOUND — killed-by below — and Thm 8 is asserted-by-source). What is adopted is
the *lifted sub-claim* that research surfaced and the librarian had already
flagged as the one genuinely useful untouched computation: test, with the run's
own verified exact oracle, whether the run's canonical es_construct extremal
sets satisfy Baek–Balko's DEF decomposition (the "deep below" definition is on
disk verbatim, lines 425–443 of the held SoCG PDF). This is a certificate the
run can produce TODAY, independent of the unproved Theorem 8, over order types
from the Aichholzer database (n ≤ 10, realizable, with realizing sets). The
recursive-decomposition certificate X = A ⊔ B with each half (n−1)-avoiding and
A deep below B, at size 2^{n-2} = 2·2^{n-3}, is a finite, exact, enumerable
claim — precisely what GOAL criterion 4 asks for — and a clean classification
table is already a new partial result whether or not the dichotomy itself holds.
The first-step below is tool_builder-workable today.

first-step: (tool_builder, today, exact, over es_construct and then Aichholzer)
(1) DEFine deep-below and decomposable exactly (both on disk); implement an
exact predicate with lib/es_geom orientation determinants: A is deep below B iff
y(A)<y(B) AND every point of B lies above every line through two points of A AND
every point of A lies below every line through two points of B. (2) Positive
control: verify es_construct(n) is EXACTLY decomposable under this definition at
n=5,6,7 (recursively: decompose X into A⊔B with each half (n-1)-avoiding,
|A|,|B|≤2^{n-3}, A deep below B). Confirm the binary tree {leaves} = X  with
each level at most halving the convexity demand. (3) The lifted test: over every
REALIZABLE n-avoiding 2^{n-2}-point order type in the Aichholzer database up to
n=10 (8-point 5-avoiding, 16-point 6-avoiding, 32-point 7-avoiding if present),
test whether each admits a recursive deep-below decomposition; report the
survival statistics (how many are neither split-tight nor decomposable). If
NONE is, that is the first lifted all-sets structural result; if the first
counterexample appears, it immediately becomes ROOT's restricted-class evidence
and refines the target. Also verify the split n-gon / split-free status of each
(exact cap/cup sharing-rightmost-point scan). State the search space and worker
count; the exact oracle is the referee. The one external upgrade: fetch JCTA
2026 full text (DOI 10.1016/j.jcta.2026.106195) for the proof of Thm 8, which
is the only piece that would promote the decomposable branch from asserted to
verified.

killed-by: (the DEDUCTIVE step to the bound, NOT the adopted structural claim)
The route "split-tight OR decomposable ⟹ ES(n)≤2^{n-2}+1" is unsound at the
split-tight branch: a SPLIT k-gon is NOT a convex k-gon. From the held Baek–Balko
text, "Split k-gon ... an a-cap and a u-cup that share the rightmost point, with
a+u=k+2; it has k or k+1 points; IF they also share the leftmost point, the k
points are in convex position." So a split n-gon shares only the rightmost point
and need not produce n points in convex position — that strictness is EXACTLY
where the hardness lives (ROOT.md §5.1). The split threshold 2^{k-2}+1 already
forces a split n-gon in EVERY 2^{n-2}+1-set, so split-tightness is automatic at
that threshold and can never discriminate extremal from non-extremal; and at the
extremal size 2^{n-2} the split threshold does NOT force a split n-gon (the tight
witness es_construct(a=u=k) is split-FREE, not split-tight), so the two disjuncts
do not cover all extremal sets on any known basis. The decomposable branch rests
on Thm 8, asserted-by-source, proof omitted in SoCG, deferred to JCTA 2026 — hence
the adoption below is of the structural certificate, not of the deductive bound.

precedent: Baek & Balko, "The Erdős–Szekeres Conjecture Revisited", SoCG 2025,
doi 10.4230/LIPIcs.SoCG.2025.13 — full text held and digested. ESsplit(k)=2^{k-2}+1
proved-in-source (Thm 3/4 via down-set injectivity Lemma 10 and delta-colorings
Lemma 11; the geometric lower-bound Lemma 12 and count Lemma 9 are "proof omitted",
deferred); CONFIRMS the definition of split k-gon (shares only rightmost) and the
fact that convex = sharing both endpoints; CONFIRMS decomposable sets satisfy the
ES conjecture (Thm 8) but that the proof is omitted in the SoCG version (asserted-
by-source, JCTA 2026 pending); CONFIRMS es_construct at a=u=k is the tightness
witness (no split k-gon) — i.e. the extremal 2^{n-2}-point set is split-FREE, not
split-tight, so "split-tight" is false of the canonical extremal set. Aichholzer
order-type database (aichholzer-order-db, n≤10, enumerated with realizing sets) is
the enumeration source for the finite test. The related "decomposable" notion is
developed by Balko–Kynčl–Langerman–Pilz, "Induced Ramsey-type results and binary
predicates for point sets" (ENDM 2017, doi 10.1016/j.endm.2017.06.023): every
decomposable set is (k,2)-Ramsey; they explicitly leave open "whether there is a
(2,2)-Ramsey point set that is not decomposable" — the same stability gap the run
is probing. NO published source proves that every n-avoiding 2^{n-2}-set is
split-tight or decomposable; that dichotomy is the run's own claim, untested over
realizable order types. The SAT/signotope target parallel: the signotope analogue
(every signotope on ≥2^{k-2}+1 vertices has a weak k-gon) is OPEN and equivalent
to a Goodman–Pollack conjecture (baek-balko-signotope-analogue-open).

falsified-by: a realizable n-avoiding set of size 2^{n-2} that is neither
split-tight (no split n-gon) nor decomposable — an explicit, exact-coordinate
witness that refutes the dichotomy and shows a new structural failure mode (and
immediately becomes ROOT's restricted-class evidence). Separately, the deductive
step "split-tight ⟹ convex bound" is already falsified by the split≠convex
distinction (killed-by), so the dichotomy alone cannot settle ES.
```
