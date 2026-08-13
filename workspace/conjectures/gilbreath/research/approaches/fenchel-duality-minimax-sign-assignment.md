# fenchel-duality-minimax-sign-assignment

```approach
idea: Express A_k(1) as the value of a combinatorial minimax over sign
assignments, then apply Fenchel–Rockafellar duality to convert the minimax
into a dual maximin whose certificate proves the value never exceeds 2.

mechanism: Start from the identity

    |a−b| = max_{σ∈{±1}} σ·(a−b)   where the max is attained at σ = sign(a−b).

Iterating: each step of the Gilbreath operator chooses a sign σ_i at each
adjacent pair, and the whole depth-k descent is

    A_k(1) = max_{σ₁} | max_{σ₂} | ... | max_{σ_k} Σ ... | | |

where the inner Σ is a signed alternating sum over the k consecutive gaps
g₁,...,g_k.

Equivalently: define the set of 2^{k−1} sign vectors
S_k = { (s₁,...,s_k) ∈ {±1}^k : s₁ = 1, and each s_i encodes the "surviving
sign" at the i-th level after absolute values are resolved }.

Then

    A_k(1) = max_{s ∈ S_k} | Σ_{j=0}^{k} ε_{k,j}(s) · g_{j+1} |

where ε_{k,j}(s) ∈ {±1} is the accumulated sign of the j-th gap after the
k levels of sign resolution. The set S_k is the set of "consistent sign
histories" — not all sign vectors, but those reachable by the max-over-σ
dynamics.

The conjecture A_k(1) ∈ {0,2} is the statement that this maximisation
over 2^{k−1} sign histories never yields a value ≥ 4 (halved ≥ 2).

Now apply FENCHEL DUALITY (Rockafellar 1970). The function

    f(s) = Σ_{j} ε_{k,j}(s) · g_{j+1}

is a linear functional on the sign vectors (the coefficients are the gaps),
and |f(s)| = max(f(s), −f(s)). The overall A_k(1) is

    A_k(1) = max_{s ∈ S_k} max_{τ ∈ {±1}} τ · f(s)
           = max_{(s,τ) ∈ S_k × {±1}} ⟨c_τ, φ(s)⟩

for an appropriate feature map φ and coefficient vector c_τ depending on the
gaps. This is a maximisation of a linear functional over a finite set.

Fenchel's theorem: the value of this maximisation equals the value of the dual
minimisation over the convex hull:

    max_{x ∈ X} ⟨c, x⟩ = min_{y ∈ Y} δ*(y | X) + δ*(−y | {c})

where δ* is the support function (convex conjugate). In particular, if we can
exhibit a dual certificate y* — a vector in the dual space — such that the
dual objective is exactly 2 (or 0), then the primal max is ≤ 2, and the
conjecture holds.

The dual certificate has a concrete interpretation: it is a convex combination
(probability distribution) over sign histories and outer signs that "balances"
the gap-weighted contributions. Specifically, find probabilities p_s,τ ≥ 0,
Σ p_s,τ = 1, such that

    Σ_{s,τ} p_s,τ · τ · ε_{k,j}(s) = 0   for all j (or sums to ±2 for one j
                                            and zero for the rest).

That is: there exists a "mixed strategy" over sign histories whose expected
signed contribution at each gap position is zero (or ±2 at a single position).
If such a distribution exists for every k, then A_k(1) ∈ {0,2} — because the
max over pure strategies cannot exceed the expectation under any mixed
strategy (the max is at least the expectation for the actual max, but the
existence of a balancing distribution forces the max itself to be small).

The engine is NOT to construct the distribution explicitly (that would require
knowing the gap sequence). Instead: prove that the sign-history polytope
conv(S_k × {±1}) has a specific facial structure that guarantees the dual
minimum is at most 2 for ANY initial gap sequence with gaps in 2ℕ. This is a
statement about the GEOMETRY of the sign-resolution polytope — a purely
combinatorial object independent of the primes.

Why this is genuinely different:

- It is not about blocks, intruders, erosion, or regeneration — the words
  never appear.
- It is not a congruence or invariant of the row entries.
- It replaces the operator |a−b| with a maximisation and then dualises it —
  turning the open "does the max exceed 2?" into "does the dual polytope
  contain a certificate of boundedness?".
- The dual polytope depends only on k (the depth) and the fact that gaps are
  even — NOT on the specific gap values. If the polytope's structure forces
  the dual minimum ≤ 2 for all k, the conjecture is proved for EVERY 2-then-
  odds sequence simultaneously. That would beat Eppstein (his construction
  works in the bounded-gap class, which is a subset of 2-then-odds — so the
  polytope theorem would have to show his construction's sign histories are
  NOT in the reachable set S_k, which would be a genuinely new structural
  fact).

Named mathematics: Fenchel–Rockafellar duality, convex conjugate, support
function, minimax theorem (von Neumann), polytope face structure, linear
programming duality (this is finite-dimensional LP duality really — Fenchel
is the general setting), combinatorial game theory (the sign assignment is
the adversary's strategy).

Speculative: the reachable sign set S_k may have a simple recursive
description (each σ_i at level i depends on whether a_{i−1} ≥ b_{i−1}
in the unsigned triangle). If S_k has a product structure or is a matroid
polytope, the dual certificate may be constructible by induction on k.

status: proposed

first-step: For k = 2,3,4,5, enumerate the full set of reachable sign
histories S_k from the actual prime triangle (depth 5, using exact integers
from the oracle). For each history s ∈ S_k, compute the vector
v_s = (ε_{k,0}(s), ..., ε_{k,k}(s)) of accumulated signs. Plot these vectors
in ℝ^{k+1} and examine their convex hull. Compute its support function in the
direction of the gap vector g = (g_1,...,g_{k+1}) and verify that
max_{v ∈ conv(S_k)} |⟨g, v⟩| = A_k(1)/2 ∈ {0,1} — i.e., the convex hull
already certifies the bound (since the max over the finite set equals the max
over its convex hull). Then, more importantly: compute the DUAL polytope
describing the set of gap vectors g for which the max is ≤ 1. This is the set
of g ∈ ℝ^{k+1} such that max_v |⟨g, v⟩| ≤ 1, which is a polyhedral cone
(intersection of halfspaces). Its facet-defining inequalities encode the exact
condition on prime gaps that forces A_k(1) ∈ {0,2}. If all even integer
vectors in this cone have entries in 2ℕ (they do, by construction), we have
a reformulation: the conjecture holds at depth k iff the prime gap vector
lies in this cone. Check whether the actual first 100 gap vectors lie in their
respective cones (they should, since the conjecture is verified). Then ask:
what is the FACIAL STRUCTURE of this cone as k grows? Does it stabilise?
Does it contain all "sufficiently irregular" gap vectors? This last question
is the dual of the "inter-giant gap boundedness" question.
```