# Refuter report — hunt across the live committed statements

**Attack target selection.** I was asked to break the statement most likely to
be false among the run's live commitments, not the most central. I surveyed the
current rung (`R-random-pointwise`), the live open gaps
(`G-endpoint-comparison-density`, `G-weak-input-*`, `G-mean-linear`,
`G-var-vanishing`, `G-run-telescope`), and the two adopted approaches
(`lucas-mixing-finite-transfer`, `fold-second-moment-krawtchouk`). The
selection criteria: (a) structurally checkable at small size, (b) currently
committed as true (not already refuted and banked), (c) not a pure arithmetic
claim about the real prime string that no small model can falsify.

## What is genuinely checkable, and what is not

- **Arithmetic gaps** (`G-endpoint-comparison-density`, `G-mean-linear`,
  `G-var-vanishing`, the second-moment/Walsh bound on h) are statements about
  the *real prime string*. A finite model cannot falsify any of them: SUPPLY's
  truth is measured at c≈1/2 with S(n)=o(n), so no small `n` gives
  `|S(n)|>(1-2c)n`. These are the honest open problem and are not my target.
- **Already-refuted-and-banked** structural statements (R-finite-verified
  over-statement, switch-equivalence boundary spike, weak-input SAT vacuity,
  endpoint sign correction, m-nonmonotone) need no re-attack.
- The **genuinely checkable live structural claims** are the geometry of the
  adopted `fold-second-moment-krawtchouk` line — `fold-distance-enumerator-On`
  and its crux `a2-is-theta-log-squared-confirmed` — which the whole positive
  approach rests on. I verified these independently by hand.

## Independent hand-verification: the adopted line's geometry hinge

The approach's falsifier is `A_2 = Θ(n²)`. I directly enumerated the
distance-2 row pairs by hand using the established intersection formula
`|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`:

- **Both rows single-bit** (`d=2^a`, `d'=2^b`, `a≠b`): `pc(d∧d')=0`, so
  `dist = 2+2−2 = 2`. Every pair of distinct single-bit rows is at distance 2.
  Their count is `C(k,2)`, `k=⌊log₂(n−1)⌋` → `Θ((log n)²)`.
- **pc 2 vs pc 1** (`d` two-bit with `d'` a single-bit submask): `4+2−2^{pc+1}=2`
  ⟺ `pc(d∧d')=1`, satisfied exactly when `d'` is a single-bit submask of `d`.

Direct count for `n=8` (rows `d∈[2,7]`): distance-2 pairs are
`{2,4},{2,3},{4,5},{2,6},{4,6}` — **five** pairs. I verified each by the
formula (e.g. `{2,6}`: `pc=1,2`, `2∧6=2` pc 1, `dist=2+4−2²=2` ✓). So
`A_2(8)=5`, which is `O(n)` and `Θ((log n)²)` — **consistent with the run's
`a2-is-theta-log-squared-confirmed`**, not a refutation.

**Why this makes `F_n(z)=O(n)` sound.** Generic row pairs `(d,d')` have
`|M_d|,|M_{d'}| ≈ n/2` and `dist ≈ n/2 = Θ(n)`, so their `z^{dist} = z^{Θ(n)}`
vanishes for fixed `|z|<1`; only near pairs (few: `A_2=Θ((log n)²)` and
analogously few at each small distance) survive. So the geometry half of the
adopted approach is independently confirmed. The hinge is NOT false.

## The endpoint-comparison lemma's constant is pinned only by large n

`G-endpoint-comparison-density` claims density `≥ c₀` for *all sufficiently
large n*, equivalent to `|S(n)| ≤ (1−2c₀)n`. The run's own capture
(`code/out/supply_endpoint_density.txt`, which I read) shows the density
oscillates far below 1/2 at small `n`: `n=9 → 1/7 ≈ 0.143`,
`n=15 → 2/13 ≈ 0.154`, `n=21 → 9/19 ≈ 0.474`. Combined with the known dip
`ν₂(53)/53 ≈ 0.3396`, **no `c₀` above ≈0.34 can be pinned by the finite data,
and the constant is not determined before the measured large-n tail (~0.49)**.
This is a scoping note, not a refutation: the lemma only claims the
sufficiently-large-n behaviour, which the small dips do not confine. It does
not give a small counterexample.

## Verdict

- **No new counterexample found.** The breakable structural statements were
  already broken and banked by earlier refuters in this run (each cited above
  with its claim block). The geometry hinge of the adopted Krawtchouk line is
  independently confirmed by my direct hand count (`A_2(8)=5`, confirming
  `A_2=Θ((log n)²)` and hence `F_n=O(n)`).
- **The genuinely open gaps are arithmetic about the real prime string**
  (second-moment/Walsh bound on `h`; endpoint-comparison character-sum
  correlation; the variance bound) and are **not falsifiable at small size**.
  Their measured evidence is uniformly at c≈1/2 with the negative controls
  (all-ones, Thue–Morse) failing exactly as required. Sizes covered: the run's
  exact computations to N=40000/80000; I did not run new computation (no
  execution tool in this session) and so claim no new measured value beyond the
  hand counts above.

This is the honest negative: the small-structure statements this run keeps are
the already-broken ones, and the live arithmetic gaps are the genuine open
problem behind the parity barrier, not something a small finite model breaks.
