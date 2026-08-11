# The Lehmer factorial norm on S_n (Zawiślak, arXiv:2111.03951)

Author: Paweł Zawiślak (SGH Warsaw School of Economics). arXiv:2111.03951v1,
submitted 6 Nov 2021, math.GR / math.CO. MSC 05A05, 62H20, 54E35, 20B99.
Source: https://arxiv.org/abs/2111.03951.
Complete text: `research/L0/lehmer_factorial_norm.body.full.md`.

## What the source establishes

- **Lehmer code distribution on S_n is factorized and uniform per digit.**
  For σ∈S_n the Lehmer code digits are c_i(σ) = #{j>i : σ(j)<σ(i)} (i=1..n),
  and the vector whose i-th entry is uniform on {0,...,i} over the uniform S_n
  — i.e. the factorial/factoradic digits of σ are *independent and each uniform
  on its own range* (Lemmas 3.1, 3.3, Cor 3.2). This is the classical Lehmer /
  factorial-number-system fact, restated here with proof.
- **Distribution of the Lehmer norm is fully described** (Theorems 4.5, 4.6 with
  Lemma 4.4), on every S_n and on S_∞. The "Lehmer factorial norm"
  LF2(σ) = Σ_i (2^i − 2^{i−k_i(σ)}) (a base-2 weight on the Lehmer digits k_i
  = c_{n−i}) is a norm/transition-invariant metric; its distribution across S_n
  follows from the independence above.

## What it implies for this problem (Project Euler 903)

Q(n) = Σ_pi Σ_{i=1}^{n!} rank(pi^i), rank = 1 + Σ_j a_j·(n−1−j)! with a_j the
Lehmer (factoradic) digits. The paper's Lemma 3.1/3.3/Cor 3.2 give an independent,
cited proof that **uniform S_n ⇒ the factoradic digits rank depends on are
independent with each digit uniform on {0,...,j}** — the structural fact behind
how the run's pair-inversion sums, and hence A_n, B_n, average over all pi. It is
a *confirmation/re-proof* of the rank structure already in place via
[[factorial_number_system_wiki]], not a new mechanism.

## Caveats (recorded so nobody over-claims)

- The paper studies the Lehmer *code of a single σ*, and the metric built from it,
  over all of S_n. It does **not** treat powers σ^i, the cyclic subgroup {σ^i},
  or the sum of ranks over that subgroup — the genuinely novel unresolved core of
  Q(10^6). Theorems 4.5/4.6 are about the norm's distribution, unrelated to A_n,
  B_n. So it is a marginal structural confirmation, not a route to a closed form
  for A_n, B_n.
- Filing rationale: fills a small gap (Lehmer-digit independence as cited
  mathematics) and rules the paper out of the A_n/B_n route without anyone having
  to re-open it.
