# The supply problem

Prove or disprove, for the sequence of primes:

> **(SUPPLY)** There is a constant `c > 0` such that `ν₂(n) ≥ c·n` for all
> sufficiently large `n`.

Everything needed to read that is defined below. **No knowledge of Gilbreath's
conjecture is required, and none should be assumed.** This is a self-contained
question about the primes and one explicit linear map.

## Definitions

Let `q_1 = 2, q_2 = 3, q_3 = 5, …` be the primes. Build the
absolute-difference triangle:

```
A_0(i) = q_{i+1}                          i ≥ 0
A_{k+1}(i) = | A_k(i) − A_k(i+1) |        i ≥ 0
```

The **right diagonal through column n** is the sequence of cells

```
δ_k(n) = A_k(n − 1 − k),        k = 0, 1, …, n−1
```

so `δ_0(n) = q_n`, and each subsequent cell sits one row lower and one column
left. Read this diagonal from its bottom end and take the longest unbroken run
of cells whose value is `0` or `2` — the **maximal {0,2} suffix**. Define

```
ν₂(n) = the number of 2s in that suffix.
```

That is the whole object. `ν₂(n)` is a well-defined non-negative integer for
each `n`, computable exactly in `O(n²)` integer operations, and the target is a
linear lower bound on it.

**Convention note.** The suffix is floored at index 2 (the run's canonical
`lib.rightdiag.cycle_and_nu2`). A variant that floors at index 0 differs by at
most 1 and changes nothing asymptotic, but pick one convention, state it, and
keep it — an earlier investigation lost a cycle to two conventions disagreeing
by exactly 1 on the degenerate cases.

## What is already established, and may be used freely

These are imported as proved. Do not re-derive them.

1. **Linearisation.** `ν₂(n) = wt(Φ_n h)` over `F₂`, where `h` is the bit string
   `h[j] = ((q_{j+1} − q_j)/2) mod 2` and `Φ_n` is the explicit
   Pascal-mod-2 (Rule-90) fold matrix with entries `C(k−1, j−(n−k)) mod 2`.
   So the question is: *how heavy is the image of the prime gap-parity string
   under an explicit binomial fold?*
2. **Lucas.** `C(d,i) mod 2 = 1` iff `i` is a binary submask of `d`. Hence the
   depth-`d` fold cell is `XOR` over submasks of `d`.
3. **Kernel.** `rank Φ_n = n−3`, nullity 1, and `ker Φ_n = span(all-ones)`
   (exact `F₂` elimination, verified `n = 2..20`).
4. **Dyadic collapse.** If `h` is eventually periodic with minimal period a
   power of two, `ν₂(n) = O(1)`. Proved from (1)+(2).
5. **The primes are not eventually periodic.** Proved, conditional on Shiu 2000
   (held at abstract level only — treat as conditional, not proved).

## What is measured

Exact integers, streamed one row at a time:

| quantity | value |
| --- | --- |
| `ν₂(n)/n`, real primes, `n = 50..3999` | `0.420 … 0.520`, no downward drift |
| `ν₂(n)/n` at `n = 4000` | `0.4933` |
| `ν₂/w` (`w` = number of gaps ≡ 2 mod 4) | min `0.7049` over `n = 100..2000` |

So the truth is `c ≈ 0.49`, and **any** fixed `c > 0` suffices. Even the far
weaker `ν₂(n) > n^{0.526}` would do — at `n = 10⁶` that asks for ~2,900 against
a measured ~490,000. The margin is not the difficulty.

## Five closed doors — do not reopen them

Each of these was a serious attempt to force `ν₂` large from a *structural*
property of `h`, with no number theory. All are refuted. A proposed solution
that implies any of them is wrong.

1. **Weight alone.** `ν₂ ≥ c·wt(h)` is **false**. Counterexample: `h` all-ones
   (consecutive odd numbers) has maximal weight and `ν₂ = O(1)` — it is exactly
   the kernel vector of (3).
2. **No long constant runs.** The hypothesis is **false for the primes** by
   Shiu 2000 (arbitrarily long runs of consecutive primes in one class mod 4,
   i.e. arbitrarily long all-zero runs in `h`).
3. **Aperiodicity.** **Insufficient.** Thue–Morse (`h[j] = wt(j) mod 2`) is
   aperiodic with `ν₂` sublinear — measured `ν₂/n` falling `0.270 → 0.011`
   across `n = 100 → 4000`.
4. **Anti-dyadicity.** **Insufficient.** Half-step strings that are balanced
   *and* anti-dyadic have `wt(Φ_m h) ∈ {1,2}` for `m = 8,16,24,32` — bounded,
   so the ratio decays.
5. **Periodicity of the primes.** Proved (5 above) and **inert**, because 4
   shows the converse fails.

**The unifying obstruction.** `Φ` has low-weight images on structurally rich
inputs. Near-injectivity (3) bounds the *kernel*, not the *weight*. Therefore
no hypothesis of the form *"h is complicated enough"* can work, however it is
sharpened. Any new route must use something other than complexity of `h`.

## The reduction that exists, and why not to take it

`ν₂ ≥ c·n` reduces to: *a positive fraction of consecutive prime pairs differ
mod 4.* That is a named open problem — Ash–Beltis–Gross–Sinnott 2011 §9 state
it is unknown whether the frequency tends to any limit and that it "cannot be
treated using L-functions". It sits behind the parity problem, and the
unconditional literature (Shiu, Ruzsa, Martin) bounds the *equal*-residue side,
the wrong direction.

So the reduction is available and is a dead end. **The reason to attack SUPPLY
directly is that the reduction discards structure**: it throws away `Φ`, Lucas,
and the kernel, and replaces a question about a folded image with a question
about raw frequency. The fold may be doing work the frequency form cannot see —
for instance `ν₂` could be forced large by cancellation properties of `Φ` on
*any* string satisfying a weaker arithmetic input than positive switch density.
That possibility is unexplored and is this problem's reason to exist.

## What counts as a result

In descending order of value.

1. `ν₂(n) ≥ c·n` unconditionally. (Solves it.)
2. `ν₂(n) > n^β` for any fixed `β > 0.525`, unconditionally.
3. `ν₂(n) ≥ c·n` for **almost all** `n`, or on a density-1 set. Sieve methods
   are sometimes not blind to averaged forms even when blind to pointwise ones;
   this is the most likely place a real theorem exists.
4. A proof from an arithmetic input **strictly weaker** than positive mod-4
   switch density — the central open question of this problem.
5. A proof that no such weaker input suffices, i.e. that SUPPLY is *equivalent*
   to the switch-density statement. This would be a genuine negative theorem and
   closes the problem honestly.
6. A sixth closed door: another structural hypothesis refuted, with witness.

Report 3, 4 or 5 as the realistic targets. **Do not report a measurement as a
proof, and do not claim Gilbreath** — this problem does not mention it and
solving it is only one input to it.
