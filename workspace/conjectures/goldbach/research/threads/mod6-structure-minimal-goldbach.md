# MOD-6 STRUCTURE OF MINIMAL GOLDBACH PARTITIONS — pattern-finder report

**What the sequence tools established, exactly.**

## 1. Proved (elementary congruence) — verified to 0 violations everywhere

For even n with minimal Goldbach partition n = p(n) + q(n) (p(n) least prime):

- n ≡ 2 (mod 6), p(n) ≠ 3  ⟹  p(n) ≡ 1 (mod 3)
- n ≡ 4 (mod 6), p(n) ≠ 3  ⟹  p(n) ≡ 2 (mod 3)
- n ≡ 0 (mod 6): unconstrained

Proof: primes > 3 are ±1 (mod 3); p + q = n forces the residues; a 0-residue
prime must be 3 itself.  This is the exact cause of Oliveira e Silva's
"white dots vs yellow dots" (p ≡ 1 mod 3) frequency anomaly — a congruence,
not a probabilistic phenomenon.  Full detail, the closed-form identity
C[(2,1)] = #{n ≡ 2 mod 6, n − 3 composite}, and the 0-violation data are in
`research/threads/mod6-structure-minimal-goldbach.md`.

## 2. Conjectured (data) — attacked, survives to S ≤ 10^7 and the OeS tail

**(C)** p > 7  ⟹  S(p) ≢ 0 (mod 6).
**(C')** p > 3: S(p) ≡ 2 (mod 6) ⟺ p ≡ 1 (mod 3), S(p) ≡ 4 (mod 6) ⟺ p ≡ 2
(mod 3); only p ∈ {5, 7} have S(p) ≡ 0 (mod 6), with S(5) = 12, S(7) = 30.

- Head data N = 10^7 (112 minimal primes, p(n) ≤ 733): residue table
  {(1,2): 56, (2,4): 52, (1,0): 1, (2,0): 1} — the two (·,0) entries are
  exactly p = 5, 7.  (C) holds for all 108 primes p > 7.
- OeS Top-50 tail (p ~ 10^4, S ~ 10^18): residue table exactly
  {(1,2): 30, (2,4): 20}, 0 (·,0) entries.
- Falsifier: a prime p > 7 with S(p) ≡ 0 (mod 6).  None found.  The naive
  uniformity expectation (~54 of 108 in the 0-class) is exceeded by 54 — the
  avoidance is exact over the whole computed range, so it is a real pattern,
  not noise.  Under the prime k-tuple conjecture it may be provable: it says
  the earliest prime q ≥ p with p + q ≡ 0 (mod 6) and p + q prime never beats
  the earliest q with p + q ≡ 2 or 4 (mod 6) once p > 7.

## 3. Sequences catalogued and not

| sequence | OEIS | structure |
|---|---|---|
| r(n) (partition count) | A045917/A002375 | no poly, no const-coeff recurrence ≤10, no mod-6 structure |
| g(n) (minimal prime p(n)) | A020481 | — |
| S(p) (first appearance) | **not in OEIS** | no poly, no recurrence ≤8, all even, (C') residues |

## 4. Where it stands

- The mod-3 law is a **proved** theorem (elementarily), verified numerically
  to 0 violations and formalisable in Lean.
- (C)/(C') is a **live conjecture** that survived a deliberate search for its
  stated falsifier at three scales (10^5, 10^7, 10^18) by two independent
  methods (ordered pair enumeration and vectorized assignment, agreeing
  exactly on all overlapping values).
- No contradiction with the thesis (Chen-prime exceptional set): the mod-3
  law constrains all Goldbach primes of n ≡ 4 (mod 6) to ≡ 2 (mod 3), which
  is exactly the class the thesis targets; (C) adds that first-appearance
  values avoid n ≡ 0 (mod 6) after p = 7.

**Files:** code/extract_sequences.py, code/extend_sp*.py, code/verify_mod3_structure.py,
code/closedform_mod3.py, code/test_tail_oes.py, code/crosscheck_sp.py,
code/rn_mod_structure.py, code/test_oes_claims.py; outputs in code/out/*.txt.
