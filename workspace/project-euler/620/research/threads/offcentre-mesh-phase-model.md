---
thread:
  question: >
    Which crossings of the monotone residue function correspond to physically
    valid arrangements, so that g(c,s,p,q) counts PE620's perfectly-meshing
    arrangements and fast_g stops overcounting G(20) by 8?
  status: near-resolved — the overcount is a lattice-class error in fast_g's
    crossing rule, not a sign, monotonicity, or endpoint-admissibility problem
  rests-on:
    - n_integer_model_validated        # grid model: all three oracle values, per-tuple G(20)=205
    - fast_g_lattice_mismatch          # integer f-levels are the wrong lattice for odd c+s
    - g20_overcount_by_eight           # checked symptom: G(20)=213 vs 205
    - tangency_enum_oracle_match       # historical sign pinning; see anchor caveat below
  blocked-by: []
  next:
    - TASKS step 1: run fast_g per tuple over G(20); confirm the differing
      tuples are exactly the odd-(c+s) ones, each by ±1, net +8
    - Patch g_fast: count integer levels of n_p = 2*Q_p, i.e.
      g = ceil(n_p(DU)) - floor(n_p(DL)) - 1 (or f-levels in the class
      f ≡ -(c+s)/2 mod 1); the strict endpoint treatment stays
    - Re-validate G(16)=9, G(20)=205 per tuple, then compute G(500)
---

# Off-centre mesh phase model — the overcount is a lattice-class error

## State of the count

The residue form is settled and validated: the grid model
`n_t(d) = [(c-t)·β(d) + (s+t)·μ(d)]/π` with β, μ the angles of the planet
centre about the ring centre O and sun centre S (upper tangency point),
valid iff `n_p ∈ ℤ` (then `n_q = c+s-n_p ∈ ℤ` automatically by the identity
`n_p + n_q = c+s`, and `n_p - n_q ≡ p-q (mod 2)` automatically because
`c = s+p+q`). `n_p` is strictly increasing on `(DL, DU)` (checked per tuple).
This reproduces all three oracle values **per tuple**: g(16,5,5,6)=9,
G(16)=9, G(20)=205 (`code/out/n_integer_model.txt`).

`fast_g.py` (monotone crossing, no grid) reproduces g=9 and G(16)=9 but
G(20)=213 (+8). The cause is not admissibility, endpoints, or planet
coincidence — it is a lattice-class error (claim `fast_g_lattice_mismatch`
below): fast_g counts *integer* levels of `f = Q_p - Q_q`, which equals
`n_p - (c+s)/2`. Integer f-levels are integer n_p-levels only when c+s is
even; when c+s is odd they are *half-integer* n_p levels — configurations the
validated model rejects. 13 of the 22 G(20) tuples have c+s odd; ±1 per such
tuple, net +8. The flagship (16,5,5,6) has c+s = 21 (odd) and still gives 9
by endpoint alignment — which is why the bug survived the g/G(16) checks.

**The fix**: in `g_fast()`, count integer levels of `n_p = 2*Q_p` instead of
integer levels of f:

    g = #{k ∈ ℤ : n_p(DL) < k < n_p(DU)} = ceil(n_p(DU)) - floor(n_p(DL)) - 1

equivalently count f-levels in the arithmetic class `f ≡ -(c+s)/2 (mod 1)`.
Worked on the flagship: n_p(DL) = 0 (degenerate endpoint, excluded), n_p(DU)
≈ 9.038 → k ∈ {1..9} = 9 ✓. Monotonicity and bounds stay as they are.
Empirical confirmation (the differing tuples are exactly the 13 odd-c+s ones)
is TASKS step 1; the net should be +8 before the patch and 0 after.

## A second checked fact: the two "winning" models disagree on configurations

