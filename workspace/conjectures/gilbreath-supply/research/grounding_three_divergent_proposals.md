# Grounding report: the three divergent proposals (level-set, Haar-chaos, Cramér–Gallagher)

Date: this run. Author: research role (grounding pass).

## Task

The inventor posted three divergent proposals and asked research to take each to
the literature and report per candidate: what the reformulation is actually
called, the precise statement of any theorem it relies on and whether its
hypotheses hold here, whether anyone has applied it to this problem, and what it
would buy — then set `status` grounded or refuted with a `killed-by`.

Verdicts: **all three refuted**, each on a specific, sourced obstruction. Two die
on the same recurring wound (the deterministic-to-random / index-vs-value gate),
one dies on its own model being wrong about the very input it needs.

---

## 1. `level-set-explicit-formula-index-correlation` — refuted

**The reformulation, named.** The route wants to turn the index-domain
correlation S(n) = Σ_d (−1)^{T(n,d)} into a "value-domain" bilinear sum by
extracting a π-level-set weight: it claims
`Σ_j χ(q_j)χ(q_{j+2^g}) = Σ_{p<p'} χ(p)χ(p')·1_{π(p')−π(p)=2^g−1}`, then re-reads
the coefficient as `[z^{2^g−1}]` of `F(z;x)=Σ_{p<p'}χ(p)χ(p')z^{π(p')−π(p)}`, to
be attacked by Perron/explicit-formula regularised weights and then Linnik
dispersion / the large sieve.

**The theorem it relies on.** The explicit formula `π(x) = Li(x) + Σ_ρ Li(x^ρ) + O(...)`
(Riemann–von Mangoldt; Montgomery–Vaughan Ch.12; Leboeuf, DOI 10.1007/s00023-003-0958-2)
and value-shifted character-sum bounds such as `Σ_{n≤x}Λ(n)χ(n−l) ≪
x exp(−0.6√ln D)` (Steklov 2018, DOI 10.1134/S0081543817080156) or
`Σ f(n)χ(n+a)` (JNT 2018). These are real and correctly stated.

**Whether the hypotheses hold here — the load-bearing hypothesis fails.**
Substitute `j = π(p)`: then `z^{π(p')−π(p)} = z^{j'−j}` and `χ(p) = χ(q_{π(p)})`,
so
`F(z;x) = Σ_{j<j'} χ(q_j) χ(q_{j'}) z^{j'−j}`.
This is a function **only of the index-domain sequence (χ(q_j))**. The characters
are evaluated at prime INDICES, never at free value arguments; every shift is an
index difference j'−j, never an integer value-shift n−l. Linnik's dispersion and
the large-sieve estimates that the route wants all act on VALUE-shifted
characters, which is exactly the index-vs-value obstruction that refuted
`dispersion-bilinear-large-sieve`. The "conversion" is an identity and never
leaves the index domain.

