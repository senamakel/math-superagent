```approach
idea: The k+1 DISTINCT length-k Fibonacci factors are exactly the k+1 CONTIGUOUS
windows at positions r = F_n - k - 1 .. F_n - 1 of the doubled standard word
q_n q_n (any n with F_n > k) — no dedup, no multi-intercept sum. Then
Psi(k) = (full cyclic sum over all F_n windows) - (sum over the first
F_n - k - 1 windows), where the full cyclic sum collapses via the cyclic
autocorrelation A of q_n (Toeplitz form, valid for ANY k < F_n) and the
correction is a PREFIX partial sum of v_r^2 that is collapsed by a
Fibonacci-block-renormalised transfer matrix. Named mathematics: standard-word
conjugate/contiguous-window position structure + cyclic-autocorrelation
(Toeplitz) second moment + constant-size sliding-window transfer matrix with
fast Sturmian/continued-fraction block product.

mechanism: The window value obeys the sliding-window step
v_{r+1} = 10*v_r - y_r*10^k + y_{r+k}, where y is the Fibonacci digit sequence
and y_r*y_{r+k} is a pair that varies Sturmianly with r (three-gap structure of
k*alpha). So the state (v, sum v, sum v^2, 1) is advanced by a constant-size
affine transfer matrix whose step depends only on the pair (y_r, y_{r+k}), giving
the prefix partial sum by a product over ~10^18 consecutive steps. Because that
pair sequence is itself Sturmian/automatic in r, the product can be collapsed in
O(log) by the continued-fraction fast-multiplication trick (same machinery that
exponentiates the substitution matrix), exactly the ~87-block renormalisation at
10^18. The full cyclic sum is a known closed Toeplitz object, so the whole of
Psi(k) is One prefix matrix product + one Toeplitz sum — a concrete combinatorial
object independent of the adopted floor-sum monoid.

status: refuted
killed-by: Two of the three load-bearing pieces are grounded, but the decisive
one — an O(log) collapse of the base-10 sliding-window matrix product independent
of the committed floor-sum monoid — has no literature precedent and, on
inspection, closes back onto the same primitive. (a) FACTOR-SET-AS-WINDOWS is
grounded as a set identity: Sivasankar & Rama (arXiv:2204.13977, Thm 7, in the
rabbit 1<->0-complement convention of PE1006's S, count k+1 invariant) gives the
length-k factors as contiguous windows at first-occurrence positions; the run's
own claim sivasankar-rama-position-theorem and the conjugate-Christoffel /
standard-word constituent claims (bugeaud-reutenauer;
richomme-saari-zamboni) support the set. But the SPECIFIC positions "r =
F_n-k-1..F_n-1 of q_n q_n" are NOT a verbatim literature statement — they are
solver-verification against mech_psi/brute, exactly as the steer and
research/notes/librarian-steering-contiguous-window.md already record. (b)
TOEPLITZ CYCLIC SUM is grounded but is the SAME A(d) second moment the adopted
universal-Euclidean route already evaluates — it buys no new mechanism and no
independence; the run's phase4-anchors-invalid claim already shows the Toeplitz
object is the out-of-domain collapse. (c) O(log) SLIDING-WINDOW TRANSFER-MATRIX
PRODUCT over the Sturmian pair orbit: no source applies a base-10 exponent
sliding-window transfer matrix to a sum of Fibonacci-factor decimal values. The
closest literature is the spectral-theory trace map for Sturmian/Fibonacci
Schrodinger operators (Damanik–Gorodetski–Yessen, Invent. Math. 2016,
arXiv:1604.07768; Mei–Yessen, arXiv:1312.2259, Fibonacci three-term transfer
matrices; Wang–Grimm–Schreiber antitrace maps) — but those are 2x2 unimodular
transfer matrices whose trace obeys a Fibonacci recursion; they do NOT carry the
base-10 affine state (v, sum v, sum v^2, 1) and do not give O(log) for it. The
claimed "~87-block renormalisation at 10^18" of a base-10 affine product has no
source and is not a named combinatorial object. So the ONE distinct contribution
this candidate could make (an independent O(log) evaluation not resting on the
floor-sum monoid) is unsupported; the parts that are grounded close back onto
machinery the run already holds. Not independent, not a distinct O(log) method.
precedent: set identity — Sivasankar & Rama, "Two-dimensional Fibonacci Words:
Tandem repeats and factor complexity", arXiv:2204.13977 Thm 7 (claim
sivasankar-rama-position-theorem at research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md);
conjugate-Christoffel claim conjugate-christoffel-factor-sturmian
(research/summaries/bugeaud-reutenauer-conjugates-christoffel.md);
standard-word factors claim fibonacci-standard-factors-l0l1. Toeplitz cyclic
sum — run's own directive-1 A(d) claim (three-gap-three-distance-autocorrelation),
refuted as general-k Ψ by phase4-anchors-invalid. O(log) collapse — NO source;
closest are spectral trace maps (Damanik–Gorodetski–Yessen arXiv:1604.07768;
Mei–Yessen arXiv:1312.2259; Wang–Grimm–Schreiber PRB 62 (2000) 14020), which are
not this object. Run's own steer: research/notes/librarian-steering-contiguous-window.md.
first-step: If revisited, restrict to what is grounded: use the Sivasankar-Rama
position-set to confirm Claim 1's set identity for k<=400 against
code/mech/mech_psi.py (already effectively done in the steer). But do NOT claim
independence or O(log) — the Toeplitz cyclic sum and any maximally-compressed
window product both return to the committed floor-sum primitive. Read the closed
reasons before proposing again.
```

