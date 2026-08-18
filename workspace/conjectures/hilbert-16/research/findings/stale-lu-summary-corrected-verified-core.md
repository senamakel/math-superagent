# Stale Lu H14_3 digest corrected — algebraic core is verified, not by-hand

## What I found

`research/summaries/lu-h14-3-hemicycle.md` still carried, in both the prose
(lines 42-47) and the claim block (`drr-lu-claims-h14-3`), the superseded claim
that the finite algebraic core of Lu arXiv:2607.13785 had been "TRANSCRIBED ...
with expected identities; that transcription is UNVERIFIED — it was claimed
by-hand with no executed program and no capture".

That statement was written under directive 3 (FIRST) *before* the verification
ran, and the note was never updated after the run. It directly contradicted the
state the workspace already held elsewhere:

- `code/bautin/verify_lu_core.py` (clean-room, exact sympy, not importing Lu's
  scripts) executed and passed; capture `code/out/lu_core.captured.txt` prints
  each identity PASS ending "ALL CLEAN-ROOM CHECKS PASS" —
  bridge identities, Darboux cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F,
  inverse-integrating-factor cofactor div X=(x+dy)+(2Bx+dy), degree-4
  obstruction 8L4=AC+CD+2DF−EF, degree-6 30-monomial equality 192·L6+P30=0.
- `code/lyap_audit.py` (byte-level reconstruction of the paper's own
  verify_bautin_recurrence.py) independently PASS.
- `code/out/mono_counts.captured.txt`: L4, L6 residuals zero exactly.
- Kernel-closed in Lean: `lu-finite-core-identity-half-checked` (formalised:
  w6_neg, p30_plus_w6, bautin_L4_identity, L4num_ne_zero, darboux_L_identity,
  darboux_F_identity, div_cofactor_identity; axioms exactly
  [propext, Classical.choice, Quot.sound]) and L8∉⟨L4,L6⟩ kernel-checked in
  Bautin.lean via evaluation witness certPt.

## What I changed

Rewrote both the prose and the claim block to state that the finite algebraic
core is VERIFIED-computationally and kernel-checked, while keeping the honest
boundary unchanged: **Theorem 1 itself is NOT established** — the human-proof
remainder (analytic root uniqueness, Hadamard divisibility, domain completeness,
zero theorems) is machine-unchecked, the preprint unrefereed, the cyclicity
bound existential.

## Status of the claim `drr-lu-claims-h14-3`

- holds-here: unchecked (the DEEP theorem is asserted-by-source on an unrefereed
  preprint)
- evidence: asserted
- The algebraic core it rests on is `checked`/`formalised`, which is a separate
  claim (`lu-finite-core-identity-half-checked`, `g-lean-cert-kernel-checked`).

## Why this matters

A reader encountering the stale note would have concluded the algebraic core is
unverified and re-derived it, or (worse) treated the whole Lu claim as weaker
than it is. The corrected status — *algebraic core machine-closed, theorem
asserted* — is the accurate picture and matches the thesis ledger
(`bautin-ideal-kernel-checked-then-drr`).

## Caveat (unchanged, from tasks/CONTEXT)

The `code/out/lean/*.json` verdict files are STALE (compiled:false, reference
pre-fix declarations) and must be re-captured against the restored Lean files
before any "verified" verdict on this disk is trusted as fresh. The Lean source
files and the `lean_check` PASS in tasks are the current evidence; the JSON
captures lag them.
