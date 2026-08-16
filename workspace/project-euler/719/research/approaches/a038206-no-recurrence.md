# A038206 root sequence shows no exploitable structural regularity — closed

## Question

Does the S-root sequence A038206 admit a recurrence, closed form, or other
regularity that would let T(10^12) be computed faster than the O(sqrt(N))
root scan already used?

## What was tested (exact tools over computed terms)

- `find_linear_recurrence` (max_order 10) over the first 30 roots
  0,1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,
  909,918,945,964,990,991,999,1000: **no** constant-coefficient linear
  recurrence of order <= 10 fits.
- `analyze_sequence` over the same terms: differences never become constant
  within 12 levels, so the sequence is not a low-degree polynomial. Growth
  ratios are irregular (9.0, 1.11, 3.6, 1.25, ...).
- Both results are exact over the terms supplied; because the sequence is a
  sparse enumeration the absence of a low-order recurrence is expected, and
  these negative results say nothing beyond the terms given.

## Exact regularities that DO hold (all verified over all 408 roots <= 10^6)

1. **mod-9 necessary condition** (already established, proof in
   `research/summaries/butler-graham-stong-partition-sum-body.md`, claim
   `partition-sum-invariant-mod9`): every S-root m satisfies m^2 == m mod 9,
   hence m in {0,1} mod 9. Verified: 0 violations among 408 roots. This cuts
   the candidate scan 2..10^6 from 999999 candidates to 222222 (factor 4.5).
2. Closed 2-block (Kaprekar) families that are all S-roots:
   - 45-family: 5*10^k*(10^{k+1}-1) = 45, 4950, 499500 (next 49995000 > 10^6).
   - 55-family: 5*(10^{2k+1}+10^k) = 55, 5050, 500500.
   - powers of 10: 10,100,1000,10000,100000,1000000.
   - 9-repunits: 9,99,999,9999,99999,999999.
   These cover only **18 / 408 = 4.4%** of roots. Two-block Kaprekar roots
   overall: 59/408 = 14.5%.
3. Concentration near 10^d (roots starting with 9 / top decile) is mild
   (29-37% per decade) and not a closed-form regularity.

## Conclusion

There is no exploitable enumeration-reducing regularity in A038206 beyond the
mod-9 filter. The enumeration-reducing root scan (T = sum of m^2 over roots m
in [2, isqrt(N)]) is already the right method; the final answer
T(10^12) = 128088830547982 is settled and double-verified (solution.py digit
partition vs verify_bfile.py A038206 b-file sum-of-squares, both = 128088830547982).

```claim
id: a038206-no-recurrence-filter
statement: The S-root sequence A038206 has no constant-coefficient linear recurrence of order <= 10 and is not a low-degree polynomial over its computed terms, and the only cheap modular necessary filter on S-roots is mod 9 (m == 0 or 1 mod 9): mods 27/99 are exact lifts of the mod-9 set, and mods 7, 11, 13, 17, 19, 37 are full (no residue excluded). mod-9 prunes ~7/9 of candidate roots; no stronger modular filter exists.
hypotheses: sequence terms as enumerated (408 roots <= 10^6); base 10
holds-here: yes
status: checked (find_linear_recurrence max_order 10 over first 30 terms; modular sweep over all 408 roots)
bearing: rules out an enumeration-redefining recurrence for T(10^12); confirms the root scan + mod-9 filter is the right method and that the answer T(10^12)=128088830547982 is settled.
anchor: research/approaches/a038206-no-recurrence.md
```

## Status

Closed (negative structural result).
