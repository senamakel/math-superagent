# Directive-55: characterization of the ν₂ ≥ c·w transfer

## Question

For a 2-then-odds sequence q (q₁=2, q₂=3, q_j odd increasing for j≥3), with
right diagonal δ(q_n), ν₂(q_n) = #2s in the maximal {0,2} suffix of δ(q_n),
and w(n) = #{j∈[2,n-1] : q_{j+1}−q_j ≡ 2 (mod 4)} (the "switch count"), which
non-degeneracy hypotheses restore the transfer ν₂ ≥ c·w?

## Method

Exact-integer triangle (one row at a time, `lib.gilbreath`-style generator),
right diagonal δ(q_n)=[A_k(n−k)], ν₂ under BOTH conventions (canonical tail
floored at index 2 — the run's `nu2_vs_gap_parity` convention — and the
literal maximal {0,2} suffix of the body floored at index 0). ν₂ cross-checked
against `lib.rightdiag.cycle_and_nu2` on the primes at n=50..1000 (6/6 match).
Oracle: generator reproduces problem.md `A_1=(1,2,2,4,2,4,2,4,6,2)`,
`A_2`, `A_3` exactly.

## (1) Constant-gap refutation (reproduced)

q = (2,3,5,7,9,11,...), all gaps 2 (consecutive odds). δ(q_n)=(2n−1,2,0,...,0,1).

| n | ν₂(canon) | ν₂(literal) | w | ν₂/w |
|---|---|---|---|---|
| 100 | 0 | 1 | 98 | 0.0102 / 0.0102 |
| 1000 | 0 | 1 | 998 | 0.0010 |
| 2000 | 0 | 1 | 1998 | 0.0005 |

ν₂ = O(1) while w = n−2 → ∞, so ν₂/w → 0. **Universal transfer nu2 ≥ c·w
REFUTED**, matching the established `g-supply-transfer-refuted`.

## (2) Measured min ν₂/w and ν₂/n over families (window n=100..2000)

| family | min ν₂c/w | min ν₂l/w | min ν₂c/n | min ν₂l/n | w-range |
|---|---|---|---|---|---|
| consecutive-odds | 0.0000 | 0.0005 | 0.0000 | 0.0005 | 98..1998 |
| all-gaps-4 | inf(w=0) | inf(w=0) | 0.0000 | 0.0000 | 0..0 |
| alternating-2/4 | 0.0010 | 0.0020 | 0.0005 | 0.0010 | 49..999 |
| 2-then-all-4 | 1.0000 | 1.0000 | 0.0005 | 0.0005 | 1..1 |
| 2,2,4,2,4,... | 0.0020 | 0.0030 | 0.0010 | 0.0015 | 50..1000 |
| **primes** | **0.7049** | **0.7049** | **0.4300** | **0.4300** | 61..1195 |

The primes satisfy nu2 ≥ c·w with c ≥ 0.70 measured (min nu2/w = 0.7049 over
n=100..2000).

## (3) Which H is the weakest that restores the transfer?

The candidate hypotheses:

- **H_a: not all bits 1** — excludes the consecutive-odds all-ones h; primes
  have h=(1,1,0,...), satisfy.
- **H_b: at least one 0 and one 1** — excludes all-ones and all-zeros.
- **H_c: w(n)→∞** — consecutive-odds satisfies (w=n−2), so does NOT exclude
  the degenerate case.
- **H_d: both values with positive lower density** — excludes all-ones.
- **H_e: w(n) ≥ c·n** — consecutive-odds satisfies (w~n), so does NOT exclude
  the degenerate case.

**H_a is the weakest that (i) excludes the constant-gap degenerate case and
(ii) the primes satisfy.** H_c and H_e are NOT sufficient (consecutive-odds
satisfies both yet ν₂/w→0).

**BUT the striking finding: NONE of H_a–H_e restores the transfer.** The
alternating-2/4 family — and 2,2,4,2,4 — satisfy every one of H_a–H_e (both
bit values present with density exactly 1/2 on every prefix, w~n/2) yet give
ν₂ = O(1) (ν₂=1 and ν₂=2 respectively) with ν₂/w → 0. Verified:

