# Lebesgue Case B — Z[i] mirror verification (unit u kept explicit)

Program: `code/lebesgueB/verify_z[i]_mirror.py`
Output: `code/out/lebesgueB_z[i].captured.txt`
Library: `code/lib/gaussint.py` (exact Gaussian integers), `math.isqrt`/`math.comb`.
All arithmetic exact (Python ints); **no floats**.

This is the *mirror* of `code/caseB/certify_lebesgue_caseB.py`: the prior run
absorbed the unit into the base (`y+i = (c+di)^p`); this run keeps the unit
**explicit**, `y+i = u·(a+bi)^p` with `u ∈ {±1,±i}`, and verifies each step over
the ranges the prompt stated.

Statement being machine-verified: **`x^p - y^2 = 1` has no positive-integer
solution for `p` an odd prime `>= 3`** (Lebesgue Case B).

## Step-by-step results (all PASS)

1. **x even impossible.** If x is even and p >= 2 then `x^p = 0 (mod 4)`, so
   `y^2 = x^p - 1 = 3 (mod 4)`, impossible because squares mod 4 are {0,1}.
   **Proved** (mod-4 argument). Bounded exact falsifier: enumerated all
   `x in [2,10^6]` × `p in {3,5,7,11,13}` with `pow(x,p,big)` and exact
   `isqrt` — **4,999,995 pairs, 0 perfect squares** (y>=1 forces x>=2; x=1
   would give y=0, outside hypothesis). Runtime 1.35 s.

2. **x odd forces y even; gcd is a unit.** x odd ⇒ `x^p` odd ⇒ `y^2+1 = x^p`
   odd ⇒ `y^2` even ⇒ y even. In `Z[i]`: `x^p = (y+i)(y-i)`,
   `N(y+i)=y^2+1` is odd, and `1+i` divides neither factor for even y (re=y
   even, im=±1 odd — `1+i | a+bi ⇔ a,b` same parity). `gcd(y+i,y-i)` verified
   a unit for every even y in `[2,10^4]`. **Proved** + checked on range.

3. **Representation `y+i = u·(a+bi)^p`.** Z[i] is a UFD, factors coprime, p
   odd ⇒ each factor is a unit times a p-th power. Verified: unit absorption
   (each `u` has a p-th root `w` with `(w(a+bi))^p = u(a+bi)^p`), norm
   identity `N(u(a+bi)^p)=(a^2+b^2)^p` (⇒ `x = a^2+b^2`), and **no** random
   `(a,b)` construction yields `Im=1` with `x^p-y^2=1` (0 genuine solutions;
   none expected). **Proved** (structure) + checked.

4. **Binomial lemmas** (exact integer arithmetic).
   - `b | Im((a+bi)^p)` and `a | Re((a+bi)^p)` for all odd primes p (biomial
     structure: odd-k terms carry `b^k`, real terms carry `a^{p-k}` with
     p-k odd). Checked over `a,b in [1,200]`, `p<=97`. **Proved** (structure).
   - **u=±1 endgame:** `Im((a±i)^p) ∉ {±1}` for `a in [1,500]`, odd prime
     `p<=97` — 0 violations over 12,000 checks. *(verified-numerically)*.
   - **u=±i endgame:** `Re((a+bi)^p)=±1` forces `a=1`; `Re((1+bi)^p) ∉ {±1}`
     for `b in [1,500]`, odd prime `p<=97` — 0 violations over 12,000 checks.
     *(verified-numerically)*.

## Falsifier / over-elimination check

The known Catalan solution `3^2 - 2^3 = 1 = (3,2,2,3)` has **y-exponent 3 and
x-exponent 2**, so it sits **outside** this case's hypothesis (`x^p - y^2 = 1`,
i.e. y-exponent 2, x-exponent an odd prime). The program reports
`inside case-B hypothesis? False` — nothing here asserts that the known
solution does not exist; Case B only claims **no** solution with y-exponent 2
and x-exponent an odd prime. **No over-elimination.**

## Honest status

- Steps 1–3 and the divisibility part of step 4 are **proved** (mod-4 parity,
  Z[i] UFD factorisation, norm/unit identities, binomial structure), and
  checked over the stated ranges.
- The two endgame statements `Im((a±i)^p) ≠ ±1` and `Re((1+bi)^p) ≠ ±1` are
  **verified-numerically** over the stated boxes (each 1≤a,b≤500, odd prime
  p≤97), **not proved**. Closing Case B in full also needs the Ljunggren-type
  lemma `T(c,p)` not a square — asserted-classical, not re-proved here (see
  prior `code/out/caseB.note.md`).

```claim
id: lebesgue-caseB-z[i]-mirror-verified
statement: Every step of the Z[i] proof that x^p - y^2 = 1 has no positive
  solution for p an odd prime >= 3 is machine-checked in exact integer
  arithmetic, keeping the unit explicit: (1) x even impossible mod 4, no
  solution for x in [2,10^6], p in {3,5,7,11,13} (4,999,995 exact pairs, 0
  squares); (2) x odd forces y even, gcd(y+i,y-i) a unit for all even
  y in [2,10^4]; (3) y+i = u(a+bi)^p, u in {+-1,+-i}, representation/norm
  consistency, no random (a,b) yields a genuine solution; (4) b | Im((a+bi)^p),
  a | Re((a+bi)^p); Im((a+-i)^p) not in {+-1} for a in [1,500], odd prime
  p<=97; Re((1+bi)^p) not in {+-1} for b in [1,500], p<=97 (12,000 checks
  each, 0 violations).
hypotheses: x,y >= 1, p odd prime >= 3, exact integer arithmetic, ranges stated
  for the numeric parts.
holds-here: yes -- the known solution 3^2 - 2^3 = 1 = (3,2,2,3) has y-exponent
  3 (q=3) and x-exponent 2 (p=2), so it sits OUTSIDE the case hypothesis
  (y-exponent 2, p odd prime). Nothing asserted excludes it; no over-elimination.
status: verified-numerically over the stated ranges with exact arithmetic;
  the mod-4 parity, Z[i] UFD factorisation, norm/unit-absorption and binomial-
  divisibility steps are proved; the two binominal endgames are verified-
  numerically (not proved).
bearing: confirms the Lebesgue Case-B reduction and each stated binomial lemma
  over the requested ranges, so the Z[i] route is consistent (no solution with
  y-exponent 2); full Case B proof still needs the Ljunggren lemma, asserted
  elsewhere.
anchor: code/out/lebesgueB_z[i].captured.txt
```
