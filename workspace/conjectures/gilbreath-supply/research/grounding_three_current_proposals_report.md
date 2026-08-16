# Grounding report — three current candidates for the reopened territory (1 < K ≲ n/2)

For each of the inventor's three proposals, what the reformulation is actually
called, the precise theorem it relies on and whether its hypotheses hold here,
whether anyone has applied it to this problem, and what it buys. All three were
taken to the literature this pass, `status` updated accordingly, `precedent`
filled with URLs and claim ids.

## A critical framing correction that touches all three

Before pricing the candidates: the run's own authoritative K* budget is
**`K*(n) = floor(n/2)`**, not `ceil(n/2)`. The `⌈n/2⌉` table in `REOPENED.md`
and the older `kstar-n20-measured-table` claim were **superseded** by the
exact-cumulative captures (`kstar_exact`, `kstar_settle`, `kstar_resolve`,
`kstar_structural_capture`, `cum_floor18`; two independent cumulative
implementations; note `research/notes/kstar_budget_not_ceiling.md`, marked
SUPERSEDED/DISCARDED for the wrong single-gram version, but the *operative*
verdict `K*(n)=floor(n/2)` is the settled one). The `n=5` "exception" of the old
table — `K*(5)=2` — is **not an exception at all**: `floor(5/2)=2`. So the
explanation that "the closed form is not yet right" was itself the tell: the
form was `ceil` when it should have been `floor`.

Every candidate below should be tested against **`floor(n/2)`**, and the n=5
value is where the floor-vs-ceil distinction is decided (a candidate that
reproduces only the even-n values 2m is missing exactly this).

## Candidate 1 — `debruijn-cyclespace-kstar` — **grounded (machinery), transfer open**

**What it is actually called.** The edge-count vector of a length-(n−K) walk on
the order-K de Bruijn graph B_K (vertices = K-words, edges = (K+1)-words). This
is literally the k-mer count / *(K+1)*-gram histogram of h in the de Bruijn-graph
genome-assembly dictionary. "S² is a function of C_K" = "constant on the fibres
of the edge-count map", and the fibre differences are cycles of B_K — this is the
standard genomic **assembly ambiguity**: distinct Eulerian trails over the same
edge counts give different strings.

**The theorem it relies on, and whether it holds here.** The de Bruijn graph's
**cycle and cut (coboundary) space have explicit canonical bases** given by the
eigenvectors of the dB Laplacian:
> Philippakis, Mallinar, Pandit, Belkin, "Eigenvectors of the De Bruijn Graph
> Laplacian: A Natural Basis for the Cut and Cycle Space", arXiv:2410.07622
> (2024) — closed-form eigenvectors forming orthogonal natural bases for the cut
> and cycle space, a basis valid for both the directed and undirected dB graph,
> and an explicit reading of **k-mer count vectors as living in the dB cycle
> space**. Eigenvalues known since Delorme–Tillich 1998.
This holds here with no extra hypotheses: the dB cycle/cut space is a property of
the graph alone, and C_K is exactly the edge-count vector.

The second, load-bearing equivalence — **"a *nonlinear* functional S² is constant
on every C_K-fiber iff it lies in the (linear) coboundary space"** — is NOT a
sourced theorem. "Constant on fibers of a linear map" is a nonlinear condition;
the candidate's clean reduction of it to a linear rank test against the cut space
is exactly what the first-step falsifier must establish. The literature (Pevzner–
Tang–Waterman PNAS 2001; Medvedev–Pop PLoS Comput. Biol. 2021; Bals et al. ESA
2025) confirms the assembly-ambiguity direction (fibres are larger than one
point, differences are cycles) but computes NO K*(n) for this fold. So the
machinery is real and precisely named; the mechanism transfer is **novel and
open**, and the closed form it must reproduce is `floor(n/2)`.

