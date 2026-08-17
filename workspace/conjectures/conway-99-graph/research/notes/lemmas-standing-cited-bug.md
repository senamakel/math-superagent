# LEMMAS.md standing bug: `Cited` axioms mislabelled `verified`, `cited axioms: none`

**Status of this note:** a report of a *harness bug* (the standing computation),
not a workspace-structure problem. It documents the exact declarations and the
header text they contradict, so it can be reported upstream. Not a claim.

**CORRECTION (directive 25):** the earlier version of this note described the
symptom (a mis-read of an "empty" axioms field). The real cause is a
**line-wrapping capture bug** in the runtime's capture loop. It is recorded
here with the truncated axioms strings verbatim, because those strings are the
proof. A report naming the wrong cause would be rejected.

## The real mechanism: Lean wraps, the capture loop drops continuation lines

- **Lean WRAPS long `#print axioms` output across lines.** The two load-bearing
  theorems' axiom lists are long (they include `Cited.makhnev_thm1`,
  `Cited.makhnev_lemmas_6_9`, `Cited.srg_multiplicity_integrality` plus
  `Classical.choice`, `Quot.sound`, `propext`), so Lean's printer breaks them
  across several physical lines.
- **The runtime's capture loop pushes only lines that themselves contain
  `depends on axioms:`.** Continuation lines — the ones carrying the actual
  `Cited.*` entries — do not contain that substring and are dropped.
- **The `Cited.*` entries sit on exactly those dropped continuation lines.**
  That is why the standing computation never sees them.

## The artifact proves it (verbatim evidence)

`code/out/lean/code_lean_makhnev1988_condstar_theorems.lean.json` holds this in
its `axioms` array — each entry truncated mid-list, **no closing bracket**:

```
"'Makhnev1988.srg33_12_1_6_infeasible_by_integrality' depends on axioms: [propext,"
"'Makhnev1988.no_srg_99_14_1_2_condstar' depends on axioms: [propext,"
```

and `"cited": []`.

The parser splits each captured line on `:` and sees only `[propext,` — the
leading token of a list whose continuation lines (holding `Cited.*`,
`Classical.choice`, `Quot.sound`) were dropped by the capture loop. So `cited`
comes back `[]` and the standing computation labels the file `verified` instead
of `conditional`. The truncated strings **are** the evidence; quote them
verbatim in any upstream report.

- Why it never surfaced: **every test fixture uses a single-line axiom string.**
  No fixture's axiom list was long enough to wrap, so the capture loop's
  line filter was never exercised against a wrapped output.

## What this means for the (99,14,1,2) run

The single most load-bearing result this run holds — **the n₃ ≥ 1 constraint**
(`n₃ = 0` ⟹ no srg(99,14,1,2), via Makhnev 1988 Thm 2) — descends from exactly
these two axioms (`Cited.makhnev_thm1`, `Cited.makhnev_lemmas_6_9`). Labelling
them `verified` would say the kernel proved Makhnev's lemmas, which it did not
and cannot. They must be `conditional`.

## The file structure (this part was always correct)

`Cited` is at the **top level** of the file, not nested inside another
namespace, so the standing computation has every chance to see the `Cited.*`
prefix:

```
82:namespace Cited
86:axiom makhnev_thm1 {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
       {n k mu : ℕ} (h : G.IsSRGWith n k 1 mu) (hs : Makhnev1988.CondStar G) :
       mu ≤ 3 ∨ (n = 27 ∧ k = 10 ∧ mu = 5)
95:axiom makhnev_lemmas_6_9 {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
       (hG : G.IsSRGWith 99 14 1 2) (hstar : Makhnev1988.CondStar G) :
       ∃ (W : Type) (_ : Fintype W) (Λ : SimpleGraph W) (_ : DecidableRel Λ.Adj),
         Λ.IsSRGWith 33 12 1 6 ∧ Makhnev1988.CondStar Λ
104:axiom srg_multiplicity_integrality {V : Type} [Fintype V] (G : SimpleGraph V)
       [DecidableRel G.Adj] (h : G.IsSRGWith 33 12 1 6) :
       (7 : ℤ) ∣ (2 * (12 : ℤ) + ((33 : ℤ) - 1) * ((1 : ℤ) - 6))
```

`#print axioms` — read at the terminal, where the full unwrapped output is
visible — confirms the dependence for the two load-bearing theorems:

