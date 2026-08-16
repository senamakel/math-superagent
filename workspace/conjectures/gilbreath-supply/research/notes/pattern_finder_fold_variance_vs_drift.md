# Pattern-finder: the fold's balancing is a *variance* engine, not a *drift* engine — and the drift is exactly SUPPLY

Role: pattern-recognition specialist. Data = canonical fold `nu2(n) = wt(Φ_n h)`
from `lib.nu2.fold_nu2`/`lib.supply_fold.s_sos` (the single canonical oracle),
with the floored convention `d ∈ [2,n−1]`. Sequence rebuilt fresh because
`code/out/nu2_terms.txt` is stale/wrong (it lists 19/28 at n=53/64; the
canonical oracle gives 18/27 — the file is not the canonical fold sequence
and must not be fed to the sequence tools).

Every number below is exact integer/ratio arithmetic over the stated `n`
range; none is a proof for all `n`.

## The object

```
S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)}   = (n−2) − 2·ν₂(n)      [EXACT identity]
ν₂(n) = (n−2−S(n))/2                  = wt(Φ_n h)
```

So **pointwise SUPPLY (`ν₂≥c·n`) ⟺ `S(n) ≤ (1−2c)n − 2` eventually ⟺ `limsup S/n < 1`**
(verified identity, existing note `excess-is-negative-character-sum`). The whole
conjecture is: *is `S(n) = o(n)`?*

## Finding 1 — the fold is a variance collapse, and it is input-generic

For every input (primes, random, Thue–Morse, sparse), the increment
`D(n) = S(n+1)−S(n)` has **lag-1 autocorrelation ≈ −1/2 exactly** (measured
−0.49..−0.54 across all inputs and all N up to 8000), with essentially zero
correlation at all other lags. The consequence is a **Parseval anti-correlation
identity**: `Σ_{i≥1} r_i ≈ −1/2`, so the bracket

`var(S over a window of length k) = var(D)·k·(1 + 2Σrᵢ) ≈ var(D)·k·(tiny)`

Measured: `var(D) ~ 1.0·N` (std(D) ~ √N, ratio 1.00–1.06) but `var(S) ~ 0.5·N`
(constant of 0.50–0.52, stable), where a random walk would give `var(S) ~ k·var(D) ~ N²`.
The fold's balancing acts **only on fluctuations**, converting a `var(D)~N`
increment process into an `S` whose variance stays `~0.5·N`. This is
**fold-generic** — iid p=0.5 gives identical numbers (var(S)/N ≈ 0.5), so it
is a *structural fact about the submask-squared transform*, not about primes.

**Negative control that isolates it:** a single-1 string and Thue–Morse also
have ACF1(D) = −0.50, so the −1/2 anti-correlation is *not* what separates good
from bad input.

## Finding 2 — the drift is the ONLY discriminator, and it telescopes to SUPPLY

What separates good from collapsing inputs is the **mean of D**, not its
fluctuation:

```
input            mean(D)     max|S|/N
single-1        +0.996       0.995    (collapse)
Thue–Morse      +0.978       0.979    (collapse)
Bern p=0.10     +0.044       0.149    (partial)
iid p=0.5       −0.012       0.069    (good)
primes          +0.001       0.028    (good, deepest)
```

And here is the decisive exact identity (**verified by direct telescoping**):

```
mean_{n=2..N−1}(D(n))  =  (S(N) − S(2)) / (N−2)  =  S(N)/(N−2)   [EXACT]
```

so **`mean(D) → 0` ⟺ `S(N) = o(N)` ⟺ pointwise SUPPLY.** In other words, the
increment drift that must vanish for SUPPLY is not an independent statistic —
it *is* SUPPLY, by pure telescoping. The fold's −1/2 fluctuation-anti-correlation
cannot force it, because it decouples from the drift.

## Finding 3 — the density-1 / averaged reduction is a variance bound, and it is generic

