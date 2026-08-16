# Pattern-finder claims (fenced blocks)

```claim
id: g-normalized-fold-weight-white-noise
statement: Over n = 3..40000 for the prime gap-parity fold, the normalized
fluctuation Z(n) = S(n)/√n, S(n) = (n−2) − 2ν₂(n), is mean-zero white noise
with E[Z²] = 0.999, kurtosis 2.95, and a measured subgaussian tail
(P(|Z|>2.5)=0.006, P(|Z|>3)=0.0011, P(|Z|>4)=0). Signatures: corr(S(n),S(n+1))
= 0.0002 (NOT a random walk), increment AC1 = −0.5009 ≈ −1/2, Var(dS)/n → 2,
E[S²]/n → 1. Hence ν₂(n)/n = 1/2 − 1/n − Z(n)/(2√n) → 1/2 at rate 1/(2√n).
hypotheses: canonical ν₂ json, guards ν₂(53)=18 ν₂(64)=27 ν₂(4000)=1975
ν₂(40000)=20081; convention d∈[2,n−1]; n≤40000.
holds-here: yes, within n≤40000 — measured evidence, not a theorem.
status: measured-not-proved
bearing: E[S²]=O(n) with exponential/subgaussian tail is exactly the input from
which density-1 SUPPLY follows by Chebyshev, and subgaussian tail would upgrade
it to finiteness of every exceptional set {ν₂/n<c}, c≤0.48. It reconciles the
prior run's "E[S²]≈n but structureless" pair via S(n)=√n·Z(n), Z white.
anchor: code/out/pattern_normalized_white_noise.md
```

```claim
id: whiteness-convention-robust
statement: The whiteness of the normalized fluctuation holds in every 2-adic
residue class: corr(S(n), S(n+next)) < 0.025 for n≡0 mod 2, ≡1 mod 2, ≡1 mod 4,
≡3 mod 8, ≡5 mod 16 (each −0.009..0.023). It is not an artifact of a periodic
convention or of a specific class.
hypotheses: n≤40000, canonical json.
holds-here: yes (measured).
status: measured
bearing: strengthens the white-noise reading as a genuine structural fact
rather than a mod-m periodicity.
anchor: this note (computed directly from nu2_primes_xor_40000.json).
```

```claim
id: exceptional-sets-finite-through-40000
statement: For the prime fold, {n : ν₂(n)/n < c} is finite through n=40000 for
every c ≤ 0.48: count=(17, 62, 329) with last member (105, 763, 5655) for
c=(0.40, 0.45, 0.48); tail min of ν₂/n over [30000,40000] = 0.4901. This is
stronger than density-1 on the measured range and consistent with ν₂/n → 1/2
upgraded to finiteness by a subgaussian tail.
hypotheses: n≤40000, canonical json.
holds-here: yes (measured).
status: measured-not-proved
bearing: if a subgaussian bound on Z were proved, this finiteness becomes a
theorem, giving SUPPLY on a cofinite set — the strongest realistic target.
anchor: computed here; consistent with code/out/pattern_finder_deliverable.md
```

```claim
id: nu2-increment-white-noise-not-checked-before
statement: The increment first-autocorrelation AC1(S(n+1)−S(n)) = −0.5009 was
not computed by the prior run's increment scripts (incr_corr.py checked D(n)
vs local h features and nu2/n only, finding ~0). It is a new statistic and its
−1/2 value is the exact signature that S is normalized white noise.
hypotheses: n≤40000 canonical json.
holds-here: yes.
status: checked (re-derivation and prior-script inspection).
bearing: clarifies the prior "structureless" reading: S has no dyadic scale
correlation but is NOT a random walk either; it is √n-scaled white noise, the
sharpest description of its fluctuation.
```
