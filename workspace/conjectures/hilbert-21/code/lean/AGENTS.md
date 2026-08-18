# Working in `code/lean/`

This is where the mathematics lives. Lean 4 against a pre-built Mathlib; no
Lake project and no `lakefile` — the runtime puts Mathlib on the search path and
`lean_check` invokes the compiler directly, so a file here compiles as it
stands.

```text
code/lean/
└── Lib/
    ├── Statement.lean          the conjecture itself
    ├── <Subject>.lean          one file per subject
    └── <Subject>/Generated/    untrusted certificate data, if any
```

## Start with the statement

`Lib/Statement.lean` states the conjecture, ending in `:= by sorry`. You are not
being asked for a proof. You are being asked for a *type* that carries every
hypothesis — and where the statement cannot be written yet, that is a finding
about the problem and belongs in `CONTEXT.md`, not a reason to skip this file.

A summary loses hypotheses. A type cannot.

## The three verdicts, and how they are earned

Never typed — read off the kernel by `lean_check`, and a claim that says
otherwise is downgraded on the next derivation.

- **`formalised`** — the kernel checked it here, resting on nothing but Lean's
  own three axioms (`propext`, `Classical.choice`, `Quot.sound`).
- **`conditional`** — the kernel checked it *given* results cited from the
  literature. This is the ordinary status for real work and is not a lesser
  one: the implication is proved, and the hypothesis is somebody else's paper.
- **`asserted`** — no passing verdict backs it. A file with a `sorry`, or a
  claim naming a file nobody checked, lands here.

End every file with `#print axioms <name>` for each theorem it states. A file
that never asks has told the runtime nothing about what its proof rests on, and
`lean_check` will not grant it the top verdict.

## A cited result is an axiom, and says whose

```lean
namespace Cited

/-- src: Gasull & Santana, Proc. AMS 2024, doi 10.1090/proc/17116, Thm 1.2 -/
axiom hilbert_number_realised (n : ℕ) : ...

end Cited
```

The docstring naming the source is not decoration — it is what lets a reader
check the step, and what stops the run treating somebody else's theorem as its
own. A `Cited` axiom earns `conditional` for everything downstream of it, which
is correct: the kernel checked your reasoning, not their paper.

## Generated data may not conclude anything

A certificate is four parts, and the separation is the point — a generator that
states its own theorem has put the statement under the control of the thing
being checked:

1. untrusted `def`s under a `Generated/` folder, marked as generated;
2. a **hand-written** checker outside that folder;
3. a `check = true ↔ Spec` soundness theorem joining them;
4. `by decide` — never `native_decide`, whose axiom is refused here.

A `theorem` inside `Generated/` is refused by the runtime, not by convention.

## What `sorry` means here

It is a placeholder for work, and it is honest. A file full of stated lemmas
with `sorry` bodies is a *blueprint the kernel type-checked* — every hypothesis
in the right place, every statement composable — and it is worth far more than
prose. The verification arm ranks these and hands the top of the ranking back to
be proved, so a `sorry` you write today is work scheduled rather than work lost.

What is not honest is a claim that calls such a file `formalised`. The runtime
catches that on the next derivation and says so by name.

## Keep the index current

`Lib/INDEX.md` says what each file states and where it stands. Refresh it when
you add, rename or delete a file — `derived/LEMMAS.md` is derived from the files
themselves, so it will disagree with a stale index and the index is what is
wrong.
