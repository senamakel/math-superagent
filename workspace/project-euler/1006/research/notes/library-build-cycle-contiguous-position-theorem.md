# Librarian cycle — contiguous-window position theorem sourced (memory down)

**Memory server:** down again (health-check timeout, 8 s, on `remember_memory`);
durable record on disk here. `describe_file`/`refresh_index` on research/ refused
(no INDEX.md by policy), so file purposes are recorded inline in this note and in
the summary itself.

## What was added and why

The library recorded two gaps for the contiguous-window reformulation of Ψ
(directive 9): (a) the *geometric-weight* universal-Euclidean monoid is anchored
only to Chinese sources, and (b) **directive 9's claim that the k+1 distinct
length-k factors occur as contiguous windows at prescribed positions is "NOT
stated verbatim in any held source"** — the Sivasankar–Rama position theorem
(2204.13977, held) and the conjugate/standard/structure sources are the
supporting constituents, but the exact window-position statement was asserted
(steer), not cited.

This cycle closed (b):

- **Downloaded:** Sivasankar & Rama, "Fibonacci Sequences of 1D, 2D Words:
  Enumerating and Locating the Factors of the Fixed Points", **arXiv:2207.04304**
  (the same authors' 1D/2D companion to 2204.13977), full text from ar5iv
  → `research/sources/fibonacci-1d-2d-enumerate-locate-factors-ar5iv.full.md`.
- **Found:** it states the position theorem **verbatim** in two forms:
  - **Lemma 2** (the Chuan–Ho conjugate-prefix theorem, ref [10]): for
    `1 ≤ k < F(n)`, the k+1 prefixes of length k of
    `T^0(q_n), T^{-1}(q_n), …, T^{-k}(q_n)` (q_n = the "special conjugate" of the
    finite Fibonacci word f_n) are the k+1 distinct length-k factors of f_∞.
  - **Proposition 1** (the contiguous-window form): for `n ≥ 2` and
    `F(n) ≤ k < F(n+1)`, the k+1 distinct length-k factors are the prefixes of
    length k of `T^i(f_{n+1})` for
    `i ∈ {0,…,F(n)-1} ∪ {F(n+2)-k-1,…,F(n+1)-1}` — i.e. a front block of F(n)
    windows plus a tail block of k-F(n)+1 windows at the stated rotation indices.
  - **§5 occurrence formula:** `occ(u) = occ(g_n) ⊞ first-occ(u) =
    𝒵_{n-1} ⊞ first-occ(u)` (𝒵 the Zeckendorf-representation sets) — exact
    location set of each length-k factor in Fibonacci numeration.

This is exactly the missing citable statement for directive 9's claim (1). The
summary `research/summaries/fibonacci-1d-2d-enumerate-locate-factors-ar5iv.md`
(replacing the structural digest) carries the full statement, the convention
note, and the bearing.

## Caveat recorded (convention)
The paper uses the **rabbit / 1↔0-complement convention** f_∞ = abaababaabaab…
(the complement of PE1006's S = 0100101001001…). Length-k factor *sets* are
invariant under digit complement, so the theorem applies to PE1006's word; but
the paper's exact rotation/window indices are in the rabbit convention and
post-rotation coordinates, so mapping them onto directive 9's absolute prefix
positions (`r = F_n-k-1 .. F_n-1` of q_n q_n in the 0/1 convention) still needs
the small-k check against `mech_psi` — which the run already does as a solver
task. The source supplies the theorem; it does not replace the verify step.

## Not re-searched
- The geometric-weight (r^i) Euclidean monoid: confirmed in a prior cycle that
  no English/arXiv primary paper states the exact (count, Σr^i, Σr^i·floor,
  Σr^i·floor²) recursion; anchored operationally to the on-disk OI-wiki / fhq /
  LOJ138 / AtCoder sources. NOT re-hunted this cycle (recorded, non-blocking).
- Berstel 1986 Book-of-L survey, de Luca 1997 full body, Morse–Hedlund 1940,
  Chuan–Ho 2005 "Locating factors of the infinite Fibonacci word" (paywalled;
  now covered verbatim by Lemma 2 / Prop 1 of this downloaded source) — all
  confirmed unobtainable/covered; not re-attempted.

## Files
- `research/sources/fibonacci-1d-2d-enumerate-locate-factors-ar5iv.full.md`
  (source URL recorded in-file). Full text, 119261 bytes markdown.
- `research/summaries/fibonacci-1d-2d-enumerate-locate-factors-ar5iv.md`
  (summary note, replaces digest — includes exact Lemma 2 / Prop 1 statements,
  convention caveat, bearing on directive 9).
- Frontier: this download added its citation list to `derived/FRONTIER.md`.

When memory recovers, the durable finding "Fibonacci-word factor position
theorem (Lemma 2 / Prop 1 of arXiv:2207.04304) anchors directive 9's
contiguous-window claim" should be stored in Cognee.
