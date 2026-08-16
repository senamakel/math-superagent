# Refutation: CA in degree 6 over F_5 is false — the root-difference-collapse char-p break, exercised at a fresh (n,p)

## What I attacked
The **collapse step** of the run's *adopted* approach `root-difference-coloring`:
its claim that the n−1 Hasse-derivative "colorings" force all roots of f to
coincide (so f is a pure power).  That collapse is a char-0-only statement (the
approach's own `charp-break` section says so and names per-color degeneracy as
the break).  I tested at **degree 6 over F_5**, the first degree the refute
folder has never exercised — exercising precisely the mechanism the approach
flags: for n = p+1 = 6, the Hasse derivatives H_2, H_3, H_4 all vanish
identically mod 5, so those colors impose *no* constraint and the two distinct
roots never get forced together.

Attacked statement: "CA holds in degree 6 over F_5" in the Hasse formulation
(a monic sextic over F_5 sharing a non-constant factor with each H_1..H_5 is a
pure power).  **Refuted.**

## The witness (hand-checked against the encoding)
f(x) = x^6 − x^5 = x^5 (x − 1) over F_5.  Two distinct roots {0,1} (0 with
multiplicity 5, 1 with multiplicity 1) ⇒ NOT a pure power.

Hasse derivatives (H_i = Σ_j C(j,i) c_j x^{j−i}, c_6=1, c_5=−1, rest 0):
  H_1 = 6x^5 − 5x^4 = x^5      gcd(f,H_1) = gcd(x^5(x−1), x^5) = x^5  (common factor)
  H_2 = C(6,2)x^4 − C(5,2)x^3 = 15x^4 − 10x^3 = 0   → DEGENERATE (vacuous)
  H_3 = C(6,3)x^3 − C(5,3)x^2 = 20x^3 − 10x^2 = 0   → DEGENERATE
  H_4 = C(6,4)x^2 − C(5,4)x   = 15x^2 − 5x     = 0   → DEGENERATE
  H_5 = C(6,5)x − C(5,5)      = 6x − 1          = x−1  gcd(f,H_5)=x−1 (common factor)
(All binomial coefficients ≡ 0 mod 5 for i = 2,3,4 because 5 | C(6,i), C(5,i); none of
 H_1, H_5 is identically zero, so the hypothesis is not vacuous overall.)

Hypothesis (CA degree 6, Hasse): f shares a non-constant factor with each H_i.
  i=1: factor x^5.   i=2,3,4: H_i ≡ 0 → gcd(f,0)=f, common factor f (vacuous).
  i=5: factor x−1.
Conclusion (CA degree 6): f is (x−a)^6, a single zero.  f has two zeros (0,1) ⇒ not.

Values on F_5 {c0..c4}={0..4}:
  f   = x^6−x^5 : f(0)=0, f(1)=0, f(2)=2, f(3)=1, f(4)=2    → (c0,c0,c2,c1,c2)
  H_1 = x^5     : identity                                  → (c0,c1,c2,c3,c4)
  H_5 = x−1     : H5(0)=4, H5(1)=0, H5(2)=1, H5(3)=2, H5(4)=3 → (c4,c0,c1,c2,c3)
(Hand-verified: f(2)=64−32=32=2, f(3)=729−243=486=1, f(4)=4096−1024=3072=2 mod 5;
 H1(3)=243=3, H1(4)=1024=4; H5 = x−1 exactly.)

## Engine result
`find_counterexample` on `code/refute/ca_deg6_char5.p` returned **refuted**
(CounterSatisfiable).  The 5-element model's f, h1, h5 tables match the
hand computation of x^6−x^5, x^5, x−1 over F_5 entry-for-entry.  All 10
pairwise-distinct axioms kept the domain the genuine field F_5 (same
load-bearing role as in the n=4 p=5 refutation).

## What this does and does not establish
- **ESTABLISHES (char-p):** CA is false in degree 6 over F_5, in the Hasse
  formulation.  **p = 5 is already in the published degree-6 bad-prime list**
  (Castryck–Laterveer–Ounaïes 2012, Table 1: 53 bad primes, first row
  "2 | 5 | 7 | 11 | 13 | 19 | …"), so this is NOT a new counterexample and NOT a
  new bad prime.  Its value is (a) fresh engine corroboration of the
  refute-encoding pipeline at an (n,p) the folder had not touched, and
  (b) the *explicit, computed* char-p break of the adopted root-difference
  approach at exactly the point that approach names: H_2,H_3,H_4 ≡ 0 mod 5
  (per-color degeneracy of the Hasse derivatives for i ≥ p), which removes the
  constraints that would collapse the two roots in char 0.
- **DOES NOT refute** any char-0 claim: not `R-ca-deg4`, not any char-0 rung.
  The witness lives in characteristic 5.  It is a negative control for the
  char-p regime, which is the danger the run's hard constraint already names.
- **Confirms the approach's char-p story is real**, not decorative: the break
  occurs at the predicted site (n = p+1 ⇒ middle Hasse derivatives vanish),
  with the witness x^{p+1}−x^p here at p=5, n=6 — the same algebraic shape
  (x^p·(x−1), two distinct roots) as the canonical char-p family.

## Honest verdict
`refuted` for "CA holds in degree 6 over F_5" (a published known-bad prime,
corroborated; no new degree settled).  The value is a verified hand-and-engine-
checked char-p witness that confirms the root-difference approach's collapse
step must and does fail for i ≥ p, exactly as its char-p-break section predicts.
Nothing here moves the char-0 conjecture.

```claim
id: deg6-char5-refuted
statement: CA in degree 6 over F_5 is false in the Hasse-derivative
  formulation: f = x^6 − x^5 = x^5(x−1) has two distinct roots {0,1} (NOT a
  pure power), shares a non-constant factor with every Hasse derivative
  H_1=x^5, H_2=H_3=H_4=0 (identically degenerate mod 5, so gcd(f,H_i)=f),
  H_5=x−1.  Hence p=5 is a bad prime for n=6, matching the published degree-6
  bad-prime list (Castryck et al. 2012 Table 1, where 5 is among the 53 bad
  primes).  The witness is exactly the root-difference-coloring approach's
  predicted char-p break: for i ≥ p the Hasse derivatives H_2,H_3,H_4 vanish, so
  those "colors" impose no constraint and the two roots never collapse.
hypotheses: characteristic 5, degree 6, Hasse-derivative formulation of the
  char-p CA hypothesis (the formulation of the published bad-prime lists)
holds-here: yes — this is the negative control for the char-p regime and the
  explicit demo that the adopted root-difference approach's collapse step fails
  for i >= p; it does NOT bear on the char-0 rungs (R-ca-deg4 etc.), which
  remain open here.
status: checked — engine-refuted on code/refute/ca_deg6_char5.p (5-element
  model's f,H_1,H_5 tables match x^6−x^5,x^5,x−1 over F_5 entry-for-entry);
  5 confirmed in the published degree-6 bad-prime list (castryck2012, Table 1)
anchor: code/refute/ca_deg6_char5.p; research/sources/castryck2012_degree12_html.full.md Table 1
falsifies: a char-free argument for CA in degree 6, or any version of the
  root-difference-collapse step that does not explicitly use characteristic 0
  and does not break at i >= p (any such proves a false char-p statement)
```
