# Saye: On two conjectures concerning the ternary digits of powers of two

**Source:** arXiv:2202.13256 (2022), published J. Integer Sequences 25 (2022) Article 22.3.4. Full text at `research/sources/saye-ar5iv-full.full.md`.

## What it establishes

1. **Verified range (both Erdős and Sloane conjectures):** for all `16 ≤ n ≤ 2·3^45 ≈ 5.9×10^21`, the ternary representation of `2^n` contains every digit 0,1,2. No counterexample to Erdős's conjecture (`2^n` always has a digit 2 once n>8) exists in this range. Method: recursive construction of powers of 2 with prescribed trailing ternary digits.
2. **History of bounds:** Erdős (1979) conjectured; Gupta (1978) verified n < 4374; Vardi (1991) extended to n ≤ 2·3^20 ≈ 7×10^9; Saye extended to n ≤ 2·3^45.
3. **Key structural lemma (this is the sieve in its cleanest form):** with `u_k = 2·3^(k-1) = φ(3^k)`:
   - (i) `u_k` is the smallest positive j with `2^j ≡ 1 (mod 3^k)`;
   - (ii) if `2^i ≡ 2^j (mod 3^k)` then `i ≡ j (mod u_k)`;
   - (iii) the (k+1)-st ternary digit of `2^(i·u_k + j)` satisfies `d_{k+1}(2^(i·u_k+j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3)`.
   The recursion builds each valid trailing-k-digit pattern into exactly three (k+1)-digit patterns, in `Θ(2^k)` total work vs `Θ(3^k)` naive.
4. **Record-breaker sequences** ρ_0, ρ_2 (smallest n with no 0 / no 2 among the last k ternary digits of 2^n entered as OEIS A351927, A351928). Example: ρ_2(100) = 710982592620911336; the notable outlier n = 201015414581294 has 98 trailing non-2 digits but ~1.3×10^14 total ternary digits.

## What it implies for this run

The sink `A_k = { n mod 2·3^(k-1) : low k digits of 2^n avoid 2 }` is exactly the object Saye's recursion enumerates for `χ=2`. Because `|A_k|` is the number of trailing-k-digit 0/1-patterns that continue to occur, and Part (iii) of the lemma governs exactly how a class at level k splits into 0, 1, 2, or 3 children at level k+1 weighted by the last digit of the representative power, this is the transfer structure the run's approach needs. The naive estimate `|A_k| ≈ 2^k/3` grows because each of the 2^k surviving digit patterns is expected to lift to ~1/3 of the 3 multiplier classes; the deviation from `2^k/3` is a measure of orbit-level correlation that a transfer-operator analysis would expose.

## Claims
```claim
id: SAYE-1
statement: The number of n ≤ 2·3^45 with (2^n)_3 omitting the digit 2 is exactly the three known values n ∈ {0,2,8} within that range; equivalently no new exception exists for 16 ≤ n ≤ 5.9×10^21.
hypotheses: n ≥ 16; all ternary digits counted (not just trailing).
holds-here: yes — this is direct numerical verification of the conjecture on the stated range.
status: verified-numerically
bearing: sets the verification bound the run can cite as reproduced literature; the run's own oracle should separately reproduce a smaller slice.
anchor: research/sources/saye-ar5iv-full.full.md
```
```claim
id: SAYE-2
statement: u_k = 2·3^(k-1) is both φ(3^k) and the order of 2 modulo 3^k; the map n → 2^n mod 3^k has period u_k, and classes split under the digit recursion given by d_{k+1}(2^(i u_k + j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3).
hypotheses: k ≥ 1, 0 ≤ j < u_k, i ∈ {0,1,2}, gcd(2,3)=1.
holds-here: yes — foundational for the sieve set A_k.
status: proved (lemma with self-contained proof in the paper)
bearing: the splitting rule is the transfer map between A_k and A_{k+1}.
anchor: research/sources/saye-ar5iv-full.full.md
```
```claim
id: SAYE-3
statement: The recursion that generates n with prescribed trailing ternary digits runs in Θ(2^K) time for depth K, versus Θ(3^K) for exhaustive testing; every n < 2^u_K is covered.
hypotheses: none beyond the lemma.
holds-here: yes — this is the efficient sieve the run should mirror (working mod 3^k, never materialising 2^n).
status: proved
bearing: the run's sieve should never iterate over all residue classes; it should recurse over surviving digit patterns.
anchor: research/sources/saye-ar5iv-full.full.md
```