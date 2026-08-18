# Scholar digest — library cycle 2026-08-19 (fractional-part closed forms verified)

Stored on disk because the Cognee memory server intermittently drops writes
(first two `remember_memory` calls this cycle succeeded; the next two were
accepted-but-dropped with a health-report timeout). Retry `remember_memory`
when the server recovers; the on-disk library is the authority meanwhile.

## What this cycle established (all verified against full texts)

### 1. Brown–Shiue 1995 — explicit CF closed form for C_α(n) (verified line-by-line)

- Source: `research/sources/brown-shiue-sums-fractional-parts-multiples-irrational.full.md`
  (https://www.sfu.ca/~vjungic/tbrown/tom-27.pdf), JNT 50 (1995) 181–192.
- Theorem 1(c): for m = z_t q_{t−1} + ⋯ + z_1 q_0 (Zeckendorf representation in
  CF denominators), C_α(m) = Σ_{j=1..t} (−1)^j z_j (1/2 − d_{j−1}(m_{j−1} +
  z_j q_{j−1}/2 + 1/2)), m_j = Σ_{i≤j} z_i q_{i−1}. This equals the claim
  block's form Σ (−1)^j (1/2) z_j (1 − d_{j−1}(m_j + m_{j−1} + 1)) because
  m_j = m_{j−1} + z_j q_{j−1}. **The claim block transcription is exact.**
- d_n := |q_n α − p_n| (their closeness measure) = Pinner's |ε_n|.
- The floor identities are **Lemmas 1 and 3** (NOT Theorem 2): Lemma 1
  ⌊kα⌋=⌊k p_n/q_n⌋ for 1≤k≤q_n; Lemma 3 ⌊Nα⌋=b p_n+⌊kα⌋ for N=b q_n+k,
  1≤k<q_n. Theorem 2 is the max bound 1/32·Σ(a_j−1) < max_{0<m<q_t}|C_α(m)|
  < 1/2·Σ a_j.
- Lemma 2: S_α(q_n) = Σ_{k≤q_n}⌊kα⌋ = (p_n q_n − q_n + p_n + (−1)^n)/2;
  C_α(q_n) = (1/2)(−1)^n(d_n(q_n+1) − 1).
- The claim block in `research/notes/fractional-part-sums-closed-form-acquisitions.md`
  has been corrected to cite Theorem 1(c) + Lemmas 1,3 with this verification.
- Bearing: first-moment closed-form engine of the adopted Ostrowski second
  route (independent verification of the same Ψ(k)).

### 2. Pinner 1997 — non-homogeneous C_m(α,γ) closed form (verified)

- Source: `research/sources/pinner-sums-fractional-parts-nα+γ-1997.full.md`
  (https://www.math.ksu.edu/~pinner/Pubs/frac.ps), JNT 65 (1997) 48–73.
- Theorem 1: C_m(α,γ) = Σ_{1≤i≤t} (−1)^i M_i with
  M_i = −(1/2) z_i |ε_{i−1}| (m_i + m_{i−1} + 1) + (β_i − 1/2) z_i
        + ⌈^?((z_i − (u_i − m_{i−1}))/q_{i−1}),
  where ε_i := q_i α − p_i, β_n (eq 3), u_n (eq 4), non-homogeneous CF c_i/γ_i
  (eqs 5–6), [x]^? = [x] if x∉Z, x−1 if x∈Z (eq 8).
- For γ=0 reduces to Brown–Shiue Theorem 1(c) — equation (9) verbatim.
- Corollary 1: |C_m(α,γ)| ≤ (3/2) Σ z_i.
- Caveat: the full text is a raw PS→text dump; re-read clean equations from the
  original PS before verbatim quotation.
- Bearing: shifted-intercept closed form the k+1 mechanical intercepts
  x_m = frac(−m·a) generically require.

### 3. Ralston arXiv:1105.5810 — substitution realisation of rotation discrepancy (verified)

- Source: `research/sources/ralston-substitutions-1-2-discrepancy-rotations-paper.full.md`
  (https://ar5iv.labs.arxiv.org/html/1105.5810).
- Theorem 1.1: orbit coding of f(x+iθ), f=χ_{[0,1/2)}−χ_{[1/2,1)}, realised by
  words ω_i and substitutions σ_i on {A,B,C} (A=[0,1/2), B=[1/2,1−θ),
  C=[1−θ,1)), θ<1/2, via a Gauss-map renormalisation; ω_0 σ_0(ω_1 σ_1(...))
  encodes the orbit up to at most two errors.
- Proposition 4.4 (verbatim): σ_n eventually periodic iff θ is a quadratic surd.
- Theorem 1.4 (verbatim): θ of finite type ⇒ ρ_n(x) = M_n(x)−m_n(x)+1 ∼ log n
  for all x; Corollary 1.5: |S_n(x)| ∉ o(log n).
- PE1006's slope 1/φ² is a quadratic surd (partial quotients all 1) ⇒ the
  renormalisation is eventually periodic — the structural fact behind an
  O(log)-coefficient (periodic-substitution) evaluation of the orbit data.
- Bearing: symbolic-dynamics complement to the arithmetic closed forms.

## Attribution contradiction (the most valuable finding this cycle)

Recalled durable memory (from `research/approaches/pe1006-ostrowski-sawtooth-closed-form.md`)
attributed "On Sums of Fractional Parts {nα+γ}", JNT 65 (1997) 48–73, to
"also Brown & Shiue, JNT 1997". The held primary sources contradict this: the
author is **Christopher Pinner** — his own publication page
(`research/sources/pinner-publications-page.full.md`, item 4) and the PS first
page ("Christopher Pinner") both confirm, and the paper credits Brown–Shiue [3]
as the homogeneous predecessor. The memory's formula content is correct; only
the author attribution was wrong. Recorded in
`research/notes/fractional-part-sums-closed-form-acquisitions.md` under
"Attribution correction".

## What the three do NOT give (unchanged)

None supplies Ψ(k): no 10^j decimal weight, no squaring, no k+1-intercept
aggregation. Gap G4 (fixed-dimensional O(log) joint-intercept evaluation)
remains the open goal. These sources arm its independent verification leg only.

## Status

No PE1006 answer value computed or claimed. The committed universal-Euclidean
monoid is untouched by this cycle.