## Precedent pass (against the literature)

This candidate is a genuine representation-change only on its surface; the
literature splits it into pieces that are either already-held (set identity,
Toeplitz cyclic sum) or unsupported (the independent O(log) collapse).

### What is grounded
- **Factor set = contiguous windows.** Sivasankar & Rama (arXiv:2204.13977,
  Thm 7; also arXiv:2207.04304 for enumeration/location in the 1D/2D fixed
  point) give the k+1 distinct length-k factors of the Fibonacci word as
  contiguous windows at first-occurrence positions. Convention caveat: their
  word is the rabbit word, the 1<->0 complement of PE1006's S; the count k+1 is
  invariant, the explicit list needs complementing. This supports the set half
  of Claim 1 but **not verbatim** the specific q_n q_n window positions
  (librarian-steering-contiguous-window.md and scholar-digest-ueuclid-api-and-
  position-anchor.md already state this honestly).
- **Toeplitz cyclic sum.** The full cyclic autocorrelation second moment over
  the standard word's rotations is Claim 3 / directive-1 A(d) — a real object,
  but it is precisely the object the run's `phase4-anchors-invalid` says fails
  at general k for Ψ, and the correction (prefix partial sum) is what the
  committed universal-Euclidean route already computes. No new mechanism.

### What is NOT grounded (the decisive gap)
- **O(log) collapse of the base-10 sliding-window transfer product.** The
  mechanism claims the pair (y_r, y_{r+k}) orbit is Sturmian and hence the
  affine product over ~10^18 windows collapses by continued-fraction block
  multiplication. No held source and no located paper does this for base-10
  exponent values of Fibonacci factors. The nearest literature — the Fi
  transfer / trace-map formalism for Sturmian Schrodinger operators
  (Damanik–Gorodetski–Yessen, Invent. Math. 206 (2016) 629, arXiv:1604.07768;
  Mei–Yessen arXiv:1312.2259; Wang–Grimm–Schreiber PRB 62 (2000) 14020) —
  treats 2x2 unimodular matrices whose traces follow the Fibonacci recurrence,
  not the 4-dimensional affine state (v, Σv, Σv², 1) with base-10 weights. The
  trace-map theory does not validate, and nobody has shown, the claimed
  ~87-block renormalisation at 10^18 for this object.

### Verdict
Refuted **as an independent/O(log) method**: its one distinct contribution (a
second, non-floor-sum O(log) evaluation) has no literature backing, and every
grounded component closes back onto machinery the run already holds (the
Toeplitz cyclic-autocorrelation second moment and the floor-sum primitive). The
set-identity claim remains useful as a *verification* check, not as a route.
