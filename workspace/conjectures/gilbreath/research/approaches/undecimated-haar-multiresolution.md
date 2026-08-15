# Undecimated Haar multiresolution

```approach
idea: The Gilbreath operator is the two-tap high-pass filter (1,−1) with an
absolute value and no decimation — the non-decimated (stationary) Haar
wavelet transform, iterated. The conjecture is the statement that the leading
detail coefficient of this wavelet pyramid is uniformly ≤ 2: a discrete
regularity statement, to be attacked with multiresolution analysis (Mallat's
coefficient-decay characterization) and the flat zones of mathematical
morphology.

mechanism: A_{k+1}(i) = |A_k(i) − A_k(i+1)| is exactly one level of the
undecimated Haar high-pass applied to the row, with no downsampling, so the
triangle IS a (redundant) wavelet transform of the gap sequence — a change of
representation, which is precisely the kind of move this problem has not yet
been given. The {0,2} block is the *flat zone*: the leading region where the
detail coefficient is ≤ 2, i.e. where the halved row is 1-Lipschitz (the
run's own established block characterization). The parity (mod 2) triangle is
the Pascal/Sierpinski structure — the standard 2-adic wavelet-packet picture —
and the mod-4 level is the known Odlyzko linearization. The conjecture says
the leftmost detail coefficient never exceeds 2 at any scale, i.e. the gap
sequence is uniformly regular at the left boundary at every scale. This is a
harmonic-analytic reframing, distinct from the refuted
walsh-hadamard-spectral-edge-stall route (which only diagonalized Rule 90
over GF(2) and bounded the max zero-run, a quantity shown to be insufficient)
and from every scalar-potential failure: regularity is read off the pyramid of
detail coefficients, not off a single functional. Honesty note: Mallat's
decay characterization is stated for a *dyadic* multiresolution; the
Gilbreath pyramid is the *stationary* (non-dyadic) variant, so Mallat is a
guide, not a literal theorem whose hypotheses are met — the first step must
pin down which named regularity result does transfer.

status: refuted
precedent: The representation claim is real and precisely named (the
  candidate's invented half is the REGULARITY-THEOREM-BITES claim, which has
  no precedent — searches for "wavelet Gilbreath", "Haar flat zone difference
  operator", "undecimated wavelet regularity conjecture primes" returned the
  general wavelet/morphology literature and NOTHING applied to Gilbreath or to
  iterated absolute-difference squares; honest could-not-find on the
  application):
  - Non-decimated / stationary Haar wavelet (a `trous` algorithm, stationary
    wavelet transform, SWT): the iterated two-tap difference with no
    downsampling is genuinely this object. Real, well-documented.
  - Mallat's coefficient-decay / regularity characterization: "A theory for
    multiresolution signal decomposition" (IEEE Trans. PAMI 11 (1989)
    674–693, https://doi.org/10.1109/34.192463) and "Multiresolution
    approximations and wavelet orthonormal bases of L²(ℝ)" (Trans. AMS 315
    (1989) 69–87, https://doi.org/10.1090/S0002-9947-1989-1008470-5):
    regularity of f (Sobolev H^s / Hölder / Lipschitz) is characterized by the
    decay of wavelet coefficients — for f ∈ H^s iff Σ_j 2^{2sj} |d_{j,k}|²
    < ∞ (dyadic, orthonormal basis); Hölder-α at a point iff
    |d_{j,k}| ≤ C 2^{−j(α+1/2)} (up to the standard two-microlocal
    refinements; Jaffard, C. R. Acad. Sci. Paris 339 (2004)). Bounded (α=0)
    coefficients ⟺ bounded function.
  - Morphological / flat-zone and undecimated morphological wavelets:
    Heijmans–Goutsias "Multiresolution signal decomposition schemes. Part 2:
    Morphological wavelets" (CWI report 1999; morphological Haar wavelet),
    and the morphological undecimated wavelet (MUDW) literature (IEEE TCAS-I
    53 (2006) 1582–1594, https://doi.org/10.1109/tcsi.2006.875172). "Flat
    zone" is a real morphological concept (maximal connected regions of
    constant value; the flat-zone segmentation approach, Signal Processing
    1997). Morphological opening/closing are IDEMPOTENT filters — but no
    morphological theorem bounds a detail coefficient; flat-zone idempotence
  is about filter iteration.
killed-by: The representation is a genuine renaming, but the load-bearing
  claim — that a NAMED regularity theorem forces the leftmost detail
  coefficient small — fails, because the theorem is a DICTIONARY, not a
  constraint, and here it runs out:
  (1) Mallat's characterization is an equivalence: bounded detail coefficients
  ⟺ bounded function (α=0 / H^0), decay ⟺ higher regularity. It never bounds
  a coefficient from an UNKNOWN regularity; it reads regularity OFF the
  coefficients. The "function" whose left-edge detail we seek to bound is the
  gap/iterate object, and whether its left-edge detail is ≤ 2 at every scale
  IS the conjecture. So Mallat supplies no input — it maps the conjecture to
  itself. No independent regularity hypothesis on the prime gap sequence that
  would imply A_k(1) ≤ 2 is known or supplied by the representation (gaps are
  unbounded, so no global smoothness holds; the whole question is whether the
  left-edge detail is tame).
  (2) The candidate's own honesty note is decisive and verified: Mallat's
  decay characterization is a DYADIC orthonormal multiresolution theorem; the
  Gilbreath pyramid is the STATIONARY (non-dyadic) variant, so Mallat's
  hypothesis (orthonormal dyadic basis) does not hold and the theorem does not
  transfer. There is no named stationary-wavelet regularity theorem that
  reproduces Mallat's equivalence for this pyramid.
  (3) The best the representation can recover is the mod-2 / Rule-90 / Pascal
  structure (the parity pyramid), which the run has already PROVED as
  `rule90-interior-xor`, and the mod-4 linearization, whose ceiling the run
  has PROVED (`mod4-pascal-invariant`: mod 8 fails, so no exact {0,2} value
  bound past mod 4). So the wavelet dictionary re-derives closed ground and
  cannot add the integer-level exact bound the conjecture needs.
  What survives: "the triangle is the iterated non-decimated Haar high-pass"
  is a correct and genuinely-named representation (a change of labelling, not
  of content), and "the {0,2} block is the leading flat zone" is the run's own
  block characterization restated. Both are already recorded under
  `rule90-interior-xor` / `lipschitz-excess-lyapunov`. The representation does
  not supply a constraint.
first-step: (superseded — see killed-by) Encode the depth-1000 rows as the
  undecimated detail pyramid and verify the identities (detail coefficient at
  scale k, position i equals A_k(i); the flat zone equals the block) — these
  hold by definition and are the run's own block characterization. Do not
  chase a regularity theorem: killed-by (1)(2) says no named theorem's
  hypothesis is met that would bound the left-most detail.
```
