# Pattern-finder report — round 20: the n3-patch forced-line identity, verified fresh

## What I did

Rounds 1-19 established that every on-disk parameter-determined family count is
a |63-quartic that does not separate 99 from its controls rook(3)/BvLS, and
declared the sequence line exhausted. The one on-disk artifact newer than round
19 (`n3_global_ledger.captured.txt` + `verify_global_ledger_parity.txt`) had not
been run through the exact tools. I replicated the growth loop faithfully
(`code/out/pf_lin_identity_faithful.py`, mirroring `n3_grow_radius.py` exactly:
seed → rule-(3) closure → enumerate free interior bits → iterate to stable
fixpoint) and extracted the one clean structural identity it carries.

## The identity, checked exactly

At the stable radius-6 fixpoint, every one of the **19 distinct survivors** (and
the radius-0 seed) satisfies

    L_in  ==  V_patch - 4

where L_in = number of forced patch 3-cliques (triangle-lines fully inside the
patch) and V_patch = number of materialised patch vertices:

    seed      (6, 2)
    survivors (8,4),(9,5),(10,6),(11,7),(12,8)

My faithful replication reproduced the published 19 survivors (radius 6, stable
fixpoint, 0 free bits) with **zero violations** of the identity across all 19
distinct configurations and the seed. Exact integer arithmetic, no floats.

## Why it holds — and why it is NOT exploitable

The identity is **bookkeeping, not structure**. Each rule-(3) lambda-witness
materialisation adds exactly one new vertex AND exactly the one triangle
{witness, i, j}; so V_patch and L_in both increment by 1 together, keeping
L_in = V_patch - 4 invariant. The only non-tautological content is that the
complete enumeration of the free interior bits never adds or cancels an extra
forced triangle at the fixpoint — every survivor still meets V-4. It is
consistent with, and implied by, the ledger's own conclusion that the residual
(223-227 lines, 669-681 incidences) is always arithmetically absorbable.

It does not separate 99 from its controls (it is a property of the local growth
rule of a specific seed, same for any member), it is not a parametric family
sequence (no extrapolating term to falsify), and it carries no lower bound that
over-subscribes the 231-line/693-incidence budget.

## Sequence-tool verdict

`analyze_sequence` / `find_linear_recurrence` are inapplicable here: this is a
finite set of bookkeeping identities over a fixed fixpoint, not a fitting
target. The identity is exact over every term supplied and is a **checked
consistency property**, not a conjecture with a falsifying term.

## Status of the sequence line

Unchanged from rounds 1-19: **NOTHING FURTHER** is available from the sequence
tools. The only 99-specific structural values remain the coclique bound 22 and
the forced n3≥3 (Makhnev conditional) — neither a sequence. Genuinely new
exploitable structure, if any, is in construction/search (the 99-vertex lift of
the super-simple 2-(22,4,2) design; the k=14 local triangle geometry).

## Files
- `code/out/pf_lin_identity_faithful.py` — faithful replication + identity check (this round).
- `code/out/n3_grow_radius.captured.txt` / `n3_global_ledger.captured.txt` — the source data.
- This report.
