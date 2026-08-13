# Ford (2014), arXiv:1212.3498 — *On primes in downward-closed sets* (the Pratt-tree thinness paper)

Full text: [[ford-pratt-trees-missing-primes-2014.full]] (readable OCR). **Abstract:** "Suppose P is a set of primes such that for every p ∈ P, every prime factor of p−1 is also in P ... either P contains all of the primes or the counting function of P is O(x^{1−c}) for some c > 0, where c depends only on the smallest prime not in P."

**Setup.** `P` a set of primes satisfying the downward-closure / Pratt condition
```
(1.1)  p ∈ P  ⇒  ∀ q | (p−1), q ∈ P.
```
Let `p0` be the smallest prime not in `P` (odd, since `2 ∉ P ⇒ P = ∅`), and `P(x) = #{p ≤ x : p ∈ P}`.

**Main result (Theorem 1).** Let `P` satisfy (1.1) and omit `p0`. There are constants `δ > 0`, `c > 0` depending only on `p0` with
```
P(x) ≤ c x^(1−δ).
```
So either `P` is the set of all primes or it is a very thin set of primes. The new sieve exploits the "large prime" restrictions (`p > √x`) that the elementary `≪ x/log² x` sieve (Prop. 1) and the `≪ x (log x)^{−5/2}` (Lemma 2.1) bounds cannot see.

**Why relevant.** The 3-Higgs primes `𝒫₃` satisfy (1.1) (downward-closed) and omit `17` (`17 − 1 = 2^4`, `v2 = 4 > 3`), so `p0 = 17` and Theorem 1 gives the power-saving thinness `Π₃(x) ≪ x^{1−δ}`. This is exactly the engine of Maciejewski's Theorem 21 (`#H_even ≤ x^{1−η}`) via the Rankin trick over the Higgs-cubefree semigroup `𝒮₃^{(≤3)}`. The run's `heven-thinness-not-finiteness` claim rests on it.

**Hypotheses.** Verified: `𝒫₃` is downward-closed (a 3-Higgs prime's `p−1` has all prime factors 3-Higgs), omits 17, `p0 = 17` odd. So the theorem applies.

**Caution on naming.** The captured file is titled "On a problem of Erdős and Graham" in the run's earlier note; the abstract here is the Pratt-tree / downward-closed prime-set thinness paper (arXiv:1212.3498, Ford 2014). I record it under the abstract that is actually on the page. The result is asserted (proved in the source, not re-checked here).

```claim
id: ford-thinness-downward-closed-primes
statement: If P is a set of primes satisfying p in P => all q | p-1 in P, and P
  omits the odd prime p0, then #{p<=x : p in P} <= c x^(1-delta) for
  delta,c > 0 depending only on p0.
hypotheses: downward-closure (1.1); P nonempty omitting an odd p0 (so P is not
  all primes)
holds-here: yes - the 3-Higgs primes satisfy (1.1) and omit 17, giving
  power-saving thinness; this is the engine of heven-thinness-not-finiteness
status: catalogued
bearing: proves rarity (power-saving thinness) of the 3-Higgs primes and hence
  of H; explicitly NOT finiteness, since at the primitive-divisor height the
  bound is still exponential in p (see the thread)
anchor: research/notes/heven-and-3-higgs-structure.md
contradicts: (none)
answers: whether-P3-is-thin
```
