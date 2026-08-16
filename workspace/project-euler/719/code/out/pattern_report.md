# Pattern report — PE 719 S-roots (A038206)

Pattern-recognition pass over the sequence data the investigation produced
(the 408 A038206 roots <= 10^6 in `code/out/roots408.txt`, the 3200-term
b-file in `research/sources/oeis_a038206_b.full.md`, and the decade tables in
`code/out/seq_decades.txt`).

## Confirmed regularities (exact over all terms tested)

### 1. Mod-9 rule (provable theorem, re-confirmed)
Every S-root m satisfies m == 0 or 1 (mod 9).
Reason: each block-value ≡ its digit-sum (mod 9) because 10^k ≡ 1 (mod 9);
block-sum (= m) ≡ digit-sum (= m^2) (mod 9), so m ≡ m^2, i.e. m(m−1) ≡ 0 (mod 9).
Verified: **0 violations** among all 3200 b-file roots (max root 1028956744 ~ 10^9).
Among the 406 roots in [2, 10^6]: residue 0 -> 198, residue 1 -> 208.
Prunes candidate roots by 7/9. This is the only enumeration-reducing
regularity; it is already used by the root-scan method.

### 2. Proven infinite two-block family (new)
m_k = 5·10^k·(10^{k+1} − 1) = 50·10^{2k} − 5·10^k: 45, 4950, 499500, 49995000, ...
For every k:
  m_k^2 = a·10^{2k+2} + b,  with a = 5·10^k(5·10^k − 1),  b = 25·10^{2k},
  and a + b = m_k.
So str(m_k^2) splits into two consecutive blocks summing to m_k — each m_k
is an S-root. Verified **algebraically over k = 0..29** and matched against
the b-file for every member within coverage (k = 0..3). This is exactly
Kaprekar's two-block/torn-number parametrisation (unitary divisors of
10^n − 1, Iannucci/Dudeney), so it is a strict subset of the S-roots, and
only 45, 4950, 499500 are <= 10^6. It adds no enumeration-reducing power for
T(10^12).

## Regularities that do NOT hold (exact failures)

- No constant-coefficient linear recurrence of order <= 10 fits the first 75
  roots of A038206.
- Decade counts D_k = [2,7,19,47,90,241,411,849,1523] and cumulative counts
  c_k = [2,9,28,75,165,406,819,1668,3191] do not fit a low-degree polynomial;
  leading ratios irregular. OEIS lookup on c_k: **no entry** (and none of
  D_k, I_k, cumulative sums is catalogued).

## Consequence
The only exploitable structure that reduces work is the mod-9 filter over the
root scan; the general arbitrary-block S-set has no closed form. The verified
answer T(10^12) = 128088830547982 (double route: solution.py recursion and
verify_bfile.py A038206 b-file sum) stands.
