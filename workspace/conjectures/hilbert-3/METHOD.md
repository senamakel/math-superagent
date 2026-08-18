Solve by explicit dissection against exact invariant computation, with the
mathematics carried in Lean wherever it will go. The subject has two moves.

**Affirmative results are certificates.** A scissors congruence is a finite list
of pieces and isometries, and checking one is exact arithmetic over a number
field: the pieces tile the source, their images tile the target, each map is an
isometry. So the affirmative direction is a *search for a certificate*, and the
instruments are exact polyhedral geometry over algebraic number fields, convex
decomposition, and the combinatorics of common refinements.

**Negative results are invariants.** An obstruction is a function of a polytope,
provably unchanged by cutting and reassembly, which separates two candidates.
The instruments are the scissors congruence group `P(X)`, Dupont–Sah's
homological description, the Bloch group and the dilogarithm, Cheeger–Simons
characteristic classes, and the `K`-theoretic reframing. A new invariant is what
would settle the conjecture negatively, and proving invariance is the whole
difficulty — the numerical part is easy and worthless on its own.

Reason about the **Dehn invariant as an element of a tensor product**: the
question of whether `Σ ℓ_i ⊗ θ_i` vanishes is a question about `Q`-linear
relations among the `θ_i/π`, and that is a statement about algebraic numbers
which must be *proved*, not observed numerically. Baker's theorem and its
effective forms, and exact arithmetic in the relevant number field, are the
tools; a high-precision zero is a lead.

**Prefer the argument Lean can finish.** The Dehn invariant of a polytope with
algebraic data, a five-term dilogarithm relation, the verification that a list
of pieces tiles a polytope — each is finite and kernel-checkable. State every
claim as a Lean type before spending an attempt on it, and record what today's
Mathlib cannot carry.

Three cautions this problem earns before any work starts.

**Euclidean scaling is the hidden hypothesis.** Every Euclidean proof uses that
a polytope can be scaled and that volume is a separate, continuous invariant.
Neither survives into `H³` or `S³`. An argument transported without naming where
scaling entered is refuted, not weakened.

**A numerically vanishing Dehn invariant is not a vanishing Dehn invariant.**
The invariant lives in `R ⊗_Z R/πQ` and its vanishing is a linear-independence
statement about angles. Compute exactly, or say the claim is numerical.

**Dimension 5 is open for a reason.** Sydler's proof is a difficult
cohomological argument that does not obviously generalise; a short argument for
`n ≥ 5` is far more likely to be an error than a breakthrough, and the honest
deliverable there is a precise statement of which step of Sydler fails to lift.
