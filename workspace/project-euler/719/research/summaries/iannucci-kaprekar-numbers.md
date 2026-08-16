# Iannucci — The Kaprekar Numbers

Source: https://cs.uwaterloo.ca/journals/JIS/VOL3/iann2a.html
(`research/sources/iannucci-kaprekar-numbers.full.md`).

**What it establishes (n-Kaprekar numbers; here n = number of right blocks).**
- **Theorem 1:** k is an n-Kaprekar number iff k = d·Inv(d, (10^n−1)/d) for some
  unitary divisor d of 10^n − 1, where Inv(a,b) is the least positive m with
  am ≡ 1 (mod b). This is the Charosh-algorithm correctness: Kaprekar numbers
  (two-block) are in one-to-one correspondence with unitary divisors of 10^n − 1.
- **Theorem 2:** every even perfect number is a Kaprekar number in base 2.

**Bearing on PE 719.** This is the structural theory for the *two-block* case
only: it gives a generation formula for Kaprekar numbers from unitary divisors
of 10^n − 1, but S-numbers permit n ≥ 2 blocks in general (three, four, …), and
no such divisor parametrisation is given for the general k-block case. The
divisor formula is therefore *not* the route to T(10¹²); the digit-partition
recursion is.

```claim
id: iannucci-kaprekar-divisor-formula
statement: k is an n-Kaprekar number iff k = d * Inv(d, (10^n-1)/d) for a unitary divisor d of 10^n - 1; Kaprekar numbers correspond one-to-one with those unitary divisors. This parametrises only TWO-block splits.
hypotheses: base 10; n>=1; unitary divisor means gcd(d,(10^n-1)/d)=1.
holds-here: yes for the two-block subcase only
status: proved (Theorem 1, Iannucci JIS 2000)
bearing: explains the two-block subcase but does NOT solve the 2+-block S-number problem; confirms recursion is needed.
anchor: research/summaries/iannucci-kaprekar-numbers.md
```

**Does not help** for the general problem: restricted to two blocks, no analogue
for arbitrary block count; the honest method stays the digit-partition search
over roots.
