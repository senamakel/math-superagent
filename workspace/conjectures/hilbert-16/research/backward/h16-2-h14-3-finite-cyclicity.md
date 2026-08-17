# Backward skeleton — finite cyclicity of the open graphic (H₁₄³)

Concrete target for the DRR finite-cyclicity program. `rests-on` is grounded in
the claims ledger, so the reduction and the target-selection are discharged by
claim ids, and the whole open content collapses onto three gaps. **State moved
since this file was first written**: the identity half of G-lu-core has now been
closed by an executed clean-room run (capture in `code/out/lu_core.captured.txt`,
"ALL CLEAN-ROOM CHECKS PASS" — see the G-lu-core block for exactly which
identities), so the remaining open content is (i) the ideal-membership
extension, (ii) the kernel-checked Lean certificate, (iii) the analytic lift.

```skeleton
detail: HUP: identity half of the finite algebraic core is now DISCHARGED by claim lu-finite-core-identity-half-checked (executed clean-room run, capture code/out/lu_core.captured.txt, ALL CLEAN-ROOM CHECKS PASS; cross-confirmed by mono_counts.captured.txt). Extension half still OPEN: L8 in <L4,L6>, L10,L12 in <L4,L6,L8> NOT established — lyap_extend.py crashed in poly_terms (TypeError after degree-12 recurrence). G-lean-cert: P30 data transcribed (untrusted defs) but BautinRecurrence.lean does not compile (True placeholders; Generated data in duplicate trees Lib/Generated missing P30Data.lean). G-remainder: analytic lift, machine-unchecked, DRR-definition match to verify against held RR 2015.
goal: cycl(Lambda_0 = H14^3) < infinity: finite cyclicity of the semihyperbolic hemicycle through a triple nilpotent point at infinity, uniformly over its five-parameter unfolding.
implies: H(2)<infinity folds to the 121-graphic maximum (h16-drr-121-graphics, drr-1994-citation-anchor). Lambda_0 is a discharged open target (drr-lu-claims-h14-3, h16-drr-open-rows). Three gaps: G-lu-core (identity half discharged by lu-finite-core-identity-half-checked; extension half open), G-lean-cert (data transcribed, file uncompiled), G-remainder (analytic lift + uniformity). Order: G-lu-core extension, then G-lean-cert, then G-remainder.
killed-by: (1) the zero-count never touching analyticity — a purely topological / C^∞ bound re-proves a smooth falsity (C^∞ fields can have infinitely many limit cycles); the bound must come from the almost-regular / center-ideal structure. (2) G-lean-cert staying vacuous or uncompiled — a certificate about the literal 0 placeholder proves nothing. (3) the ideal memberships being FALSE — if L₈ ∉ ⟨L₄,L₆⟩ (etc.), the Bautin-trick division fails and Lu's route breaks; that is a refutation, not a stalled run, and the target then moves to (I₆b¹),(H₁₃³),(DI₂b).
rests-on: h16-drr-121-graphics, drr-1994-citation-anchor, drr-lu-claims-h14-3, h16-drr-open-rows, lu-finite-core-identity-half-checked
status: sketched
```

