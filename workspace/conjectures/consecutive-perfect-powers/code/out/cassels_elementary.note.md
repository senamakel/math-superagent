# Note — Elementary structure behind Cassels p|y, q|x

Program: `code/cassels/elementary_structure.py`. Output:
`code/out/cassels_elementary.captured.txt`. Exact integer arithmetic only
(integer-Newton roots via `lib.perfectpow.iroot`, then exact `b**q == value`);
no floats anywhere. Wall time 1.17s total, EXIT 0.

## The structural fact being swept

`x^p - 1 = (x-1) * Phi_p(x) = y^q`, with `Phi_p(x) = (x^p-1)/(x-1)`. The gcd
lemma `gcd(x-1, Phi_p(x)) = gcd(x-1, p)` (since `Phi_p(x) == p (mod x-1)`) puts
the gcd in `{1, p}`. If `p | y` is false then `p ∤ x^p - 1 = y^q`, so
`p ∤ x-1` (Fermat), the two factors are coprime, and each is a perfect q-th
power: **x - 1 = a^q and Phi_p(x) = b^q** — the reduced system, with `p ∤ a`.
Conversely any reduced-system pair gives a solution `(x, y) = (a^q+1, ab)` with
`p ∤ y`. So "`Phi_p(a^q+1)` is never a perfect q-th power" is *exactly* the
missing half of Cassels's `p | y`. The mirror `y^q + 1 = (y+1)*Phi_q(-y)`,
`Phi_q(-y) == q (mod y+1)`-style coprimality with `q ∤ y+1`, is the spine of
`q | x`, giving the mirrored reduced system `y = c^p - 1`,
`Phi_q(-y) = ((c^p-1)^q + 1)/c^p` a perfect p-th power.

## Checks run (all exact)

| Check | Content | Result |
| --- | --- | --- |
| 0 | Machinery self-test: roots, Phi values, gcd-lemma base cases | PASS (14/14) |
| 1 | gcd lemma: `gcd(x-1, Phi_p(x)) == gcd(x-1, p)`, p in {3,5,7,11,13,17}, x in [2, 200000] | PASS, 1,199,994 cases, 0 failures |
| 2 | Fermat equivalence: `p | x-1 <=> p | x^p - 1`, same range | PASS, 1,199,994 cases, 0 failures |
| 3 | **Reduced system, spine of p|y**: `Phi_p(a^q + 1)` a perfect q-th power? p ≠ q odd primes, p in {3,5,7,11,13} × q in {3,5,7}, a in [1, 20000], p ∤ a | PASS — 202,886 (p,q,a) cases, **ZERO perfect q-th powers** |
| 4 | **Mirror, spine of q|x**: `Phi_q(-(c^p-1))` a perfect p-th power? c in [1, 5000], q ∤ c | PASS — 46,480 (p,q,c) cases, **ZERO** for c ≥ 2 (y ≥ 1); the 12 c=1 cases are the degenerate `Phi_q(0)=1=1^p` trivial solution `(x,y)=(1,0)`, excluded by y>0 |
| 5 | Calibration at (3,2,2,3): p=2 even (odd-prime hypothesis excludes it); gcd(2,4)=2=gcd(2,2); 2\|3-1; 3\|2+1; Cassels conclusions 2\|2, 3\|3 hold anyway | PASS |
| 6 | Independent root cross-check: gmpy2.iroot on 258 sampled cases, floor roots agree with integer Newton, no spurious exact flags | PASS |

Largest values tested: reduced side `x = 20000^7 + 1` (101 bits),
`Phi_13(20000^7+1)` (1201 bits); mirror side `y = 5000^13 - 1` (160 bits),
`Phi_7(-(5000^13-1))` (959 bits).

## Falsifier discipline

The known solution `3^2 - 2^3 = 1` has p = 2 (even), so the odd-prime
hypothesis of Cassels excludes it from every lemma here; it is never
eliminated. Outside the hypothesis its Cassels conclusions hold anyway
(2 | 2, 3 | 3). No lemma here implies that no solution exists: check 3 (resp.
4) says only that no *reduced-system* solution exists — the branch in which
p ∤ y (resp. q ∤ x) — and the known solution lives in the easy branch
p | x-1 (resp. q | y+1), so the checks are consistent with it.

## Status

Numerical spine of the two Cassels halves, exact-integer, over the stated
ranges. The gcd lemma and Fermat equivalence are exact-proved (elementary
identities, spot-checked independently); the reduced-system sweeps are
numerical (checked) facts about a ≤ 20000 / c ≤ 5000, not proofs for all a, c —
the proof of "Phi_p(a^q+1) never a q-th power for all a" remains the open
content of p|y.

```claim
id: cassels-reduced-system-sweep
statement: >
  Let p != q be odd primes with p in {3,5,7,11,13} and q in {3,5,7}. For
  every integer a in [1, 20000] with p {bar} a, Phi_p(a^q + 1) =
  ((a^q+1)^p - 1)/a^q is not a perfect q-th power (exact integer test,
  integer-Newton root plus b**q == value); 202,886 (p,q,a) cases, zero
  perfect q-th powers. Mirror: for every c in [2, 5000] with q {bar} c,
  Phi_q(-(c^p - 1)) = ((c^p-1)^q + 1)/c^p is not a perfect p-th power;
  46,468 non-degenerate (p,q,c) cases, zero. The 12 degenerate c=1 cases give
  Phi_q(0) = 1 = 1^p, the trivial solution (x,y) = (1,0) excluded by y > 0.
  Together with the gcd lemma gcd(x-1, Phi_p(x)) = gcd(x-1, p) (1,199,994
  cases, 0 failures) and the Fermat equivalence p | x-1 <=> p | x^p - 1
  (1,199,994 cases, 0 failures), this is the numerical spine of Cassels's
  p | y and q | x for odd-prime solutions of x^p - y^q = 1.
hypotheses: >
  p, q distinct odd primes in the stated sets; a in [1,20000] with p {bar} a;
  c in [2,5000] with q {bar} c; exact integer arithmetic throughout.
holds-here: yes — the reduced system is exactly the branch p {bar} y (resp.
  q {bar} x) of a hypothetical odd-prime solution; the known solution
  (3,2,2,3) has p = 2 even, is excluded by the odd-prime hypothesis, and sits
  in the easy branch (2 | 3-1, 3 | 2+1), so it is never eliminated.
status: checked (exact-integer sweep over the stated ranges; gcd lemma and
  Fermat equivalence are exact-proved elementary identities, spot-checked by
  an independent route; roots cross-checked with gmpy2.iroot on 258 samples)
bearing: >
  The reduced-system sweep is the elementary reduction that p|y and q|x turn
  into; a reduced-system solution (a, b) with Phi_p(a^q+1) = b^q would be an
  odd-prime solution with p {bar} y. Zero hits over 202,886 reduced cases
  (and 46,468 mirrored) is the numerical spine of the Cassels divisibility,
  not a proof — the full proof for all a remains open.
anchor: code/out/cassels_elementary.captured.txt
```
