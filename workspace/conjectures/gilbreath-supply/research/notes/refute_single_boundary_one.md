# Refutation attempt: single-sparse-1 at the window's final index

Attacked the committed rung `R-switch-equivalence` and the literal windowed form
of `G-sup-implies-switch` (research/weakened/supply.md, research/backward/
supply-switch-equivalence.md).

## Statement attacked (as written)

> **R-switch-equivalence**: "For every binary string h, if ν₂(n) ≥ c·n for all
> sufficiently large n then h has positive mod-4 switch density. Equivalently:
> every h with switch density 0 has ν₂(n) = o(n)."
>
> **G-sup-implies-switch (literal windowed form)**: "if a window h[a..b] has
> w ones with w = o(b−a), then its diagonal contribution #{d : T(b,d)=1} is
> o(b−a)."

## The witness, by hand

Take the *per-window* family `h^{(n)} = e_{n−1}`: a single 1 at index `n−1`,
zeros elsewhere in the window. The fold diagonal cell is

    T(n,d) = ⊕_{o ⊆ d} h[n−1−d+o],

and for **every** d ∈ [2, n−1], the offset `o = d` is a bitwise submask of `d`
and lands on the last index `n−1`, where h = 1. Hence T(n,d) = 1 for all
n−2 depths, so

    ν₂(n) = wt(Φ_n h^{(n)}) = n−2 = Θ(n).

The switch density (frequency of 1s in the window) is 1/(n−1) → 0. So:
switch density 0 yet ν₂(n) = Θ(n), and the window [0, n−1] has w = 1 = o(n)
ones yet its diagonal contribution is n−2 = Θ(n), not o(n).

Hand check for n = 6 (h = e_5):

    d=2 (10): submasks {0,2}, window h[3..5]:  h3⊕h5 = 0⊕1 = 1
    d=3 (11): submasks {0,1,2,3}, window h[2..5]: h2⊕h3⊕h4⊕h5 = 1
    d=4 (100): submasks {0,4}, window h[1..5]: h1⊕h5 = 1
    d=5 (101): submasks {0,1,4,5}, window h[0..5]: h0⊕h1⊕h4⊕h5 = 1
    wt = 4 = n−2.  ✓

Mechanically: encoded as `code/refute/sparse_last_one.p` (XOR-gate CNF for
n = 6, forcing h = e_5 and the four T values). `find_counterexample` returned
**undecided**: no falsifying model, i.e. no assignment makes the conjecture
"all four T-cells are 1" false — consistent with the hand proof (a ground
propositional system with the witness forced in; the proof is the hand check,
the engine just confirms no counter-model exists).

## What this refutes, precisely

The obstruction is structural: the diagonal for depth n always reads the
window's **final index** (offset `o = d`, the largest submask) for every depth d
in [2, n−1]. A single 1 at that shared boundary index therefore feeds every
depth and amplifies to linear weight. So:

- The **absolute-zeta form** — false (known, run-flagged "single sparse 1
  amplifies").
- The **literal windowed form** of G-sup-implies-switch as stated — also false:
  the window has w = 1 = o(b−a) ones yet a linear diagonal contribution. The
  run hoped windowing would dodge the amplification (w = o(length) was meant to
  kill it); it does not when the 1 sits at the read boundary every depth shares.
- The **unqualified rung R-switch-equivalence** ("switch density 0 ⇒ ν₂ = o(n)")
  — false on this family for every n.

## What this does NOT refute — be scrupulous

This is a **per-window family**, not a single fixed infinite string. A *fixed*
single 1 at position j lands at offset `o = d + j − n + 1`, which for growing n
is not a submask of d for most d, so a fixed single 1 does **not** give linear
ν₂ across all large n. Therefore:

- The meaningful fixed-string statement that SUPPLY is equivalent to positive
  switch density (GOAL priority 3), and the positive witness wanted by
  `G-weak-input-strictness` (some *fixed* h* with switch density 0 yet
  ν₂ ≥ c·n) are **NOT** settled by this and remain open.

## Consequence for the run

The run pinned G-sup-implies-switch's window form to escape "single sparse 1
amplifies"; my computation shows the window boundary placement is the residual
hole. Before that lemma is used (or R-switch-equivalence stated unqualified),
either exclude boundary spikes at the window's final index, or state the lemma
for fixed h. The two-line witness is a cheaper find than either.

```claim
id: single-boundary-one-refutes-switch-equivalence-as-stated
statement: The per-window family h^{(n)} = e_{n-1} (single 1 at the final index, zeros elsewhere) has switch density 1/(n-1) -> 0 yet ν₂(n) = wt(Φ_n h^{(n)}) = n-2 = Θ(n). This refutes the unqualified statements "every h with switch density 0 has ν₂(n) = o(n)" (R-switch-equivalence) and the literal windowed form of G-sup-implies-switch (a window with w = o(length) ones can have a linear diagonal contribution), because the depth-d diagonal reads the window's final index n-1 (offset o = d, always a submask of d) for every d in [2,n-1].
hypotheses: floor convention at index 2, d-range [2,n-1]; fold diagonal T(n,d) = ⊕_{o ⊆ d} h[n-1-d+o] as in problem.md facts 1-2; h inspected per window (not fixed across n).
holds-here: yes — it is exactly the run-flagged "single sparse 1 amplifies" obstruction, shown to survive the literal windowing because the 1 sits at the read boundary every depth shares.
status: checked by hand for n=6 (wt=4=6-2, all four depths T=1) and consistent with engine (no counter-model to the forced witness); per-window family, not fixed-string.
bearing: G-sup-implies-switch and R-switch-equivalence as literally stated are false; they must be restricted to fixed h or the boundary spike excluded before the equivalence (GOAL priority 3) or the switch-side gap is used. The fixed-string equivalence and G-weak-input-strictness are untouched and stay open.
anchor: code/refute/sparse_last_one.p; this note.
```