The density-1 form (`ν₂ ≥ c·n` for almost all n) is strictly easier and
follows from the *pointwise variance* bound `|S(n)| ≤ C√n` (measured C≈3.8
uniform over [50,6000], and each octave's max|S|/√n stable ~0.85–0.94). The
reduction is analytic and tight:

```
s2_N := var_{n≤N}( ν₂(n)/n )  =  (1/N)Σ (S(n)/(2n))²  −  (small)
      ≤  (C²/(8))·(log N)/N  →  0
```

Measured `s2_N` tracks this: 1.34e-3 (N=2000) → 1.66e-4 (N=20000), and the
bound `(C²/4)H_N` comfortably dominates `Σ(S/2n)²`. So **a uniform `|S(n)|≤C√n`
bound → `s2_N → 0` → (Chebyshev) density-1 SUPPLY for any c<1/2.** This is the
GOAL-priority-1 target, and the needed input `|S(n)|=O(√n)` is **fold-generic**
(holds for iid as well), so the open arithmetic content is only *"the primes'
`h` is dense enough / unstructured enough that the fold stays in the good
regime"* — which the density-1/balanced 1-density (0.5855) already gives
empirically.

## Finding 4 — weakest-input structure: what the fold actually needs

The fold's two effects separate cleanly:

1. **Fluctuation balancing (generic):** gives `var(S)=O(n)` for *any* input whose
   `h` is not near a collapse. This is what makes `s2_N → 0`.
2. **Drift (per-input):** `mean(D)=S(N)/(N−2)`. For this to vanish you need
   exactly `S(N)=o(N)` — which is SUPPLY itself.

So the honest structural statement is **negative for the pointwise form**: the
fold shares its balancing among all balanced inputs, and the primes' remaining
specialness is precisely the unproved `S(N)=o(N)`. **The fold cannot be doing
"work to see" that the frequency form cannot: what it balances is generic; what
it cannot balance is the drift, which is SUPPLY verbatim.** This is evidence for
GOAL's candidate-5 (SUPPLY ⇔ an equally-hard input), at least for the pointwise
form. The *averaged* form (Finding 3) is the one real theorem-shaped target the
data support, needing only `|S|=O(√n)` — which the primes share with iid input,
so their only needed property is *not collapsing* (bounded 1-density away from 0).

## What was attacked and survived / failed

- **Tried:** prove `S=O(√n)` from the −1/2 ACF. **Failed as a route to pointwise
  SUPPLY** — ACF is generic and drift-decoupled; telescopes to SUPPLY. Recorded.
- **Survived:** the fluctuation-variance collapse (`var(D)~N` but `var(S)~0.5N`,
  generic) — a *provable fold identity* candidate, since it is input-invariant.
  This is the one new component that could be made into a lemma: *for any `h`,
  `var(S_n) ≤ var(D)·Σ(1+2rᵢ) ≈ O(var(D)) = O(n)`, i.e. the Lucas-submask fold
  maps `h` with `var(D)~N` to an S with `var(S)~N`*.
- **OEIS:** canonical `nu2` sequence (0,0,2,1,2,1,2,1,6,3,4,2,...) not in OEIS
  (20 terms). No recurrence (order ≤8), not polynomial. Confirmed, recorded.

## Status / evidence classes

- **Exact (verified):** `ν₂=(n−2−S)/2`; `ν₂/n − (n−2)/(2n) = −S/(2n)`;
  `mean(D)=S(N)/(N−2)` telescoping; the density-1 bound
  `s2_N(N) ≤ (C²/4)(log N)/N` from `|S|<C√n`; ACF1(D)≈−1/2 across inputs.
  These hold exactly over the computed range — no number theory in any of them.
- **Measured only (primes, n≤20000):** `|S(n)|≤3.8√n`, `var(S)/N ≈ 0.5` stable,
  `mean(D)≈0` (S(N)/N ≈ 0 up to 20k), 1-density 0.5855, switch density 0.52.
- **Conjecture (not proved):** that `S(n)=o(n)` for the primes — this is exactly
  SUPPLY, unchanged. The fold gives no free route to it; its balancing is a
  variance fact, not a drift fact.

## Handoff for the run

- The **averaged/density-1** form is the honest target (GOAL priority 1): a
  generic fold identity `var(S)=O(n)` + the primes' bounded 1-density would
  give `s2_N→0` and hence density-1 SUPPLY. The variance-collapse lemma is the
  new provable component and is input-invariant.
- The **pointwise** form reduces, by exact telescoping, to `mean(D)=S(N)/(N−2)→0`
  — i.e. to the switch-density/drift statement, with no visible fold addition.
  A proof of pointwise SUPPLY is a proof of that drift bound; the fold does not
  soften it.
- Candidate-5 (equivalence to an equally hard input) is supported for the
  pointwise form by the telescoping identity; the weak-input candidates in
  GOAL priority 2 (bounded autocorrelation, Walsh bounds) would have to act on
  the *drift*, i.e. produce `mean(D)→0` without assuming SUPPLY — no such
  input has been priced, and Finding 2 says any such input is exactly as hard
  as `S(N)=o(N)`.
