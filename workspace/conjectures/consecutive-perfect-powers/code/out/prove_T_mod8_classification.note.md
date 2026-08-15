# Case B key lemma strengthened: mod-8 classification of T(c,p)

Programs: `code/prove_T_c_odd_nonsquare.py`,
`code/prove_T_mod8_classification.py`
Outputs: `code/out/prove_T_c_odd_nonsquare.captured.txt`,
`code/out/prove_T_mod8_classification.captured.txt` (both EXIT 0 in the
Python layer; the `Bad substitution` on stderr is a `/bin/sh` PIPESTATUS
shell quirk, not a program failure — the program body ran to completion and
printed RESULT).

## Setting

Case B of Catalan's equation: `x^p - y^2 = 1`, p an odd prime, x, y > 0.
The machine-certified reduction (claim `exp2-case-B-reduction`,
`code/out/caseB.note.md`) forces

    x = c^2 + 1,   y = c·m,   m^2 = T(c, p) := Σ_{k=0}^{p-1} (c^2+1)^k

for positive integers c, m.  Whether `T(c, p)` is ever a square is exactly
the Case-B obstruction.  That lemma was previously only verified numerically
(c <= 2000, odd prime p <= 101, 0 squares) and asserted by the classical
Ljunggren-type theorem `(X^n-1)/(X-1) = Y² ⇒ (n,X,Y) = (4,7,20),(5,3,11)`.

## New result (PROVED here, not a numerical check)

For every odd prime p >= 3 the residue of `T(c,p)` mod 8 depends only on
`c mod 8` and `p mod 8`, by three exact formulas (each certified over wide
ranges by exact integer arithmetic):

| c | x = c²+1 mod 8 | T(c,p) mod 8 | square-viable? |
|---|---|---|---|
| c odd | 2 | 7 | **never** (7 ∉ {0,1,4}) |
| c ≡ 0 (mod 4) | 1 | p | only if p ≡ 1 (mod 8) |
| c ≡ 2 (mod 4) | 5 | 3p−2 | only if p ≡ 1 (mod 8) |

Hand proofs:
- **c odd**: c² ≡ 1 (mod 8) so x ≡ 2 (mod 8).  For u ≡ 2 (mod 8), uᵏ ≡ 0
  (mod 8) whenever k ≥ 3 (u = 8t+2 is even and uᵏ divisible by 2ᵏ, and
  2ᵏ = 8·2^{k−3}).  Hence T ≡ 1+2+4 ≡ 7 (mod 8) for **any** p ≥ 3,
  independent of p.  Squares mod 8 are {0,1,4}; 7 is never a square.
  ⇒ **the entire c-odd branch (x even) is impossible**, unconditionally.
- **c ≡ 0 (mod 4)**: c² ≡ 0 (mod 8), x ≡ 1 (mod 8), every xᵏ ≡ 1,
  T ≡ p (mod 8); square iff p ≡ 1 (mod 8) (odd prime residue 1 only).
- **c ≡ 2 (mod 4)**: c² ≡ 4 (mod 8), x ≡ 5 (mod 8); terms alternate
  1,5,1,5,... so T ≡ (p+1)/2·1 + (p−1)/2·5 ≡ 3p−2 (mod 8); square iff
  3p−2 ≡ 1 (mod 8), i.e. p ≡ 1 (mod 8).

## Consequence

The mod-8 square obstruction alone **proves** `T(c,p)` is a non-square for
every `(c,p)` except possibly **c even AND p ≡ 1 (mod 8)**.  All other
classes — in particular the whole c-odd branch, and all c even with
p ≢ 1 (mod 8) — are settled by a two-line modular argument, with no recourse
to Ljunggren.

The direct isqrt square-test over c in [1,4000] and the first 13 odd primes
finds **0 actual squares** in the 48,000 eliminated-class pairs (must be 0,
and is) and 0 squares in the remaining open classes (consistent, not proof).

## Falsifier / over-elimination

The known solution `(3,2,2,3)` has y-exponent 3, so it is outside Case B's
hypothesis (y-exponent 2) entirely; no over-elimination.  Within Case B the
claim "T(c,p) is a non-square for all but c even & p≡1 mod 8" is a negative
statement about a hypothetical second solution, consistent with the oracle
`(3,2,2,3)` unique below 10^8.

## Claim

```claim
id: exp2-caseB-t-mod8-classification
statement: For Case B of Catalan (x^p - y^2 = 1, p odd prime >= 3), the
  reduction gives x = c^2+1, y = c*m, m^2 = T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k
  for positive integers c, m.  T(c,p) mod 8 is: 7 for c odd (for every p >= 3),
  p mod 8 for c == 0 (mod 4), and 3p-2 mod 8 for c == 2 (mod 4); 7, and all
  of these except p == 1 (mod 8), are non-squares mod 8.  Hence T(c,p) is
  NOT a perfect square for every (c,p) except possibly c even AND p == 1
  (mod 8).  In particular the whole c-odd branch (x even) is impossible.
hypotheses: p an odd prime >= 3, c >= 1, exact integer arithmetic; three
  residue formulas certified over wide exact ranges, the mod-8 congruence
  proof is unconditional (no dependence on Ljunggren).
holds-here: yes -- the known solution has y-exponent 3, outside Case B's
  hypothesis (y-exponent 2); no over-elimination.  The claim is a negative
  statement about hypothetical second solutions with y-exponent 2.
status: checked (proved mod-8 classification; residual classes c even,
  p == 1 mod 8 are left to the classical Ljunggren theorem, not proved here).
bearing: strengthens the Case-B key lemma from "verified numerically +
  classical-asserted (full theorem)" to "proved elementary for all classes
  except c even & p == 1 mod 8"; the only remaining Case-B gap is that one
  residue class, closed by the asserted Ljunggren-type theorem.
anchor: code/out/prove_T_mod8_classification.captured.txt, code/out/prove_T_c_odd_nonsquare.captured.txt
```
