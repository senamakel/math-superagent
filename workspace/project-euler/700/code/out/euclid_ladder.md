# Pattern-finder: exact structure of the PE700 Eulercoin sequences

All 102 Eulercoins already computed (solution.txt). Pattern-finder
established the exact structure of the sequences and independently
recomputed the answer strictly from it.

## Value sequence: Euclidean-ladder reconstruction (EXACT, verified)

Let A = 1504170715041707, M = 4503599627370517, and run Euclid on (M, A),
recording remainders r1 = A, r2, ..., r35 = 1, r36 = 0.

**Claim:** the 102 coin *values* are generated exactly by this ladder:

- odd-indexed remainders r1, r3, ..., r33 are exactly the 17 *run-start*
  coin values.
- even-indexed remainders r2, ..., r34 are exactly the 17 AP *step* magnitudes
  of the piecewise-arithmetic decomposition.
- run k (0-indexed) starts at r_{2k-1}, steps down by r_{2k} a total of
  q_k = r_{2k-1} // r_{2k} times (= the Euclidean quotient), ending at
  r_{2k+1} (or 0 for the last run).

This reconstruction reproduces the full 102-term value sequence **exactly**
(`reconstructed == computed` → True), and summing by the AP formula per run
gives V = 1517926517777556, exactly equal to the documented answer.

Every value-difference between consecutive coins is an even-indexed remainder
(verified); every run-start value is an odd-indexed remainder (verified). The
piecewise-AP structure of the record lows is therefore *fully explained by
plain Euclid on (M,A)* — no recurrence or continued-fraction machinery needed.

## Quotients / run lengths
q_k = [1, 1, 2, 3, 2, 1, 2, 2, 1, 38, 1, 2, 3, 34, 3, 1, 4]; sum = 101, so
1 + sum(q) = 102 coins, matching the count.

## Index sequence
The 102 record-low *indices* split into the same 17 runs (identical boundaries
and step counts). Within each run the index step is constant. The assertion
that these index steps are the continued-fraction/best-approximation
convergent denominators was **checked and refuted** (the convergent-denominator
set differs). They satisfy the linearity relation A·D ≡ −r_{2k} (mod M) for
run k (verified for all 17 runs: A·D mod M = M − r_{2k} exactly), the
sign-flipped form of the earlier A·D ≡ d (mod M) relation, and are recovered
from the same Euclidean data via that modular equation.

## Status
Conjecture over the terms supplied (102 terms is the entire sequence the
problem has), which has survived a deliberate independent check: the answer is
recomputed from scratch by the Euclidean ladder with no use of the coin list
or the recurrence, and matches. Because gcd(A,M)=1 and indices are recovered
from the same Euclidean data, this is the structural explanation of the
piecewise-arithmetic pattern found earlier (research/approaches/pe700-ap-runs.md).

## Files used/checked
- code/out/solution.txt (source of all 102 terms)
- code/out/run_structure.py, ap_relation.py, ap_verify2.py (prior AP work)
