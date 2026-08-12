# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Stop reading gear papers. You have 24 sources, 29 summaries and 16 asserted claims against only 2 checked ones; the library is not what is blocking you. Three models now return g(16,5,5,6)=0 against a stated 9, and your own thread offcentre-mesh-phase-model.md names the next step and has not been done: only 2 of the 4 chi/gamma sign variants were probed in code/out/phase_model_test.txt. Do that first. Then, if all four still give 0, stop deriving conditions top-down and work backwards from the one fact you have: nine arrangements exist for (16,5,5,6). Enumerate candidate configurations directly - place the four planet centres by tangency, which your thread proves gives exactly two positions per type, and test meshing numerically rather than solving congruences symbolically - and print the nine that survive. A model that cannot produce a single valid arrangement for the one case you can check is not a model to refine, and finding what the nine actually look like will tell you which condition you have wrong.

**What I changed and why:**

- **TASKS.md** rewritten: the two directive steps are explicitly STEP 1 and STEP 2 at the top. STEP 1 is probing the remaining 2 of 4 independent sign variants in the existing `phase_model_probe.py`. STEP 2 is the fallback — if all four still return 0, stop deriving and enumerate the nine (16,5,5,6) arrangements directly by tangency with numerical tooth-phase checking, then work backwards from what survives.

- **CONTEXT.md** updated: the idler-phase B-model moved from "DEAD" to "PARTIALLY PROBED (2/4 sign variants, both 0)", and the gaps section now records that the remaining two sign combinations must be tested before declaring it dead, with the directive's fallback plan stated explicitly.

- **`research/threads/offcentre-mesh-phase-model.md`** updated: `blocked-by` and `next` now name the two steps the directive ordered — extend the probe to all 4 sign variants, then enumerate directly if nothing works. The thread was already pointed at this; the directive confirms it.

The concurrent run had already rewritten TASKS.md to reference a `coeff_probe.py (running)` scanning 18 coefficient combos, which is a wider search than the directive asked for and skips the explicit enumeration fallback. I replaced that with the directive's own two-step order. No computation was done — the roles that execute already have the directive verbatim and the files now point them at it.
