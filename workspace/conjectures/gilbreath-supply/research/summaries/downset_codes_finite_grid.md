# Downset codes over a finite grid — Srinivasan–Tripathi–Venkitesh 2019

<!-- source: https://arxiv.org/pdf/1908.07215 | arXiv:1908.07215 | converted from PDF -->

Srinivasan, Tripathi, Venkitesh. *Decoding Downset codes over a finite grid*. arXiv:1908.07215 (2019). Follow-up journal version: *Decoding Variants of Reed-Muller Codes over Finite Grids*, ACM Trans. Comput. Theory 2020 (STOC'20).

## What it establishes

Generalises the Kim–Kopparty (2017) deterministic unique-decoding algorithm —
for polynomials of bounded total degree on a grid `S₁×…×S_m` — to the whole
family of **downset codes**. A downset code `C(S,D)` is the space of evaluations
of all polynomials whose monomial support lies in a downset `D` (closed under
taking factors), with the degree of `X_i` bounded by `|S_i|−1`. Key results:

- **Fact 1 / uniqueness of representation.** Every function `f : S → F` has a
  unique polynomial representation with the degree of `X_i ≤ |S_i|−1`; the full
  function space is `C(S,M)` with `M` the full monomial set.
- **Lemma 2 — downset Schwartz–Zippel (the load-bearing content for us).**
  For `f ∈ C(S,M)` with leading monomial `X^α` under any monomial order,
  `|Supp(f)| ≥ |∇(α)|`, where `∇(α)` is the downset below `α` — i.e. a
  polynomial's support size is bounded below by the size of the downset of its
  leading monomial. This is a *support = weight lower bound for polynomial
  codes* via downset (factor-closure) structure.
- **Lemma 3/4 — distance bound.** For distinct `G,H ∈ C(S,D)`,
  `∆(f,G)+∆(f,H) ≥ ∆(G,H) ≥ µ(S,D)`; two codewords cannot both lie strictly
  within `µ(S,D)/2` of a weighted received word. `µ(S,D)` is the code distance
  from Macaulay's theorem.
- **Theorem 5.** A deterministic polynomial-time `WeightedDownsetDecoder`
  returns a codeword within distance `µ(S,D)/2` of a weighted received word
  when one exists.

## Bearing on SUPPLY

The connection is **structural, not operational**. This run *proved* that the
fold's row set `R_n = {1_{M_d} : d ∈ [2,n−1]}` has a digital-downset structure:
`M_d ∩ M_d' = M_{d∧d'}` (claim `downset-row-intersection-meet-formula`,
claim `fold-distance-enumerator-On`). This paper is the coding-theory home of
that same downset/factor-closure geometry — the downset Schwartz–Zippel
(Lemma 2) is the closest literature shape to a "support ≥ downset size" lemma,
which is morally the kind of submask-positive lower bound the open request
`walsh-spectral-subset-b904` wants. But the object differs: the paper lower
bounds the support of a **polynomial under evaluation on a grid**, whereas the
fold's concern is the **F₂ image weight** `wt(Φ_n h) = Σ_d T(n,d)` of a
submask-XOR linear map acting on an arbitrary string `h`. There is **no direct
transfer**; it does not settle `walsh-spectral-subset-b904`, and it touches
none of the five closed doors. It is a genuine "go wide" reference on downset
geometry, not an input to the live third-pass threshold computation.

## Why it is in the library

FRONTIER.md ranked it (cited-by 2, via the Yoshida fractal-code / downset
neighbourhood) and it was never held. It is the strongest unworked frontier
candidate tied to the run's proved downset row-set geometry, so it was
downloaded to fix that angle. Held with URL on line 1; indexed for
`search_documents`. No measurement or theorem of this run rests on it.
