# Li–Liu–Xiao 2025 — lowest upper bound for a class of hyperelliptic Abelian integrals

Full text: [[abelian-zeros-special-hyperelliptic-2025.full]] (Sci. China Math.,
DOI 10.1007/s11425-023-2334-8).

## What the source establishes (held full text)

**Object:** isolated zeros of hyperelliptic Abelian integrals
I(h) = ∮_{Γ_h} (α + βx) y dx, α,β ∈ ℝ, where Γ_h is a compact component of
{y² + P₅(x) = h} with P₅ of degree five in the Liu–Xiao normal form
P₅(x) = −(uv/2)x² + ((u+v+uv)/3)x³ − ((1+u+v)/4)x⁴ + (1/5)x⁵.

**Known lower bound:** for (v,u) ∈ Θ = {v = ū, Im(v) ≠ 0, (Re(u)−2)² + (Im(v))² < 1},
there exist α,β with I(h) having **at least two isolated zeros** (Liu–Xiao 2013).

**This paper's contribution:** a new simplification technique reducing the degree of a
polynomial by at least half, to attack the question whether **two is also the upper
bound** of the number of isolated zeros of I(h) for (v,u) ∈ Θ. The abstract states the
technique; the resolution of the two-is-the-upper-bound question is the paper's
content (the digest is truncated before the main theorem statement).

## What it lets this run conclude

- This is a special-family Abelian-integral zero count (GOAL result-type 3, the
  `h16-sharp-abelian-named-family` goal): a named hyperelliptic family with an
  explicit sharp-count question (2 or fewer zeros), and a *simplification technique*
  that reduces polynomial degree by half — potentially the exact kind of
  kernel-checkable reduction the run's Wronskian/ECT pipeline can validate.
- The hypothesis structure (Liu–Xiao normal form, Θ region, α,β real) is explicit and
  machine-checkable in principle: the run could clean-room verify "the simplification
  reduces the degree by ≥ half" and the zero-count bound for specific (v,u).
- It does not touch H16.2 or any graphic cyclicity.

```claim
id: h16-llx2025-hyperelliptic-zero-bound
statement: Li–Liu–Xiao (2025, Sci. China Math., DOI 10.1007/s11425-023-2334-8): for the hyperelliptic integrals I(h)=∮_{Γ_h}(α+βx)ydx over ovals of {y²+P₅(x)=h} with P₅ in Liu–Xiao normal form, there exist α,β with at least two isolated zeros for (v,u)∈Θ (Liu–Xiao 2013 lower bound), and the paper's simplification technique (reducing polynomial degree by at least half) attacks whether two is the upper bound. The two-is-upper-bound statement's status is the paper's content; the digest does not establish it as a theorem of this note.
hypotheses: P₅ degree five in Liu–Xiao normal form; (v,u) ∈ Θ; α,β ∈ ℝ; Γ_h compact ovals over a maximal interval Σ.
holds-here: yes — a named special-family Abelian zero-count target for the sharp-abelian goal; does not affect H16.2.
status: asserted
evidence: full text held at research/sources/abelian-zeros-special-hyperelliptic-2025.full.md; abstract states the lower bound (Liu–Xiao 2013) and the technique.
falsifier: a (v,u) ∈ Θ with three isolated zeros of I(h) for some α,β (if the paper claims two is the upper bound), or an error in the simplification technique.
sources: https://doi.org/10.1007/s11425-023-2334-8
anchor: research/sources/abelian-zeros-special-hyperelliptic-2025.full.md
follows-from: h16-abelian-integral-bounds
answers:
```
