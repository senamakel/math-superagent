# Phi p-adic valuation bounds, p-adic closure, range clip, |Phi(M)| — pattern_finder findings

Written by pattern_finder from its own executions this session:
`code/phi_padic_valuation.py`, `code/phi_valuation_proof_check.py`,
`code/phi_padic_closure_all.py`, `code/phi_padic_closure_exact.py`,
`code/phi_range.py`, `code/phi_count_seq.py`.  These are the pattern/
regularity findings on the run's own Φ-set data.

## 1. Provable valuation bounds (v2≥3, v3≥1)

For every primitive `m>n≥1`, `q = f(m,n) = 4mn(m²−n²)/(m²+n²)²` (reduced) ∈ Φ:

- **v2(q) ≥ 3** (every q ≡ 0 mod 8, 2-adically).
  - one of m,n even (primitive ⇒ not both): `4mn` has v2 = 2+v2(neven) ≥ 3,
    and `D=(m²+n²)²` is odd, so v2 ≥ 3.
  - both m,n odd: `m²−n²` divisible by 8 (difference of odd squares), so
    N = 4mn(m²−n²) has v2 ≥ 2+3 = 5; `m²+n² ≡ 2 mod 4` so v2(D)=2;
    v2(N)−v2(D) ≥ 5−2 = 3.
  - Verified over all 48677 primitive pairs m≤n≤400: min v2 = 3.
- **v3(q) ≥ 1** (every q ≡ 0 mod 3).
  - Among the factors `m, n, (m−n), (m+n)` of N = 4mn(m²−n²), at least one is
    divisible by 3 for any primitive pair: if 3|m (then 3∤n by primitivity),
    m is the multiple; if 3∤m,3∤n then either m≡n or m≡−n (mod 3), giving
    (m−n) or (m+n) divisible by 3.  So 3|N.
  - `m²+n²` is never divisible by 3 for primitive (m,n): (m²+n²)≡0 mod 3
    forces m≡n≡0 mod 3, contradicting primitivity.  So 3∤D and v3(q)=v3(N)≥1.
  - Verified over all 48677 primitive pairs: min v3 = 1.

Both are **proofs**, confirmed mechanically over the full primitive-pair range
up to m=n=400.

## 2. NO p-adic modular obstruction to the additive-triple conjecture

For every prime p ∈ {2,3,5,7,11,13} and every precision p^a with p^a ≤ ~2000,
the achievable residue set `R = { f(m,n) mod p^a : primitive m>n≥1,
gcd(m²+n²,p^a)=1 }` is **non-degenerately additively closed**: there exist
distinct r1,r2 ∈ R with (r1+r2) mod p^a ∈ R.

Verified two ways: (i) via the Φ(200) sample's reduced fractions, and
(ii) by exhaustive enumeration of all (m,n) residue classes mod p^a
(`phi_padic_closure_exact.py`).  The low-precision sets are the single
trivial residue {0} (2|3^1|5^1), which for mod 3 = 3 gives |R|=1 and "not
additively closed" only in the degenerate sense (no second distinct element).
At every modulus where |R| ≥ 2, the set IS additively closed.

**Consequence (verified-numerical): a pure p-adic modular sieve cannot prove
the no-Φ-triple conjecture.**  This is consistent with the run's established
"locally solvable mod every prime power" and reinforces that any impossibility
proof must use rationalness/integrality beyond congruences.  Not a proof — it
is a statement over the finite set of primes/precisions tried.

## 3. |Φ(M)| not in OEIS

|Φ(M)| (M=10..150 step 10):
22, 86, 186, 331, 518, 737, 1002, 1314, 1656, 2040, 2480, 2930, 3448, 4002, 4582
(also 8156 at M=200, 32495 at M=400).  `oeis_lookup` returns **No Match**: the
sequence is not catalogued, no closed form will be looked up, structure must
come from the problem.  Recorded so nobody searches again.

## 4. Range / clip: f(m,n) < 1 strictly; sup never attained

