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

named mathematics: Fenchel–Rockafellar duality, convex conjugate, support
function, minimax theorem (von Neumann), polytope face structure, linear
programming duality (this is finite-dimensional LP duality really — Fenchel
is the general setting), combinatorial game theory (the sign assignment is
the adversary's strategy).

status: refuted
killed-by: >
  Refuted on three grounds, the first two decisively.

  (1) The core identity A_k(1) = max_{s∈S_k} |Σ ε_{k,j}(s)·g_j| is false as
  written, and the correction that would make it true destroys the polytope
  claim. The nested maximisation |max|...|max Σ| resolves to
  max_{s∈S_k} Σ ε(s)·g only when the min branch never activates — but the
  min branch is the whole content of the operator. When it does activate,
  the correct expansion is |a−b| = max_{σ∈{±1}} σ(a−b), and at the NEXT
  level the σ's interact through the intermediate absolute values, so the
  reachable set S_k is not a static set of 2^{k−1} sign vectors: membership
  in S_k depends on the gap values themselves (which histories are reachable
  is decided by the comparison a_i ≥ b_i at each level, i.e. by the gaps).
  This is the same obstruction the run already recorded: the identity
  A_k(i) = |Δ_k(i)| fails at (k=3,i=2) inside the block
  (fwd-diff-identity-refuted), and the sign histories that the approach's
  S_k would need are exactly the min-branch choices it cannot make
  independent of the input.

  (2) The universal claim — "the polytope's structure forces the dual
  minimum ≤ 2 for ANY even-gap input" — is FALSE as a class statement. The
  Colonna delete-5 example (claim colonna-deletion-left-edge-failure, held)
  is a 2-then-odds sequence with all gaps after the first even
  (2,3,7,11,13,17,19,23,...) whose triangle has A_1(1) = 4 (second entry
  4), i.e. the maximisation over its sign histories yields 4, not ≤ 2.
  Any dual certificate claiming the max ≤ 2 for every even-gap input is
  contradicted by a concrete even-gap input in the class. (Hand-checkable
  from the claim's own rows: gaps 1,4,4,2,4,2,4,4,... give
  A_1 = (1,4,4,2,4,2,4,...), so A_1(1)=4.) The polytope statement would
  have to be restricted to a proper subclass — but which subclass, and why
  the primes lie in it, is precisely the conjecture. The candidate itself
  flags this ("the polytope theorem would have to show his construction's
  sign histories are NOT in the reachable set S_k") — that is exactly the
  unproved regeneration content.

  (3) The reachable-sign-set geometry is not in the literature in a usable
  form. The closest bodies — the absolute value equation (AVE) literature
  (Mangasarian 2007; Hladík et al. 2024) and absolute-value LP duality
  (Hladík–Hartman 2023) — establish that AVE solution sets are unions of at
  most 2^n convex polyhedra (one per orthant) and that solving them is
  NP-hard. They give the orthant/sign-pattern decomposition the approach
  postulates, but they do NOT give a facial-structure theorem forcing the
  max ≤ 2 for even-gap inputs, and the NP-hardness results are evidence
  against any such cheap universal certificate. No source applies
  Fenchel–Rockafellar duality to the iterated absolute-difference operator.
precedent: >
  - https://doi.org/10.48550/arxiv.2404.06319 (Hladík et al. 2024: AVE
    orthant decomposition — the reachable-sign-set geometry is a union of
    ≤ 2^n convex polyhedra, one per sign pattern)
  - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.416.1189
    (Mangasarian 2007: absolute value equations are NP-hard; sign-pattern /
    orthant solution structure)
  - https://doi.org/10.48550/arxiv.2307.03510 (Hladík–Hartman 2023:
    absolute-value LP duality — the named duality exists but is for AVE/LP,
    not for iterated nested absolute values)
  - https://doi.org/10.1090/s0025-5718-1993-1182247-7 (Odlyzko 1993 — the
    mod-4 linearization is the only known exact congruence handle)
  - claims: colonna-deletion-left-edge-failure, fwd-diff-identity-refuted
holding-claims: colonna-deletion-left-edge-failure, fwd-diff-identity-refuted
falsifies: >
  That A_k(1) = max over a static sign set of a linear functional (false:
  reachable sign histories depend on the gap values through the min branch),
  or that the dual polytope forces max ≤ 2 for every even-gap input (false:
  the Colonna delete-5 sequence is an even-gap 2-then-odds input with
  A_1(1)=4).
buy: >
  A reformulation with genuine expressive power (nested absolute values as a
  minimax) and a real literature (AVE orthant geometry, absolute-value LP
  duality) — but no theorem in that literature bounds nested-absolute
  iterates on even-gap inputs, the universal class claim is false, and the
  subclass restriction that would save it is the conjecture itself. Refuted
  as stated; the AVE orthant-decomposition picture is worth keeping as a
  language, not as a proof engine.

first-step (superseded): >
  The proposed first step — enumerating reachable sign histories S_k for
  k=2..5 and checking max_v |⟨g,v⟩| = A_k(1)/2 — would verify the identity
  on small rows, but the identity is already known false at (k=3,i=2)
  (fwd-diff-identity-refuted), so the enumeration would confirm the
  refutation, not build a certificate.
```

```claim
id: fenchel-duality-sign-assignment-refuted
statement: The Fenchel–Rockafellar / minimax sign-history route to Gilbreath
  fails: (i) the representation A_k(1) = max over a static sign set of a
  linear functional is false because reachable sign histories depend on the
  gap values through the min branch (the identity A_k=|Δ_k| it needs fails
  at (k=3,i=2), claim fwd-diff-identity-refuted); (ii) the universal dual-
  certificate claim is false — the Colonna delete-5 sequence is a 2-then-odds
  input with all gaps after the first even and A_1(1)=4 (claim
  colonna-deletion-left-edge-failure); (iii) the AVE literature (Mangasarian
  2007, Hladík 2024) gives the orthant geometry but no bound for nested
  absolute iterates, and AVE solvability is NP-hard.
hypotheses: any 2-then-odds even-gap input; the sign-history polytope of
  depth-k descents.
holds-here: yes
status: refuted (the universal class claim is falsified by a concrete held
  example; the identity is falsified by a stored machine-checked claim)
bearing: closes the convex-duality line as a universal-class proof; the AVE
  orthant language survives only as vocabulary. A subclass restriction that
  excludes the Colonna example is the conjecture itself.
anchor: research/approaches/fenchel-duality-minimax-sign-assignment.md
```
