# Maynard — Dense clusters of primes in subsets

<!-- source: https://arxiv.org/pdf/1405.2593 | James Maynard, Compositio Math 152 (2016) 1517–1554 -->

## What it establishes (for this problem)

Maynard proves that *any subset of the primes that is well distributed in
arithmetic progressions* contains dense clusters of primes close together. The
two theorems that matter here:

**Theorem 3.3 (extends Shiu, with density).** Fix ε > 0. Uniformly for
`m ≤ cε log log x`, `q ≤ (log x)^{1−ε}`, `(a,q) = 1`,

```
#{pn ≤ x : pn ≡ ... ≡ pn+m ≡ a (mod q), pn+m − pn ≤ ε log x}
    ≫ε π(x) / (2q)^{ exp(C m) }.
```

This is a *positive-density lower bound* for strings of `m` consecutive
congruent primes in a fixed class `a mod q`. Shiu (2000) had only the weaker
`≫ x^{1−ε(x)}` in the shorter range `m ≪ (log log x)^{1/φ(q)−ε}`. Maynard's is
the strongest unconditional statement in the library on *equal-residue* runs.

## Why it concerns SUPPLY

- Closed door **#2** ("no long constant runs of h") rests on Shiu/strings of
  congruent primes. Maynard 3.3 is the modern strengthening in the *equal*
  residue direction.
- Reading `h[j] = ((q_{j+1} − q_j)/2) mod 2`: a run `pn ≡ ... ≡ pn+m ≡ a
  (mod q)` at `q` the class gives runs of equal `h` entries. For `q` even/odd
  parity of `h`, equal residues make `h` constant on the run. So 3.3 shows
  **positive density** of long all-`h`-constant runs — the *equal*-residue
  (wrong) direction again, precisely the direction the switch-density
  reduction does NOT need.
- The relevant missing direction is the *switch* (pairs differing mod 4), and
  Maynard does not touch it. This confirms problem.md's claim: the
  unconditional literature strengthens the equal-residue side and leaves the
  switch side behind the parity barrier.

**Theorem 3.1** is the general framework (well-distributed `A ⊂ primes`,
admissible `L`, Bombieri–Vinogradov-type Hypothesis 1). **Theorem 3.4**
bounded gaps for general admissible forms. **Theorem 3.5** Galois/Chebotarev
clusters.

## Hypotheses that hold here

- For `A = primes`, `P = primes` the "well-distributed in APs" hypothesis is
  exactly (a form of) Bombieri–Vinogradov, which holds unconditionally. So 3.3
  is unconditional for the full primes.
- Holds for every fixed `q` (e.g. `q = 4`) and every `(a,q)=1`.

## Relation to the switch-density reduction

Maynard 3.3 does **not** imply positive switch density (it is the
equal-residue bound). It is the strongest available instance of the *wrong
direction*, so it is the load-bearing citation for why door #2's hypothesis
("no long constant runs") is false *with density*, not merely occasionally.

## Claim block

```claim
id: maynard-positive-density-congruent-strings
statement: Fix ε > 0. Uniformly for m ≤ cε log log x, q ≤ (log x)^{1−ε}, (a,q)=1,
  # {pn ≤ x : pn ≡ ... ≡ pn+m ≡ a (mod q), pn+m − pn ≤ ε log x} ≫ε π(x)/(2q)^{exp(Cm)}.
  That is, there is a positive fraction of primes that begin a string of m consecutive
  congruent primes in a fixed class a mod q, within an ε-logarithmic gap.
hypotheses: q ≤ (log x)^{1−ε}, m ≤ cε log log x, (a,q)=1, A = full primes well-distributed
  in APs (Bombieri–Vinogradov holds unconditionally).
holds-here: yes — for q=4, a=1 or 3, holds unconditionally. Gives positive density of
  constant runs in the gap-parity string h.
status: proved (Maynard 2016, Thm 3.3).
bearing: The equal-residue side is positive-density and unconditional — this is the
  strongest available instance of the direction SUPPLY does NOT need (equal, not switch).
  Reinforces door 3 (no long constant runs) as false with density; confirms the switch
  side is the only live target and it is untouched by this machinery.
anchor: Maynard 2016 Thm 3.3; digest research/summaries/maynard_dense_clusters_primes_subsets.md.
```

## Full text

`research/sources/maynard_dense_clusters_primes_subsets.full.md`
