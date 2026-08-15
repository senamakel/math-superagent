# Note — cross-prime minus-class-number divisibility sweep

Program: `code/crossprime_sweep.py` (written this run's earlier sessions, never
executed until now). Outputs captured:
- `code/out/crossprime_sweep.captured.txt` (bound 60)
- `code/out/crossprime_sweep200.captured.txt` (bound 200)

All arithmetic is exact-integer. The h^-(Q(zeta_p)) value is computed exactly
via `lib.cyclo.h_minus` (analytic formula `2p * prod_{chi odd}(-1/2 B_{1,chi})`
in exact cyclotomic arithmetic) and matches OEIS A000927 for every odd prime
reached (3,5,7,...,199).

## What was computed

For every distinct odd-prime pair p < q <= B, evaluate the cross-prime
minus-class-number divisibility condition

    q | h^-(Q(zeta_p))   AND   p | h^-(Q(zeta_q)).

This is a necessary condition on a hypothetical odd-prime solution x^p - y^q =
1 (the descent's claimed consequence, analogous to the classical Cassels /
cross-prime Bernoulli divisibility). The matrix is an exact-integer O(n^2)
pass over the precomputed h^- values.

Results:

| bound | surviving pairs (both divisibilities hold) |
| --- | --- |
| 60 | none |
| 200 | **only (47, 139)** |

The sole survivor (47,139): `139 | h^-(Q(zeta_47)) = 695 = 5*139` (true) and
`47 | h^-(Q(zeta_139))` (true).

## Independent verification of the surviving pair's death by the other condition

The known solution (3,2,2,3) has p=2 even, so it is excluded-by-hypothesis
(is_odd_prime_pair=False), never rejected — matching the calibration of every
other condition in this run. The h^- sequence matches OEIS A000927 exactly for
all 45 odd primes <= 200, so the divisibility values are trusted.

A hypothetical odd-prime pair must satisfy BOTH the cross-prime h^- condition
AND the double-Wieferich congruences (q^(p-1)==1 mod p^2, p^(q-1)==1 mod q^2).
The unique cross-prime survivor below 200, (47,139), fails both Wieferich
congruences (checked exactly: `pow(139,46,47^2)!=1`, `pow(47,138,139^2)!=1`),
so it is not a double-Wieferich pair. Hence **no odd-prime exponent pair with
both primes < 200 can be a hypothetical solution**, given both necessary
conditions believed (Cassels -> Wieferich descent, and the h^- cross-prime
divisibility).

## Honest scope

This is a **verified-numerical** elimination over a finite range, not a proof
for all pairs: it eliminates p,q < 200 (with the known double-Wieferich pair
(83,4871) outside that range, and h^-(4871) astronomically out of computational
reach). It is a genuine, executed, checked partial result: the cross-prime h^-
condition is not vacuous (it has exactly one survivor below 200) and that
survivor is killed by the unrelated double-Wieferich condition.

```claim
id: crossprime-hminus-divisibility-sweep
statement: >
  For every distinct odd-prime pair p < q <= 200, the exact-integer
  evaluation of q | h^-(Q(zeta_p)) AND p | h^-(Q(zeta_q)) has exactly one
  surviving pair, (47,139). That unique survivor fails the double-Wieferich
  congruences q^(p-1)==1 mod p^2 and p^(q-1)==1 mod q^2 (both false). Known
  solution (3,2,2,3) has p=2 even and is excluded-by-hypothesis, not
  rejected. The h^- sequence matches OEIS A000927 for all 45 odd primes
  <= 200.
hypotheses: >
  p,q distinct odd primes; exact integer arithmetic throughout; the h^-
  formula and the double-Wieferich necessity are taken as believed (not
  re-proved here); the elimination is over the finite range p,q < 200, not
  all pairs.
holds-here: yes (the known solution lies outside the odd-prime hypothesis)
status: checked (verified-numerically over p,q < 200; not a proof for all pairs)
bearing: >
  Two independent necessary conditions on a hypothetical odd-prime solution
  jointly eliminate every odd-prime pair below 200. The cross-prime h^-
  condition is shown non-vacuous (unique survivor) and that survivor is
  killed by the double-Wieferich condition. The open gap remains the
  odd-prime descent over pairs above 200, where h^-(4871) is infeasible.
anchor: code/out/crossprime_sweep200.captured.txt, code/out/crossprime_sweep.captured.txt
```
