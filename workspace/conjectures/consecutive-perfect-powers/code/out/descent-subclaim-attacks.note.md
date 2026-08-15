# Descent sub-claim attacks — settled this run

Date: this run. Programs executed (all exact integer arithmetic, no floats):

- `code/refute/thue_descent_check.py` → `code/out/thue_descent_check.captured.txt`
- `code/refute/thue_run2.py` → `code/out/thue_run2.captured.txt`
- `code/rfixed23_proof.py` → `code/out/rfixed23_proof.captured.txt`

## What was attacked

The intermediate Thue-type/descent sub-claim in the exponent-2 odd-prime case:

> r^q - 2^{mq-2} s^q = ±1, with q an odd prime, m ≥ 1, r,s ≥ 1, gcd(r,s)=1,
> has only the solution q=3, m=1, r=s=1.

If any other pair solved it, the descent lemma as stated would be FALSE — a
located gap.

## Results

`thue_descent_check.py`: known-solution calibration reproduces (q=3,m=1) →
[(1,1,-1)]. Sweep over q ≤ 13, m in 1..6, r,s ≤ 200: **0 counterexamples**
(signatures ±1) other than the known (q=3,m=1,r=s=1).

`thue_run2.py`: wider sweep over q ≤ 29, m in 1..7, r,s ≤ 300: **0 counterexamples**
other than the known solution.

`rfixed23_proof.py`: full reproduction of the x^2 - y^3 = 1 descent:
brute x≤10^4 finds only (3,2) [plus trivial (1,0)]; sympy parity facts confirm
x-even impossible and x-odd reduces to 4k(k+1)=y^3; the {k,k+1}={c^3,2d^3}
distribution holds on the single cube-bearing odd x; Thue c^3-2d^3=±1 swept to
d≤10^6 gives only (1,1,-1); maps back to (x,y)=(3,2). Direct cross-check to
y=10^5 and against the oracle solutions(N) for N in {1e4,1e6,1e8} all = (3,2,2,3).

## Status

Verified-numerically (finite range; not an unbounded proof). The range stated:
q≤29 odd primes, m≤7, r,s≤300 for the sub-claim; the fixed-exponent p=2 case
swept to the stated bounds and cross-checked by two independent routes.

## Anchor

captured output: `code/out/thue_descent_check.captured.txt`,
`code/out/thue_run2.captured.txt`, `code/out/rfixed23_proof.captured.txt`

```claim
id: exp2-descent-subclaim-no-extra
statement: The descent equation r^q - 2^{mq-2} s^q = ±1 (q odd prime, m>=1,
  r,s>=1, gcd(r,s)=1) has no solution other than (q,m,r,s)=(3,1,1,1) in the
  verified finite range q odd prime <= 29, m <= 7, r,s <= 300.
hypotheses: q odd prime, gcd(r,s)=1, exponents to stated bounds.
holds-here: yes; the known-solution (q=3,m=1,r=s=1) is the unique hit and is
  NOT eliminated.
status: verified-numerically
bearing: confirms no located gap in the exponent-2 odd descent; does NOT prove
  the unbounded statement.
anchor: code/out/descent-subclaim-attacks.note.md
```