- alternating-2/4 is a **SUCCESSFUL** 2-then-odds sequence (leading column 1
  to depth 3000), so it refutes the universal transfer lemma, never the
  general-class theorem.
- Independently confirmed a second way (`lib.rightdiag.incremental_diagonals`,
  a different O(N²) construction): ν₂=1 at n=200..5000 while w~n/2.
- Hand-verified on the n=10 triangle.

## Conclusion / distinction

- A refuted transfer ROUTE is not a refuted theorem. The constant-gap example
  (and the alternating example) are themselves SUCCESSFUL 2-then-odds
  sequences — they collapse to all-1 rows — so they only break the *universal*
  transfer lemma ν₂ ≥ c·w, never the general-class theorem (which they
  satisfy).
- **The ν₂ ≥ c·w transfer is genuinely prime-specific, and no simple
  non-degeneracy condition on the halved-gap bit string (not all-1, both
  values present, positive density, linear growth of w) suffices to restore
  it.** The constant-gap case is not the only degenerate family; alternating
  2/4 gaps is a second, fully non-degenerate, fully successful one.
- Deterministic periodic gap families of period dividing 4 (all gaps in
  {2,4}) appear to produce ν₂=O(1). This matches the established position that
  G-supply is a statement about the particular prime bit string — arithmetic,
  not a generic combinatorial transfer.

## Anchors

- Main: `code/directive55/nu2_transfer_characterize.py`
  → `code/out/nu2_transfer_characterize.captured.txt`
- Trend: `code/directive55/alt_trend_check.py`
  → `code/out/alt_trend_check.captured.txt`
- Verification: `code/directive55/verify_findings.py`
  → `code/out/verify_findings.captured.txt`
- Success: `code/directive55/verify_success.py`
  → `code/out/verify_success.captured.txt`
- Independent route: `code/directive55/alt_indep_route.py`
  → `code/out/alt_indep_route.captured.txt`

## Claim

```claim
id: nu2-transfer-not-restored-by-nondegeneracy
statement: For 2-then-odds sequences, the transfer nu2(q_n) >= c*w(n)
  (w(n)=#{j in [2,n-1]: gap_j ≡ 2 mod 4}) is NOT restored by any of the
  listed non-degeneracy hypotheses on the halved-gap bit string
  h[j]=(gap_j/2) mod 2: (H_a) not all bits 1, (H_b) at least one 0 and one
  1, (H_c) w(n)->infinity, (H_d) both values with positive lower density,
  (H_e) w(n) >= c*n. Every H is met by the alternating-2/4 family
  q=(2,3,5,9,11,15,17,...) (a SUCCESSFUL 2-then-odds sequence, leading
  A_k(0)=1 to depth 3000) yet nu2 = 1 (both conventions) = O(1) while
  w ~ n/2, so nu2/w -> 0. The constant-gap consecutive-odds family
  (h == all-ones, successful) also gives nu2=O(1), w=n-2. Hence the
  nu2 >= c*w transfer is genuinely PRIME-SPECIFIC: the primes measure
  min nu2/w = 0.7049 over n=100..2000 (nu2 >= 0.70*w). H_a is the weakest
  hypothesis that excludes the degenerate consecutive-odds case and that
  the primes satisfy, but it does not restore the transfer. Deterministic
  periodic {2,4}-gap families of period dividing 4 give nu2 = O(1).
hypotheses: any 2-then-odds sequence; nu2 = #2s in maximal {0,2} suffix of
  the right diagonal delta(q_n); w = Hamming weight over [2,n-1]; exact
  integer arithmetic; both nu2 conventions (tail floored at index 2 and
  literal floored at index 0) give the same conclusion.
holds-here: yes (measured, two independent constructions)
status: checked
bearing: the counterexamples (consecutive-odds, alternating-2/4) are
  SUCCESSFUL sequences, so they refute only the universal transfer LEMMA
  nu2 >= c*w, never the general-class theorem; a refuted transfer ROUTE is
  not a refuted theorem. Confirms G-supply is a statement about the
  particular prime bit string (arithmetic), not a generic combinatorial
  transfer.
anchor: code/out/nu2_transfer_characterize.captured.txt,
  code/out/alt_indep_route.captured.txt, code/out/verify_success.captured.txt
```
