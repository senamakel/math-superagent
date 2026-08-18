> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/tao-almost-all-orbits.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: tao-almost-all
answers: exact-statement-2019-348f
statement: For the Collatz map Col on N+1 = {1,2,3,...}, for any function f: N+1 → R with lim_{N→∞} f(N) = +∞, one has Col_min(N) < f(N) for almost all N in the sense of logarithmic density. (Theorem 1.3)
hypotheses: f grows without bound; "almost all" means logarithmic density 1, i.e. (1/log x) Σ_{N≤x} 1_{Col_min(N)<f(N)} → 1.
holds-here: true — direct statement about the Collatz map this run studies.
evidence: proved in source (Tao 2019, Forum Math Pi 2022); full proof in research/sources/tao-almost-all-orbits.full.md
status: proved
falsifies: a counterexample — an infinite logarithmic-density set of N with Col_min(N) ≥ f(N) for some unbounded f — or a published proof that Col_min(N)=1 for all N (which would make the result trivially true but the conjecture resolved).
```

```claim
id: tao-korec-baseline
statement: For any θ > log 3 / log 4 ≈ 0.7924, one has Col_min(N) ≤ N^θ for almost all N in the sense of natural density (Korec).
hypotheses: θ > log 3/log 4 ≈ 0.79248125...; natural density.
holds-here: true — prior result cited in Tao's paper, used as the baseline.
evidence: asserted by source (Tao cites Korec 1994, "A density estimate for the 3x+1 problem", Mathematica Slovaca 44, 85-89).
status: asserted-by-source
falsifies: a published counterexample or a stronger density result replacing it.
```

```claim
id: tao-does-not-close
statement: Tao's theorem does NOT rule out divergent orbits or non-trivial cycles; the exceptional set of logarithmic density zero can still be infinite, and the conjecture remains open.
hypotheses: none — this is the exact scope of Theorem 1.3.
holds-here: true — this is precisely what the theorem states and what it does not claim.
evidence: the theorem's statement concerns "almost all N", which is a density statement; divergence/cycles concern individual N.
status: asserted-by-source
falsifies: a source showing Tao's theorem (or a published strengthening) rules out divergent orbits or non-trivial cycles outright.
```

<!-- source: https://arxiv.org/pdf/1909.03562 | converted from PDF -->

## What is in it

- {N ∈ N + 1 ∩ [1, x] : Colmin(N ) = 1} ≫ x0.84
- {j ∈ N + 1 : bj = 3, (j, b[1,j]) ∈ W } ≡ #{k ∈ N + 1 : v[1,k] ∈ W },


## What it claims

Abstract. Define the Collatz map Col : N + 1 → N + 1 on the positive integers
N + 1 = {1, 2, 3, . . . } by setting Col(N ) equal to 3N + 1 when N is odd and N/2 when
N is even, and let Colmin(N ) := inf n∈N Coln(N ) denote the minimal element of the
Collatz orbit N, Col(N ), Col2(N ), . . . . The infamous Collatz conjecture asserts that
Colmin(N ) = 1 for all N ∈ N + 1. Previously, it was shown by Korec that for any
θ > log 3
log 4 ≈ 0.7924, one has Colmin(N ) ≤ N θ for almost all N ∈ N + 1 (in the sense
of natural density). In this paper we show that for any function f : N + 1 → R with
limN →∞ f (N ) = +∞, one has Colmin(N ) ≤ f (N ) for almost all N ∈ N+1 (in the sense
of logarithmic density). Our proof proceeds by establishing a stabilisation property for
a certain first passage random variable associated with the Collatz iteration (or more
precisely, the closely related Syracuse iteration), which in turn follows from estimation
of the characteristic function of a certain skew random walk on a 3-adic cyclic group
Z/3nZ at high frequencies. This estimation is achieved by studying…

## Statements it makes

Conjecture 1.1 (Collatz conjecture). We have Colmin(N ) = 1 for all N ∈ N + 1.

Definition 1.2 (Almost all). Given a finite non-empty subset R of N + 1, we define1

Theorem 1.3 (Almost all Collatz orbits attain almost bounded values). Let f : N+1 →
R be any function with limN →∞ f (N ) = +∞. Then one has Colmin(N ) < f (N ) for
almost all N ∈ N + 1 (in the sense of logarithmic density).

Conjecture 1.5 (Collatz conjecture, Syracuse formulation). We have Syrmin(N ) = 1
for all N ∈ 2N + 1.

Theorem 1.6 (Almost all Syracuse orbits attain almost bounded values). Let f : 2N +
1 → R be a function with limN →∞ f (N ) = +∞. Then one has Syrmin(N ) < f (N ) for
almost all N ∈ 2N + 1.

Definition 1.7 (Geometric random variable). If µ > 1, we use Geom(µ) to denote a
geometric random variable of mean µ, that is to say Geom(µ) takes values in N + 1
with
 P(Geom(µ) = a) = 1
µ
 ( µ − 1
µ
 )a−1

Proposition 1.9 (Distribution of n-Syracuse valuation). Let n ∈ N, and let N be a
random variable taking values in 2N+1. Suppose there exist an absolute constant c0 > 0
and some natural number n
′ ≥ (2+c0)n such that N mod 2n′ is approximately uniformly
distributed in the odd residue classes (2Z + 1)/2n′Z of Z/2
ℓZ, in the sense that

Proposition 1.11 (Stabilisation of first passage). For any y with 2N + 1 ∩ [y, yα] is
non-empty (and in particular, for any sufficiently large y), let Ny be a random variable

Lemma 1.12 (Recursive formula for Syracuse random variables). For any n ∈ N and
x ∈ Z/3n+1Z, one has

Proposition 1.14 (Fine scale mixing of n-Syracuse offsets). For all 1 ≤ m ≤ n one
has Oscm,n (P(Syrac(Z/3
nZ) = Y mod 3
n))Y ∈Z/3nZ ≪A m
−A (1.26)

Proposition 1.17 (Decay of characteristic function). Let n ≥ 1, and let ξ ∈ Z/3
nZ be
not divisible by 3. Then Ee−2πiξSyrac(Z/3nZ)/3n ≪A n−A (1.28)
for any fixed A > 0.

Lemma 2.1 (Description of n-Syracuse valuation). Let N ∈ 2N + 1 and n ∈ N. Then
⃗a(n)(N ) is the unique tuple ⃗a in (N + 1)n for which Aff⃗a(N ) ∈ 2N + 1.

Lemma 2.2 (Chernoff type bound). Let d ∈ N + 1, and let v be a random variable
taking values in Zd obeying the exponential tail condition

Theorem 3.1 (Alternate form of main theorem). For N0 ≥ 2 and x ≥ 2, one has
1
log x
 ∑

Lemma 4.1 (Tail bound). We have

Proposition 5.2 (Approximate formula). Let E ⊂ 2N + 1 ∩ [1, x] and y = xα, x
α2.
Then we have

Lemma 5.3. We have cn(X) ≪ 1 for all n ∈ Iy and X ∈ Z/3n−m0Z.

Lemma 6.2 (Injectivity of offsets). For each natural number n, the n-Syracuse offset
map Fn : (N + 1)
n → Z[ 1
2] is injective.

Corollary 6.3 (3-adic separation of offsets). Let CA be sufficiently large, let n be
sufficiently large (depending on CA), let k be a natural number, and let l be a nat-
ural number obeying (6.8). Then the residue classes Fk+1(ak+1, . . . , a1) mod 3…


*[further statements in the full text]*

*[digest of a 123515 character source; every section, statement, and proof in full at `research/sources/tao-almost-all-orbits.full.md`]*
