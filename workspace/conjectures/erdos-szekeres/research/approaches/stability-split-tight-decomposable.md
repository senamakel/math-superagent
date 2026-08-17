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

status: grounded-as-structural-conjecture (the dichotomy is a real, novel,
enumerable structural claim worth testing — GOAL criterion 4 material — but the
inventor's stated deductive route to the bound is UNSOUND, see killed-by; do not
treat this as a proof route until the split-tight→convex step is repaired)

killed-by: (the deductive step to the bound, not the structural claim itself)
The route "split-tight OR decomposable ⟹ ES(n)≤2^{n-2}+1" is unsound at the
split-tight branch, because a SPLIT k-gon is NOT a convex k-gon. From the held
Baek–Balko text (research/summaries/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md):
"Split k-gon ... an a-cap and a u-cup that share the rightmost point, with
a+u=k+2. It has k or k+1 points; IF THEY ALSO SHARE THE LEFTMOST POINT, the k
points are in convex position." So a split n-gon shares only the rightmost point
and need not give n points in convex position — indeed that strictness is EXACTLY
where the hardness lives (ROOT.md §5.1: "the obstruction that makes the original
conjecture hard survives only in the strictness of 'convex' versus 'split
convex'"). A set being split-tight therefore contributes NO convex-n-gon forcing;
it only says it contains a relaxation of one. The split threshold theorem
2^{k-2}+1 already guarantees EVERY 2^{n-2}+1-point set contains a split n-gon —
so split-tightness at the threshold size is automatic for every set and can never
be the discriminator that separates extremal from non-extremal. Moreover (a) the
decomposable theorem (Baek–Balko Thm 8) is itself only asserted-by-source in this
library ("The proof of Theorem 8 is omitted" in the held SoCG version; deferred
to JCTA 2026), so the decomposable branch rests on an unverified theorem; and (b)
the dichotomy is stated at size 2^{n-2}, where split-tightness is NOT guaranteed
(at that size, even the split threshold does not force a split n-gon — the tight
extremal witnesses are split-free), so the two disjuncts do not cover all extremal
sets on any known basis. WHAT SURVIVES: the dichotomy as a NOVEL TESTABLE
STRUCTURAL CLAIM about 2^{n-2}-point n-avoiding sets — a genuine classification
question that, if it held (or produced a counterexample), would be a real partial
result (GOAL criterion 4), but it does not by itself resolve the upper bound.

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

first-step: (tool_builder, today, exact, over Aichholzer order types) Positive
control on the template: verify es_construct(5,6,7) is decomposable / contains
top-level split-n-gons (exact cap/cup sharing-rightmost-point scan with
lib/es_geom at n=5,6,7). Then the real first target: over every REALIZABLE
n-avoiding set of size 2^{n-2} in the Aichholzer order-type database up to n=10
(8-point 5-avoiding, 16-point 6-avoiding, 32-point 7-avoiding if present), test
the dichotomy: is each one split-tight (contains a split n-gon) or decomposable?
State the survival statistics: how many n-avoiding 2^{n-2}-sets are neither. If
NONE is (the 2^{n-2}-size gives enough room to force a split/decomposable
certificate), that is the first lifted (all-sets) structural result of the run;
if the FIRST counterexample (a realizable 2^{n-2}-set that is neither split-tight
nor decomposable) appears, that is the counterexample that kills the dichotomy
and refines the target. Concretely first compute over all 8-point and 16-point
realizable order types (small enough to enumerate exactly, in Aichholzer's n≤11
database) the FULL table: which are n-avoiding, which are split-free, which are
decomposable — this is a finite, several-CPU-job enumeration with a stated
search space and the exact oracle as referee. Speculative core to attack first:
whether "not decomposable at any level" forces a split-n-gon (i.e. extremal sets
are split-rich), or whether a split-free decomposable-free realizable set exists
at some n. NOTE the sharpened framing: this first-step is valuable as a STRUCTURAL
classification (does every no-convex-n-gon 2^{n-2}-set have a recursive
deep-below decomposition, even if not line-separated?), NOT as a route to the
bound — the decomposable branch is the only one that gives convex position, and
it is asserted-by-source.

falsified-by: a realizable n-avoiding set of size 2^{n-2} that is neither
split-tight (no split n-gon) nor decomposable — an explicit, exact-coordinate
witness that refutes the dichotomy and shows a new structural failure mode (and
immediately becomes ROOT's restricted-class evidence). Separately, the deductive
step "split-tight ⟹ convex bound" is already falsified by the split≠convex
distinction (killed-by), so the dichotomy alone cannot settle ES.
```