The tangency enumeration and the n_integer model both return 9 for the
flagship but at **disjoint d-sets** (claim `tangency_enum_d_mismatch`).
The residue conditions are algebraically different:
`Q1_t = [(c-t)β_t + (t-s)γ_t]/2π` (tangency_enum, mod-1 equality across the
four planets) versus `n_t/2 = [(c-t)β_t + (s+t)γ_t]/2π` (n_integer, both n_t
integral); the two differ by the d-dependent, in general non-integer term
`2s·γ_t/2π = s·γ_t/π`. So the models count different arrangements, and only
n_integer has passed the per-tuple G(20) test (205). Do NOT generalise
tangency_enum to G(20) (the librarian session report's suggestion predates
n_integer's 205 success): n_integer is the per-tuple oracle; tangency_enum's
role is historical (it first pinned the (−1,−1) sign family).

## Caveat on the sign-pinning claim itself

`tangency_enum_oracle_match` reports an 8-variant sign scan in which only
(σ,η,θ)=(−1,−1,−1) gives 9 and (+1,+1,+1) *also* gives 9. The anchor output
`code/out/tangency_enum.txt` contains only **4** variants (σ,η rows with θ
evidently fixed): (−1,−1):9, (−1,+1):7, (+1,−1):10, (+1,+1):6. The
single-theta-axis exclusivity statement and the (+1,+1,+1)=9 row are not
reproducible from the anchor (the on-disk run predates the 8-variant code).
Core facts that ARE in the anchor: (−1,−1)→9; the 9 d-values; the UU/LL-only
structure; Q(L) = −Q(U) mod 1 exactly. Re-run the 8-variant scan before
quoting the exclusivity sentence. The n_integer validation does not depend on
it.

## Sources that do not help (already read; do not re-read for the count)

- Coaxial least-mesh-angle / assembly-divisibility sources — Guo 5.21–5.25,
  UTS 1162/1165, Drivetrain Hub, Gear Solutions, Zou 2015, Sun 2017,
  Wikipedia/TEC-science epicyclic: correct for coaxial trains; the off-centre
  case is explicitly different (Kurasov eq. 1 is the coaxial baseline only).
- Dynamics/whine papers — White & Patil main body, Frontiers 2026 three-gear,
  ISMA 2016, Parker–Lin 2004 (paywalled): phase *formalism* corroboration
  only; no counting statement beyond what Zhao–Li and Segade-Robleda give.
- Inversion/limiting-point, Steiner chain, Pappus chain, Apollonius/ellipse
  geometry: establish the ellipse locus of planet centres and the negative
  fact that inversion does not preserve tooth mesh; not the count.
- Simionescu 1998: abstract only (paywalled); Xue 2020: abstract only
  (JS-rendered pages, DOAJ 403).

## Source-level basis of the winning congruence (all on disk, verified)

Kurasov 2020 (MATEC 329:03027) full text: off-centre GES assembly condition
is a **system of per-satellite-pair signed (angle × tooth-count) congruences
equated to integers** (eqs. 6–8 verbatim in the PDF; eq. 7/8 glyphs
OCR-garbled but the structure and integer-K parameters are clear), plus a
separate vector-loop diameter/location closure (eqs. 9–14); the coaxial rule
(Z1+Z3)/k = C (eq. 1) is stated as the coaxial baseline only. Zhao–Li 2018
eq. 39: internal-mesh ring terms negative in the signed sum — matches the
oracle-pinned sign. Segade-Robleda 2012 eq. (1): pitch-difference whole-number
condition, same shape. Monagan (trig polynomials): the exact
root-count machinery for the closed form's endpoint floors (unit-circle
substitution z = e^{iβ_p} → degree-(c+s) polynomial, approach
`arc-closure-cs-polynomial`).

```claim
id: n_integer_model_validated
statement: The grid model n_t(d) = [(c-t)*beta(d) + (s+t)*mu(d)]/pi, valid iff n_p(d) in Z with n_q = c+s-n_p automatic (identity n_p+n_q = c+s) and the parity condition automatic because c = s+p+q, reproduces g(16,5,5,6)=9, G(16)=9, and per-tuple G(20)=205 (all 22 rows, sum 205). n_p is strictly increasing on (DL,DU) and takes consecutive integer values; degenerate endpoints (y ~ 0) are excluded.
hypotheses: planet centre at the upper tangency point of the two-circle intersection; beta, mu measured about ring centre and sun centre; DL = max_t|a_t-b_t|, DU = min_t(a_t+b_t, R-r-1).
holds-here: yes — this is the run's own validated computation (checked against all three oracle values, including the per-tuple G(20) table)
status: checked
bearing: the per-tuple oracle for every future g/G value; the counting rule the closed form must reproduce
anchor: code/out/n_integer_model.txt; code/pattern/n_integer_count.py
source: this-run-computation
```

