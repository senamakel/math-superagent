# Refuter: two LIVE proposed structural claims are FALSE (concrete counterexamples)

Attacked two **proposed** (unchecked, status `proposed`, explicitly flagged
"speculation to be priced") approaches that the run's other schools are about
to build on:

- `abel-boundary-recurrence` — the first-order neighbour relation
  `T(n,d) = T(n−1,d) ⊕ T(n−1,d−1)` (from Pascal's rule in the d index).
- `substitution-incidence-perron` — the four substitution rules
  `T(2n,2d)=T(n,d)`, `T(2n,2d+1)=0`, `T(2n+1,2d)=T(n,d)`,
  `T(2n+1,2d+1)=T(n,d)`.

Both are claimed to hold for **any** {0,1} string h. Both are FALSE as stated,
by one-line counterexamples. These are the most falsifiable live claims in the
run's active workspace (they are the only ones stated at small, checkable size),
so they are the right target for the adversarial first instinct.

## Fold cell (problem.md facts 1-2)

    T(n,d) = ⊕_{o ⊆ d} h[n−1−d+o],   d = 2..n−1.

## Refutation A: abel-boundary-recurrence

Claim: `T(n,d) == T(n−1,d) ⊕ T(n−1,d−1)` for all n,d,h.

Take h = (0,0,0,1), n = 4, d = 2 (binary `10`, submasks {0,2}).

    T(4,2) = h[4−1−2+0] ⊕ h[4−1−2+2] = h[1] ⊕ h[3] = 0 ⊕ 1 = 1
    T(3,2) = h[0] ⊕ h[2] = 0
    T(3,1) = h[1] ⊕ h[2] = 0
    RHS    = T(3,2) ⊕ T(3,1) = 0        (≠ 1)

So LHS = 1 ≠ RHS = 0. The relation is FALSE.

Structural reason: the three cells read different contiguous windows of the
*same* h — T(n,d) reads the length-(d+1) window ending at n−1, T(n−1,d−1) the
length-d window ending at n−2, T(n−1,d) a window shifted left by one. The
interior submasks do not cancel because the window *starts* move with n, so
the boundary at the far end (index n−1) never cancels. Equivalently the
relation fails exactly to the extent h[3] ≠ h[0] in the example:
`T(4,2)⊕T(3,2)⊕T(3,1) = h[3]⊕h[0]`, not identically 0.

**Fair caveat — "up to the window reversal".** The approach's prose appended
"(up to the window reversal)", i.e. it anticipated some indexing subtlety.
My refutation is against the cells **as actually defined** by problem.md
facts 1-2 (the only well-defined cells of the real fold). The relation, in
whatever reversed indexing the proposer intended for the folded/reversed
window, still connects the *same* cells (reversal flips h within a window but
does not change which h values each cell is a submask-XOR of), so it does not
rescue the claimed identity `T(4,2)=T(3,2)⊕T(3,1)` for h=(0,0,0,1). This is
exactly what the approach's own first-step ("machine-verify it against the
brute submask-XOR oracle") would have caught; the relation must be re-derived
with correct indexing before the Abel-summation body is built on it.

## Refutation B: substitution-incidence-perron

Claim rules (first two suffice to kill):

(i) `T(2n,2d) = T(n,d)`: h = (0,0,0,1), n=2, d=1:
    T(4,2) = h[1]⊕h[3] = 1 ;  T(2,1) = h[0]⊕h[1] = 0.  FALSE.

(ii) `T(2n,2d+1) = 0`: h = (1,0,0), n=1, d=0: T(2,1) = h[0]⊕h[1] = 1 ≠ 0. FALSE.

Structural reason: `Φ^d = (1+σ)^d` and dyadic scaling gives
`Φ^{2d} = (1+σ)^{2d} = (1+σ^2)^d`, whose action at a position reads
h[x], h[x+2], h[x+4], … (even offsets), whereas `Φ^d` reads h[x], h[x+1],
…. These are different data of a fixed h. The claimed self-similarity would
need h to be periodic/dyadic-extended, which is precisely a closed door; for a
general h the four rules fail.

## Engine status (scrupulous)

`find_counterexample` returned **undecided** on both encodings
(`code/refute/abel_boundary_n4d2.p`, `code/refute/substitution_incidence_n2d1.p`).
That is the documented limitation: these are finite-propositional problems whose
axioms already decide every Boolean atom, so the model-finder has no free
Boolean left to satisfy — it finds neither a model nor a proof. The engine does
NOT confirm the refutation; the refutation is the hand counterexamples above,
each a complete, checked Boolean proof on a specific string. Reported honestly:
the refutation is a hand proof, the engine is silent on this encoding class.

## What survives and what dies

- Dies: the *exact literal* neighbour relation and the *exact literal* four
  substitution rules, **as stated**.
- Survives (NOT attacked): the approaches' deeper speculation — that the d-sum
  of S(n) telescopes into a local boundary term (abel), and that a spectral gap
  exists in the h-weighted substitution incidence matrix (perron). Those are
  open. My refutation kills the specific first-order/self-similarity identities
  each mounts on, so each approach's own first-step falsifier fires and the
  proposer must restate the relation with correct indexing before proceeding.

```claim
id: abel-boundary-recurrence-relation-false
statement: The proposed first-order neighbour relation T(n,d)=T(n−1,d)⊕T(n−1,d−1)
  for the SUPPLY fold cell T(n,d)=⊕_{o⊆d}h[n−1−d+o] is FALSE for general {0,1}
  h: with h=(0,0,0,1), n=4, d=2, LHS T(4,2)=1 while RHS=T(3,2)⊕T(3,1)=0.
  Generally T(4,2)⊕T(3,2)⊕T(3,1)=h[3]⊕h[0], not identically 0. Structural:
  the cells read different windows of the same h and the window-start shifts
  prevent the far-end boundary from cancelling.
hypotheses: fold cell definition (problem.md facts 1-2), d in [2,n−1], h any
  {0,1} string of length ≥ n.
holds-here: yes (counterexample on a finite string)
status: checked by hand (explicit Boolean arithmetic); engine undecided
  (finite-Boolean encoding limitation), so NOT independently engine-confirmed.
bearing: kills the literal first-order relation of the proposed approach
  abel-boundary-recurrence; its first-step falsifier fires. The approach's
  deeper "local boundary term" speculation is untouched and must be re-stated
  with a correct indexing relation.
anchor: code/refute/abel_boundary_n4d2.p; this note.
```

```claim
id: substitution-incidence-rules-false
statement: The proposed substitution rules T(2n,2d)=T(n,d), T(2n,2d+1)=0,
  T(2n+1,2d)=T(n,d), T(2n+1,2d+1)=T(n,d) for the fold spacetime are FALSE for
  general {0,1} h. Counterexamples: (i) h=(0,0,0,1), n=2,d=1: T(4,2)=h[1]⊕h[3]
  =1 but T(2,1)=h[0]⊕h[1]=0 (rule T(2n,2d)=T(n,d) fails); (ii) h=(1,0,0),
  n=1,d=0: T(2,1)=h[0]⊕h[1]=1≠0 (rule T(2n,2d+1)=0 fails). Structural:
  Φ^{2d}=(1+σ^2)^d reads even offsets while Φ^d reads consecutive offsets —
  different data of a fixed h; self-similarity would need dyadic periodicity
  (a closed door).
hypotheses: fold cell definition, Φ=1+σ over F2, h any {0,1} string.
holds-here: yes (counterexamples on finite strings)
status: checked by hand; engine undecided (same limitation), NOT engine-confirmed.
bearing: kills the exact substitution rules of proposed approach
  substitution-incidence-perron; its first-step falsifier fires. The approach's
  deeper spectral-gap speculation is untouched.
anchor: code/refute/substitution_incidence_n2d1.p; this note.
```
