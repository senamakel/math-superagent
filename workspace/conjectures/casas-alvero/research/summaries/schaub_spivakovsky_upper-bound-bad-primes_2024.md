# Schaub–Spivakovsky, *A description of and an upper bound on the set of bad primes* (arXiv:2411.13967, 2024)

Full text: [[schaub_spivakovsky_upper-bound-bad-primes_2024.full]]

Companion to the 2023 bad-primes paper. Gives an **exact criterion** for bad primes (via gcds of minors of explicit matrices) and, assuming CA holds in degree n char-0, an **explicit upper bound** on the bad primes for n. This is the most direct source usable as a *computable filter* by the run for the reduction-mod-p method.

## Setup (following Ghosh 2024, Prop 5.2)

For `j∈{1,…,n−1}`, involutions `Φ_j` on `K[x_1,…,x_{n−1}]` with `Φ_j(x_i)=x_i−x_j`, `Φ_j(x_j)=−x_j`, `Φ_n = id`. With `σ_i` the i-th elementary symmetric of `x_1,…,x_{n−1}` and for each tuple `T=(j_1,…,j_{n−1})∈{1,…,n}^{n−1}`, define homogeneous `G_{T,i} = Φ_{j_i}(σ_i(x_1,…,x_{n−1}))`, `deg G_{T,i}=i`.

CA in degree n (any characteristic) ⇔ for every T the sequence `(G_{T,1},…,G_{T,n−1})` is a regular sequence (Ghosh 2024 Prop 5.2), equivalently `sqrt(G_{T,1},…,G_{T,n−1})=(x_1,…,x_{n−1})`.

## Main theorem

```claim
id: bad-prime-minors-criterion
statement: A prime p is bad for degree n iff p | J_T for some T ∈ T, where J_T is the
  greatest common divisor of all C×C minors of the matrix M_T formed by the row vectors
  of the monomials of degree d = (n²−3n+4)/2 lying in the ideal (G_{T,1},…,G_{T,n−1});
  equivalently p | lcm_{T∈T} J_T. (C = binomial((n²−n)/2, n−2).)
hypotheses: CA holds in degree n over char-0 to have a finite bad set; the criterion
  itself is unconditional
holds-here: yes
status: proved (Theorem 3.1, by Macaulay 1916: md ⊂ (f_1,…,f_n) ⇔ rank of the matrix
  of degree-d monomials is maximal)
follows-from: ghosh-complete-intersection
bearing: Gives the run an *exact*, *computable* characterization of bad primes: compute
  integer minors and their gcds. This is precisely the sort of elimination/linear-algebra
  computation over Z the run's method allows. For CA_{dp^k} lifting one needs p NOT bad
  for d.
anchor: research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md (Thm 3.1)
falsifies: a prime p that is bad for n but divides none of the J_T.
```

```claim
id: bad-prime-upper-bound
statement: If CA_{n,0} holds and p is a bad prime for n, then
  p < C! · Π_{i=1}^{n−1} (i+n−2 choose n−2)(d−i+n−2 choose n−2),
  where d=(n²−3n+4)/2, C=( (n²−n)/2 choose n−2 ). (A sharper form via a monotone
  rearrangement is given in Remark 3.4, eq (7).)
hypotheses: CA_{n,0} holds; p bad for n
holds-here: yes (a bound, not a classification)
status: proved (Corollary 3.2 + Lemma 3.3, by Hadamard-type bound on the minors)
follows-from: bad-prime-minors-criterion
bearing: If the run establishes CA for a degree n, this bounds the primes one must
  check before trusting a mod-p reduction. It also shows the bad-prime set of a fixed
  degree is finite — supporting the "finitely many bad primes ⇒ CA_{n,0} holds iff
  CA_{n,p} holds for all but finitely many p" architecture.
anchor: research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md (Cor 3.2)
falsifies: a bad prime for n exceeding the stated bound (while CA_{n,0} holds).
```

## What it does not settle
The bound is astronomically large in practice (the authors note the denominator-factoring is the bottleneck in the related Castryck algorithm). It does not prove CA for any degree; it characterises bad primes *given* that CA holds. The complete-intersection/regular-sequence reformulation is taken from Ghosh 2024, which is itself an unverified preprint.
