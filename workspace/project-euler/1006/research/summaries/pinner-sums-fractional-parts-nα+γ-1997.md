# Pinner, "On Sums of Fractional Parts {nα+γ}" (J. Number Theory 65 (1997) 48–73)

Source: https://www.math.ksu.edu/~pinner/Pubs/frac.ps (author's page, KSU; PostScript converted to text). Peer-reviewed: J. Number Theory 65 (1997) 48–73, doi:10.1006/jnth.1997.2080. Full text at `research/sources/pinner-sums-fractional-parts-nα+γ-1997.full.md`. The conversion is a raw PostScript→text dump with interleaved typesetting commands; read the original PS/PDF for clean equations, but the statement-level content below is reliably readable (verified against the visible Theorem 1 in the source).

## What it establishes

The **non-homogeneous** version of Brown–Shiue: for α irrational and γ real,

  C_m(α,γ) = Σ_{1≤k≤m} ({kα + γ} − 1/2).

**Theorem 1** (explicit formula): if m = z_1 q_0 + ⋯ + z_t q_{t-1} is the Zeckendorf (continued-fraction denominator) representation of m, then

  C_m(α,γ) = Σ_{1≤i≤t} (−1)^i M_i,

where M_i = −(1/2) z_i |ε_{i-1}| (m_i + m_{i-1} + 1) + (β_i − 1/2) z_i + ⌈(z_i − (u_i − m_{i-1}))/q_{i-1}⌉^+ (with the β_i, ε_i, u_i, m_i defined from the regular and non-homogeneous continued fraction expansions of γ w.r.t. α; the notation ⌈·⌉^+ is the "integer part with the ?-variant" [x]^? defined in the paper for the boundary case x ∈ Z).

For γ = 0 it reduces to Brown–Shiue Theorem 1(c): C_m(α,0) = Σ (−1)^i (1/2) z_i (1 − |ε_{i-1}|(m_i + m_{i-1} + 1)) — the homogeneous case. The paper also states the analogous explicit formula for the **discrepancy** D_m(α,γ) = max_{0≤j<m} |C_j(α,γ)| bounds, links the sums to Hardy–Littlewood lattice-point problems, and notes the fluctuations are governed by the non-homogeneous continued fraction expansion of γ w.r.t. α (bounded partial quotients no longer force ±log m swings; γ = 1/2 with α = √2 is one-sided bounded).

## Why it is in the library for PE1006

The mechanical-word digit formula for PE1006 is digit_j(x) = ⌊x + (j+1)a⌋ − ⌊x + ja⌋ with the k+1 intercepts x_m = frac(−m·a). Summing digits over m (the orbit of the rotation by a) produces sums of floor values and fractional parts of the form {kα + γ} with α = a and γ a shift — precisely the object C_m(α,γ). Pinner's explicit continued-fraction/Zeckendorf formula is the primary, citable, openly downloadable statement for the **shifted** case, which Brown–Shiue (γ = 0) does not cover and which the k+1 intercepts generically require. Together with Brown–Shiue it is the closed-form engine of the adopted Ostrowski route (`pe1006-ostrowski-sawtooth-closed-form`), giving a genuinely independent evaluation of the same Ψ(k) — the step-5 verification route.

## Caveats

- Gives first-moment sums Σ({kα+γ}−1/2), not the squared geometric-weighted second moment Ψ needs; extending to squares with the 10^j decimal weight is the run's own derivation.
- The PostScript text conversion is noisy; before quoting Theorem 1 verbatim in a proof, read the clean equations in the original PS (the file holds them, interleaved with dvips commands) or the journal PDF via doi:10.1006/jnth.1997.2080.
- The exact "non-homogeneous continued fraction" machinery (β_i, ε_i, u_i) is intricate; the run should verify any implementation against mech_psi at small k before relying on it at 10^18.
