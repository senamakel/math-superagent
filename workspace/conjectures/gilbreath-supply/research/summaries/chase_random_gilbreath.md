# Summary — A Random Analogue of Gilbreath's Conjecture

Source: Z. Chase, arXiv:2005.00530 (2022). Source URL: https://arxiv.org/pdf/2005.00530.
Full text: `[[chase_random_gilbreath.full]]`.

## What this establishes

Proves a precise random analogue of the "Gilbreath property" (first term of every
iterated absolute-difference row is 1) for sequences with small, random gaps.

**Theorem 1:** Let `f: N → N` be increasing with `f(M) ≤ (1/100)·loglog M / logloglog M`
for large M and `f(M) ≥ 2`. Let `a_1 = 2, a_2 = 3`, and for n ≥ 2
`a_{n+1} = a_n + 2u_n` with `u_n` iid uniform on `{0,…,f(n)−1}`. Then with probability 1
the first term of the sequence is 1 after M iterations for all large M.

**Theorem 2 (heart):** For M large, with `2 ≤ C ≤ (1/100)loglog M/logloglog M`, an initial
sequence of length M from `{0,…,C−1}` iid: with probability ≥ `1−e^{-e^{20√log M}}`, after
`e^{5√log M}` iterations everything is 0 or 1.

**Randomness is necessary:** e.g. a sequence of only 0s and 3s stays 0..3 forever.
There are exotic sequences over {0,…,6} whose iterates forever avoid reducing (only 0s
and 3s survive), showing how far a proof of the Gilbreath property is.

## What it implies here

Chase's random analogue supports Odlyzko's heuristic: *generic* small-gap, sufficiently
random gap strings do collapse to the {0,2} spine (the thing ν₂ measures) quickly. The
primes are conjecturally such a string. So the {0,2}-suffix (the object of SUPPLY) being
long-and-dense is the *generic* behaviour on random inputs — but the whole difficulty is
that SUPPLY needs a *specific* deterministic string, the primes, and (five closed doors)
the fold has low-weight images on rich inputs, so "random-looking" is not usable.

It also underscores why the *prime gaps* being special matters. The concrete obstruction
in GOAL: the primes do have Shiu-long constant runs and Thue–Morse-like aperiodicity, so
every "complexity of h" hypothesis fails. Chase shows the generic input collapses — but a
collapse to {0,2} is not a lower bound on ν₂'s suffix length; it's a statement that most
cells become 0/2, orthogonal to how *long* the {0,2} suffix is.

## What it does not settle

Nothing about the specific prime string. No lower bound on ν₂. It is the random-ground-
truth analogue: generic behaviour supports optimism that the primes might behave
generically here, but gives no deterministic input and no quantitative lower bound on the
suffix.

```claim
id: chase-random-gilbreath
statement: For a random increasing sequence a_1=2,a_2=3, a_{n+1}=a_n+2u_n with u_n iid
  uniform on {0,…,f(n)−1} and f(M) ≤ (1/100)loglog M/logloglog M, with probability 1 the
  first term of the iterated absolute differences is 1 after M iterations for all large M.
hypotheses: f increasing, f(M) ≥ 2, f(M) ≤ (1/100)loglog M / logloglog M for large M.
holds-here: no — the primes are deterministic, not drawn from this distribution; the
  conclusion concerns the leading term (Gilbreath), not the ν₂ suffix length.
status: proved (Chase 2022)
bearing: heuristic ground truth that generic small-gap random strings collapse to {0,2};
  supports the plausibility that the primes behave generically, but offers no deterministic
  lower bound on ν₂ and does not transfer to the specific prime string.
anchor: chase_random_gilbreath.full, Theorems 1–2
```
