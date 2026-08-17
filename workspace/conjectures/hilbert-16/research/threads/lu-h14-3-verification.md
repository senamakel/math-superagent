# Lu H14_3 finite-core verification — live thread

```thread
question: Does the finite computational core of Lu arXiv:2607.13785 (local uniform
          finite cyclicity of the H14_3 semihyperbolic hemicycle) stand up to
          independent exact re-derivation and a kernel check, or does it fail?
status: open
rests-on: RR 2015 leave H14_3 as the one triple-point-at-infinity graphic with no
          partial result (research/threads/drr-status.md); Lu's paper is an
          unrefereed 2026 preprint claiming to close it, shipping a
          h14_3_reproducibility bundle (Bautin-recurrence and center-basis scripts).
blocked-by: none for the computational core — Lu's own reproducibility scripts and
          definitions in research/summaries/lu-h14-3-hemicycle.md are the input.
next: (directive 5) The algebraic core is VERIFIED and kernel-closed —
      code/bautin/verify_lu_core.py passed clean-room (capture
      code/out/lu_core.captured.txt), and the host-fixed
      code/lean/Lib/BautinRecurrence.lean is VERIFIED (h14_p30_check,
      p30_sound, bautin_L6_identity, L4num_ne_zero, param_identities,
      darboux_L_identity, darboux_F_identity; no sorry, no cited axiom —
      P30 data inline in a Generated namespace, coefficientwise decide over
      Fin 30, L4num not /8) and Bautin.lean is CONDITIONAL on the Cited
      Bautin-1952 axioms; both pass lean_check. Do not revert either file.
      NEXT Lean task: cofactor-certificate-L8-not-in-L4-L6 — membership
      (code/out/membership.captured.txt, verify_membership.py, exact over Q)
      shows L8∉⟨L4,L6⟩ (16-monomial remainder) and L6∉⟨L4⟩, so three
      generators are genuinely needed; L10∈⟨L4,L6,L8⟩ and L12∈⟨L4,L6,L8⟩
      hold exactly (remainder 0, G.contains, cofactor identity —
      Bautin-trick step SURVIVES). NOTE: an earlier version of this thread
      reported L10,L12∉⟨L4,L6,L8⟩ — that came from reading sympy 1.11
      reduce()'s quotient list instead of its remainder and is VOID; the
      corrected triple-checked run is the capture above. Exhibit cofactor
      certificates the kernel can close. Also
      re-capture lean_check: code/out/lean/*.json is stale (still reports
      compiled:false and pre-fix declarations). What stays existential, and
      asserted-by-source rather than established: Lu's Theorem 1 (finite
      cyclicity of H14_3, unrefereed, bound B existential; the two bundle
      scripts verify_h14_center_bautin.py and
      verify_h14_center_global_domains.py still not held).
```

## Why this is the most valuable target in the workspace

The steer directive says so explicitly: rather than *summarise* Lu's 80-page
preprint, this run verifies or refutes its finite computational core — the
Bautin-recurrence and center-basis scripts — with exact arithmetic, states that
core as a kernel-checkable Lean theorem, and reports exactly which step was
reproduced, which could not be, and what the paper leaves existential.

This is the ideal shape for a Lean target: a finite algebraic core (Bautin ideal
membership, a center-basis sign condition) that Lean can actually *finish*
rather than merely state. It is also the right response to an unrefereed claim —
preprints that promise a "reproducibility bundle" are exactly what a first pass
can and should stress-test before any downstream work leans on them.

## What the paper claims (asserted-by-source, not established)

- H14_3, the one graphic RR 2015 left with no partial result (through a triple
  nilpotent point at infinity, hemicycle, two semi-hyperbolic points on the
  equator), has **local uniform finite cyclicity** in one fixed annular collar,
  uniformly over the full five-parameter quotient unfolding.
- Identified with the B = 0 case of RR 2015 Theorem 3.1's family; "Roussarie–
  Rousseau explicitly leave the B = 0 H14_3 case outside their finite-cyclicity
  result."
- 80 pages, computer-assisted finite derivations, ancillary bundle
  `h14_3_reproducibility/`. The cyclicity bound B is **existential** — no
  explicit number is given.

## Where this fits (and does not complete the DRR program)

- Even if correct, this is ONE graphic. The DRR program still needs all 121; the
  partially-closed full graphics (I_6b^1, H_13^3, DI_2b) and the 11 degenerate
  graphics remain. See research/drr-list.md and the drr-status thread.
- "Local uniform finite cyclicity in one collar" must still be checked against
  the DRR definition of finite cyclicity of a graphic (DRR 1994 not held).

## Evidence class discipline

Until independently re-derived in this run, everything Lu claims is
**asserted-by-source, unrefereed**. A kernel-checked Lean theorem closing the
finite core would upgrade that specific step to **verified-computationally** in
this run; the paper's analytic claims stay asserted. The claims ledger rows
h16-drr-h14-3-lu-2026-claim and drr-lu-claims-h14-3 carry this caveat and are
marked **unchecked** until this thread resolves them.