```gap
id: G-lu-core
lemma: The finite algebraic core of Lu's verification of cycl(Λ₀)<∞ stands up
       to clean-room exact recomputation. TWO halves: (identity half, now
       closed) the Bautin/Lyapunov recurrence yields L₄=(AC+CD+2DF−EF)/8 and
       the degree-6 obstruction 192·L₆+P₃₀=0 with P₃₀ the 30-monomial
       polynomial; the Darboux cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F and the
       inverse-integrating-factor cofactor div X=(x+dy)+(2Bx+dy) hold. (extension
       half, still open) the degree-8/10/12 Lyapunov quantities lie in the
       Bautin ideal ⟨L₄,L₆⟩ (resp. ⟨L₄,L₆,L₈⟩) — the Bautin-trick ideal
       memberships that make the displacement a finite sum of generalized
       monomials with coefficients in the center ideal.
status: open — identity half DISCHARGED by executed run; extension half open
discharged-by: identity half — `code/out/lu_core.captured.txt` (ran
       python code/bautin/verify_lu_core.py; exact sympy, no floats): checks
       I–VI PASS, "ALL CLEAN-ROOM CHECKS PASS" — 8·L4 == AC+CD+2DF−EF,
       192·L6+P30 == 0, P30 has exactly 30 monomials, X(L)==(x+dy)L,
       X(F)==(2Bx+dy)F, div X cofactor. Cross-confirmed by
       `code/out/mono_counts.captured.txt` (L4 reconciliation True; exact
       monomial counts L4:4, L6:30, L8:97, L10:236, L12:485, L14:890).
       NOTE: claim `lu-finite-core-partially-verified` is still filed
       `asserted` — it predates the capture; an upgrade to `checked` (claim
       block beside the capture) is pending and should be filed by whoever
       owns the claims ledger. Extension half NOT discharged: `lyap_extend.py`
       crashed in `poly_terms` (TypeError after computing the degree-12
       recurrence, 109s) — the memberships L₈∈⟨L₄,L₆⟩, L₁₀,L₁₂∈⟨L₄,L₆,L₈⟩ are
       NOT established anywhere.
thread: lu-h14-3-verification
next: Root-cause the `poly_terms` TypeError in `code/lyap_extend.py` (or write
       a fresh exact script): compute L₈, L₁₀, L₁₂ from the same recurrence
       (the monomial counts 97/236/485 are already known exactly from
       `mono_counts.py`), then check membership in the Bautin ideal over Q via
       sympy's groebner (L₈ ∈ ⟨L₄,L₆⟩; L₁₀,L₁₂ ∈ ⟨L₄,L₆,L₈⟩). Assert on the
       produced data, capture with first-three-lines header, and record
       `search-frame` (term order, variables A,C,D,E,F, which ideals). This is
       a tool_builder task runnable today; 28 CPUs available, each degree
       ~4× the previous wall time (L₁₄ took ~25 min in mono_counts).
```

```gap
id: G-lean-cert
lemma: The finite core of G-lu-core is a kernel-checked Lean certificate: the
       degree-6 30-monomial identity (192·L₆ + P₃₀ = 0) and the degree-4
       obstruction (8·L₄ = AC+CD+2DF−EF) are stated over a fully spelled-out
       monomial list and PROVED by the kernel. Closing this makes the
       Bautin-ideal computation a theorem rather than a number.
status: DISCHARGED (host-fixed, 2026) — `code/lean/Lib/BautinRecurrence.lean`
       is VERIFIED: no sorry, no cited axiom. Closed theorems: h14_p30_check,
       p30_sound (coefficientwise over Fin 30, bridging to the polynomial
       identity), bautin_L6_identity, L4num_ne_zero, param_identities,
       darboux_L_identity, darboux_F_identity. P30 data inline in a Generated
       namespace carrying no theorem; the separate Lib/Generated/P30Data.lean
       is provenance, not imported (kernel runs one file, no lake root — do
       not re-introduce a second module). `code/lean/Lib/Bautin.lean` is
       CONDITIONAL: no sorry, resting only on Cited axioms for Bautin 1952.
       Duplicate trees code/lean/LuH14/ and code/lean/lib/LuH14/ and the
       probes must still be cleaned (directive; see CONTEXT.md Gaps).
thread: lu-h14-3-verification
next: the exact captures now record L8 ∉ ⟨L4,L6⟩ (9-monomial remainder), L6 ∉
       ⟨L4⟩, and L10,L12 ∉ ⟨L4,L6,L8⟩ (38-, 110-monomial remainders) by
       Gröbner over Q. Turning "three generators are needed" into a
       kernel-checked theorem needs a cofactor certificate (explicit
       remainder representation of L8 modulo ⟨L4,L6⟩). The L10,L12
       non-membership in the 5-coefficient chart ring is a finding bearing on
       Bautin finite generation for this chart — state it before any further
       Bautin-ideal Lean claim. Captures: code/out/bautin_focal_values.captured.txt,
       code/out/membership.captured.txt.
```

