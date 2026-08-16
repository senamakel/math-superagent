# Goal — third pass

**Read `research/CONCLUSION-PASS2.md` first.** The second pass closed with a
negative: no functional at order `1 < K ≲ ⌊n/2⌋` survived pricing against an
input weaker than pointwise mod-4 switch density. Three results stand from it
and are not to be re-derived — linear supply without positive switch density,
the ~1/8 weight threshold, and `K*(n) = ⌊n/2⌋`.

## The one computation this pass owes

The second pass left exactly one thing unfinished, and it is concrete:

> Does the minimum weight ratio at which linear supply becomes typical tend to
> **0**, or plateau near **1/8**?

The measured column is `0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125`
for `n = 8, 10, 12, 14, 16, 32, 64, 128`. It fell monotonically and then held at
0.125 twice, and the run was stopped before resolving it. The two answers mean
different things:

- **Tends to 0** — linear supply is typical at *any* positive density, so the
  arithmetic input the primes need reduces to positive density plus
  non-adversariality. That is a materially weaker demand than switch density and
  would be this workspace's first affirmative result.
- **Plateaus at a constant** — that constant is real, belongs in the statement,
  and the demand does not weaken.

Push `n` as far as the sampled method allows, report the ratio per `n`, raise
the sample count above 300 per weight so the `frac` column can support the
claim, and say which behaviour the data supports **without declaring beyond it**.
Everything else in this file is secondary to that column.

## Note on directives

Operator directives now reach detached specialist runs directly, not only the
next attempt and the director. If a directive contradicts what you are doing,
it outranks it — apply it and say in your report what you stopped. The previous
two passes lost hours to directives that were acknowledged in the ledger and
never executed by the role they were aimed at; that channel is now fixed and
will be used.

---

# Goal — second pass (retained)

Attack **SUPPLY** (`problem.md`) as a self-contained problem about the primes
and one explicit `F₂` fold. Gilbreath's conjecture is not the goal and must not
be claimed.

**Read `research/REOPENED.md` first.** This workspace was closed once and has
been reopened for a specific reason, and the first pass's conclusion is partly
withdrawn.

## What this pass is for

The first pass answered its hypothesis in the negative and closed. Its closing
argument was that every second-moment route collapsed at the coarsest dyadic
scale to the mod-4 switch-pair correlation, which made equivalence to switch
density look like the answer.

**That argument is refuted.** `Φ` provably sees structure up to correlation
order `K*(n) = ⌊n/2⌋` (settled, directive 41), with an explicit witness at `n=8`. The collapses were a
weakness of the eight routes chosen, not a law about the fold.

So the single question this pass exists to answer is:

> **Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≤ ⌊n/2⌋`, that is controllable by an arithmetic input strictly weaker
> than pointwise mod-4 switch density?**

Every one of the eight prior routes lived at `K = 1`. **The entire range
`1 < K ≤ ⌊n/2⌋` is unexplored.** That is this pass's territory and it should not
spend time anywhere else. (The `⌊n/2⌋` bound is settled by directive 41 — three independent routes —
see priority 3; cite it and move on.)

## Priorities

1. **Build a functional that is provably not `K=1`.** Start from the witness
   construction — it shows exactly how two strings with identical pair
   correlations separate under `S²`. The separating quantity is the arithmetic
   of the read-cone/hit-set of a position under the submask relation (a 1 at
   position `j` is read by exactly `#{d∈[2,n-1] : (n-1-j) ⊆ d}` depths), NOT
   any correlation of `h`. Name it, define it for general `h`, verify it is
   constant on `C₁` fibres but not on the whole cube, and find the lowest `K`
   at which it becomes determined (task `build-hit-set-functional`). This is
   concrete and comes first.
2. **Price each candidate against the arithmetic.** For a functional at order
   `K`, the question is what it demands of `h`. State that demand precisely and
   compare it to pointwise switch density. A functional that sees more but
   demands more is worthless; the target is one that sees more and demands
   *less*.
3. **Establish the budget — DONE (directive 41).** `K*(n) = ⌊n/2⌋`, confirmed
   by three independent routes (kstar_exact, the sat_solver oracle, the
   structural check). `kstar_structural_capture.txt` honestly refutes its own
   candidate characterisation `R(n)-1` rather than fitting it, and
   `fold_cell_degree_correction.md` caught a wrong structural fact in a library
   source (degree is `2^popcount(d)`, not `popcount(d)`). Cite `⌊n/2⌋` and move
   on; do not open more work on `K*` itself.
4. **If every order-`K` functional also collapses, prove that** — as a theorem
   this time, not as an observation across candidates. That would restore the
   equivalence conclusion on a sound footing and close the problem honestly.

## Rules

These are carried from the first pass, where each was learned the hard way.
None is advisory.

- **One canonical oracle.** `code/lib` holds the floored `k ∈ [2, n−1]` fold and
  nothing else computes `ν₂`. Every statistical script calls
  `assert_supply_guard` at entry — `ν₂(53)=18`, `ν₂(64)=27`, `ν₂(4000)=1975`,
  `μ_N(4000) ≈ 0.4977` — and asserts on the **produced array**, not on a fresh
  oracle call. A guard that validates the oracle while the data path feeds a
  control sequence catches nothing; that happened three times.
- **Captures write to a temp file and move on exit 0.** Five captures were found
  at zero bytes because a redirection truncated on open and the command failed.
  An empty capture is a failed run, not a missing one.
- **Every capture states, in its first three lines, which sequence it ran, which
  oracle function it called, and the exact range.**
- **A negative control, shown failing, in every verification.** A capture of 51
  million passes measured nothing until a deliberately broken variant produced
  438 failures beside it.
- **A measurement is not a proof.** Label it, and name the ceiling.
- **Do not reopen the six closed doors** in `problem.md`. The collapse
  refutation is not about any of them.
- **Do not re-derive settled results.** The rank fact, surjectivity, the exact
  binomial law, the telescoping identity, the endpoint-sign correction and the
  `O(n)` distance enumerator are all proved and recorded. Cite them.
- **`problem.md` is not authoritative.** Three of its seeded values were wrong
  and computation caught all three. Print the stated value beside your own
  whenever they disagree.

## Out of scope

Gilbreath's reduction, Lemma 5.4, the demand side, BHP record gaps, and the
absorption/descent machinery are proved in the parent workspace. Cite, do not
rebuild.
