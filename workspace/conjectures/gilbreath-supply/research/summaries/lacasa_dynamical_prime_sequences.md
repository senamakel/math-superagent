# Summary — On a Dynamical Approach to Some Prime Number Sequences

Source: Lacasa, Luque, Gómez, Miramontes, arXiv:1802.08349 (published Entropy 20(2):131, 2018). Full text: `[[lacasa_dynamical_prime_sequences.full]]`. Open access arXiv PDF.

## What this establishes

A symbolic-dynamics study of two residue sequences derived from the primes, with exact enumeration of **higher-order (K>1) block structure** — the regime this pass's reopened question lives in.

**1. Primes mod k (k with φ(k)=2, i.e. k=3,4,6).** Topologically maximally chaotic (topological entropy h(0)=log 2, no forbidden patterns), and Dirichlet gives equiprobability for blocks of size m=1. BUT the Rényi entropy spectrum h(β) is **monotone decreasing in β**, non-trivially, for every k — i.e. blocks of size m>1, while all admissible, occur with **different probabilities**. This is a *higher-order* pattern: it only appears for m>1; for m=1 Dirichlet forces uniformity. A non-uniform (Cramér/type-I) null model at the empirical symbol frequencies does NOT reproduce it (it gives h(β)≈log 2 ∀β) — so it is real, not a Tchebychev-bias or finite-size artifact (checked against a same-size logistic-map binary sequence whose spectrum collapses to log 2).

**2. Prime gap residues mod 6** (gaps always even; mod 6 is natural: classes 2,4,0 mod 6 = twin-, cousin-, sexy-like). This is the more structured sequence. Two unconditional facts:
- **(i) Forbidden patterns at every m>1, divisibility-forced.** A block of m consecutive gap-residue classes is forbidden iff some prime r is "ticked" by all partial sums (each partial sum ≡ a distinct residue 1..r−1 mod r). Exact enumeration (proved, not conjectured, argument shown for (2,2): any q,q+2,q+4 has an element divisible by 3 except q=3):
  - |A(m)| = 2^{m+1} admissible blocks, |F(m)| = 3^m − 2^{m+1} forbidden blocks, over the 3 symbols.
  - First forbidden block: m=2, (4,4). Counts: m=3 → 11, m=4 → 49. (Table I.)
  - Consequently h(0) = lim H_m(0)/m = log 2 < log 3 = log p: weaker than a full shift, but positive KS entropy ⇒ still chaotic.
- **(ii) Non-uniform block density, conditional on Hardy–Littlewood.** Eq. (8) expresses the probability of an admissible gap-residue block as a Z-normalised sum of Hardy–Littlewood constants C(3i_1+g_1, …, 3i_m+g_m). A Cramér model would give uniform block frequencies and cannot explain the observed β-dependence. Empirical first-symbol frequencies (10^6 gaps): p(0)≈0.43, p(2)≈p(4)≈0.28. Truncated-HL third-order approximation gives p(0)≈0.479, p(2)≈0.255, p(4)≈0.266 — not uniform, converges slowly.

The **topic of the whole arc**: the fold's input is a *collapse* of gap residues — `h[j] = ((q_{j+1}−q_j)/2) mod 2`, i.e. only gap parity survives, so the rich mod-6 residue structure projects onto a binary switch string. The forbidden-pattern enumeration is **unconditional** (divisibility of integers), whereas the non-uniform *frequencies* are conditional on HL.

## What it implies here

This is the strongest on-topic source for the reopened pass (GOAL priority 2: a functional of order `1 < K ≲ n/2`):

- The prime gap sequence carries a **provable, unconditional, prime-specific K>1 structure**: forbidden patterns at every block order m>1, with exact counts attached to divisibility — *not* to the switch-density (pair, K=1) question. Every blocked partial-sum residue condition is a divisibility event.
- Closed door 3 (no long constant runs) already used Shiu; this source is the *on the other side* of that: exactly which multi-gap patterns are impossible is now enumerated. In the gap-parity bit h, these map to forbidden binary blocks — a candidate *weaker arithmetic input* than pointwise mod-4 switch density, because it is K>1 and unconditional.
- But note the projection caveat: mod-6 residue classes collapse many → few under parity, and it is not automatic that the forbidden 6-residue blocks survive the mod-4/parity projection used by the fold. Whether the surviving constraint on h is strong enough, and controllable by a K>1 functional, is precisely the open question — this source supplies the raw unconditional constraint, not the transfer.

## What it does NOT settle

- Nothing about the fold matrix Φ, wt(Φ_n h), or ν₂. It is a property of the prime gap sequence alone.
- The frequency distribution of blocks is conditional on Hardy–Littlewood (conjectural); only the *forbidden-pattern* counts are unconditional.
- No transfer to a K>1 functional of the fold.

```claim
id: lacasa-forbidden-gap-blocks-unconditional
statement: For the prime gap sequence mod 6 (symbols {0,2,4}), a block (2g_1,…,2g_m) is
  forbidden iff some prime r is "ticked" by all partial sums (each partial sum ≡ a distinct
  residue of 1..r−1 mod r). For every m: |A(m)|=2^{m+1} admissible, |F(m)|=3^m−2^{m+1}
  forbidden blocks; first forbidden block (4,4) at m=2; |F(3)|=11, |F(4)|=49. Hence the
  topological entropy is log 2 < log 3. The primality argument is unconditional
  (divisibility of integers), shown for (2,2).
hypotheses: gap sequence p_{n+1}−p_n reduced mod 6; symbols 0,2,4 (classes 0,2,4 mod 6).
holds-here: yes — the fold's parity string h[j]=((p_{j+1}−p_j)/2) mod 2 is a projection of this
  sequence, and these are the K>1 constraints the reopened pass asks whether the fold can read.
status: proved (the enumeration; conditional in part on HL only for the *frequencies*, not the forbidden counts).
bearing: supplies the strongest unconditional K>1 structure on the prime gap sequence — exact
  forbidden-block enumeration from divisibility, independent of the switch-density (K=1) question.
  Whether the surviving constraint on the parity string h is a valid arithmetic input strictly weaker
  than pointwise mod-4 switch density is the open question this pass must settle; the obstruction is
  that mod-6 classes collapse under the mod-4/parity projection.
anchor: lacasa_dynamical_prime_sequences.full, §III D (gaps residue sequence) and Table I; Eq. (8).
```

## Keyword map
forbidden gap patterns; prime gaps mod 6; Rényi entropy spectrum; higher-order block structure; Hardy–Littlewood k-tuple; twin/cousin/sexy; prime constellations.
