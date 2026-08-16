# Refutation: CA in degree 6 over F_2 is false — p=2 is a bad prime for n=6, exercised at a fresh (n,p)

## What I attacked
The statement "CA holds in degree 6 over F_2" in the Hasse formulation (a
monic sextic over F_2 sharing a non-constant factor with each H_1..H_5 is a
pure power), plus the char-p break of the root-difference-coloring collapse
step at the **first** published degree-6 bad prime, p = 2 — an (n,p) the
`code/refute/` folder had never exercised (it had only n=6 at p=5).

## The counterexample (hand-checked against the encoding)
f(x) = x^6 + x^2 over F_2.  Since x^4+1 = (x+1)^4 in char 2,
f = x^2(x^4+1) = x^2(x+1)^4 — TWO distinct roots {0 (mult 2), 1 (mult 4)},
so NOT a pure power.

Hasse derivatives H_i = Σ_j C(j,i) c_j x^{j−i}, c_6 = 1, c_2 = 1, rest 0:
  H_1 = C(6,1)x^5 + C(2,1)x          = 6x^5 + 2x          ≡ 0   (deg. vacuous)
  H_2 = C(6,2)x^4 + C(2,2)           = 15x^4 + 1          ≡ x^4+1  (divides f)
  H_3 = C(6,3)x^3                    = 20x^3              ≡ 0   (deg. vacuous)
  H_4 = C(6,4)x^2                    = 15x^2              ≡ x^2     (root 0)
  H_5 = C(6,5)x                      = 6x                 ≡ 0   (deg. vacuous)
(All the binomial coefficients are ≡ 0 mod 2 for i = 1,3,5 because
C(6,i), C(2,1) ≡ 0; H_2 and H_4 are non-degenerate, so the hypothesis is not
vacuous overall.)

Values on F_2 = {c0=0, c1=1}:
  f  = x^6+x^2 : f(0)=0, f(1)=0   ->  (c0, c0)
  H_1 = 0      : (c0, c0)
  H_2 = x^4+1  : H2(0)=1, H2(1)=0 ->  (c1, c0)
  H_3 = 0      : (c0, c0)
  H_4 = x^2    : H4(0)=0, H4(1)=1 ->  (c0, c1)
  H_5 = 0      : (c0, c0)

Hypothesis (CA degree 6): shares a root with each H_i.
  i=1 (H_1=0): X=0 (f(0)=0, h1(0)=0).   i=2: X=1 (f(1)=0, H2(1)=0).
  i=3 (H_3=0): X=0.                     i=4: X=0 (f(0)=0, H4(0)=0).
  i=5 (H_5=0): X=0.
Conclusion (CA degree 6): f is a pure power, i.e. one of
  g0 = x^6        : (c0, c1)
  g1 = (x+1)^6 = x^6+x^4+x^2+1 : (c1, c0)
f = (c0, c0) is neither -> counterexample.

## Engine result
`find_counterexample` on `code/refute/ca_deg6_char2.p` returned **refuted**
(CounterSatisfiable).  The 2-element model's f, h1..h5 tables match the hand
computation of x^6+x^2, 0, x^4+1, 0, x^2, 0 over F_2 entry-for-entry.

## What this does and does not establish
- **ESTABLISHES (char-p):** CA is false in degree 6 over F_2.  **p = 2 is
  already the first entry of the published degree-6 bad-prime list**
  (Castryck–Laterveer–Ounaïes 2012, Table 1, read verbatim: begins
  "2 | 5 | 7 | 11 | 13 | 19 | …").  So this is NOT a new counterexample —
  it is fresh engine corroboration at an (n,p) the refute folder had not
  touched, exercising the very first (and smallest) degree-6 bad prime.
- **Confirms the break story at a second n=p+1**: like the p=5 case, the
  witness x^2(x+1)^4 (the canonical x^{p+1}−x^p family at p=2) collapses the
  middle Hasse derivatives — here H_1,H_3,H_5 ≡ 0 mod 2 — removing the
  constraints that would force the two distinct roots together in char 0.
- **DOES NOT refute** any char-0 claim (not `R-ca-deg4`, not any char-0 rung).
  This witness lives in characteristic 2 and is a negative control for the
  char-p regime only.