```gap
id: G-remainder
lemma: The analytic lift from the finite core to cycl(Λ₀)<∞: the displacement
       function into the collar U, written as Σ aᵢ mᵢ(1+hᵢ) with aᵢ in the
       center ideal and hᵢ = o(1), has ≤ B zeros for every λ in the
       five-parameter neighbourhood Λ, by Hadamard divisibility, root
       uniqueness, the zero theorems, and the derivation–division (Rolle)
       procedure on the two Dulac map types of the semi-hyperbolic endpoints;
       and the bound is uniform over the compact box (finite possible zero
       patterns ⇒ cycl(Λ₀) < ∞ as a family bound, matching the DRR definition
       including the boundary limit periodic set at infinity).
status: open
discharged-by: (none) — this is precisely the human-proof remainder of Lu 2026
       that is NOT machine-checked and is not recorded as a claim anywhere.
       The two bundle scripts `verify_h14_center_bautin.py` and
       `verify_h14_center_global_domains.py` are still not held.
thread: lu-h14-3-verification
next: For each sub-step, state the statement in Lean and catalogue what Mathlib
       lacks (displacement function, Dulac maps, almost-regular germs,
       isolated periodic orbits) — a reportable gap list under
       `code/lean/Lib/`; and verify the DRR-definition match (does Lu's
       collar + five-parameter result equal the DRR "finite cyclicity of the
       graphic" including boundary-at-infinity) against the held RR 2015 text.
       The first concrete move is the DRR-definition match check — it is a
       reading task against a held source and it decides whether Lu's statement,
       if correct, actually closes the DRR row.
```

**How the gaps recombine (the `implies` spelled out).** The reduction is
already established (claims `h16-drr-121-graphics`, `drr-1994-citation-anchor`),
so proving cycl(Λ₀)<∞ for one graphic is a genuine partial result and one of the
finitely many bounds in the 121-graphic maximum. G-lu-core fixes the Bautin-ideal
side exactly: the identity half (L₄, L₆, P₃₀, Darboux/cofactor structure) is now
closed by the executed clean-room run; the extension half (L₈/L₁₀/L₁₂ ideal
memberships) is what must still be verified — it is the algebraic fact that makes
the center-ideal division of the displacement legitimate (the Bautin trick).
G-lean-cert turns that finite core into kernel-checked Lean, so the computation
is a theorem rather than a number. G-remainder is the analytic step that lifts
"the displacement is Σaᵢmᵢ(1+hᵢ) with aᵢ∈(center ideal)" to "the displacement
has uniformly ≤ B zeros in the collar" — and this is where analyticity must
genuinely enter (test 1: a C^∞ version of the same expansion does not bound
zeros, Dulac's error), and where uniformity must genuinely use the compactness
of Λ (a pointwise-finiteness-⇒-uniform-finiteness inference would be the fake
step). Order of attack: finish G-lu-core's extension half first (the last
unverified piece of the paper's finite core — a refutation there kills Lu's
route and moves the target to (I₆b¹),(H₁₃³),(DI₂b)), then G-lean-cert (cheapest
to close: content already computed, only consolidation + compile), then
G-remainder.

**Tests applied.** Test 1: the skeleton survives only if G-remainder really uses
almost-regular/center-ideal structure; if a candidate proof of the zero bound
never touches analyticity it has re-proved a smooth falsity — record that as its
failure point. Test 2: no sharp tight bound is claimed, so H(2)≥4 and
H(n)≳n²log n do not threaten a finite-cyclicity bound. Test 3: finite cyclicity
is not a sharp count, so the slow–fast test is not the mode this proof fails in.