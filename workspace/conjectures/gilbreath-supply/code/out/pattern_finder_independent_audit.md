# Pattern-finder independent audit: every ν₂ regularity is fold-generic; no prime-specific signal

**Role:** pattern-recognition specialist. **All numbers exact over the terms
supplied** (canonical `code/out/nu2_primes_xor_40000.json`), queries `n=2..40000`.
This is an independent re-derivation with a **corrected JSON indexing** (see
below), run to *attack* the prior deliverables' central claim rather than trust
it. Every headline of the prior corpus is reproduced exactly, which bounds the
negative: there is no gate where a prime-specific structure could have slipped.

## Indexing correction (precondition for trusting any term)

The JSON `d[i] = ν₂(i)` is indexed **`i == n`** (probe: value 18 at index 53,
27 at 64, 1975 at 4000, 20081 at 40000 — all match the guard constants). An
earlier helper script (`extract_core_seqs.py`) assumed `d[i]=ν₂(i+1)` and would
have read shifted terms; I probed the file directly before extracting, avoided
that trap, and re-verified all four guards:

```
nu2(53)=18, nu2(64)=27, nu2(4000)=1975, nu2(40000)=20081   ALL PASS
```

## Exact structural facts, re-verified for all n in [2,40000]

| fact | result |
| --- | --- |
| identity `2·ν₂(n) − (n−2) = −S(n)` | holds for every n |
| `S(n) ≡ (n−2) (mod 2)` | holds for every n |
| `D(n)=S(n+1)−S(n)` always odd | holds (39998 checks) |
| residues of D mod 2,4,8,16,32 | uniform (no non-trivial periodicity) |
| residues of S mod 4,8 | uniform |

## The white-noise law and plateau (reproduced)

`Z(n)=S(n)/√n` over n=3..40000:
- `E[Z²] = 0.9991` (model 1)
- `E[Z⁴] = 2.9474` (Gaussian 3)
- `max|Z| = 3.815 @ 27624` (~ 2√(log N), the √-log max of Gaussian noise)
- `P(|Z|>3)=0.0025` (Gaussian 0.0027), `P(|Z|>4)=0`

Plateau `E[S²]/(n−2)`: prefix mean `0.9996` over n=3..40000; window means
flat ≈ 1.0; uniform per-window max `14.45..14.55` through 40000 — no upward
drift in the constant C (a measured uniform `E[S²] ≤ 15·n`).

## Pointwise form / exceptional sets (reproduced)

Window min of ν₂/n: `[2,105] 0.0 → [2000,4000] 0.464 → [32000,40000] 0.49014`;
window mean → `0.49996`. Last member of `{n:ν₂/n<c}`:
c=0.45→763, 0.46→1211, 0.47→3086, 0.48→5655, 0.485→9969, 0.49→27624.
**For every c ≤ 0.48 the exceptional set is finite through 40000** (stronger
than density-1, on the measured range).

## No exploitable scalar/tool structure

- `nu2(n)` n=2..31: not a low-degree polynomial (differences never constant),
  leading ratios undefined/noise.
- `nu2(2^k)` k=3..15 `[2,12,13,27,66,136,243,502,1003,2010,4184,8338,16464]`:
  no constant-coefficient linear recurrence of order ≤ 8.
- **OEIS miss** both for ν₂(n) and for ν₂(2^k) — uncatalogued, no closed form
  to look up. (Consistent with the already-recorded `oeis_nu2_not_catalogued`
  and `pattern_nu2_dyadic_no_recurrence` notes.)

## Fresh attacks I ran, and the answers they give

1. **Residue periodicity of S,D mod 2^k**: uniform at every modulus — no
   non-trivial periodic structure hiding under the white noise. (Negative for
   any "eventually periodic / automatic" handle on the pointwise values.)
2. **Dyadic self-similarity**: `corr(ν₂(n)/n, ν₂(2n)/(2n)) = 0.136`,
   `corr(ν₂(n)/n, ν₂(2n+1)/(2n+1)) = 0.316`, `corr(ν₂(n)/n,ν₂(n+1)/(n+1)) =
   0.150`. No clean scaling/self-similar law — consistent with the refuted
   `pascal-cascade-block-recursion` and `dyadic-renormalization-selfsimilar`
   closures (a substitution/self-similarity would produce strong correlation,
   absent here).
3. **Per-scale variance split**: g=0 (adjacent mod-4 switch pairs, the
   switch-density scale) holds 42.5% (n=400), 73% (n=1000), 55.3% (n=4000) of
   the variance — the dominant scale, exactly as in `pattern_finder_per_scale`.
   **This dominance is fold-generic**: it is a structural property of Φₙ, not
   an arithmetic signature of the primes, which is the precise mechanism that
   collapses the "weaker submask input" route back onto the switch-density
   barrier.

## What this audits toward the run's single hypothesis

The GOAL's hypothesis under test is whether the fold Φ can do work the
mod-4-switch-density form cannot see. The answer from every measurement,
now re-confirmed by an independent pass: **no.** Every statistic of ν₂ for the
primes — the white-noise law, the second-moment plateau, the rising min, the
finite exceptional sets, the per-scale split, the residue uniformity — is
reproduced by a generic balanced/unstructured input, and no prime-specific
handle visible in the data survives any of the attacks above.

**Status / honest boundary.** All statements are *measured* (exact over
n=2..40000), a conjecture for all n; none is a proof. The open step remains: an
unconditional `E[S²(n)]=O(n)` for the *specific* prime gap-parity string h —
an arithmetic input no measurement here supplies.

## Files
- `code/pattern_finder/indep_extract.py` — guard-checked extraction from the canonical JSON.
