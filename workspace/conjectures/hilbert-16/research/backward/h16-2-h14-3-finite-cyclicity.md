# Backward skeleton — finite cyclicity of the open graphic (H₁₄³)

Concrete target for the DRR finite-cyclicity program. `rests-on` is now
grounded in the claims ledger (which did not exist when the frame skeleton
`h16-2-finite-cyclicity.md` was first written), so the reduction and the
target-selection are discharged by claim ids, and the whole open content
collapses onto three sharpenable gaps whose first moves are computed today.

```skeleton
goal: cycl(Lambda_0 = H14^3) < infinity: finite cyclicity of the semihyperbolic hemicycle through a triple nilpotent point at infinity, uniformly over its five-parameter unfolding.
implies: H(2)<infinity folds to the 121-graphic maximum (h16-drr-121-graphics, drr-1994-citation-anchor). Lambda_0 is a discharged open target (drr-lu-claims-h14-3, h16-drr-open-rows). Three gaps: G-lu-core (exact Bautin-ideal core), G-lean-cert (kernel-checked certificate), G-remainder (analytic lift + uniformity).
killed-by: if the analyticity never enters (a purely topological/C^∞ bound on the zeros), the lemma is a smooth falsity: C^∞ fields can have infinitely many limit cycles. The zero-count must genuinely come from the almost-regular / center-ideal structure that fails for C^∞ perturbations. G-lean-cert being vacuous (a theorem about the literal 0 placeholder instead of the real 30-monomial identity) would also kill the argument — a certificate about nothing proves nothing.
rests-on: h16-drr-121-graphics, drr-1994-citation-anchor, drr-lu-claims-h14-3, h16-drr-open-rows, lu-finite-core-partially-verified
status: sketched
```

```gap
id: G-lu-core
lemma: The finite algebraic core of Lu's verification of cycl(Λ₀)<∞ stands up
       to clean-room exact recomputation from the paper's stated definitions:
       the Bautin/Lyapunov recurrence yields L₄ = (AC+CD+2DF−EF)/8 and the
       degree-6 obstruction L₆ = −P/192 (30 monomials), the Darboux cofactors
       X(L) = (x+dy)L and X(F) = (2Bx+dy)F hold, and the degree-8/10/12
       Lyapunov quantities lie in the Bautin ideal ⟨L₄,L₆⟩ (resp.
       ⟨L₄,L₆,L₈⟩) — i.e. the displacement is a finite sum of generalized
       monomials with coefficients in the center ideal (the Bautin trick).
status: open
discharged-by: NOT discharged — `lu-finite-core-partially-verified` is itself
       asserted-not-checked: the degree-4 and cofactor identities were
       "re-derived by hand", the degree-6 30-monomial equality was transcribed
       but never re-executed, `lyap_extend.py` crashed before finishing L₈/L₁₀/L₁₂
       and the ideal-membership statement, so by this workspace's own rule the
       core is a measurement nobody can reproduce. It must be closed by execution.
thread: lu-h14-3-verification
next: Write `code/bautin/verify_lu_core.py` clean-room from the paper's stated
       definitions (NOT importing Lu's scripts), exact rational/symbolic
       arithmetic via sympy, computing L₄, L₆, the Darboux cofactors, and the
       degree-8/10/12 ideal memberships; assert on the produced data
       (8L₄ = AC+CD+2DF−EF, etc.); capture to `code/out/lu_core.captured.txt`
       whose first three lines name what ran, which definitions, which
       identities. This is a tool_builder task runnable today.
```

```gap
id: G-lean-cert
lemma: The finite core of G-lu-core is a kernel-checked Lean certificate: the
       degree-6 30-monomial identity (192·L₆ + P₃₀ = 0) and the ideal memberships
       are stated over a fully spelled-out monomial list and proved by the
       kernel (`decide`/`ring`/`norm_num` after expansion), not by a stub that
       defines P₃₀ := 0. Closing this makes the Bautin-ideal computation a
       theorem rather than a number.
status: open
discharged-by: (none) — `code/lean/Lib/BautinRecurrence.lean` line 90 defines
       P₃₀ as the literal 0 with a placeholder comment, so the theorem
       192·L₆ + P₃₀ = 0 is currently a statement about zero and proves nothing
       about the paper.
thread: lu-h14-3-verification
next: Spell out all thirty monomials of P₃₀; put the generated coefficient data
       as untrusted defs under `code/lean/Lib/Generated/`, write the checker
       by hand OUTSIDE that folder, and prove check=true iff the identity,
       closing it with `decide` rather than `native_decide`. No theorem inside
       Generated/. Doable by the lean_prover role today.
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
thread: lu-h14-3-verification
next: For each sub-step, state the statement in Lean and catalogue what Mathlib
       lacks (displacement function, Dulac maps, almost-regular germs,
       isolated periodic orbits) — a reportable gap list under
       `code/lean/Lib/`; and verify the DRR-definition match (does Lu's
       collar + five-parameter result equal the DRR "finite cyclicity of the
       graphic" including boundary-at-infinity) against the held RR 2015 text.
```

**How the gaps recombine (the `implies` spelled out).** The reduction is
already established (claims `h16-drr-121-graphics`, `drr-1994-citation-anchor`),
so proving cycl(Λ₀)<∞ for one graphic is a genuine partial result and one of the
finitely many bounds in the 121-graphic maximum. G-lu-core fixes the Bautin-ideal
side exactly (the coefficients and ideal memberships that make the center-ideal
division legitimate). G-lean-cert turns that finite core into kernel-checked
Lean, so the computation is a theorem. G-remainder is the analytic step that
lifts "the displacement is Σaᵢmᵢ(1+hᵢ) with aᵢ∈(center ideal)" to "the
displacement has uniformly ≤ B zeros in the collar" — and this is where
analyticity must genuinely enter (test 1: a C^∞ version of the same expansion
does not bound zeros, Dulac's error), and where uniformity must genuinely use
the compactness of Λ (a pointwise-finiteness-⇒-uniform-finiteness inference
would be the fake step). The order of attack is G-lu-core first (the directive's
close-both-gaps mandate), then G-lean-cert, then G-remainder.

**Tests applied.** Test 1: the skeleton survives only if G-remainder really uses
almost-regular/center-ideal structure; if a candidate proof of the zero bound
never touches analyticity it has re-proved a smooth falsity — record that as its
failure point. Test 2: no sharp tight bound is claimed, so H(2)≥4 and
H(n)≳n²log n do not threaten a finite-cyclicity bound. Test 3: finite cyclicity
is not a sharp count, so the slow–fast test is not the mode this proof fails in.
