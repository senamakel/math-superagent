# Macintyre — "On the zeros of successive derivatives of integral functions" (Trans. AMS 67 (1949) 241–251)

Full text held at `research/sources/macintyre1949_zeros-successive-derivatives.full.md`.
Source URL: https://www.ams.org/journals/tran/1949-067-01/S0002-9947-1949-0032743-0/S0002-9947-1949-0032743-0.pdf

## What the paper establishes

This is the classical Gontcharoff-polynomial / Whittaker-constant paper. The Gontcharoff polynomials are defined iteratively as

G_0(z) = 1;  G_n(z; z_1, …, z_n) = ∫_{z_1}^z dz' ∫_{z_2}^{z'} dz'' … ∫_{z_n}^{z^(n−1)} dz^(n)

and are the unique degree-n polynomials with G_n^(r)(z_{r+1}) = 0 for r = 0,…,n−1 (Abel–Gontcharoff interpolation). The paper's content:

1. **Bounds on |G_n|.** With M_n = max|G_n(z_0; z_1,…,z_n)| over |z_r| ≤ 1, L_n = max|H_n(z_1,…,z_n)| over |z_r| = 1 where H_n = G_n(0; ·):
   - Levinson's inequalities (2.1) and (2.4), re-proved: M_n ≤ max_{0≤α≤π/2} Σ_r (2|sin rα|/r!) L_{n−r}, and n M_n ≤ M_{n−1} + 2 Σ_r M_{r−1} M_{n−r}.
   - Exact values M_2 = (3/2)^{3/2} < 2.5981, M_3 > 3.6378; bounds M_3 < 3.6379, M_4 < 4.8414; then an improved iteration (3.1) n L_n ≤ Σ_r L_{r−1} M_{n−r} yields the appendix table of upper bounds for M_n, L_n through n = 10, with L_n/(1.3775)^n ≈ 0.768… < 1.
   - **Theorem I:** if z_r are in the unit circle, then M_n ≤ (1.3775)^{n+1} for n ≥ 4 (Levinson's bound, slightly sharpened in proof).
   - **Theorem II:** if z_r ∈ [−1,1] real, then |G_n(z_0; z_1,…,z_n)| ≤ 2(4/π)^n.

2. **Whittaker-constant theorems (zeros of f and all derivatives).**
   - Levinson's Theorem (stated): if f is integral, limsup log M(r)/r < 0.7199, and f and each derivative have at least one zero in/on the unit circle, then f ≡ 0. The constant .7199 is not best possible; cannot be replaced by ≥ .7378; the best value is the Whittaker constant W.
   - Macintyre's improvement: **W ≥ .7259** (the "best possible" lower bound as of 1949).
   - **Theorem III:** if limsup log M(r)/r < .7259 and f(z_1) = 0, f^(n−1)(z_n) = 0 (n ≥ 2) with the sequence {z_r} having all limit points in the unit circle, then f ≡ 0.
   - **Theorem IV (Schoenberg's theorem, extended):** if limsup log M(r)/r < π/4 and f(z_1) = 0, f^(n−1)(z_n) = 0 with {z_r} limit points in [−1,1], then f ≡ 0. π/4 is best possible (example cos(πz/4) + sin(πz/4)).
   - **Theorem V:** version where limit points lie in the "stadium" H = {points at distance ≤ h from [−1,1]}, constant (π/4)exp(−π²h/8), better than the circle-bound .7259/(1+h) only for h ≤ 0.23.

The proof method: expand f(z) = Σ (n+k)! a_{n+k} G_{n+k}(z; z_1,…,z_n, 0,…,0) (Levinson's binomial-type expansion), bound via (5.6) |G_n| ≤ A'(γ+ε)^n, then f ≡ 0 by letting n → ∞ when the growth constant beats γ.

## Relationship to the run's problem

- The Gontcharoff polynomials are exactly the interpolation polynomials used in Massri's normal form f = G(x; y_0,…,y_{n−1}) (research/sources/massri2018_degree20_html.full.md, Section 3) and in Ghosh's downward induction (research/sources/ghosh2025_proof_html.full.md, §3: G_m(z; z_1,…,z_m) is "the unique monic polynomial of degree m with G_m^(k)(z_{k+1}) = 0").
- The Whittaker-constant theorems are the analytic backbone of the **real-rooted/half-plane** and **Gauss–Lucas-hull** constraints on CA counterexamples: they say that if a CA-like polynomial (f and every derivative sharing roots in a bounded region) is not 0, then it must have growth at least e^{γr} — i.e. a polynomial counterexample forces a quantitative statement about where its roots can lie. The run's thread root-difference-coloring (Abel–Gontcharoff factorization H_i(f)(x) = e_{n−i}(x−β_1,…,x−β_n)) and the Laterveer–Ounaïes Gauss–Lucas-hull results (claim at-least-five-distinct-roots) sit directly on this literature.
- Claim `ghosh-char0-step` records that Ghosh's proof uses "Abel–Gontcharoff polynomials and the topological theory of Brouwer degree" for the global step — Macintyre/Levinson is the classical reference for the analytic side of that same toolchain.

## Caveats

- 1949 paper, pre-computer numerical bounds (the .7259 Whittaker lower bound was later improved). Its role for this run is: (a) primary statement of the Gontcharoff polynomial definition and bounds (which Massri relies on); (b) the classical zero-concentration theorems that motivate the "roots of f and all derivatives in a bounded region ⇒ f ≡ 0" principle. It does not mention Casas-Alvero (predates it by 52 years).
- The OCR of the PDF is imperfect (formulas garbled in places); the statements above were cross-checked against the appendix table and the section structure.

## What it implies for this run

## What it implies for this run

If the root-difference-coloring approach needs a bound on |G_n| or a statement of the Abel–Gontcharoff interpolation properties in char 0, this is the primary source (with Levinson 1944, which is paywalled — see the download-failure record). The explicit M_n, L_n table and the (1.3775)^n / (4/π)^n bounds are the concrete estimates available.

```claim
id: macintyre-goncaroff-bounds
statement: The unique degree-n polynomial G_n(z; z_1,...,z_n) with
  G_n^(r)(z_{r+1}) = 0 for r = 0,...,n-1 (the Abel-Goncaroff polynomial) has
  |G_n| <= (1.3775)^(n+1) over the unit circle (Theorem I, n >= 4), and
  |G_n| <= 2(4/pi)^n when all z_r are real in [-1,1] (Theorem II). The
  repeated-integral definition is char-free (holds over any field of
  characteristic 0 via formal integration).
hypotheses: characteristic 0; nodes z_r in the unit circle (Thm I) or in
  [-1,1] (Thm II)
holds-here: yes -- these are the concrete bounds available to the run's adopted
  root-difference-coloring / Abel-Goncaroff toolchain (thread
  root-difference-coloring), and the char-free definition is what lets the
  Abel-Goncaroff expansion G_m be written over Q exactly.
status: asserted-by-source (proved in the 1949 paper; the bounds are classical
  and standard -- not re-derived by this run)
bearing: The analytic (char-0-only) side of a CA argument must eventually meet
  this growth/Max-modulus machinery; the Gauss-Lucas-hull collapse step has no
  char-p analogue (already established), and these bounds quantify the
  char-0-only content.
anchor: research/sources/macintyre1949_zeros-successive-derivatives.full.md
falsifies: a statement that the unit-circle or real-line bound on G_n does NOT
  hold, or a claim that the Abel-Goncaroff expansion requires characteristic p
  or a division.
```

Wikilink to full text: [[macintyre1949_zeros-successive-derivatives]]
