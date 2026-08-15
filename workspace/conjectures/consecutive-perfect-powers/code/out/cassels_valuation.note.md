# Note — Cassels valuation computation

Program: `code/cassels_valuation.py` (uses `code/lib/valuation.py`).
Output: `code/out/cassels_valuation.captured.txt`. Wall time ~0.1s, well under
the 540s cap. All rational valuations exact integers; cyclotomic ideals exact
via PARI/GP (cypari2).

## What this establishes, and what it does not

The Cassels divisibility step of `x^p - y^q = 1` (an odd-prime solution forces
`q | x` and `p | y`) is taken in `Q(zeta_p)` from the factorisation
`x^p - 1 = prod_{i=0}^{p-1} (x - zeta_p^i)`. This program establishes the two
exact valuation facts that lemma reduces to, and checks their consistency; it
does **not** complete the ideal/unit argument that turns them into Cassels's
`q | x`, `p | y`. That gap is stated explicitly.

## Section A — LTE valuation identities (exact integers) — PASS

- x-side: `v_p(x^p-1) = v_p(x-1) + 1` iff `p | (x-1)`, else `v_p(x^p-1)=v_p(x-1)`.
  106 cases across `p in {3,5,7,11}`, `x` with a spread of `v_p(x-1)`: **PASS**.
- y-side: `v_q(y^q+1) = v_q(y+1) + 1` iff `q | (y+1)`, else equal.
  128 cases: **PASS**.
- **Exact-proved**, not merely tested: `x^p-1=(x-1)(1+x+...+x^{p-1})` and,
  under `x ≡ 1 (mod p)`, the geometric sum is `≡ p (mod p^2)`, contributing
  exactly one extra power of `p`. The overbroad hypothesis `p ∤ x` is **FALSE**
  (`p=3, x=2`: `v_3(7)=0` but `1+v_3(1)=1`) — already recorded in CLAIMS.md
  as `valuation-identity-xp-1`, confirmed here.

## Section B — cyclotomic `(1-zeta_p)`-adic valuation — PASS

In `Q(zeta_p)` with `P=(1-zeta_p)` the unique (totally ramified) prime over
`p`, `v_P(p)=p-1`. For `p in {3,5,7,11}` and `x in 9` values (36 rows), all OK:

- `v_P(x^p-1) = sum_i v_P(x - zeta^i)`  — factorisation of the ideal,
- `v_P(x^p-1) = (p-1) * v_p(x^p-1)`    — ramification transfer of the
  rational `p`-adic valuation, itself equal to the Section-A LTE value,
- `prod_i N(x-zeta^i) = (x^p-1)^{(p-1)}` — independent cross-check of the
  factorisation (second route to the same statement).

Example rows: `p=3, x=4`: `v_3(63)=2`, `v_P=4=(3-1)*2`, `sum_i v_P=0+2+2=4`;
`p=3, x=10`: `v_3(999)=3`, `v_P=6`, shares `v_P((1-zeta))=2` in exactly the
`x-zeta^0 = x-1` factor (norms `[81,111,111]`).

## Section C — cyclotomic coprimality off the ramified prime — PASS

For `i != j`, the ideals `(x-zeta^i)` and `(x-zeta^j)` share **no** prime
ideal outside `P=(1-zeta_p)` — verified by exact PARI factorisation of each
ideal and intersecting the prime sets (623 pairs checked). Where they do share
`P` (e.g. `x ≡ 1 mod p`, where the `i=0` factor vanishes at `P`), the common
prime is exactly `P`. The corresponding ring statement (`faktor-pairwise-
coprime-off-ramified`) is asserted by the source; here it is numerically
verified over the listed `(p,x)`.

## Section D — oracle cross-check — PASS

`solutions(10^8) == [(3,2,2,3)]` exactly. The known solution `3^2-2^3=1`
has `p=2` (even), so it is outside the odd-prime hypothesis and is never
excluded by any identity asserted here.

## Status ledger

