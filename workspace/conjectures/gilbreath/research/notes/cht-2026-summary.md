# CHT 2026 — Cramér random model + deterministic analysis (TASKS item 4 — DONE)

**Chase, Hunter, Tao, "Gilbreath's conjecture: a Cramér random model and a
deterministic analysis", arXiv:2607.08712v1 [math.CO], 9 Jul 2026.**
Full text: `research/sources/chase-hunter-tao-2026-full-html.full.md`
[[chase-hunter-tao-2026-full-html.full]] (HTML body); abstract-page duplicate
`chase-hunter-tao-2026-cramer-random-model-gilbreath.full.md`.

## Normalized-gap equivalence

Removing the top row and left diagonal, dividing by 2, subtracting 1 from the
new top row: **GC ⟺ the left diagonal of the array from
`a_n = (p_{n+2}−p_{n+1})/2 − 1` is eventually `{0,1}`-valued.** First nine
normalized gaps `0,0,1,0,1,0,1,2,0` (OEIS A100820). This is the run's
`{0,2}`↔`{0,1}` correspondence exactly (claim `cht-normalized-gap-definition`).

## Theorem 1.6 — the deterministic inverse theorem (the object of Route C)

If
- `a_n ≤ 2^M`,
- **no length-L 0-block**, and
- **no `{0,d}`-block** (`2^{M−m} < d ≤ 2^{M−m+1}`) **of length `≥ R_m − 3R_{m−1}`
  at depth `≤ 2R_{m−1}`**, where `R_m ≥ 4R_{m−1}`, `R_0 ≥ 100L·8^M`,

then `a(N−1,1) ∈ {0,1}`. **The only obstructions to decay are long zero-blocks
or very long shallow `{0,d}`-blocks** (claimed by the contrapositive machinery
of towers and good blocks).

### The column restriction (iii), verbatim

> There does NOT exist `1 ≤ m ≤ M`, `2^{M−m} < d ≤ 2^{M−m+1}`, `0 ≤ i ≤ 2R_{m−1}`,
> `k ≥ R_m − 3R_{m−1}`, `N' ≤ j ≤ N−i−k`, with `a(i,j),..,a(i,j+k−1) ∈ {0,d}`.

with `N' = ⌊N/2⌋` — **the `{0,d}`-block obstruction (d ≥ 2) is confined to the
RIGHT HALF (columns j ≥ N')**. The run's own leading `{0,2}` block at j=1 is
category d=1 (outside (iii)) and sits at j < N', so it never violates (iii).

### Hypotheses held here? — holds-here: NO

Checked on real prime data to depth 1000 (sieve 2e7, 1,270,607 primes): max
normalized gap = 89 → M=7; longest 0-run L=2 (provably exact: p,p+2,p+4 cannot
all be prime); `R_0 = 100·L·8^M = 419,430,400 ≫ 1000`. The theorem does not
bite at reachable depths (`cht-inverse-theorem-hyp-check`,
`cht-inverse-theorem-hyp-check-v2`).

**Directive 35 item 1 (this run): the right-half scan** at 6e8/depth 400
(`research/notes/cht-right-half-scan.md`, claim `cht-right-half-0d-scan-6e8`)
resolved the column restriction empirically: longest right-half `{0,d}`-block
(d≥2) = 25 (row 14, d=2); longest d≥4 = 24 (row 37); smallest CHT threshold
`T_1 = R_1 − 3R_0 = 5.63e16` (M=8, L=2) exceeds every observed block by
≥ 2.25e15×. The `{0,d}`-block obstruction is absent at every scale Theorem 1.6
controls, in the half where it matters. **The theorem does not bite at
reachable depths; route C calibrated.**

### The authors' own difficulty assessment

The run's thread records the authors' assessment of the obstacle hypotheses
(themselves: hypotheses (ii) and (iii) look "difficult to establish rigorously,
even if one assumes strong conjectures on the primes such as the
Hardy–Littlewood prime tuples conjecture"). This is the best calibration
available: the people who proved the inverse theorem judge the obstructions it
isolates to be as hard as the conjecture itself, short of unproved analytic
number theory. Also, axiom (i) for the primes needs Cramér (gaps O(log² n)),
open and strictly stronger than BHP (α=0.525 unconditional). So Route C needs
strictly more than Route B (Granville ν₂, which needs only BHP).

## Other CHT statements this run can use

- **Theorem 1.3 (general random models):** for every ε>0 ∃δ>0, independent
  nonneg-integer `a_n` with (i) `a_n ≤ δn` a.s. and (ii)
  `P(a_n ∈ A) ≤ 1−ε` for every 2-separated set A ⇒ a.s. left diagonal
  eventually `{0,1}`. Growth threshold between δn (works) and 2^{n+1} (fails).
  This is the cleanest validation of the run's
  `two-separation-hypothesis`: 2-separated non-concentration is the operative
  general-class hypothesis (consistent with Ross 2026 and Eppstein).
- **Lemma 3.10 (parity formula):** `a(i,j) ≡ Σ_k C(i,k) a_{j+k} (mod 2)`;
  Lucas' theorem governs. Generalizes Odlyzko's mod-4 linearization to the
  parity of any entry — the mod-4/rule-90 level is parity-only, never fixes
  the exact `{0,2}` value.
- **Lemma 3.7–3.8:** `{0,d}` closed under |x−y|; parentage dichotomy of
  `{0,d}`-blocks. (This closure is the run's `closure-0d-double-edge` — the
  same mechanism that pins 1 at d=2 preserves large disturbances at d≥4.)
- **Theorem 1.4 (continuous model):** `c_i = E[a(i,j)]` in i.i.d.-exponential
  model has `Σ_{i≤n} c_i ≥ log(n+e)`; `c_i` cannot decay faster than 1/i.
  c_0=1,c_1=1,c_2=7/9,c_3=227/288 (non-monotone). Neither convergence to 0 nor
  boundedness is proved (`cht-decay-lower-bound-logn`).

## Status

The `{0,d}`-block row of the CHT list is closed for this run (right-half scan,
Directive 35 item 1 DONE): Theorem 1.6's bite is out of range, matching the
authors' own difficulty assessment. Route C stays calibrated (not pursued);
the run stays on Route B (Granville ν₂) as primary. What CHT contributes to
the live route: the parity formula (Lemma 3.10) is the algebraic handle behind
the mod-4 linearization, and Theorem 1.3 is the rigorous statement of the
2-separation hypothesis that general-class work should lean on.
