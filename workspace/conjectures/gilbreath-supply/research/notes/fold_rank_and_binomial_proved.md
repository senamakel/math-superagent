# Fold rank n−2 and exact Binomial(n−2, 1/2) weight distribution — PROVED

Two all-n structural facts, established in this attempt and verified two
independent ways (exact F₂ elimination n=2..40 crossed against an exhaustive
brute-force kernel census n=2..12, and exhaustive 2ⁿ weight enumeration n=2..9).
Capture: `code/out/fold_alln_theorems.captured.txt`; executors:
`code/lib/fold_matrix.py`, `code/fold_rank/verify_alln_theorems.py`.

## The two theorems and the argument

**Theorem 1 (rank).** Under the operative convention (rows `d=2..n-1`, an
`(n-2)×n` matrix), `rank Φ_n = n-2` and `ker Φ_n = span(even-alt, odd-alt)`.

The full square `Z[d][s] = [s ⊆ d]` (submask-XOR) is **unit lower-triangular**:
`s ⊆ d` bitwise implies `s ≤ d`, and `Z[d][d]=1`, so `det Z = 1` — `Z` is
invertible. Dropping rows `d=0,1` leaves exactly the two image coordinates
`v₀, v₁` free, so `dim ker M = 2` and `rank M = n-2`. The two freed directions
*generate* the kernel and are exactly `even-alt` and `odd-alt`, whose XOR is
all-ones (so closed door 1 is untouched: all-ones stays in the kernel).

**Theorem 2 (exact binomial).** Since `Φ_n` is surjective onto `F₂^{n-2}`,
every image has exactly `2² = 4` preimages. For `h` uniform on the cube,
`wt(Φ_n h)` is **exactly `Binomial(n-2, 1/2)`**: `E[wt] = (n-2)/2`,
`Var(wt) = (n-2)/4` (exact Fractions, e.g. `n=7: E=5/2, Var=5/4`). Hence
`Var(ν₂/n) = (n-2)/(4n²) ≈ 1/(4n)`.

## The weight-distribution check (exact, n=2..9)

```
n  #preimg/val  dist==Bin(n-2,1/2)  E[wt]==(n-2)/2  Var==(n-2)/4
2   4              True                 True            True
3   4              True                 True            True
...
9   4              True                 True            True
```

`E[wt]=3/2, Var=3/4` at n=5; `E=2, Var=1` at n=6; `E=5/2, Var=5/4` at n=7 —
exact, not fitted.

## Oracle still exact (canonical fold_nu2)

`nu2(53)=18`, `nu2(64)=27`, `nu2(4000)=1975`, `mu_4000 = 0.497259` (within 0.01
of 0.4977), and `s_sos == literal submask-XOR` at 53, 64, 100.

## What this establishes and what it does not

This makes directive 10's `fair-model-exact-binomial` claim **PROVED** rather
than measured: the exact binomial distribution is a *consequence* of the rank
fact, not an empirical fit. The independence/weak-dependence of the sequence
`ν₂(n)/n` across `n` for the *fixed prime* `h` is NOT settled — that is
precisely the content of `s2_N → 0`, still the open problem.

None of the five closed doors is touched: this is a statement about the fold on
uniform input, orthogonal to the structural "h is complicated enough"
hypotheses the doors refute (all-ones stays kernel, Thue-Morse stays sublinear,
anti-dyadic stays bounded).

## Falsifier / attack

For Theorem 2 to fail, some image of `Φ_n` would need a fiber of size other
than 4, or `wt` not binomially distributed on the uniform cube — both
contradicted by the exhaustive census (`2^(n-2)` images, every fiber size 4,
n=2..8) and the exact moments (n=2..9). Verified by two routes, so this stands
as proved.

```claim
id: fold-rank-n-minus-2-binomial-proved
statement: Under the operative row range d=2..n-1 (an (n-2)x(n) matrix), the
  submask-XOR fold matrix Phi_n has rank n-2 and kernel span(even-alt,
  odd-alt) whose XOR is all-ones; Phi_n is surjective onto F2^{n-2} and every
  image has exactly 4 preimages; for h uniform on the cube wt(Phi_n h) is
  exactly Binomial(n-2, 1/2) with E[wt]=(n-2)/2 and Var(wt)=(n-2)/4, so
  Var(nu2/n)=(n-2)/(4n^2) ~ 1/(4n). This makes the exact-binomial and the
  prefix-variance null log(N)/(4N) rest on a proved rank fact, not a fit.
hypotheses: floored convention d in [2,n-1]; the submask-XOR cell
  T(n,d)=XOR_{s subseteq d} g[s] as the definition of Phi_n (verified equal to
  the Pascal-mod-2 binomial-fold); h uniform on the cube; exact F2 elimination
  (n=2..40), exhaustive kernel census (n=2..12), exhaustive 2^n enumeration
  (n=2..9), and canonical oracle values nu2(53)=18, nu2(64)=27, nu2(4000)=1975,
  mu_4000=0.497259 all reproduced.
holds-here: yes (epoch fixed by the rank argument; the moments hold for uniform
  h at every n as a consequence, verified by exhaustive enumeration n=2..9).
status: proved
bearing: the uniform-h expectation and prefix-variance null are now proved
  rather than measured — the whole contraction to the primes is that the fixed
  prime string h is not known to be non-adversarial for Phi (measured mu_N
  0.499658 sits exactly on 1/2). Sharpen: prove s2_N -> 0 for the prime h is
  the entire open problem (directive 14 sharpest form). None of the five closed
  doors reopened: all-ones stays in the kernel, Thue-Morse stays sublinear.
anchor: code/out/fold_alln_theorems.captured.txt ; code/lib/fold_matrix.py ;
  code/fold_rank/verify_alln_theorems.py
```
