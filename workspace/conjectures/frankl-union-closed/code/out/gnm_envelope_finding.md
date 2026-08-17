# Find: per-family-size rare-element envelope g(n,m) = max(1, m − 2^{n−1})

## Date, scope, provenance
- Program: `code/out/g_nm_min_count.py` (cascade over all UC families on [n], exact
  integer per-element counts; validated against the canonical oracle counts
  2, 12, 120, 4958, 2771102 = A121921 − 1 + off-by-one handling at every level).
  Cross-check: `code/out/g_nm_crosscheck.py` — *direct* brute-force oracle
  (sanctioned n≤4) at n=4, independent of the cascade.
- Output shown in full above. Both programs print every family size reached and
  the exact min present count; no floats anywhere.

## Definition
For a union-closed family F on ground set [n], let
`rare(F) = min over present elements x of count_x(F)` (the least frequent
element's count). Define

`g(n, m) = min over UC families F on [n] with |F| = m of rare(F)`.

The conjecture studied here: **`g(n, m) = max(1, m − 2^{n−1})`** for every m.

## Verification (exact, exhaustive at each n)
- n=1 (2^{n−1}=1): m=1→1, 2→1
- n=2 (=2):      1,1,1,2
- n=3 (=4):      1,1,1,1,1,2,3,4
- n=4 (=8):      1…1 (m=1..9), 2,3,4,5,6,7,8
- n=5 (=16):     1…1 (m=1..17), 2,3,…,16  (NEW — one n past the prior ceiling;
  the old scans stopped at n=4 with exactly this table but never identified it)

Every row: `g(n,m) == max(1, m − 2^{n−1})`. No exceptions in the whole
exhaustive range. Cross-check at n=4 via a *different* code path (direct
subfamily brute force through the oracle `lib.uc`) reproduces every value and
exhibits attaining families.

## Provenance of the lower bound (trivial part)
For an element x, the sets of F not containing x are subsets of [n]∖{x},
at most 2^{n−1} of them; so count_x = m − #(sets lacking x) ≥ m − 2^{n−1}; and
count_x ≥ 1 for every present element. Hence `rare(F) ≥ max(1, m − 2^{n−1})`
for every UC family. **This bound holds with no union-closed hypothesis**
— it is a fact about any family of subsets of [n].

## The content: tightness (nontrivial)
The claim is that for **every** size m, some union-closed family attains it.
That is not automatic: naive constructions ("cube plus extra x-sets") break
union-closure; e.g. at n=4, m=10 the attaining family is
`{∅, {1},{2},{3},{4}, {1,2},{1,3},{1,4},{2,3}, {1,2,3,4}}`
(bitmasks `[0,1,2,3,4,5,6,7,11,15]`, abundances `[6,6,5,2]`, rare=2=10−8) —
a proper "almost-cube" whose added sets are carefully placed to keep the rare
element at exactly 2 while remaining union-closed. Similar explicit witnesses
verified at m=12, 14, 16.

## Relation to known results
- Generalizes the run's WORST(n) = 1/(2^{n−1}+1) extremal: the single size
  m = 2^{n−1}+1 of g gives g = 1, i.e. density 1/(2^{n−1}+1), attained by the
  near-n-cube (sourced, Das–Wu/Nagel sharpness). The envelope shows that at
  *every* size the least-frequent count can be driven to the subset-count
  bound. So the extremal near-n-cube is not isolated: it is a point on a
  tight family of extremals.
- At sizes m ≤ 2^{n−1}+1, g(n,m)=1: a UC family of at most 2^{n−1}+1 sets can
  always have a singleton-frequency element. Note claim C (no degree-1 element
  without an abundant element) is consistent: those families DO have abundant
  elements; degree-1 is the rare element, another is abundant.
- `g>1` starts at m = 2^{n−1}+2, i.e. rare ≥ 2 there; consistent with the
  n=5 claim C check (degree-1 element families all have an abundant element).

## Status
- **Verified-computational**: exhaustive, exact, n ≤ 5, both code paths agree;
  and the oracle confirms the constructions for n in 1..6 (all m). This
  verifies instances of the proof; it is not the proof itself.
- **Proved (general statement)**: g(n,m) = max(1, m−2^{n−1}) for all n, all m.
  The lower bound is elementary (no union-closure needed). The tightness (an
  attaining UC family of every size) is proved constructively — the proof is
  the prose in §Proof below; the program verifies its instances, it does not
  replace the argument.
- **First falsifier** for the general statement: any n with some UC family of
  size m whose least-frequent count is strictly below max(1, m−2^{n−1}).
  n=6 is above the exhaustive-enumeration ceiling (cascade level-6 infeasible),
  but the constructive proof covers all n, so the general statement needs no
  further enumeration.

## Proof of tightness (the general statement)

Lower bound (elementary, no union-closure): for a present element x, the m−c_x
sets of F avoiding x are subsets of [n]∖{x}, at most 2^{n−1} of them; and every
present element has count ≥ 1. Hence `rare(F) ≥ max(1, m − 2^{n−1})` for every
family F, UC or not.

**Size lemma (Lemma: every size is realisable as an upset).** For every N and
every s in [0, 2^N], there is an upward-closed subfamily (upset) U ⊆ 2^[N] with
|U| = s. *Proof (induction on s, from the whole cube downward, equivalently on
the complementary size):* the complement D = 2^[N]∖U of an upset U is a
downset (if A ∈ D and B ⊆ A then B ∈ D, else A would lie above a member of U).
If U ≠ 2^[N], then D ≠ ∅, so by finiteness D has an inclusion-maximal element x.
Moving x from D into U (setting U′ = U ∪ {x}) leaves U′ an upset: any strict
superset of x is not in D (x is maximal in the downset D), hence already in U,
and x itself is in U′. Thus |U′| = |U| + 1 and U′ is an upset. Starting from the
minimal upset U = ∅ (size 0) and applying this move repeatedly realises every
size 0, 1, …, 2^N. ∎
**Careful — the move direction is the subtly correct one.** Moving a MAXIMAL
element of the complementary downset D into the upset U preserves up-setness
(x's strict supersets are already in U). The mirror-image move — removing a
maximal element of an up-set — does NOT preserve up-setness (a member below it
may now have no upper bound in the family), as the half-density probe's first
up-set generator discovered the wrong way
(`code/out/half_density_probe.py`, fixed in P2; the canonical cascade's
minimal-removal test `(y|x)==x` is the right one). Any later reader who
re-derives this lemma or implements an up-set enumerator should use the
downset-maximal / upset-minimal direction only.

*Direction warning (recorded per directive 20 on deferring the Lean
formalisation of this lemma): the move that works is moving an
inclusion-MAXIMAL element of the complementary DOWNSET in — that preserves
up-setness, because every strict superset of such an x was already in U.
Removing a maximal element of the UP-SET does NOT preserve up-setness (the
removed element's supersets would be left) — that is the shape of the bug that
broke a buggy up-set generator in agent-run-78, and it is the step anyone
formalising or re-deriving this size lemma must get in the correct direction.*

Every upset is union-closed (a union of members has them all as subsets, so is
again a member), so the size lemma gives a union-closed subfamily of every size.

**Construction A (m ≥ 2^{n−1}+1).** Put c = m − 2^{n−1} (so 1 ≤ c ≤ 2^{n−1}).
Let G ⊆ 2^[n−1] be an upset of size c (exists by the size lemma), and set
F = 2^[n−1] ∪ {A ∪ {n} : A ∈ G}. Then F is union-closed (2^[n−1] is a subcube;
union with a member of G ∪ 2^[n−1] stays in G ∪ 2^[n−1] since G is upward-closed),
|F| = 2^{n−1} + c = m, and element n appears in exactly c sets. Every x < n
appears in at least 2^{n−1} ≥ c sets; so rare(F) = c = m − 2^{n−1} by the
avoiding-set lower bound.

**Construction B (m ≤ 2^{n−1}+1).** Let H ⊆ 2^[n−1] be an upset of size m−1
(exists by the size lemma; m−1 ≤ 2^{n−1}), U its union, and set
F = H ∪ {U ∪ {n}}. F is union-closed (H upward-closed; U∪{n} is the top of the
construction and contains every member as a subset), |F| = m, and element n
appears in exactly 1 set (masked by B: its only occurrence is {n}∪U). So
rare(F) = 1 = max(1, m − 2^{n−1}).

Together A and B give, for every n and every m, a union-closed F with
|F| = m and rare(F) = max(1, m − 2^{n−1}), matching the lower bound. ∎

```claim
id: gnm-envelope-rarest-floor-tight
statement: Define g(n,m) = min over union-closed families F on [n] with |F| = m
of rare(F), where rare(F) is the least frequent present element's count. Then
g(n,m) = max(1, m - 2^{n-1}) for every m, verified EXHAUSTIVELY and EXACTLY for
n <= 5 (two code paths: the projection/up-set cascade g_nm_min_count.py and the
independent direct brute-force oracle g_nm_crosscheck.py at n=4, both against the
canonical oracle lib.uc; no floats). The lower bound
rare(F) >= max(1, m-2^{n-1}) is elementary and needs NO union-closure: the m -
c_x sets avoiding x are subsets of [n]\{x}, at most 2^{n-1} of them. The
tightness (an attaining union-closed family of EVERY size m) is the nontrivial
half; equalities with explicit witnesses at n=4, m=10,12,14,16. The near-n-cube
at m=2^{n-1}+1 is a point on this tight family, generalising the sourced
Das-Wu/Nagel extremal.
hypotheses: F a union-closed family of subsets of [n], |F| = m; rare its least
frequent present element's count.
holds-here: yes
status: verified-computational for n <= 5 (exhaustive, exact, cross-checked),
plus oracle confirmation of the constructions for n in 1..6 (all m);
and the GENERAL statement g(n,m) = max(1, m-2^{n-1}) for all n, all m is PROVED
constructively -- tightness holds for EVERY n. The proof is the prose in
code/out/gnm_envelope_finding.md §Proof (anchor); the program
code/out/gnm_envelope_verify.py verifies its instances at n in 1..6, it is not
the argument.
Bearing: the lower-bound half (sets avoiding x are subsets of the other n-1
elements, so rare >= m - 2^{n-1}) is PROVED and union-closure-independent. The
tightness half is ALSO PROVED constructively for every n; the proof is the
prose in code/out/gnm_envelope_finding.md §Proof, anchored there, and the
programs verify its instances. The one step the general claim rests on — the
size lemma, that every size s in 0..2^N is realisable as an upward-closed
subfamily (upset) of 2^[N] — is proved by induction there (complement an upset
is a downset, a maximal element of the non-empty complementary downset can be
moved in and the new family is still an upset), not merely cited. Then for
m >= 2^{n-1}+1 with c = m-2^{n-1}, F = 2^[n-1] u {A u {n} : A in G} with G an
upset of 2^[n-1] of size c (size lemma) is union-closed, |F|=m, and element n
appears in exactly c sets, so rare = c by the avoiding-set lower bound. For
m <= 2^{n-1}+1, F = H u {U u {n}} with H an upset of size m-1 (size lemma), U
its union, is union-closed and element n has degree 1, so rare=1. The programs
verify (union-closed, |F|=m, rare == max(1, m-2^{n-1})) for ALL n in 1..6, ALL
m in 1..2^n, and exhaustively cross-checked over all n<=4 families — that is
instance verification, not the argument.
CONSEQUENCE: the extremal near-n-cube at m=2^{n-1}+1 is one point on a tight
family of extremals at every size, generalising the sourced Das-Wu/Nagel
extremal; the rarest-element floor is attained at ALL sizes for all n.
anchor: code/out/gnm_envelope_finding.md §Proof (the proof text is the anchor —
        the avoiding-set lower bound, the two constructions A for
        m >= 2^{n-1}+1 and B for m <= 2^{n-1}+1, and the size lemma proved by
        induction). The programs are its VERIFICATION of instances, not the
        proof: code/out/gnm_envelope_verify.py (verifies the constructions
        through the oracle for n in 1..6, all m), code/out/gnm_envelope_verify.captured.txt,
        code/out/g_nm_min_count.py and code/out/g_nm_crosscheck.py (the
        exhaustive n<=5 / independent n=4 oracle cross-check).
```

## What it is NOT
- Not a proof of Frankl's conjecture (g constrains the *minimum* density, the
  hard direction; it is a lower bound on rare density, matching the known
  sharp Das–Wu extremal family). To restate plainly: g measures the rarest
  element's count (the minimum density), and Frankl asks about an abundant
  element (the maximum). A tight lower-bound envelope on the minimum says
  nothing about whether some element exceeds half the sets; it is therefore
  not a proof of Frankl, whatever its strength.
- Not a new bound on the *maximum* abundance.
- Not a new constant and not a route to one: the tightness here is a structural
  fact about which union-closed families exist at each size, not a statement
  about the 1/2 threshold.