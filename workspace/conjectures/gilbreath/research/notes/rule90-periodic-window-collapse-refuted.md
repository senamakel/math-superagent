# Contradiction: `rule90-periodic-window-collapse` (any p) vs the proved dyadic-collapse theorem (power-of-2 p)

**Scholar, 2026.** Two on-disk claims about the same object — the maximal
`{0,2}`-suffix length / `nu2` of the right diagonal of a periodic halved-gap
bit string `h` — say different things, and one is false as stated.

## The two statements

**Claim A — `rule90-periodic-window-collapse` (status: asserted).**
> If h is periodic with period p, then every {0,2}-tail cell is an XOR-fold of
> a bounded window of h, taking only finitely many values ... Hence the
> {0,2}-suffix length and nu2 are O_p(1).

This asserts collapse for **ANY** period p.

**Claim B — the proved dyadic-collapse theorem**
(`research/notes/dyadic-collapse-proof.md`, status: proved; machine-verified
`code/out/dyadic_collapse_final_verify.captured.txt`, ALL OK).
> If h is eventually periodic with period a POWER OF TWO, then
> `nu2(q_n) ≤ N0 + 2^k` for all n (exact case: `nu2 ≤ 2^k − 1`). The proof
> (submask factorization `d = D·2^k + s`) works **iff the period is a power of
> two**.

Claim B is strictly stronger information and is **proved**; Claim A is only
**asserted** and is **false as stated**.

## The refuting data (on-disk, exact integers)

`code/out/dyadic_periodicity_correct.captured.txt`:

| period p | nu2 at n=4000 | behavior |
|---|---|---|
| 1,2,4,8,16 (powers of 2) | 0..1 | bounded (collapses) |
| 3 | 2666 | **linear** (~0.66·n) |
| 5 | 2132 | linear (~0.53·n) |
| 7 | 2284 | linear |
| 9 | 1648 | linear |
| 15 | 1064 | linear |

The odd-factor periods grow linearly with n; they are **not** O_p(1). Claim A
predicts they are bounded — directly refuted.

## Why Claim A's reasoning fails (located flaw)

The first sentence of Claim A is trivially true but does not imply the
conclusion. Every fold cell value is in `{0,1}` (halved) / `{0,2}` (raw),
i.e. "finitely many values" is trivial — each cell is 0 or 2 regardless of
periodicity. But **the length of the maximal {0,2} suffix is not controlled by
the finiteness of each cell's value-set**: a long suffix can consist of cells
each drawn from `{0,2}` whose fold bits happen to be 1. Periodicity of `h`
does NOT force the fold bits of the deep cells to vanish — that vanishing is
exactly the power-of-2 submask-factorization argument, which fails whenever the
period has an odd factor (binary digits of a non-power-of-2 shift overlap, the
inner XOR is not an even number of equal terms).

So the correct, proved statement is B (period a power of 2 ⟹ collapse). The
"any p" version (A) is a leaky over-generalisation: it borrows the collapse
conclusion from the power-of-2 case without the hypothesis that makes the
proof work.

## Resolution / action

- **`rule90-periodic-window-collapse` must be corrected** to read "period a
  power of two" (or marked refuted and superseded by the proved B). As filed it
  is a false load-bearing-looking claim.
- The correct collapse side of the dyadic dichotomy is **already the proved
  theorem B**; nothing is lost. The open content is unchanged: the odd-factor
  converse (`nu2 ≫ n` for period with odd factor) is conjectured, not proved,
  and G-supply (`nu2 ≥ c·n` for the aperiodic primes) stays the named-open
  hypothesis (`abgs-2011-s9-mod4-switch-limit-open`).

## Files
- This note: `research/notes/rule90-periodic-window-collapse-refuted.md`
- Proved theorem: `research/notes/dyadic-collapse-proof.md`
- Verification: `code/out/dyadic_collapse_final_verify.captured.txt`
- Measurement: `code/out/dyadic_periodicity_correct.captured.txt`

```claim
id: rule90-periodic-window-collapse-refuted
statement: The claim "h periodic of period p ⟹ nu2 = O_p(1)" (id rule90-periodic-window-collapse) is FALSE as stated for periods with an odd factor. The correct and proved statement is the dyadic-collapse theorem: h eventually periodic of period a POWER OF TWO (2^k) ⟹ nu2(q_n) ≤ N0 + 2^k (exact case nu2 ≤ 2^k − 1), whose submask-factorization proof works iff the period is a power of two. For odd-factor periods nu2 grows with n, e.g. period 3 gives nu2 = 2666 at n = 4000 and 132 at n = 200 (measured, exact), so nu2 is not O_p(1).
hypotheses: periodic halved-gap bit string h driving a 2-then-odds Gilbreath triangle; nu2 = #2s in the maximal {0,2} suffix of the right diagonal.
holds-here: yes (as a statement about the claim being false / the dichotomy being real)
status: checked (on-disk exact captures dyadic_periodicity_correct.captured.txt, dyadic_collapse_final_verify.captured.txt; the flaw located: finiteness of each cell's value-set {0,2} does not bound the suffix length)
bearing: supersedes rule90-periodic-window-collapse (asserted); the collapse side of the dyadic dichotomy is the PROVED dyadic-collapse theorem, not the over-general asserted claim. Does NOT close G-supply; the odd-factor converse (nu2 ≫ n) is still conjectured, and nu2 ≥ c·n for the aperiodic primes stays named-open (abgs-2011-s9-mod4-switch-limit-open).
contradicts: rule90-periodic-window-collapse
follows-from: dyadic-collapse-proved (proved theorem), rule90-interior-xor (proved)
anchor: research/notes/rule90-periodic-window-collapse-refuted.md
```
