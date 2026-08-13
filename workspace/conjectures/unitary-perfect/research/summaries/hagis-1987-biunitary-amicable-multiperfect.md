# Hagis (1987), *Bi-Unitary Amicable and Multiperfect Numbers*, Fibonacci Quarterly 25(2):144–151

Full text: [[hagis-1987-biunitary-amicable-multiperfect.full]]
Source: https://www.fq.math.ca/Scanned/25-2/hagis.pdf

## What it establishes

Definitions: `d` is a **bi-unitary** divisor of `n` when `cd=n` and `(c,d)*=1`
(greatest common *unitary* divisor). `σ**(n)` is the sum of bi-unitary
divisors; `σ**(p^a) = σ(p^a)` for odd `a`, `σ**(p^a) = σ(p^a) − p^{a/2}` for
even `a`. `n` is **bi-unitary perfect** when `σ**(n)=2n` (Wall 1972: exactly
6,60,90), **bi-unitary multiperfect** when `σ**(n)=kn`, k≥3.

- **Theorem 1.** No odd bi-unitary multiperfect numbers exist.
- **Theorem 3.** For a bi-unitary amicable pair `(m,n)` with `m=2^a M`,
  `n=2^b N`, `M,N` odd, `a<b`: `ω(M) ≤ a` and `ω(N) ≤ b`.
- **Corollary 3.1.** `(2M, 2^b N)`, `b>1`, bi-unitary amicable with `M,N` odd
  ⟹ `M=p^c`, `N=q^d`.
- **Theorems 4.1–4.3.** Scaling rules: if `(aM,aN)` is bi-unitary amicable and
  `σ**(b)/b = σ**(a)/a` with coprimality, then `(bM,bN)` is likewise
  (and unitary/ordinary analogues for 4.2/4.3).
- Computer searches: 13 bi-unitary multiperfect numbers with `k=3` and 4 with
  `k=4` below `10^?`; 60 bi-unitary amicable pairs with smallest member
  `< 10^6` (Table 2); bi-unitary aliquot cycle tables.

## Bearing on this problem — the 10^102 provenance

**This paper contains, in its introduction, the sentence "if `n` is a
unitary multiperfect number, then `n > 10^102` and `n` has at least 46
distinct prime factors," citing Hagis [3] = Hagis 1984
(`hagis-1984-lower-bounds-ump`), which is already in the library.**

This is the source of the garbled "Wall searched past 10^102" claim that
GOAL.md/ROOT.md previously carried as a *search bound for unitary perfect
numbers*. The corrected reading:
- **10^102 is Hagis's lower bound for unitary *multiperfect* (triperfect,
  k=3) numbers — `n > 10^102` in Hagis 1984 Theorem 3** — not a search
  bound.
- **Wall 1975** proves the fifth UPN `W ≈ 1.46e23` is next after 87360
  (search bound `N < W`); it contains no 10^102.
So the "10^102" orphan claim is **resolved as a category confusion**: it is a
genuine, sourced bound, but for the wrong class (UMP k=3, which has no known
members), where the unitary *perfect* (k=2) case is untouched.

```claim
id: hagis1987-10e102-is-ump-triperfect-bound
statement: Hagis (1984 Thm 3 / 1987 intro) gives n > 10^102 for unitary
  triperfect (multiperfect, k=3) numbers, with at least 46 distinct prime
  factors. This is a lower bound for the k>=3 multiperfect class, NOT a
  search bound for unitary perfect numbers; Wall 1975's actual bound is
  N < W ~ 1.46e23 for the fifth UPN.
hypotheses: sigma*(n) = k n with k >= 3 (multiperfect); for k=2 (unitary
  perfect) the bound does not apply
holds-here: yes as provenance clarification; resolves the orphan 10^102 claim;
  no implication for the k=2 finiteness question
status: asserted (source primary, both Hagis 1984 and 1987 held)
bearing: closes the provenance of the garbled 10^102 figure; corrects
  GOAL.md/ROOT.md which conflated the UMP bound with a UPN search bound
anchor: research/sources/hagis-1987-biunitary-amicable-multiperfect.full.md
answers: provenance-of-10e102
```