**Additional defects.** (a) Off-by-one: the pair (q_j, q_{j+2^g}) has
π(p')−π(p)=2^g, not 2^g−1, so at g=0 the proposal's [z^{2^g−1}]=[z^0] coefficient
is empty while the real adjacent/separation-1 stratum is the [z^1] one. (b) In
any reading, the coarsest-scale coefficients the extraction must recover are the
mod-4 switch-pair objects, which are the named parity barrier
(`abgs-p1-wide-open`: L-function-inaccessible; `lau-nonconstant-pattern-open`:
even one non-constant 2-term pattern open).

**Who has applied it.** Nobody applies the value-domain toolbox to a weight that
is a level-set indicator of π (a function of the index); no source was found.
This is a statement about my search, not a theorem of absence — but the
structural substitution above already answers the falsifier.

**What it would buy.** Nothing over `dispersion-bilinear-large-sieve`: same
object, same index-value obstruction, seen from the other side.

## 2. `haar-chaos-hypercontractive` — refuted

**The reformulation, named.** Read S(n)=Σ_d Π_R s_{a_R}s_{b_R} (s_j=χ(q_j), a
product over the dyadic-run boundary pairs) as a structured chaos (Wiener–Itô /
Haar) form on {±1}^n and bound it by **hypercontractivity / the Bonami–Beckner
inequality**: `‖f‖_q ≤ (q−1)^{d/2}‖f‖_2` for degree-d polynomials on the cube.

**The theorem it relies on — real and correctly stated.** Bonami (1970), Beckner
(1975), Gross (1975); exact statement and constant in Biswal arXiv:1101.2913 and
O'Donnell Ch.9–10; vector-valued refinements in Eskenazis–Ivanisvili
DOI 10.1007/s00440-020-00973-y, Keller–Lifshitz–Marcus arXiv:2307.01356. All
confirmed.

**Whether the hypotheses hold here — they fail at the level of what the theorem
can say.** Bonami–Beckner is a statement about a RANDOM vector (x uniform on the
cube): it bounds moments ‖f‖_p of a random evaluation. It therefore bounds the
root-mean-square of S(n) over random digit strings s — which the F₂-fair model
already supplies exactly (wt(Φ_n h) is Binomial(n−2,1/2), `fair-model-exact-binomial`,
proved from rank=n−2). It does NOT bound the FIXED prime string S(n). Turning
"random s gives S(n)=O(√n)" into "the fixed primes give S(n)=O(√n)" is precisely
the deterministic-to-random finite-prefix transfer that refuted
`lucas-mixing-finite-transfer` and `dyadic-martingale-azuma` — and no source
supplies it.

**Second defect.** The route's priced arithmetic input is the L² mass /
autocorrelation of s, whose g=0 (adjacent) term is Σ_j χ(q_j)χ(q_{j+1}), the
mod-4 switch-pair = the parity barrier. Not weaker than switch density — it IS
the barrier at the coarsest scale, where the measured bulk of S(n) sits.

**Who has applied it.** Hypercontractivity is heavily applied in Boolean-function
analysis, but never to force linear fold weight of a fixed prime string; the
search found no such application. The basis point (an s-domain monomial is a
genuine Walsh monomial) is correct and clean, but orthogonal to the failure.

**What it would buy.** Nothing beyond the fair model's exact random bound, which
is already proved and which does not transfer to the primes.

## 3. `cramer-gallagher-second-moment` — refuted

**The reformulation, named.** Compute E[S(n)²] in the **Cramér–Gallagher**
random-prime model via the Hardy–Littlewood singular series, get E[S²]=O(n), and
read it as a conditional averaged-SUPPLY, isolating an unconditional gap "weaker
than switch density".

**The theorems it relies on — real and correctly stated.** Cramér (1936);
Gallagher "On the distribution of primes in short intervals", Mathematika 23
(1976) 4–9, DOI 10.1112/S0025579300016442 (h~λlogN gives Poisson mean-λ count,
from a quantitative HL k-tuple conjecture via the singular series
S(D)=∏_p(1−ν_p(D)/p)(1−1/p)^{−k}); Pintz arXiv:1004.1084 (SH(H)→1 over k-sets);
Montgomery–Soundararajan variance ~ H log(N/H) (ANTS 2025, DOI 10.2140/ant.2025.19-4).

**Whether the hypotheses hold here — the model is wrong about the input it
needs.** The classical Cramér–Gallagher model is **mod-4 unbiased**: it assigns
the four ordered mod-4 pairs equal weight. But the g=0 stratum of the fold's
second moment, and the measured mean of the fold, are carried by mod-4 **switch
density**, which is NOT uniform: LOS PNAS 2016 (DOI 10.1073/pnas.1605366113)
measures switch pairs (1,3),(3,1)≈57.5% vs equal≈42.5% (`abgs-mod4-nonuniform-measured`),
and ABGS §9 says the pair asymptotics are L-function-inaccessible
(`abgs-p1-wide-open`). The route's own first-step (4) — "calibrate the g=0
adjacent-switch mean" — would fire: the model cannot match even the first
moment of the fold, so it cannot be trusted for the second.

**Also.** The index↔value transfer at ~2^g log x and the "singular series cancels
at second order" claim are heuristics within the model (the transfer is unproved,
and short-interval moments don't determine the χ(q_j)χ(q_{j+2^g}) pair
correlation without an HL input that is itself conjectural). And even granting
E[S²]=O(n) in the model, "the real primes match Cramér–Gallagher at second
order" IS the unconditional gap — the finite-prefix transfer — which the model
computation does not establish. A conditional theorem about the model is
evidence (like the white-noise measurements), not a conditional SUPPLY.

**Who has applied it.** The Cramér–Gallagher/singular-series machinery is
standard for short-interval prime statistics, but (per LOS) the mod-4 pair bias
is precisely a place where the primes deviate from the model — so applying the
model to the fold's switch-driven second moment is applying it where it is known
to be wrong. No source was found applying it to this fold.

**What it would buy.** A computation in a model the primes contradict, whose
conclusion does not transfer. Nothing beyond the already-measured evidence.

---

## What this adds to the run

Two of the three die on the deterministic-to-random / index-vs-value gate that
has now killed `dispersion-bilinear-large-sieve`, `dyadic-martingale-azuma`,
`lucas-mixing-finite-transfer`, `matomaki-radziwill`, `prime-race-variance` and
the new `level-set` + `haar-chaos` (the transfer) and `cramer-gallagher`
(model wrong about switch density). This reinforces the GOAL assessment: the
fold's g=0 (adjacent, switch-pair) stratum is the load-bearing parity barrier,
and no route that either (a) reads the object in the index domain and then
tries value-domain tools, or (b) bounds a random model and claims the fixed
prime string, has any literature support. A genuine route must bound a
DETERMINISTIC object in the fold's own coordinates — which is what the adopted
`fold-second-moment-krawtchouk` (Delsarte/MacWilliams row-code distance) and
`downset-row-code-distance-closed-form` attempt.
