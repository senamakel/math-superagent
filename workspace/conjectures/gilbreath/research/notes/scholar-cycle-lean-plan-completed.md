# Scholar cycle — the Lemma 5.4 Lean formalisation plan is COMPLETE on disk; TASKS rows 3/4 are closed

**What is genuinely new this cycle.** The research agent's new material is the
Lean formalisation work that closes the two remaining legs of Granville Lemma
5.4. I verified the on-disk kernel-check verdicts directly and against the
ledger. Result: **TASKS.md rows `formalise-link-a-...` and
`formalise-the-composition-...` are now DONE — the ledger is stale, not the code.**

## On-disk formalisation state (verified against the lean_check JSONs this cycle)

| File | lean_check | What it proves |
| --- | --- | --- |
| `code/lean/descent_lemma.lean` | compiled=true, verified=true, sorries=[] | the abstract halved `{0,1}^L` core (claims 1/2: `w≤ν₁+1⟹d_L∈{0,1}`; `ν₁+1<w⟹d_L=w−ν₁`) |
| `code/lean/lemma54_even_domain.lean` | compiled=true, verified=true, sorries=[] | even-domain theorem via the halving identity `dist_even_halves`: `lemma54_even_forward` (`v≤2ν₂+2⟹d_L∈{0,2}`), `lemma54_even_high` (`2ν₂+2<v⟹d_L=v−2ν₂`), and the full biconditional `lemma54_even_iff` |
| `code/lean/lemma54_composition.lean` | compiled=true, verified=true, sorries=[] | Link A's engine (`dist_le_max` = `\|a−b\|≤max(a,b)`, `run_le`, `orbit_le_max`) **and** the composition `lemma54_composition` (`Even v ∧ v≤g ∧ g≤2ν₂+2 ⟹ d_L∈{0,2}`), `lemma54_composition_via_max`, `lemma54_full` |
| `code/lean/link_a.lean` | **compiled=false** | STILL DOES NOT COMPILE — its `import descent_lemma` fails in this container (no olean files) |

All pass their `#print axioms` footprint within
`propext`/`Classical.choice`/`Quot.sound`, zero `sorryAx`, zero
`native_decide`/`Lean.ofReduceBool`.

## The one stale/misleading ledger row

`lemma54-link-A-lean-formalised` is recorded "asserted / does not compile" —
and the JSON confirms `link_a.lean` itself indeed does not compile. **But this
is no longer the blocker:** the self-contained `code/lean/lemma54_composition.lean`
proves the *same* Link A engine (`dist_le_max`, `run_le`, `orbit_le_max`) plus
the composition, and IS kernel-checked. So the Link-A content the run needed is
proved; the failure is specific to the `import`-based `link_a.lean` file, which
is dead code superseded by the self-contained composition file. A later role
must NOT re-attempt to fix `link_a.lean` (the container cannot build oleans, so
a cross-file `import descent_lemma` can never work); the correct file is
`lemma54_composition.lean`.

## TASKS rows closed by this

- **`formalise-link-a-v-g-n-...`** — DONE: `orbit_le_max`/`dist_le_max`/`run_le`
  in `lemma54_composition.lean` are the `v ≤ g*_n` bound (g*_n identified with
  `max v (maxAll el)`), kernel-checked.
- **`formalise-the-composition-g-n-2-2-v-g-n-success`** — DONE:
  `lemma54_composition` / `lemma54_composition_via_max` / `lemma54_full` are the
  `g*_n ≤ 2ν₂+2 ∧ v ≤ g*_n ⟹ success` transitivity, kernel-checked.

Together with the even-domain theorem (`lemma54_even_domain.lean`), the full
**nondimensional** Lemma 5.4 chain (Link A + descent + composition) is now
kernel-checked sorry-free. The known claim ledger rows
`lemma54-composition-lean-formalised` (formalised), `lemma54-descent-lean-formalised-even`
(formalised), `descent-lemma-halved-formalised` (formalised) all reflect this.

## What is still NOT in Lean (unchanged, correctly scoped out)

- The **reduction passage** `δ_k(q_n) = |δ_{k−1}(q_n) − ε_k|` (claim
  `reduction-passage-exact`, status: proved at the recurrence level, not a Lean
  theorem). It needs the actual triangular array.
- The **record-gap construction** `g*_n` from the triangle (in the Lean files g
  is a free parameter).
- The **supply side** `ν₂(q_{n−1}) ≥ c·n` — the entire remaining open mathematical
  content, a named-open two-point mod-4 correlation bound (claim
  `abgs-2011-s9-mod4-switch-limit-open`).

So `lemma54-re-derived-proof` is NOT upgraded to `proved` beyond what the kernel
gives — the reduction passage and supply side remain outside the formalisation.
That honesty claim is unchanged.

## Contradictions with recalled memory

None new. The recalled `lemma54-link-A-lean-formalised` "compile" status is
*confirmed* by the JSON (link_a.lean does not compile); the clarification added
here is that the same content lives in the kernel-checked composition file, so
the ledger's "called formalised, not backed by kernel" entry points at dead code
rather than at the live proof. No held source, claim, or memory is contradicted.