## Adversarial check of the root-difference identity (the directive's target)
The directive asked for an adversarial reading of the adopted approach's
foundation, the identity H_i(f)(x) = e_{n−i}(x−β_1,…,x−β_n), whose capture
(`code/out/rootdiff_identity.captured.txt`) does not exist.  This refuter
cannot execute Python (no execution tool here), so I cannot write that
capture.  What I can do is check the identity's truth independently:

- Identity 1 is the textbook Taylor expansion f(x+t) = Π_j((x−β_j)+t) =
  Σ_i e_{n−i}(x−β_1,…,x−β_n) t^i, so H_i(f) = [t^i]f(x+t) =
  e_{n−i}(x−β_1,…,x−β_n) — correct, exactly, char-free (Hasse derivative).
  Spot-checked symbolically: n=4, i=1, H_1(f)=f' = Σ_j Π_{k≠j}(x−β_k)
  equals e_3(x−β_1,…,x−β_4) (the four 3-subsets), term for term.  Holds.
- Identity 2, R_i = Res_x(f,H_i) = Π_j H_i(β_j), is the standard
  resultant-norm identity (monic f kills the leading-coefficient factor):
  Res_x(f,g) = Π_{f(β)=0} g(β).  Correct.
- So the identity has no char-p break and no sign/constant subtlety for monic
  f, as the scripts assert.  The break the approach predicts is downstream
  — per-color degeneracy for i ≥ p (H_i ≡ 0 or constant, so that "color"
  imposes no constraint).  That is exactly the mechanism this n=6, p=2
  witness exercises at a second fresh (n,p): H_1,H_3,H_5 all vanish, so only
  H_2 and H_4 constrain at all, and the two roots are free to remain two.

The capture still needs a code-executing role to run
`code/rootdiff/verify_rootdiff_identity.py` to the exact path in the task
(`code/out/rootdiff_identity.captured.txt`); the refuter's contribution is the
independent confirmation that the identity is true where the script's
failure criterion says it could be false.

## Honest verdict
`refuted` for "CA holds in degree 6 over F_2" — a genuine, hand-and-engine
checked char-p counterexample at a fresh (n,p), corroborating the published
degree-6 bad-prime list's first entry (p=2) and the root-difference approach's
predicted break mechanism.  Nothing here moves the char-0 conjecture.

```claim
id: deg6-char2-refuted
statement: CA in degree 6 over F_2 is false in the Hasse-derivative
  formulation: f = x^6+x^2 = x^2(x+1)^4 has two distinct roots {0,1} (NOT a
  pure power), shares a non-constant factor with every Hasse derivative
  H_1=0, H_2=x^4+1, H_3=0, H_4=x^2, H_5=0 (H_1,H_3,H_5 degenerate identically
  mod 2, so gcd(f,H_i)=f for those).  Hence p=2 is a bad prime for n=6,
  matching the first entry of the published degree-6 bad-prime list (Castryck
  et al. 2012 Table 1, which begins 2, 5, 7, 11, 13, 19, ...).  This is the
  second n=p+1 exercise of the root-difference-coloring approach's predicted
  char-p break (middle Hasse derivatives vanish for i >= p, removing the
  constraints that would collapse the two roots in char 0).
hypotheses: characteristic 2, degree 6, Hasse-derivative formulation of the
  char-p CA hypothesis (the formulation of the published bad-prime lists)
holds-here: yes — negative control for the char-p regime at a fresh (n,p);
  does NOT bear on the char-0 rungs (R-ca-deg4 etc.), which remain open here
status: checked — engine-refuted on code/refute/ca_deg6_char2.p (2-element
  model's f,H_1..H_5 tables match x^6+x^2, 0, x^4+1, 0, x^2, 0 over F_2
  entry-for-entry); 2 confirmed as the first entry of the published degree-6
  bad-prime list read verbatim (castryck2012 Table 1, lines 191-215)
anchor: code/refute/ca_deg6_char2.p; research/sources/castryck2012_degree12_html.full.md Table 1
falsifies: a char-free argument for CA in degree 6, or any version of the
  root-difference-collapse step that does not explicitly use characteristic 0
  and does not break at i >= p (any such proves a false char-p statement)
```
