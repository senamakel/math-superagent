# The identity A_k(i) = |Δ_k(i)| fails on the primes — sign-coherence dead

Program: `code/out/check_fwd_diff_identity.py` (written earlier, never run);
executed this cycle, output `code/out/check_fwd_diff_identity.captured.txt`.
Independent sampler (fresh rng, uniform even gaps in [2,500], 60 trials,
1839 triples): `code/out/check_fwd_diff_identity_sampled.captured.txt`.

## What was checked

The proposed approach `research/approaches/sign-coherence-forward-differences.md`
reduces Gilbreath to a signed linear recurrence via the identity

```
A_k(i) = |Δ_k(i)|,   Δ_k(i) = Σ_{j=0}^k (−1)^j C(k,j) A_0(i+j)
```

(the signed forward-difference triangle D, built by D_{k+1}(i) = D_k(i) −
D_k(i+1)). If that identity held, `A_k(1)` would be the absolute value of a
binomial transform of the initial gaps and could be attacked by parity. The
identity holds iff every adjacent pair feeding an absolute-value step has
`u·v ≥ 0` (since |u−v| = ||u|−|v|| iff u·v ≥ 0).

## Result (exact integers, oracle-first)

- rows A_1..A_5 reproduce problem.md exactly.
- D matches its closed form (after fixing the sign exponent: the recurrence
  builds (−1)^j, not (−1)^{k−j} — the two differ by the global factor
  (−1)^k and only |D| is compared downstream, so the substance is
  unaffected; the bug was in the assertion, caught by the assertion).
- **first violation anywhere: (k,i) = (3,2)**: |Δ_3(2)| = 4 but the actual
  A_3(2) = 0 — *inside* the leading {0,2} block (row A_3 = 1,2,0,0,0,...).
  Fatal for the approach: the positions claimed to be linear include the
  very cells where it breaks.
- **first violation at position 1: k = 4**: Δ_4(1) = −6 (|Δ| = 6) vs
  A_4(1) = 2; then failing in 17 of the 20 rows checked.
- mechanism: first adjacent opposite-sign pair (D_3(2), D_3(3)) = (2, −2);
  signed rows oscillate [4, −4, 4, −4] where the actual rows are constant 0.
- generic: derived D_1(i) = −gap_i, D_2(i) = gap_{i+1} − gap_i, so any
  strict local extremum of the gap sequence (primes: gaps 2,4 at i=2) gives
  opposite signs at k=2, hence failure at k=3. The sampler fails all 60
  random 2-then-odds within 3 rows (first failures at (k=3, i=0..3)).

## Status

Refuted at its base step; do not re-propose. Any linearization must survive
the (k=3, i=2) cell: |Δ_3(2)| = 4, A_3(2) = 0.

```claim
id: fwd-diff-identity-refuted
statement: The identity A_k(i) = |Δ_k(i)| (iterated absolute difference
  equals the absolute value of the signed forward difference Δ_k(i) =
  Σ_{j=0}^k (−1)^j C(k,j) A_0(i+j)) is FALSE on the prime triangle: first
  violation at (k,i)=(3,2), where |Δ_3(2)|=4 but A_3(2)=0 — inside the
  leading {0,2} block — and first violation at position 1 is k=4
  (|Δ_4(1)|=6, A_4(1)=2), failing in 17 of 20 rows. Mechanism: |u−v| =
  ||u|−|v|| holds iff u·v ≥ 0, and the signed triangle has adjacent
  opposite signs (first pair (D_3(2),D_3(3))=(2,−2)). An independent
  sampler over the 2-then-odds class (uniform even gaps in [2,500], 60
  trials, 1839 triples) fails all 60 within their first 3 rows, first
  failures at (k=3, i=0..3); derived: D_1(i)=−gap_i, D_2(i)=gap_{i+1}−gap_i,
  so any strict local extremum of the gaps (the primes have one at i=2:
  gaps 2,4) kills the identity.
hypotheses: rows are iterated absolute differences of the primes below
  400000, depth 20, width 40; signed triangle built by D_{k+1}=D_k−D_{k+1}
  with D_0=A_0; sample class 2-then-odds with even gaps in [2,500]
holds-here: yes (the identity fails here; the approach's hypothesis of
  sign-coherence does not hold)
status: checked
bearing: refutes the sign-coherence/forward-difference linearization at its
  base step — A_k(1) is NOT |binomial transform of gaps|, so that route to a
  parity+magnitude argument cannot start; any linearization must survive
  (k=3, i=2).
anchor: code/out/check_fwd_diff_identity.captured.txt,
  code/out/check_fwd_diff_identity_sampled.captured.txt,
  research/approaches/sign-coherence-forward-differences.md
source: operator-computation
```