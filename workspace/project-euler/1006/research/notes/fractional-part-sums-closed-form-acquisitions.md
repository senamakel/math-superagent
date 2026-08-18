# Fractional-part sums of rotations: explicit continued-fraction closed forms (library acquisitions)

This cycle added three primary treatments to the library for the adopted
Ostrowski route (`pe1006-ostrowski-sawtooth-closed-form`). Each claim below
carries the `answers:`/`bearing` lines and names its full-text source with URL.

```claim
id: brown-shiue-fractional-part-sum-explicit-formula
status: asserted
statement: For irrational α, 0<α<1, and C_α(n)=Σ_{1≤k≤n}({kα}−1/2), an explicit
  closed form for C_α(n) holds in terms of the simple continued fraction of α:
  with m = z_t q_{t−1} + ⋯ + z_1 q_0 the Zeckendorf-type (convergent-denominator)
  expansion, C_α(m) = Σ_{1≤i≤t} (−1)^i (1/2) z_i (1 − |ε_{i−1}|(m_i+m_{i−1}+1));
  and the auxiliary floor-identities ⌊kα⌋=⌊k p_n/q_n⌋ for 1≤k≤q_n and
  ⌊Nα⌋=b p_n+⌊kα⌋ for N=b q_n+k (1≤k<q_n) hold at convergents p_n/q_n.
  (Brown–Shiue, J. Number Theory 50 (1995) 181–192, Theorem 1(c) for the
  explicit formula — verified line-by-line against the full text: the paper's
  form is Σ_j (−1)^j z_j (1/2 − d_{j−1}(m_{j−1} + z_j q_{j−1}/2 + 1/2)), which
  equals Σ_j (−1)^j (1/2) z_j (1 − d_{j−1}(m_j + m_{j−1} + 1)) since
  m_j = m_{j−1} + z_j q_{j−1} — and Lemmas 1 and 3 for the floor identities.
  Theorem 2 is the max bound 1/32·Σ(a_j−1) < max_{0<m<q_t}|C_α(m)| < 1/2·Σ a_j,
  NOT the floor identities; d_{j−1} = |q_{j−1}α − p_{j−1}| is Brown–Shiue's
  closeness measure, equal to Pinner's |ε_{j−1}|.)
hypotheses: α irrational in (0,1); m≥1; q_i the continued-fraction denominators of α.
holds: yes (primary peer-reviewed source, author's open PDF)
source: https://www.sfu.ca/~vjungic/tbrown/tom-27.pdf
anchor: research/sources/brown-shiue-sums-fractional-parts-multiples-irrational.full.md
bearing: Primary citable closed form for sums of fractional parts of multiples of
  an irrational — the engine of the adopted Ostrowski second route (first moment
  of the rotation orbit); the shifted case is Pinner (below).
```

```claim
id: pinner-nonhomogeneous-fractional-part-sum-explicit-formula
status: asserted
statement: For α irrational and γ real, C_m(α,γ)=Σ_{1≤k≤m}({kα+γ}−1/2) has an
  explicit closed form in the Zeckendorf expansion of m and the regular +
  non-homogeneous continued fraction data of γ w.r.t. α (Pinner Theorem 1):
  C_m(α,γ)=Σ_{1≤i≤t} (−1)^i M_i with M_i given explicitly in terms of z_i,
  ε_{i-1}, m_i, m_{i-1}, β_i, u_i and the [?]-integer-part variant; for γ=0 it
  reduces to Brown–Shiue's homogeneous formula. The analogous explicit formula
  for the discrepancy max_{0≤j<m}|C_j(α,γ)| is also given.
  (Pinner, J. Number Theory 65 (1997) 48–73, Theorem 1 and Corollaries.)
hypotheses: α irrational; γ real; m≥1; Zeckendorf expansion in convergent denominators q_i.
holds: yes (primary peer-reviewed source, author's open PostScript)
source: https://www.math.ksu.edu/~pinner/Pubs/frac.ps
anchor: research/sources/pinner-sums-fractional-parts-nα+γ-1997.full.md
bearing: Non-homogeneous (shifted-intercept) version of the fractional-part
  closed form — the k+1 mechanical intercepts x_m=frac(−m·a) generically need
  the γ-shift; completes the Ostrowski route's closed-form engine.
```

