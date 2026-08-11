# Goal

Compute Q(n) = sum over all permutations π of {1..n} of [ sum_{i=1}^{n!} rank(π^i) ],
where rank is the 1-based lexicographic position of a permutation in the sorted list of all n! permutations.
Return Q(10^6) mod (10^9+7).

## Symbols
- π: a permutation of {1,...,n}, written in one-line notation π(1)...π(n).
- rank(π): 1-based index of π in lexicographically sorted list of all n! permutations.
- π^i: the permutation obtained by applying π i times (π composed with itself i times). π^1 = π.
- Q(n) = sum_π sum_{i=1}^{n!} rank(π^i), the double sum over all permutations and all i from 1 to n!.

## Worked examples (test oracle)
- rank(2,1,3) = 3.
- Q(2) = 5
- Q(3) = 88
- Q(6) = 133103808
- Q(10) ≡ 468421536 (mod 10^9+7)

## Completion criteria
1. brute.py reproduces all of: Q(2)=5, Q(3)=88, Q(6)=133103808 (mod p) [and lex example rank(2,1,3)=3].
2. solution.py (efficient, exact mod-p arithmetic) agrees with brute.py on every case brute can reach.
3. solution.py reproduces Q(10) ≡ 468421536 mod p (secondary example).
4. solution.py computes Q(10^6) mod p.
5. Answer verified by a second, independent route or stated as unverified.
