# Research grounding pass: three reformulations taken to the literature

The inventor's message failed, so I grounded the three lines the run has listed
but nobody had yet checked. Full detail in
`research/notes/research_grounding_three_reformulations.md`; claim ids mirror into
`research/CLAIMS.md`.

## abel-boundary-recurrence — REFUTED
Mounts Abel summation by parts (Abel–Zeilberger, arXiv:1105.0178 — real) on the
literal neighbour relation `T(n,d)=T(n−1,d)⊕T(n−1,d−1)`. **That relation is false**
for the real fold cell T(n,d)=⊕_{o⊆d}h[n−1−d+o]: h=(0,0,0,1), n=4,d=2 gives
T(4,2)=1 but T(3,2)⊕T(3,1)=0. The far-end boundary h[n−1] never cancels because the
three cells read different contiguous windows (claim `abel-boundary-recurrence-relation-false`).
First-step falsifier fires; the "local boundary" hope has no correct relation to run on.

## substitution-incidence-perron — REFUTED
Mounts the Perron–Frobenius of primitive-substitution incidence (Bédaride–Hilion
2012 — real) on four substitution rules. **They are false** (claim
`substitution-incidence-rules-false`): Φ^{2d}=(1+σ²)^d reads even offsets of a fixed
h while Φ^d reads consecutive offsets — different data; self-similarity needs
dyadic-periodic h, a closed door. E.g. T(2,1)=h[0]⊕h[1]=1≠0 kills rule T(2n,2d+1)=0.

## f2-gram-disjointness-spectrum — GROUNDED (machinery), transfer open
Z²=I over F₂ and Gram=disjointness are real; the golden Kron spectrum is standard
(Mattila–Haukkanen, Discrete Math 2014, the meet/join-matrix home). Caveat: the
clean spectrum is the *full-cube* one; the operative principal-submatrix
(d∈[2,n−1]) spectrum is unverified and the weight-bound transfer has no published
precedent. Cheap first-step (compute the submatrix spectrum vs primes/controls)
is the decisive test.

Both refutations are hand-verified Boolean arithmetic matching the on-disk record;
`code/out/research_verify_relations.py` is written for tool_builder to machine-confirm
over the full small range.
