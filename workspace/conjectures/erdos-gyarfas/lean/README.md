# Lean formalisation of the Erdős–Gyárfás conjecture

This directory carries the run's Lean 4 / Mathlib formalisation of the
Erdős–Gyárfás conjecture:
**every finite simple graph with minimum degree ≥ 3 has a cycle whose length is
a power of two** (`2^k` for `k ≥ 2`, i.e. 4, 8, 16, …).

## Environment and how to build

- **Lean**: 4.34.0-rc1 (`lean --version`).
- **Mathlib**: prebuilt at `/opt/mathlib4` (root `/opt/mathlib4/Mathlib`).
  There is no writable `lake` project; files are checked with `lean` directly,
  which is why the build below sets `LEAN_PATH` by hand.
- The container root filesystem is read-only, so `lean` does not auto-emit
  `.olean` files next to sources; the build writes them explicitly with `-o`.
  Because `lean` refuses to read sources outside its root, put the source plus
  the freshly built `.olean` on the same `LEAN_PATH`, and **always compile
  `c4_lemma.lean` first** so `erdos_gyarfas.lean` (which imports it) finds its
  `.olean`.

The command sequence that works in this container:

```sh
# one-time: assemble the mathlib + mathlib-package LEAN_PATH (already does
# everything except /workspace/lean)
LEAN_PATH="/opt/mathlib4/.lake/build/lib/lean"
for p in /opt/mathlib4/.lake/packages/*; do
  [ -d "$p/.lake/build/lib/lean" ] && LEAN_PATH="$LEAN_PATH:$p/.lake/build/lib/lean"
done
export LEAN_PATH="$LEAN_PATH:/workspace/lean"   # adds this dir for imports

cd /workspace/lean
lean c4_lemma.lean -o c4_lemma.olean            # must come first: builds the import
lean erdos_gyarfas.lean -o erdos_gyarfas.olean
lean axioms_check.lean -o axioms_check.olean    # prints #print axioms for both theorems
```

An empty (or warning-only) output means the file elaborated successfully.

## Files

| File | What it establishes |
| --- | --- |
| `c4_lemma.lean` | Defines `ErdosGyarfas.IsEGConclusion G` (the conjecture's conclusion: a simple cycle of length `2^k`) and proves **`c4_implies_conclusion`**: a 4-cycle already implies the conclusion. This lemma is **kernel-checked — no `sorryAx`** — its only axiom is `propext`. |
| `erdos_gyarfas.lean` | States the conjecture itself as `ErdosGyarfas.erdos_gyarfas`: for a finite type `V` with `DecidableEq`, any `SimpleGraph G` with `3 ≤ G.minDegree` satisfies `IsEGConclusion G`. The body is `by sorry` — there is no proof to formalise yet. |
| `cut_vertex.lean` | **Kernel-checked, no `sorry`.** Formalises the geometric heart of the run's cut-vertex structure lemma: for a simple cycle `p : G.Walk v v` through `v`, its two `v`-neighbours `p.snd` and `p.penultimate` are connected by a walk inside `G - v` (modelled as `G.induce {x | x ≠ v}`), so all non-`v` vertices of the cycle lie in a single connected component of `G - v`. Axioms: `propext, Classical.choice, Quot.sound` — no `sorryAx`. See `cut_vertex_axioms.lean`. |
| `axioms_check.lean` | Reports `#print axioms` for the c4 and conjecture theorems. |

## What the statement means, and its conventions

- `G : SimpleGraph V` is Mathlib's **simple graph**: an irreflexive, symmetric
  adjacency relation `G.Adj : V → V → Prop`. No loops, no multiple edges —
  exactly the conjecture's setting.
- `3 ≤ G.minDegree` is the minimum-degree hypothesis. Mathlib's `minDegree` is
  defined over a `Fintype`; on an empty vertex type it returns `0`, so the
  hypothesis is simply false there and the implication is vacuously true — it
  asserts nothing wrong about empty graphs.
- `Walk.length` counts **edges**. `IsCycle` requires a nonempty trail whose only
  repeated vertex is the start (a simple cycle). So a cycle of length `4` is a
  genuine 4-cycle and `4 = 2^2` gives `k = 2`.
- The conclusion is `∃ k : ℕ, ∃ u, ∃ p : G.Walk u u, p.IsCycle ∧ p.length = 2^k`.
  This allows any power of two including `k = 0, 1` (`1, 2`); since the
  hypothesis forces a triangle or longer, the effective lengths are `≥ 4`, but
  the formal statement does not artificially restrict `k ≥ 2` — the conjecture
  is about the *existence* of a power-of-two-length cycle, which this captures.

## Axioms

From `axioms_check.lean`:

```
'ErdosGyarfas.c4_implies_conclusion' depends on axioms: [propext]
'ErdosGyarfas.erdos_gyarfas' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

- `c4_implies_conclusion` is a **real proof**: its only axiom is the harmless
  `propext`. There is no `sorryAx`.
- `erdos_gyarfas` depends on `sorryAx` **by design** — the conjecture is open and
  its body is `by sorry`. Beyond `sorryAx` it uses only the standard
  `Classical.choice` and `Quot.sound`, so no hidden unproved axioms were
  introduced.

## Remaining `sorry`s

Exactly one: the body of `ErdosGyarfas.erdos_gyarfas`. It stands in for the
open conjecture, and is flagged by Lean's warning
`declaration uses 'sorry'` at line 45. Every other declaration is `sorry`-free.
