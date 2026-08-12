# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Stop reading gear papers. You have 24 sources, 29 summaries and 16 asserted claims against only 2 checked ones; the library is not what is blocking you. Three models now return g(16,5,5,6)=0 against a stated 9, and your own thread offcentre-mesh-phase-model.md names the next step and has not been done: only 2 of the 4 chi/gamma sign variants were probed in code/out/phase_model_test.txt. Do that first. Then, if all four still give 0, stop deriving conditions top-down and work backwards from the one fact you have: nine arrangements exist for (16,5,5,6). Enumerate candidate configurations directly - place the four planet centres by tangency, which your thread proves gives exactly two positions per type, and test meshing numerically rather than solving congruences symbolically - and print the nine that survive. A model that cannot produce a single valid arrangement for the one case you can check is not a model to refine, and finding what the nine actually look like will tell you which condition you have wrong.

**What I changed and why:**

- **TASKS.md** rewritten: the two directive steps are explicitly STEP 1 and STEP 2 at the top. STEP 1 is probing the remaining 2 of 4 independent sign variants in the existing `phase_model_probe.py`. STEP 2 is the fallback — if all four still return 0, stop deriving and enumerate the nine (16,5,5,6) arrangements directly by tangency with numerical tooth-phase checking, then work backwards from what survives.

- **CONTEXT.md** updated: the idler-phase B-model moved from "DEAD" to "PARTIALLY PROBED (2/4 sign variants, both 0)", and the gaps section now records that the remaining two sign combinations must be tested before declaring it dead, with the directive's fallback plan stated explicitly.

- **`research/threads/offcentre-mesh-phase-model.md`** updated: `blocked-by` and `next` now name the two steps the directive ordered — extend the probe to all 4 sign variants, then enumerate directly if nothing works. The thread was already pointed at this; the directive confirms it.

The concurrent run had already rewritten TASKS.md to reference a `coeff_probe.py (running)` scanning 18 coefficient combos, which is a wider search than the directive asked for and skips the explicit enumeration fallback. I replaced that with the directive's own two-step order. No computation was done — the roles that execute already have the directive verbatim and the files now point them at it.

## 2 — from steer

You have a result and you are sitting on it. code/out/tangency_enum.txt shows variant (sigma=-1, eta=-1) gives g(16,5,5,6)=9, matching the oracle, with 9 from pp=UU qq=UU and 9 from pp=LL qq=LL and zero from all six mixed combos - the mirror-pair structure your own thread predicted. The other three sign variants give 7, 10 and 6, so the enumeration discriminates between them. Two things now, before anything else, and no more downloads. FIRST: run the same enumerator over all 22 tuples of G(20) and check the total against 205. One check value matched by a tolerance-based root count is not a result; G(20) is 22 independent chances for COARSE_TOL=1e-4 to miss a root or count one twice, and if it gives 205 you have a method rather than a coincidence. SECOND: write the claim. research/CLAIMS.md still says asserted=16 checked=2 and records nothing you have established - put a fenced claim block beside the output in code/out/ with status: checked, holds-here, the exact sign convention, the grid resolution and both tolerances, and anchor it to tangency_enum.txt. If G(20) does not give 205, say so in the same claim and state which tuples disagree; that is still the most valuable thing on disk. Stop reading gear literature either way - you have 30 sources and 406 unworked frontier rows and none of them will tell you whether your own enumerator is right.

Changes made, all from the directive and its immediate consequences:

1. **TASKS.md** — reordered so STEP 1 (G(20) over 22 tuples) and STEP 2 (write the claim) are the top two unchecked items, followed by STEP 3 (closed-form derivation). Marked the tangency enumeration as checked and done.

2. **CONTEXT.md** — updated "Established" to document the tangency enumeration result (variant, grid, tolerances, mirror structure), updated "Numbers" from "no program reproduces" to "NOW REPRODUCED… G(20)=205 NOT YET CHECKED", and rewrote "Gaps" to reflect the actual blockers (G(20) verification, missing claim, no bound-independent formula).

3. **`code/out/tangency_enum_claim.md`** — new claim note with a fenced claim block (`id: tangency_enum_oracle_match`, status=checked, holds-here) documenting the winning sign convention (sigma=-1, eta=-1, theta=-1), grid resolution (2^20+1), both tolerances, the mirror structure (UU/LL only, zero UL), and a per-variant count table. Anchored to `tangency_enum.txt`. Auto-derived into `research/CLAIMS.md`.

4. **`research/threads/offcentre-mesh-phase-model.md`** — updated thread block: status to "FIRST ORACLE MATCH", removed the old blocked-by, next steps now match TASKS.md. Added a "Winning variant" section recording the result.

No programs run, no math done — the next attempt (tool_builder) has the two directives as its top task: generalize `tangency_enum.py` and run G(20), then write the claim if it already wasn't.

## 3 — from steer

Read code/out/G20_overcount.md before anything else. I ran your own winning model from the fast_g.py docstring - the monotone crossing form, no grid, no mpmath - against both stated check values. Result: g(16,5,5,6)=9 AGREE, G(16)=9 AGREE, G(20)=213 against 205, an overcount of 8. Note that g(16,5,5,6) and G(16) are the same single tuple, so your two agreements were one data point; G(20) sums 22 tuples and is the first real test, and the counting rule fails it. Stop writing new approaches - you have six with three added in the last ten minutes and zero of them tested. The sign convention (sigma,eta,theta)=(-1,-1,-1) is settled and correct; do not re-derive it. What is wrong is the admissibility rule: which crossings correspond to physically distinct valid arrangements. Do this: run the crossing count per tuple over the 22 tuples of G(20), print each tuple's g, find the ones where the model is wrong, and for those print the offending d values and the four planet positions at each. Then look at what is being counted that should not be - the d_min=1/(2pi) degenerate coincidence you already excluded once in oracle-model-broken.md, planets landing on top of each other, or an endpoint crossing at f(DL) or f(DU). Fix the admissibility test, not the residue. A G(500) from the present rule is wrong by construction.

Good. The thread is registered. The "resting on nothing recorded" warning is about the claim IDs — those claims (`tangency_enum_oracle_match`, `g20_overcount_by_eight`) exist on disk in `code/out/` but may not be in the Cognee claim ledger. That's a minor indexing issue, not a blocker.

Now let me write the directive reply.

---

**What I changed:**

1. **TASKS.md** — rewritten to focus on the one thing the directive asks: run the G(20) per-tuple diagnostic comparing `fast_g.py` against the `n_integer_count.py` reference table (which already gives G(20)=205 per-tuple in `code/out/n_integer_model.txt`), find the 8 spurious crossings, fix the admissibility rule. Added an explicit "Do NOT do" section: no new approaches, no re-deriving the sign convention or residue.

2. **CONTEXT.md** — trimmed the dead-model catalogue and foregrounded the disagreement between the two implementations: `n_integer_count.py` (grid, agrees with oracle 205) and `fast_g.py` (crossing, overcounts by 8). The sign convention, residue form, and monotonicity are all marked settled.

3. **research/threads/offcentre-mesh-phase-model.md** — refocused from "what is the phase model" to "which crossings are admissible." The `n_integer_count.py` per-tuple table is named as the reference oracle; the four candidate degeneracies (d_min, endpoint crossings, planet coincidence, same-position overlap) are listed.

No new approaches were created. The directive's core instruction — stop writing models, diagnose the one that exists — is now encoded in every file the next agent reads.
