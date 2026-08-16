```ladder
goal: For every integer n > 8, the base-3 representation of 2^n contains at least one digit 2 (equivalently, 2^n is not a sum of distinct powers of 3 once n > 8).
difficulties: unbounded-n, unbounded-ones, middle-digits, sieve-nonclosure, density-gap, exceptions, independence
status: open
```

```rung
id: R-witness
statement: Among n in {0,...,8}, the base-3 expansion of 2^n avoids the digit 2 exactly for n in {0, 2, 8}; i.e. 2^0 = 1 = (1)_3, 2^2 = 4 = (11)_3, 2^8 = 256 = (100111)_3, and every other n <= 8 has a digit 2.
off: unbounded-n, unbounded-ones, middle-digits, sieve-nonclosure, density-gap, independence
stance: settled
claim: direct computation of 2^n in base 3 for n <= 8 (witnesses listed in problem.md)
merge: Extending the classification beyond n = 8 is exactly turning unbounded-n back on. These three witnesses are the falsification oracle every later rung must pass: any argument that also forbids n = 0, 2, 8 is false, and the n > 8 boundary is where the known digit-2-free powers sit.
```

```rung
id: R-finite
statement: For every integer n with 9 <= n <= 1000, the base-3 expansion of 2^n contains at least one digit 2.
off: unbounded-n, unbounded-ones, middle-digits, sieve-nonclosure, density-gap, independence
stance: open
merge: Removing the ceiling turns unbounded-n back on. The direct check is mechanical (n <= 1000 needs no big-integer cost beyond ~630 ternary digits), and the recursive trailing-digit construction (Saye, Lemma 1: u_k = 2*3^(k-1) is the order of 2 mod 3^k) is the tool that pushes a fixed finite ceiling toward the literature's n <= 2*3^45 bound without ever building 2^n whole. Reproduce a modest bound first, then extend only with the bound stated.
```

```rung
id: R-low-k
statement: For every fixed k >= 1, the claim "every n > 8 has a digit 2 among the low k ternary digits of 2^n" is FALSE: every n = 8 (mod 2*3^(k-1)) has 2^n = 256 (mod 3^k), and 256 = (100111)_3 has all ternary digits in {0,1}, so its low-k tail is digit-2-free for every k.
off: middle-digits, unbounded-ones, density-gap, independence
stance: failed
merge: This is the sieve-nonclosure difficulty in its sharpest, unverified-lead-free form: n = 8 (mod 2*3^(k-1)) replicates the digit-2-free tail of 2^8 at every finite depth, so no fixed k can close the low-digit sieve. The only way forward is to constrain digits the sieve never sees — the middle and leading digits — which is exactly turning middle-digits back on, and that is the open problem. (This refutation needs only ord_{3^k}(2) = 2*3^(k-1), stated in problem.md and Saye Lemma 1; it does not depend on the unverified |A_k| = 2^(k-1) lead.)
```

```rung
id: R-leading-trailing
statement: For a stated L, for every integer n > 8, the base-3 expansion of 2^n contains a digit 2 among its first L leading digits or its last L trailing digits.
off: middle-digits, density-gap, independence
stance: open
merge: The trailing part is the low-L sieve, which R-low-k shows leaves n = 8 (mod 2*3^(L-1)) alive; excluding those survivors requires finding a 2 in the leading L digits, i.e. controlling the fractional parts {n*log_3(2)} on the arithmetic progression n = 8 + m*2*3^(L-1). That is precisely where density-gap bites first, and it is the first rung that gets hard: leading digits are determined by an irrational rotation, and no unconditional method controls it on a thin sequence. This rung is attackable only by splitting into (a) a bounded-L computation over residue classes plus (b) an honest statement of what the leading-digit check needs that is not yet available.
```

```rung
id: R-bounded-ones
statement: The only integers n for which 2^n is a sum of at most twenty-five distinct powers of 3 are n in {0, 2, 8}; equivalently, if n is not in {0, 2, 8} then the base-3 expansion of 2^n contains at least one digit 2 or at least twenty-six digits 1.
off: unbounded-ones, middle-digits, density-gap, independence
stance: settled
claim: Dimitrov–Howe 2021 Theorem 1.2, elementary congruences (research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md lines 97-101)
merge: This is the conjecture with the ones-count capped at 25, proved by elementary congruence methods (Dimitrov–Howe 2021, Theorem 1.2; anchor: research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md, lines 97-101). Lifting the cap to infinity — turning unbounded-ones back on — is the full conjecture; no known argument pushes 25 to infinity, and naming that gap precisely is itself the finding this rung banks.
```