**Has anyone applied it to this problem?** No. The dB cycle-space machinery is
applied to genome assembly and to k-mer compression (Eulertigs, "Making dBGs
Eulerian"), never to a correlation-order budget of a Boolean fold.

**What it buys.** Replaces the exponential `2^n` witness search with a rank
computation on `~2^K × (n−2)²` matrices, exponential only in the order K probed
(consistent with the reopened territory's `1 < K ≲ n/2 ≈ floor(n/2)`); it makes
the K* ≪ n−1 cancellation into a linear-dependence statement about the row-code
distance distribution.

## Candidate 2 — `derivative-ladder-order-k-functional-family` — **grounded, but priced to the barrier**

**What it is actually called.** The F₂ finite-difference operator Δ=1+σ, the
Frobenius collapse (1+σ)^{2^m}=1+σ^{2^m}, and the binomial transform
Δ^{K−1}h[j] = ⊕_i C(K−1,i) h[j+i] mod 2 — this is **Boolean differential
calculus** (Carlet). The family `F_K(h)=ν₂(Δ^{K−1}h)` is a fold functional whose
order-(K−1) statistics of Δ^{K−1}h are order-K statistics of h.

**The theorem it relies on, and whether it holds here.** The ladder
`T_{Δ^k h}(n,d)=T(n+k,d+k)`, the anti-Pascal relation, and
`Δh[j]=[q_j≠q_{j+2} mod 4]` are **machine-verified** (claim
`derivative-ladder-identities-survive`, status checked) — they are exact F₂
bookkeeping, no hypotheses missing. Carlet, "Boolean differential calculus and
its application to switching theory" (IEEE Trans. Comput., 1973) and
"On the boolean partial derivatives and their composition" (Appl. Math. Lett.
2011) are the named home of Δ and its higher directional derivatives on Boolean
functions in the ANF.

**The decisive pricing (what it buys).** For EVERY K≥1, `Δ^{K−1}h` is a linear
statistic of length-K consecutive mod-4 residue patterns of the primes. The
literature is unambiguous that **all non-constant length-≥2 mod-4 pattern
frequencies are open**:
- `abgs-p1-wide-open`: L-functions cannot treat the consecutive-pair residue
  frequency (Ash–Beltis–Gross–Sinnott 2011 §9).
- `lau-nonconstant-pattern-open`: even a single 2-term non-constant pattern
  mod 4 is not known to occur infinitely often; `lau-pattern-count-bound` fails
  at modulus 4 (not squarefree).
- The fold's cells, by `endpoint-sign-corrected-identity`, are products over run
  PAIRS χ(r_a)χ(r_b) — the non-constant side. Equal-residue (constant) patterns
  are controlled (Shiu; BFTB bounded gaps), precisely the *wrong* direction.

So **the scan's hypothesis — a K whose demanded input is provably strictly
weaker than pointwise mod-4 switch density — has no support at any K in the
literature.** The honest product for EVERY K is the parity-barrier equivalence
(GOAL priority-4 flavour), not a weaker-input win. The one conditional opening
(a K whose Δ^{K−1}h is a *constant* equal-residue pattern statistic, which
Shiu/BFTB control) must be checked mechanically in the first step; there is no
literature support it exists. Status **grounded** (exact invariance theorem with
a well-defined ordering), priced to the barrier.

## Candidate 3 — `shift-invariant-correlation-spectrum` — **grounded (machinery), characterization open**

**What it is actually called.** Translation-orbit grouping / class functions and
Burnside orbit averaging over Boolean-function monomials (the rotation-symmetric
Boolean function family), and the sliding-autocorrelation spectrum as the
Fourier dual of k-gram counts (Wiener–Khintchine: autocorrelation =
Walsh-spectrum-squared).

**The theorem it relies on, and whether it holds here.** The machinery is real
and sourced:
- Burnside orbit counting / grouping monomials by a shift orbit: Cusick & Stănică
  "Rotation Symmetric Boolean Functions — Count and Cryptographic Properties"
  (2004), and the general orbit-class-function view in Kawut & Yücel
  (arXiv:0808.0684). These make "group monomials by shift orbit, sum orbit
  coefficients" a recognized operation on ±1 monomial expansions — holds here.
- Sliding autocorrelation = Fourier dual of k-gram counts: Wiener–Khintchine in
  the Boolean/DLCT literature (e.g. arXiv:2506.00674 Walsh-Fourier expansion;
  the DLCT autocorrelation references at inria hal-03520200). This is the named
  basis for "the order S² is sensitive to = span of surviving monomial classes".
- In-workspace: the boundary reflection x↦n−1−x (claim
  `downset-row-intersection-meet-formula`) already unwinds the right-anchoring of
  M_d that blocks a pure translation symmetry — this is the candidate's key
  enabling step and it is **proved**.

**What is NOT sourced.** The specific hypothesis — `K*(n)=max span of surviving
translation-orbit coefficients`, reproducing `floor(n/2)`, n=5 included — has **no
literature precedent**. It is the run's own decomposition, to be tested in the
first step against the `floor(n/2)` table. Whether orbit grouping is the RIGHT
invariant (rather than some other symmetry of the M_d △ M_{d'} family, e.g. the
dyadic/submask one) is precisely what n=4..20 decides.

**What it buys.** Would convert the "cancellation that lowers K*" from a mystery
into a spectral/combinatorial count on the row-code distance distribution,
replacing the `2^n` fibre search — and would *explain* (not just reproduce) the
floor(n/2) closed form including why n=5 is floor not ceil. It is the only one of
the three that directly targets the "explain the cancellation" goal, but the
price is that its central characterization is unproven and novel.

## Verdict for the inventor

- **Candidate 1 (`debruijn-cyclespace-kstar`)**: machinery grounded and precisely
  named; the rank-test ⟺ K* transfer is unproven and open. Run-test against
  floor(n/2). Most bibliographically concrete.
- **Candidate 2 (`derivative-ladder-order-k-functional-family`)**: exact and
  grounded, but the literature prices every K onto the non-constant pattern
  barrier — the honest deliverable is the equivalence theorem at every K, not a
  weaker-input win (GOAL priority 2 stays open as an unconditional theorem).
- **Candidate 3 (`shift-invariant-correlation-spectrum`)**: machinery grounded;
  the specific K* characterization is novel/open and is the only one of the three
  that aims to *explain* the cancellation. Test against floor(n/2), n=5 included.

None of the three reopens a closed door: none is a Walsh/subset-sum bound on a
"complicated" h (doors 1–5), none is the Möbius/ANF relabeling (refuted anf),
none is the Cramér/switch-density route (refuted), and none is the
orderk-kstar-sat CP-SAT search (candidate 1 explicitly replaces it).
