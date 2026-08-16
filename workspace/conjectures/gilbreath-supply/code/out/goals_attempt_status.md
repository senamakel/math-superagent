# Attempt 2 — goals report

## Line of attack
The averaged/structural line (GOAL priority 1, the single hypothesis under
test: what a provable-from-structure statement about the fold contributes beyond
the switch-density reduction). Two concrete moves this attempt:
(A) prove the two all-n structural theorems of the fold, converting the
uniform-random expectation and the prefix-variance null from *measured* to
*proved*; (B) settle directive 15's like-for-like primes-vs-fair Monte Carlo
prefix-variance ratio at the N=40000 ceiling.

## Completed (this attempt)

***PROVED*** — claim `fold-rank-n-minus-2-binomial-proved`:
Under the operative row range d=2..n-1, the submask-XOR fold matrix Φ_n
(Z[d][s]=[s⊆d], **unit lower-triangular**) has rank n−2 and kernel =
span(even-alt, odd-alt), all-ones in the kernel (closed door 1 untouched).
Hence Φ_n is surjective onto F₂^{n−2}, every image has exactly 4 preimages, so
for uniform h `wt(Φ_n h)` is exactly Binomial(n−2,1/2): E=(n−2)/2,
Var=(n−2)/4, Var(ν₂/n)=(n−2)/(4n²)≈1/(4n), and the log(N)/(4N) prefix-variance
null is a *consequence*, not a fit. Verified two independent ways: exact F₂
elimination n=2..40 and exhaustive 2ⁿ enumeration n=2..9, plus the canonical
oracle (nu2(53)=18, 64=27, 4000=1975, mu_4000=0.497259).
Anchor: `code/out/fold_alln_theorems.captured.txt`.

***MEASURED — settled*** — claim `fair-mc-primes-ratio-constant-133-40000`:
directive 15's like-for-like primes-vs-fair Monte Carlo prefix-variance ratio at
N=40000 (5 uniform trials, script `code/averaged/fair_prefix_variance_40000.py`):
primes/fair = 1.492@1000 → 1.329@40000, monotone decreasing with decelerating
decrements (slope vs ln N −0.044). The excess above the uniform fair model
PERSISTS over [1000,40000] (~33% at 40000); the fair side independently tracks
the proved log(N)/(4N) null. Per directive 19 the limit (1 vs a constant above
1) is NOT decided by two decades. Anchor:
`code/out/fair_prefix_variance_40000.txt`.

## What this means
The uniform-random expectation (mean 1/2) and the log(N)/(4N) prefix-variance
null now rest on a proved rank fact, isolating the difficulty precisely: the
entire contraction to the primes is that the *fixed prime string h* is not known
to be non-adversarial for Φ. Measured mu_N = 0.499658 sits exactly on 1/2 and
the excess is real (~33%) and stable over [1000,40000].

## Open (unchanged, now stated sharply)
Prove `s2_N → 0` for the prime h — equivalently that the exceptional set
{n : ν₂(n)/n < c} is finite for every c < 1/2. This is the weaker sufficient
input for SUPPLY (density-1 via Chebyshev); the pointwise-finite-exceptional-set
statement is stronger than needed. This attempt proved the fair side and
quantified the prime excess; the boundary-to-0 step remains the open problem.
SUPPLY itself is NOT claimed — it is untouched.

## Evidence classes
rank/binomial claims: proved (two mechanical routes + sourced-less derivation).
Fair-MC ratio: measured, not proved.
