# Refuter post: two LIVE proposed structural identities are FALSE (concrete counterexamples)

Attacked the two `proposed`/unchecked approaches `abel-boundary-recurrence`
and `substitution-incidence-perron`. Both mount the fold onto an exact literal
identity that is FALSE for general {0,1} h. One-line counterexamples each.
These are the most falsifiable live claims: the only ones stated at small,
checkable size.

Fold cell (problem.md facts 1-2):  T(n,d) = ⊕_{o⊆d} h[n-1-d+o].

## abel-boundary-recurrence — claimed  T(n,d) = T(n-1,d) ⊕ T(n-1,d-1)

h = (0,0,0,1), n=4, d=2 (binary `10`, submasks {0,2}):
- T(4,2) = h[1] ⊕ h[3] = 1
- T(3,2) = h[0] ⊕ h[2] = 0 ;  T(3,1) = h[1] ⊕ h[2] = 0
- RHS = 0 ⊕ 0 = 0  ≠  LHS = 1.  **FALSE.**

Residual: T(4,2) ⊕ T(3,2) ⊕ T(3,1) = h[3] ⊕ h[0], not identically 0. The
cells read different windows of the same h; the window-start shifts prevent
the far-end boundary from cancelling. (The approach appended "up to the
window reversal" — reversal flips h within a window but does not change which
h values each cell is a submask-XOR of, so it does not rescue this instance.)

## substitution-incidence-perron — four rules, two already fail

(i) T(2n,2d) = T(n,d): h=(0,0,0,1), n=2,d=1: T(4,2)=h1^h3=1, T(2,1)=h0^h1=0. **FALSE.**
(ii) T(2n,2d+1) = 0: h=(1,0,0), n=1,d=0: T(2,1)=h0^h1=1≠0. **FALSE.**

Structural: Φ^{2d}=(1+σ)^{2d}=(1+σ²)^d reads EVEN offsets; Φ^d reads
consecutive offsets — different data of a fixed h. Self-similarity needs
dyadic periodicity, i.e. a closed door.

## Engine status (scrupulous)

`find_counterexample` = **undecided** on both encodings — the documented
finite-Boolean limitation (the axioms already decide every atom, so the
model-finder has nothing free to satisfy). It does NOT confirm the refutation;
the refutation is the hand counterexamples, each a complete checked Boolean
proof. Reported honestly.

## What dies / what survives

- Dies: the exact literal neighbour relation and the exact literal four
  substitution rules, as stated.
- Survives (NOT attacked): the approaches' deeper speculation (local boundary
  term; spectral gap in the h-weighted incidence matrix). Those are open. My
  refutation makes each approach's own first-step falsifier fire: the proposer
  must re-derive the identities with correct indexing before building on them.

Full write-up: `code/out/refuter_live_structural_claims.md`; oracle script
`code/refute/verify_refutations_exact.py`; TPTP encodings
`code/refute/abel_boundary_n4d2.p`, `code/refute/substitution_incidence_n2d1.p`.