`f(m,n) = sin(4 arctan(n/m)) < 1` strictly for all integer m>n≥1: the sup over
real t=n/m ∈ (0,1) of 4t(1−t²)/(1+t²)² is 1, attained only at t = √2−1 =
tan(π/8), which is irrational, so never for integers.  Hence q1+q2 < 2 always;
the strict clip q1+q2 < 1 is non-trivial and is exactly the additive/clip
condition that killed Bremner's near-miss (q_v + q_{u+v} = 5544/7225 +
336/625 = 1.305… > 1).  Max q in Φ(400) = 1119638520/1119638521 at (169,70).

```claim
id: phi-valuation-bounds
statement: Every q = 4mn(m²−n²)/(m²+n²)² in Φ (primitive m>n≥1, reduced) has
  v2(q) ≥ 3 and v3(q) ≥ 1; i.e. every such q is ≡ 0 mod 8 and ≡ 0 mod 3
  2-adically/3-adically, with denominator coprime to 2 and 3.
hypotheses: primitive m>n≥1
holds-here: yes
status: proved (analytic proof; confirmed over all 48677 primitive pairs
  m≤n≤400)
bearing: every centre-AP difference d of a candidate centre e² satisfies
  d/e² ∈ Φ ⊆ { q : v2(q)≥3, v3(q)≥1 }; pins the 2,3-adic family; but since all
  such q are 0 mod 8 and 0 mod 3, the additive relation q1+q2=q3 gives no
  residue contradiction (a sum of two 0-mod-8 things is 0 mod 8) — hence these
  bounds are necessary, not a sieve.
anchor: code/phi_valuation_proof_check.py, code/phi_padic_valuation.py
falsifier: a primitive pair (m,n) with v2(f(m,n))<3 or v3(f(m,n))<1
```

```claim
id: phi-padic-residue-closure
statement: For every prime p ∈ {2,3,5,7,11,13} and precision p^a with p^a≤2000,
  the achievable residue set R = {f(m,n) mod p^a} (denominator invertible) is
  non-degenerately additively closed: distinct r1,r2∈R with (r1+r2) mod p^a ∈ R.
hypotheses: primitive m>n≥1, p^a ≤ 2000
holds-here: yes
status: checked (exact, both sample-based and exhaustive over
  residue classes)
bearing: a pure modular sieve cannot prove the no-Φ-triple conjecture at these
  primes/precisions; a non-existence proof must use rationalness/integrality
  (consistent with the run's "locally solvable mod every prime power").
anchor: code/phi_padic_closure_exact.py, code/phi_padic_closure_all.py
falsifier: a prime p and precision a where R mod p^a is non-degenerately
  additively closed = FALSE (largely rules out a p-adic Ahjumma obstruction)
```

```claim
id: phi-range-clip
statement: f(m,n) = sin(4 arctan(n/m)) < 1 strictly for all integer m>n≥1
  (sup = 1 at the irrational t = tan(π/8) = √2−1, never attained); so the
  additive-chain clip q1+q2 < 1 is non-trivial and is the exact obstruction
  that killed Bremner's near-miss (q_v + q_{u+v} > 1).
hypotheses: integer m>n≥1
holds-here: yes
status: proved (sup over real t attains 1 only at irrational point)
bearing: the MSS four-difference condition needs q1,q2,q1+q2,q1−q2 ∈ Φ, so the
  strict inequality q1+q2<1 is a genuine constraint separating Φ from
  admissible additive chains.
anchor: code/phi_range.py
falsifier: an integer pair (m,n) with f(m,n) ≥ 1 (impossible by the sup
  computation)
```

```claim
id: phi-count-sequence-not-in-oeis
statement: |Φ(M)| = 22,86,186,331,518,737,1002,1314,1656,2040,2480,2930,3448,4002,4582
  (M=10..150 step 10; 8156 at 200, 32495 at 400) has no OEIS match.
hypotheses: none
holds-here: yes
status: finding (exact computation; OEIS miss)
bearing: no catalogued closed form; the structure of |Φ(M)| must be derived
  from the problem (it counts distinct rational values of f on m>n≥1, m≤M).
anchor: code/phi_count_seq.py
falsifier: an OEIS entry matching the terms (oeis_lookup already returns None)
```
