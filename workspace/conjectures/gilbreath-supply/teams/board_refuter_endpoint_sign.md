# REFUTER REPORT — supply-averaged-second-moment / endpoint-parity (recorded)

## What I attacked, and the verdicts

I ran the refutation pass over the *checkable* committed statements — the
pure-Boolean structural pieces a refuter can actually break — and separately
the arithmetic gaps, which are the real open problem. Bottom line: **no new
refutation**, because every small structural statement is already closed or
documented. The genuinely live gaps are arithmetic and not falsifiable at small
size.

**1. Spurious sign — FALSE, but already documented.** The character-sum form of
G-endpoint-comparison-density (prose in `supply-from-endpoint-parity.md` and
`BACKWARD.md`):

    (-1)^{T(n,d)} = (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})

is **false as written**, by a hand proof at d=3 (single run [0,3]):
T = h0^h1^h2^h3 telescopes to r0^r4 (each h[j]=r_j^r_{j+1}, interior cancels),
so (-1)^T = chi(r0)chi(r4), and the extra (-1)^1 = -1 makes the equation
(-1)^T = -(-1)^T, impossible since the value is ±1. **False for every string.**
Corrected identity (no sign) is verified on 6868 (n,d) pairs. **Already banked**
in the refuted approach `dyadic-gap-character-correlation` and board-posted
("Two sign/identity corrections"); the only stale part is the prose still in
the two live skeleton files — update them so no reader recomputes the wrong
product. Nothing downstream depends on the factor (density #{T=1} unaffected).

**2. G-run-telescope — TRUE, exhaustive.** Run decomposition (2^{popcount-g}
runs of length 2^g, blocks [m·2^g, (m+1)·2^g-1]) and telescoping verified on
disk over d=0..2^14 + 51M (d,pos) pairs. I re-derived the count by hand; matches.

**3. R-random-pointwise — already CLOSED.** wt(Phi_n h) >= n/4 w.p.
1-exp(-Omega(n)) for uniform h is a proved corollary of the exact-binomial
(rank n-2, surjective, Chernoff), claim `r-random-pointwise-closed-by-exact-binomial`.
The WEAKENED.md "open" marker is stale. Small-n constant failure is the
binomial's lower tail, not a disproof.

**4. Sparse-strictness rivals — settled.** General sparse=>sublinear transfer
refuted (h=e_{n-1}, single 1, wt=n-2); every fixed sparse string has liminf 0.
Documented in `code/out/sparse_fold_capture.settles.md`.

## Tool limitation to share

`find_counterexample` returns **undecided on finite-propositional problems whose
axioms already decide all boolean atoms** (h from r, T from h, T<=>mismatch).
It only exhibits a countermodel when free boolean variables remain (as in the
n4/n5 random-pointwise checks). So the boolean model-finder is not an instrument
for these telescoping sign identities — the hand proof is (and for 5-visible
booleans is decisive). Worth knowing before the next attempt encodes a
submask-XOR / ancestor-sum relation that way.

## What is genuinely live (not breakable at small size)

All honest-so-far gaps are arithmetic: the second-moment/variance bound on the
prime string, the submask-window autocorrelation, positive switch density, and
the dyadic-gap correlation of the quadratic character. These ARE the open
problem and are the correct target for the prover side, not for a small-model
refuter.

## Deliverable for the run

A cleanup, if wanted: (a) strip `(-1)^{#runs}` from the two skeleton files'
prose; (b) merge the closed `R-random-pointwise` rung so it stops being
re-attacked. Both are bookkeeping; neither changes the math's status.