```
'Makhnev1988.no_srg_99_14_1_2_condstar' depends on axioms: [propext, Cited.makhnev_lemmas_6_9, Cited.makhnev_thm1, Classical.choice, Quot.sound]
'Makhnev1988.srg33_12_1_6_infeasible_by_integrality' depends on axioms: [propext, Cited.srg_multiplicity_integrality, Classical.choice, Quot.sound]
```

(These are the *unwrapped* lines; inside the captured JSON the same two lines
are truncated at `[propext,` — exactly the loss the capture bug causes.)

## The contradiction with the deducer's own header

The deducer's header (`derived/LEMMAS.md` line 7) defines the statuses:

> The standing is a fact about the *file*, not about the one declaration: Lean
> fails a file, not a theorem. `verified` is the kernel resting on its own
> three axioms; `conditional` is the kernel resting additionally on results
> cited from the literature under `namespace Cited`, so the implication is
> proved and the hypothesis is somebody's paper; ...

Yet the rows list the three `Cited.*` axioms (and therefore the whole file) as
`verified`, because the capture loop dropped the continuation lines that would
have populated `cited`:

```
| `Cited.makhnev_lemmas_6_9`        | axiom   | verified | ... |
| `Cited.makhnev_thm1`              | axiom   | verified | ... |
| `Cited.srg_multiplicity_integrality` | axiom | verified | ... |
| `Makhnev1988.no_srg_99_14_1_2_condstar` | theorem | verified | ... |
| `Makhnev1988.srg33_12_1_6_infeasible_by_integrality` | theorem | verified | ... |
```

Under the header's own definitions this is wrong on both counts:

1. **A `Cited` axiom cannot be `verified`.** A Cited axiom is somebody's paper
   taken on faith; the kernel checks nothing about it. It should be at best
   `conditional` (resting on the literature) — and for the axioms themselves
   there is no sense in which they are verified at all.
2. **The standing is a fact about the file.** A file containing `Cited`
   axioms should not be `verified` for every declaration in it; the file's
   standing is `conditional`.

The `lean_check` verdict `cited axioms: none` is a second symptom of the **same**
capture bug: it reads `[]` from the truncated/line-filtered artifacts despite
the unwrapped `#print axioms` listing the `Cited.*` entries. Because
`compiled: true` / `outcome: verified` then decides the status, the presence of
cited axioms is invisible to the computation.

## Fix, phrased for whoever owns the harness

The capture loop must gather wrapped axiom output as one logical list — either
read the full `#print axioms` output and join continued lines before filtering,
or change the filter criterion from "the line contains `depends on axioms:`" to
"the line is inside an open `[...]` axiom-list bracket started by one that does".
The test suite needs at least one fixture whose `#print axioms` output wraps
across lines, so this path is exercised. After the fix, the declaration rows
under `namespace Cited` must read **conditional** (never verified), and
`cited` must list the three `Cited.*` names.

**Cannot be filed upstream from inside this container** — a report would be
spend with no artifact. This note is the deliverable; the operator carries it
out.

## The correct status, stated honestly

- **Fully `formalised`** (kernel on its own three axioms, no `Cited`): the
  arithmetic kernel — `condstar_discriminant` (δ = 49 = 7²),
  `condstar_mult_num` (numerator = −136), `not_seven_dvd_neg_136`,
  `not_seven_dvd_pos_136`, `not_seven_dvd_mult_num`, `srg33_param_contradicts_thm1`,
  `controls_in_mu_le_three`. These depend only on propext / Classical.choice /
  Quot.sound.
- **`conditional`** (rests on `Cited.*`): `srg33_12_1_6_infeasible_by_integrality`
  (on `Cited.srg_multiplicity_integrality`), and
  `no_srg_99_14_1_2_condstar` (on `Cited.makhnev_thm1`,
  `Cited.makhnev_lemmas_6_9`).
- The three `Cited.*` axioms themselves are **sourced declarations**, not
  proved; each should carry a claim naming the paper (Makhnev 1988, Mat.
  Zametki 44(5)).

## Reported facts for upstream

- Exact declarations: `Cited.makhnev_thm1`, `Cited.makhnev_lemmas_6_9`,
  `Cited.srg_multiplicity_integrality` (signatures above).
- Header text contradicted: `derived/LEMMAS.md` line 7 (quoted above).
- Symptom: `lean_check` reports `cited axioms: none` for a file whose
  unwrapped `#print axioms` lists `Cited.*`; the derivation then labels the
  whole file `verified`.
