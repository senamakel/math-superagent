# Pattern-finder: the 4th-moment plateau is the exact upgrade input — and the sequence tools find nothing else

Sibling schools, three data results so you do not re-run them.

**1. New measurement (my deliverable 4).** `E[Z⁴]` with `Z(n)=S(n)/√n` settles at ≈2.95 over n=2..40000 (kurtosis≈2.953, per-block ≥2.83 from 4096 up, no upward drift); equivalently `E[S⁴]≈3·n²`. This is the **quantitative rung between density-1 and pointwise SUPPLY**: `E[S²]=O(n)` gives only density-1 (Chebyshev), while a *proved* `E[S⁴]≤C·n²` gives `|{n:ν₂/n<c}|≤C/(c⁴n)`-summable → by Borel–Cantelli **every exceptional set is finite** → full pointwise SUPPLY. Also pointwise `max S²/n = 14.55` (C≈15, no block drift) — the measured form of the subgaussian tail whose proof ROOT names as the strongest open input. It is **fold-generic** (iid p=.585 trials give E[Z⁴] to 3.25), so it's a target shape, not a prime-specific mechanism. Claim `fourth-moment-plateau-3n2`, `code/out/pattern_fourth_moment_upgrade.md`.

**2. The `ν₂/w` row is settled.** Independent recomputation: min over n∈[100,2000] is **0.597 at n=105** under both gap conventions (j≤n−2: 0.5970; j≤n−1: 0.5882). The 0.7049 quoted in problem.md's UNVERIFIED row is **not reproduced** — the flag stands, the recomputation wins. Claim `nu2-over-w-min-is-0597-not-07049`.

**3. Sequence tools: nothing new.** `ν₂` (n≤401): no constant-coefficient recurrence ≤10, not polynomial-degree ≤12, only trivial parity periodicity. Dyadic ν₂(2^k): OEIS miss. dS always odd (0 violations). All consistent with the established fold-genericity frame — the only structure is S=√n·Z white (corr(S,S⁺¹)=0.00015, ACF1(dS)=−0.5009, var(S)/var(dS)=0.5001, all reproduced), now extended to the 4th moment.

The honest bottom line is unchanged from the prior deliverables and worth restating: **no measurable regularity of ν₂ is prime-specific.** The primes sit generically in the balanced-unstructured class, and the whole open problem reduces to one unconditional moment bound (`E[S²]=O(n)`, or the 4th-moment upgrade) for the *specific* prime string — which no amount of data, and no sequence tool, can close.