```claim
id: ralston-substitution-realisation-rotation-discrepancy
status: asserted
statement: The 1/2-discrepancy sums D_n(x)=Σ_{i=0}^{n−1}(χ_{[0,1/2)}(x+iθ)−χ_{[1/2,1)}(x+iθ))
  of an irrational rotation by θ are realised through a sequence of substitutions
  on the three-symbol alphabet {A,B,C} (A=[0,1/2), B=[1/2,1−θ), C=[1−θ,1)),
  produced by a renormalisation/Gauss-map procedure; the substitution sequence
  is eventually periodic iff θ is quadratic irrational, and for badly
  approximable θ the discrepancy range over i=0..n−1 grows like log n.
  (Ralston, arXiv:1105.5810 — Theorem 1.1 for the substitution realisation;
  Proposition 4.4 for "eventually periodic iff θ is a quadratic surd",
  verified verbatim; Theorem 1.4 for ρ_n(x) ∼ log n when θ is of finite type,
  verified verbatim. The discrepancy D_n(x) is S_n(x) = Σ_{i=0}^{n−1} f(x+iθ),
  f = χ_{[0,1/2)} − χ_{[1/2,1)}; M_n/m_n/ρ_n are its running max/min/range.)
hypotheses: θ irrational; x∈[0,1); f = χ_{[0,1/2)} − χ_{[1/2,1)}; additions mod 1.
holds: yes (arXiv full text)
source: https://ar5iv.labs.arxiv.org/html/1105.5810
anchor: research/sources/ralston-substitutions-1-2-discrepancy-rotations-paper.full.md
bearing: Symbolic-dynamics realisation of rotation-orbit sums; Fibonacci slope
  1/φ² is quadratic irrational so the renormalisation is eventually periodic —
  the structural fact behind an O(log) (periodic-substitution) evaluation of the
  orbit data for PE1006's slope.
```

## What these do NOT give (verified, on the record)

None of the three supplies the decimal-weighted **second** moment Ψ(k) = Σ_m v(x_m)²
with v(x)=Σ_j digit_j(x) 10^{k−1−j}: Brown–Shiue and Pinner give first-moment
fractional-part/floor closed forms, Ralston gives the ±1 indicator sums. The
10^j weighting, the squaring, and the k+1-intercept aggregation remain the run's
own derivation (gap G4). These sources are the closed-form *engine* of the
independent verification route, exactly as the approach note requires.

## Downloads attempted and failed this cycle (recorded)
- Chuan, "α-Words and factors of characteristic sequences", Discrete Math. 177 (1997) 33–50 (doi:10.1016/S0012-365X(96)00355-X): ScienceDirect 403; no open copy found.
- Chuan–Ho, "Factors of characteristic words: Location and decompositions", Theoret. Comput. Sci. 411 (2010) 2827–2846 (doi:10.1016/j.tcs.2010.04.013): ScienceDirect paywalled; no open copy found.
- Berstel–de Luca, "Sturmian words, Lyndon words and trees", Theoret. Comput. Sci. 178 (1997) 171–203 (doi:10.1016/S0304-3975(96)00101-6): no open PDF (MathSciNet/IRIS records only).
- van Ravenstein, "The Three Gap Theorem (Steinhaus Conjecture)", J. Austral. Math. Soc. A 45 (1988) 360–370: open copies are scanned without text layer (anaphoria.com/steinhaus.pdf too large to convert; oeis.org/A000045/a000045_1.pdf no text layer); Mayero's detailed formalisation of van Ravenstein's proof IS held (`research/sources/van-ravenstein-three-gap-theorem-1988-hal.full.md`).
- Ostrowski, "Bemerkungen zur Theorie der Diophantischen Approximationen", Abh. Math. Sem. Univ. Hamburg 1 (1922) 77–98: paywalled (already recorded in `research/summaries/ostrowski-1922-bemerkungen-dio-approx.md`); Brown–Shiue 1995 gives its content in modern explicit form.
- The first Pinner download attempt (`JoeSums.pdf`) misfiled a character-sums paper (Pigno–Pinner–Sheppard); overwritten by the correct `frac.ps`. No residual wrong content remains under the Pinner name.

## Attribution correction (verified against held sources)

Recalled durable memory (from `research/approaches/pe1006-ostrowski-sawtooth-closed-form.md`)
stated that the shifted fractional-part paper "On Sums of Fractional Parts
{nα+γ}" is "also Brown & Shiue, JNT 1997". The held primary sources contradict
that: the author of J. Number Theory 65 (1997) 48–73, "On sums of fractional
parts {nα+b}", is **Christopher Pinner** — his own publication page
(`research/sources/pinner-publications-page.full.md`, item 4) and the first
page of the PS file (`research/sources/pinner-sums-fractional-parts-nα+γ-1997.full.md`,
"Christopher Pinner") both confirm it, and the paper itself credits Brown–Shiue
[3] as the homogeneous (γ=0) predecessor. The memory's formula content is
correct (Pinner's Theorem 1 IS the shifted C_m(α,γ) closed form, and it reduces
to Brown–Shiue Theorem 1(c) at γ=0); only the author attribution was wrong.
Use Pinner's name in any citation.
