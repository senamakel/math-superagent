# Pattern-finder survey — re-run of the run's sequences and one new correction

Scope: every integer sequence the run has actually computed, re-examined, plus
one new exact computation. Each item states whether it is checked, settled
elsewhere, or too short to support a regularity.

---

## 1. Abundance-profile WORST denominators — settled, not new

WORST(n) = 1/(2^{n-1}+1) for n=1..4, achieving family the near-k-cube. I re-ran
`abundance_profile.py` (n=1..4, exhaustive oracle scan): WORST = 1/2, 1/3, 1/5,
1/9 exactly. The denominators 2,3,5,9,17 are OEIS A000051 = 2^n+1 (catalogued
closed form). This matches `abundance_profile_analysis.md` and the Das–Wu Nagel
sharpness (`daswu-nagel`, sourced theorem). **No regularity here is new**; the
values are checked, the general statement is a sourced theorem. I corroborate
`nearcube_check.py` through n=5: profile [2^{n-2}+1 repeated n-1 times, 1],
rare element density exactly 1/(2^{n-1}+1).

## 2. Union-closed enumeration counts — catalogued, ruled out

counts 3, 13, 121, 4959 = OEIS A121921. Already handled; a recurrence there
says nothing about abundance and is out of scope by directive.

## 3. FC(4,n) = 5, 7, 10, 12 — too few terms, no regularity

Re-ran `analyze_sequence([5,7,10,12])`: differences 2,3,2 (not a low-degree
polynomial); the only periodicity reported is residues mod 5 with period 2,
which is an artifact of the 4-term sample (10,12 ≡ 5,7 mod 5) and not a
structural pattern. Not catalogued (oeis miss already recorded). **No honest
conjecture can be offered on 4 terms.** Extending FC(4,n) is the SMT/coder
route (`pulajwood-fc-values`: 10, 12, and lower bounds beyond), not a
sequence-tool job. NOTHING FURTHER here.

## 4. k-fold iid barrier c_k — already proved

c_k strictly decreasing in k≥2, max at k=2 = (3−√5)/2, corroborated to k=60.
Recorded and proved in `kfold_barrier_claim.md`. No new sequence analysis.

## 5. NEW: mobius_algebra_check.py FAIL is a checker bug, not a refutation

`code/out/mobius_algebra_check.py` prints FAIL on idempotent expansion and
orthogonality for B_3, B_4. I inspected its logic: it tests `if p:` (a
nonempty dict) to detect a nonzero product. A zero-coefficient product like
`{15: Fraction(0,1)}` is a nonempty dict, so **zero is reported as truthy** and
every such row is a bogus FAIL. The mathematics was never refuted.

I wrote `code/out/mobius_verify2.py`, which detects zero correctly
(`all(c == 0 for c in v.values())`). Exact result:

```
B_2: expansion_ok=True  orthogonal_ok=True  dim_ok=True
B_3: expansion_ok=True  orthogonal_ok=True  dim_ok=True
B_4: expansion_ok=True  orthogonal_ok=True  dim_ok=True
```

So the two Möbius-algebra facts that ground the
`mobius-algebra-join-irreducibles` approach **do hold** on the Boolean lattice:
a = sum_{b≥a} e_b (Möbius inversion), e_a·e_b = δ_ab·e_a (orthogonality), and
dim(L·a) = |↑a|. The earlier FAIL must not be treated as a counterexample to
that grounding — and is not.

**Falsifier tested:** a genuinely nonzero product e_a·e_b with a≠b, or an
expansion a ≠ sum_{b≥a} e_b, on any of B_2..B_4. None exists; all pass. This
is a second, independent check (different zero-detection and the standard Möbius
recursion) confirming the construction, which is also the classical
Solomon/Knop 2007 result in the literature — so it is sourced + checked.

---

## Which regularity is most likely to yield a derivation

The one structural regularity the run has that actually constrains a minimal
counterexample is the **abundance-profile extremal**: the unique worst case
(min min-density) is the near-k-cube with value 1/(2^{n-1}+1). It is not a
route to a new bound (it is a lower bound on the minimum density, the hard
direction, and equals the sharp Das–Wu extremal), but it fixes the shape any
proposed barrier must beat. The other candidate sequences offer nothing exact
to derive: the counts are catalogued/ruled out, FC(4,n) has too few terms, and
c_k is already proved.

The one new verified item this pass adds is the Möbius-algebra grounding being
confirmed against a bogus FAIL — a dead-end detection, not a new conjecture.