- **Root cause (directive 25): line-wrapping capture bug.** Lean wraps the
  `#print axioms` list; the capture loop keeps only lines containing
  `depends on axioms:` and drops the continuation lines that carry the
  `Cited.*` entries. Verbatim truncated artifact strings:
  `'...srg33_12_1_6_infeasible_by_integrality' depends on axioms: [propext,`
  and `'...no_srg_99_14_1_2_condstar' depends on axioms: [propext,`
  (both from `code/out/lean/code_lean_makhnev1988_condstar_theorems.lean.json`,
  `"cited": []`). It never surfaced because every fixture uses a single-line
  axiom string.

---

```claim
id: makhnev1988-condstar-arithmetic-kernel
statement: The arithmetic kernel of Makhnev 1988's condition (*) at the forced
  subobject srg(33,12,1,6): the eigenvalue-multiplicity numerator
  2k + (v-1)(lam-mu) = 2*12 + 32*(-5) = -136 is not divisible by sqrt(delta)=7,
  where delta = (lam-mu)^2 + 4(k-mu) = (1-6)^2 + 4(12-6) = 49 = 7^2; hence
  srg(33,12,1,6) is infeasible by multiplicity integrality.
hypotheses: none beyond the standard natural-number/integer arithmetic the
  kernel checks directly; the multiplicity-formula step is not needed for the
  divisibility facts themselves (they are pure integer arithmetic).
holds-here: yes — every divisibility/rational fact is fully kernel-checked in
  code/lean/makhnev1988_condstar_theorems.lean (condstar_discriminant,
  condstar_mult_num, not_seven_dvd_neg_136, not_seven_dvd_pos_136,
  not_seven_dvd_mult_num), depending only on propext/choice/quot, no Cited axioms.
status: formalised
formalisation: code/lean/makhnev1988_condstar_theorems.lean
bearing: the exact divisibility step that makes Makhnev's forced srg(33,12,1,6)
  infeasible, upgraded from checked-integer to kernel-proof.
anchor: research/summaries/makhnev-1988-lambda1-russian-fulltext.md
```

```claim
id: srg33-12-1-6-infeasible-by-integrality-lean
statement: No strongly regular graph with parameters srg(33,12,1,6) exists:
  its multiplicity numerator -136 is not divisible by sqrt(delta)=7.
hypotheses: the eigenvalue-multiplicity integrality of SRGs (Bose-Mesner
  algebra), taken as Cited.srg_multiplicity_integrality; the divisibility
  arithmetic is kernel-checked.
holds-here: yes — the theorem srg33_12_1_6_infeasible_by_integrality compiles;
  it rests on Cited.srg_multiplicity_integrality plus kernel arithmetic. This
  is a literature result, so the claim is conditional.
status: conditional
formalisation: code/lean/makhnev1988_condstar_theorems.lean
bearing: Makhnev Thm 2's forced subobject cannot exist at all, by multiplicity
  integrality alone (the run's shorter proof).
anchor: research/notes/makhnev-99-shorter-proof.md
```

```claim
id: makhnev1988-condstar-theorems-lean
statement: The Lean rendering of Makhnev 1988 node
  makhnev1988-condstar-theorems: the (99,14,1,2) case of Theorem 2 — there is
  no srg(99,14,1,2) satisfying condition (*) [n3=0]. A putative such graph
  forces srg(33,12,1,6) satisfying (*) (Lemmas 6-9), which Theorem 1 rejects
  because mu=6>3 and it is not the (27,10,1,5) exception.
hypotheses: Gamma is an srg(99,14,1,2) with lambda=1; condition (*) holds;
  Makhnev Thm 1 and Lemmas 6-9 and the SRG multiplicity-integrality condition
  are taken as Cited axioms (they are the source's word, not proven here); the
  parameter contradiction (6 !<= 3, 33 != 27) is kernel-checked.
holds-here: yes — no_srg_99_14_1_2_condstar compiles; it rests on
  Cited.makhnev_thm1 + Cited.makhnev_lemmas_6_9 plus kernel arithmetic. This
  is a literature result, so the claim is conditional.
status: conditional
formalisation: code/lean/makhnev1988_condstar_theorems.lean
bearing: the n3>=1 lever at (99,14,1,2) descends from exactly these two axioms;
  this file makes the dependence explicit and kernel-checks the local steps.
anchor: research/summaries/makhnev-1988-lambda1-russian-fulltext.md
```