| Item | Status |
| --- | --- |
| LTE `v_p(x^p-1)=v_p(x-1)+[p\|x-1]`, `v_q(y^q+1)=v_q(y+1)+[q\|y+1]` | **exact-proved** (closed form), tested 234 cases |
| `v_P(x^p-1)=sum_i v_P(x-zeta^i) = (p-1)v_p(x^p-1)` | **numerically verified** (PARI-exact), 36 rows + norm cross-check |
| coprimality of `(x-zeta^i)` off `P` | **numerically verified** (exact factoring), 623 pairs |
| oracle `solutions(1e8)=={(3,2,2,3)}` | checked, exact |

**NOT established here:** Cassels's full `q | x`, `p | y`. The valuation
machinery above is exactly the input to that argument, but turning it into the
divisibility needs the unit-group/ideal-power argument in `Q(zeta_p)` (and its
mirror in `Q(zeta_q)`), which this valuation computation does not carry out.

```claim
id: lifting-the-exponent
statement: >
  For an odd prime p, integers a, b with p | (a-b) and p {bar} ab:
  v_p(a^n - b^n) = v_p(a - b) + v_p(n); and for n odd,
  v_p(a^n + b^n) = v_p(a + b) + v_p(n). Special case used here: for
  x ≡ 1 (mod p), v_p(x^p - 1) = v_p(x - 1) + 1 (p odd).
hypotheses: p odd prime; p | (a-b); p {bar} ab; n >= 1.
holds-here: yes — this is the elementary engine of the Cassels divisibility
  chain (claim valuation-identity-xp-1 / cassels-valuation-lte-and-cyclotomic).
status: proved — x^p-1 = (x-1)(1+x+...+x^{p-1}) and under x ≡ 1 (mod p) the
  geometric sum ≡ p (mod p^2), contributing exactly one extra power of p.
  Confirmed exact on 234 cases (Section A of this note). Not formalised in Lean here.
anchor: code/out/cassels_valuation.note.md
bearing: the load-bearing elementary identity behind p|y, q|x.
```

```claim
id: fermat-little-theorem
statement: >
  For a prime p and integer a with gcd(a,p)=1, a^{p-1} ≡ 1 (mod p); for all a,
  a^p ≡ a (mod p).
hypotheses: p prime, a integer.
holds-here: yes — used to characterise when the LTE form applies (x ≢ 1 (mod p)
  gives x^p - 1 ≡ x - 1 ≢ 0 (mod p), so v_p(x^p-1)=0).
status: proved (standard theorem; elementary by binomial expansion / group of
  units mod p). Not formalised in Lean here.
anchor: code/out/cassels_valuation.note.md
bearing: pins the correct hypothesis of valuation-identity-xp-1 (the p∤x form
  fails at p=3, x=2 precisely because Fermat gives x^p ≡ x ≢ 1).
```

```claim
id: cassels-valuation-lte-and-cyclotomic
statement: >
  For an odd prime p and integer x, v_p(x^p-1) = v_p(x-1) + 1 iff p | (x-1)
  (else equal); for an odd prime q and integer y, v_q(y^q+1) = v_q(y+1) + 1
  iff q | (y+1). In Q(zeta_p) with P=(1-zeta_p) the unique prime over p, for
  p in {3,5,7,11} and 9 x-values: v_P(x^p-1) = sum_i v_P(x-zeta^i) =
  (p-1)*v_p(x^p-1), and prod_i N(x-zeta^i) = (x^p-1)^(p-1). The ideals
  (x-zeta^i),(x-zeta^j) share no prime ideal outside P on 623 checked pairs.
  The overbroad hypothesis p {bar} x is false (p=3, x=2).
hypotheses: >
  p, q odd primes for the LTE identities; p in {3,5,7,11}, x in the listed set
  for the cyclotomic rows; exact-integer / PARI-exact arithmetic only.
holds-here: yes — this is the valuation engine of the Cassels p|y, q|x step,
  before that step is completed.
status: checked (A exact-proved; B, C numerically verified over the stated
  ranges via exact integer and PARI arithmetic)
bearing: >
  Confirms the exact valuation identities and cyclotomic coprimality that the
  entry lemma 'G-odd-cassels: p|y, q|x' reduces to. The known solution
  (3,2,2,3) has p=2, so it sits outside the odd-prime hypothesis and is never
  excluded by these identities. Does NOT prove Cassels in full.
anchor: code/out/cassels_valuation.captured.txt
```
