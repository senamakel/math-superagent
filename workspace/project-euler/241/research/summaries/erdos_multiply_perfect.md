# Erdős (1956) — On perfect and multiply perfect numbers

Source: https://doi.org/10.1007/BF02411879 — `[[erdos_multiply_perfect.full]]`
(P. Erdős, *Annali di Matematica* 42 (1956) 253–258).

## What it proves

- P(x) = #{n ≤ x : σ(n) ≡ 0 (mod n)} (multiperfect, incl. abundancy ≥ 2).
  **P(x) < x^(3/4+ε)**.
- P₂(x) = #{n ≤ x : σ(n) = 2n} (perfect). **P₂(x) < x^((1−c)/2)** for some c>0.

So the number of perfect numbers up to x is ≪ x^0.5 (a sub-polynomial-power
density), and multiperfects are ≪ x^0.75+ε.

## Relevance to PE 241

These are early density bounds for the **integer-abundancy** family — the twin
of this run's half-integer-abundancy set. They do **not** transfer to a bound
on the hemiperfect count ≤ 10^18: half-integer abundancy is a different
condition, and no analogous density bound for hemiperfects is given (and none
is known — A317681 states the k≥4 half-integer sets are not even known
finite). The Erdős bounds corroborate only the *sparsity* expectation, not a
numeric count.

## Verdict

**Background; does not help the solver's number.** Confirms the classical
rarity of the family, consistent with the empirical count 22 below 1e18, but
gives no enumeration method, no bound on hemiperfects, and no member of the
answer set. No contradiction with anything on disk.

Keep one line: Erdős 1956 proves sub-polynomial density of perfect and
multiperfect numbers; sparsity background only.

No separate claim block: the density results are not used by the method, and
no claim row is warranted (adding dead rows to CLAIMS.md misleads).