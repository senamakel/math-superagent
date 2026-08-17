# Working in `code/lean/`

Lean 4 against a pre-built Mathlib; no Lake project and no `lakefile` — the
runtime puts Mathlib on the search path and `lean_check` invokes the compiler
directly, so a file here compiles as it stands.

```text
code/lean/
└── Lib/
    ├── Answer.lean             the result this run reports
    ├── <Subject>.lean          the identity the fast method rests on
    └── <Subject>/Generated/    untrusted computed data, if any
```

## What to state

Not the answer alone. The answer alone has a shape that compiles, needs no
axiom, and says nothing:

```lean
theorem pe622_answer : 3010983666182123972 = 3010983666182123972 := by rfl
```

The runtime refuses that by name — both sides textually identical, across `=`
or `↔`. What it cannot refuse is a statement that is merely *beside the point*,
and nothing mechanical can, so the judgement is yours: state the **identity the
fast method assumes**, and derive the answer from it.

## The three verdicts, and how they are earned

Never typed — read off the kernel by `lean_check`, and a claim that says
otherwise is downgraded on the next derivation.

- **`formalised`** — the kernel checked it here, resting on nothing but Lean's
  own three axioms (`propext`, `Classical.choice`, `Quot.sound`).
- **`conditional`** — the kernel checked it *given* results cited from the
  literature as axioms under `namespace Cited`. The implication is proved; the
  hypothesis is somebody else's paper.
- **`asserted`** — no passing verdict backs it.

End every file with `#print axioms <name>` for each theorem it states. A file
that never asks has told the runtime nothing about what its proof rests on.

## A cited result is an axiom, and says whose

```lean
namespace Cited

/-- src: Concrete Mathematics, 2nd ed., eq. (5.25) -/
axiom vandermonde_convolution : ...

end Cited
```

## Generated data may not conclude anything

Four parts, and the separation is the point — a generator that states its own
theorem has put the statement under the control of the thing being checked:

1. untrusted `def`s under a `Generated/` folder, marked as generated;
2. a **hand-written** checker outside that folder;
3. a `check = true ↔ Spec` soundness theorem joining them;
4. `by decide` — never `native_decide`, whose axiom is refused here.

A `theorem` inside `Generated/` is refused by the runtime, not by convention.

## Keep the index current

`Lib/INDEX.md` says what each file states and where it stands. `derived/LEMMAS.md`
is derived from the files themselves, so it will disagree with a stale index and
the index is what is wrong.