```claim
id: fast_g_lattice_mismatch
statement: fast_g counts integer levels of f(d) = Q_p(d) - Q_q(d) with Q_t = [(c-t)*beta_t + (s+t)*gamma_t]/(2*pi) turns; since n_t = 2*Q_t and n_p + n_q = c+s, f = n_p - (c+s)/2. Integer f-levels are integer n_p-levels when c+s is even, but HALF-INTEGER n_p-levels (configurations the validated model rejects) when c+s is odd. Hence fast_g systematically counts the wrong lattice for the
13 odd-(c+s) tuples of G(20) (exactly the opposite-parity (p,q) tuples), and
the observed net overcount is +8 (per-tuple magnitudes/signs are the TASKS
step-1 diagnostic). g(16,5,5,6), c+s=21 odd, agrees by endpoint alignment. The corrected rule is g = ceil(n_p(DU)) - floor(n_p(DL)) - 1, i.e. count integer levels of n_p = 2*Q_p.
hypotheses: n_p monotone increasing on (DL,DU) (checked per tuple); integer n_p levels are the validated arrangement condition; fast_g's Q_t, DL, DU identical to n_integer's.
holds-here: yes — pure algebra from the two programs' own formulas on disk; verified arithmetically on (16,5,5,6) and (20,5,5,10)
status: checked (rule equivalence); the empirical prediction (which tuples differ, net +8→0 after patch) is TASKS step 1, not yet run
bearing: the exact patch for fast_g; unblocks the bound-independent G(500) route
anchor: code/pattern/fast_g.py; code/pattern/n_integer_count.py
answers: offcentre-mesh-phase-model (admissibility rule found)
source: this-run-computation
```

```claim
id: tangency_enum_d_mismatch
statement: On (16,5,5,6) the tangency enumeration (winning variant) and the n_integer model both count 9 valid d but at disjoint d-sets: tangency_enum {0.15960, 0.16326, 0.17100, 0.18385, 0.20371, 0.23430, 0.28322, 0.36863, 0.54658} vs n_integer {0.16096, 0.16657, 0.17670, 0.19273, 0.21733, 0.25572, 0.31940, 0.43890, 0.73162}. The residue conditions differ algebraically (their Q's differ by the d-dependent term s*gamma_t/pi), so at most one model is the problem's arrangement condition; only n_integer passes per-tuple G(20)=205.
hypotheses: both outputs are from the runs of record; identical c,s,p,q and d parameterisation.
holds-here: yes
status: checked (direct comparison of code/out/tangency_enum.txt and code/out/n_integer_model.txt)
bearing: do not generalise tangency_enum to G(20); n_integer is the per-tuple oracle
anchor: code/out/tangency_enum.txt; code/out/n_integer_model.txt
contradicts: tangency_enum_oracle_match
source: this-run-computation
```

```claim
id: tangency_claim_anchor_gap
statement: The note code/out/tangency_enum_claim.md reports an 8-variant sign scan where only (sigma,eta,theta)=(-1,-1,-1) gives 9 and (+1,+1,+1) also gives 9; its anchor code/out/tangency_enum.txt contains only 4 variants (sigma,eta rows, theta evidently fixed): (-1,-1):9, (-1,+1):7, (+1,-1):10, (+1,+1):6. The theta-axis exclusivity statement and the (+1,+1,+1)=9 row are not reproducible from the anchor output on disk.
hypotheses: the anchor .txt is the run of record for that note.
holds-here: yes
status: checked (file comparison)
bearing: re-run the 8-variant scan before quoting the 'only (-1,-1,-1)' exclusivity; the core facts ((-1,-1)->9, the 9 d-values, UU/LL-only, mirror identity) are in the anchor
anchor: code/out/tangency_enum.txt
contradicts: tangency_enum_oracle_match
source: this-run-computation
```