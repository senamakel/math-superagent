# Descent sub-claim: two-route verification (q<=37, m<=8, r,s<=500)

Executed `code/exp2_descent/verify_subclaim.py`, EXIT 0. Captured output in
`code/out/verify_subclaim.captured.txt`.

## The sub-claim tested

For q an odd prime, m >= 1, r, s >= 1 with gcd(r,s) = 1:

    r^q - 2^{mq-2} s^q = ±1

has only the solution (q, m, r, s) = (3, 1, 1, 1).

Via the bijection x = 2·r^q + 1, y = 2^m·r·s this is the exponent-2 Case-A
descent form of Lebesgue's theorem x^2 - y^q = 1, whose only solution is
(3,2,3).

## Two independent routes

- **Route 1 (direct)**: exact-integer sweep of r^q - 2^{mq-2}s^q in {+1,-1}
  over odd primes q <= 37, m in [1,8], r, s in [1,500], gcd(r,s)=1. Because the
  routine filters the known (3,1,1,1) before appending, "total found 0 / known
  0" reads as **zero counterexamples** on this range.
- **Route 2 (Lebesgue equivalence)**: odd x <= 200000, test whether x^2 - 1 is
  an exact q-th power. Only (q,x,y) = (3,3,2) found.

## Cross-check

The route-1 image {(q, x=2r^q+1, y=2^m r s)} restricted to x <= 200000 equals
the route-2 full image: both are exactly {(3,3,2)}. Reported `True`.

## Settled

The descent sub-claim holds (only the known solution) over the union of the two
swept ranges — strictly wider in all three parameters (q, m, r,s) than the
earlier `thue_descent_full` (q<=13, m<=6, r,s<=200) and `thue_run2` (q<=29,
m<=7, r,s<=300) sweeps. This extends the verified-numerically range, not a
proof.

## Where the known solution sits

The known solution (3,1,1,1), mapping to (3,2,3), is *returned* by the
sub-claim (it is the sole solution), never excluded. Falsifier check: the
sub-claim does not assert "no solution"; it asserts uniqueness, and the unique
solution is the known one. Satisfied, not refuted.

## Status

verified-numerically (two independent exact-integer routes, agreeing). Not a
proof.

```claim
id: exp2-descent-subclaim-extended-verify
statement: For q odd prime <= 37, m in [1,8], r,s in [1,500] with gcd(r,s)=1,
  r^q - 2^{mq-2}s^q = ±1 has only the solution (3,1,1,1), and its
  Lebesgue image x^2 - y^q = 1 (x<=200000, q<=37) is only (3,2,3).
hypotheses: q odd prime, m>=1, r,s>=1, gcd(r,s)=1; bound q<=37, m<=8, r,s<=500.
holds-here: yes (known solution is the unique solution returned, not excluded)
status: checked (verified-numerically, two independent exact-integer routes)
bearing: extends the Case-A descent sub-claim sweep (was q<=29); the native
  setting is deg-2 (Z[sqrt(y)] / descent on q), per the rising-sea board.
anchor: code/out/verify_subclaim.captured.txt
```
