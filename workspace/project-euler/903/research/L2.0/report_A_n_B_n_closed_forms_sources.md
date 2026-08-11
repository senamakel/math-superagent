# Sources for closed forms of A_n and B_n in f_n(k) = A_n + (k−1)B_n

**Date:** research run. **Question answered:** which published results give
(a) per-gap pair-inversion probabilities affine in the gap,
(b) a concrete summation (over cycles / fixed points / Eulerian numbers) that could
produce A_n, B_n as functions of n, and (c) an Eulerian-polynomial closed form for
per-gap inversion counts.

**Bottom line:** No located source computes the run's specific statistic
f_n(k) = #{(π,i): 0≤i<n!, (π^i)(k) < (π^i)(0)} (a sum *over the cyclic subgroup
{π^i}*).  Every result below is a *per-pair-inversion probability of a single
permutation*, either per conjugacy class or per fixed-point count.  These are the
mechanism behind the empirical gap-linearity and the concrete summation routes to
A_n and B_n, but none of them is A_n or B_n themselves.  The genuinely novel core —
summing ranks/Lehmer-weighted inversions over {π^i} — is unaddressed by all sources.

---

## (a) Pair-inversion probabilities affine in the gap

### Source 1 — Campion Loth, Levet, Liu, Stucky, Sundaram, Yin, "Permutation Statistics in Conjugacy Classes of the Symmetric Group", arXiv:2301.00898
Full text in this library: `research/L0/conjugacy_class_statistics_body.full.md`.
URL: https://arxiv.org/abs/2301.00898 (ar5iv: https://ar5iv.labs.arxiv.org/html/2301.00898)
DOI: 10.48550/arXiv.2301.00898.

**Exact statement, Lemma 4.7** (§4.1 Inversion indicator functions).  Let
λ = (1^{a_1}, 2^{a_2}, …, n^{a_n}) ⊢ n, and C_λ the conjugacy class of cycle
type λ.  For any i < j in [n], Pr_λ[I_{i,j}=1] = Pr over uniform ω∈C_λ that
ω(i) > ω(j).  Then

    Pr_λ[I_{i,j}=1] = 1/2 + a_2/(n(n−1)) − a_1(a_1−1)/(2n(n−1))
        + (j−i−1) · [n − n·a_1 − a_1 + a_1² − 2·a_2] / [n(n−1)(n−2)].

Two consequences used by this run:
- depends only on n, a_1, a_2 and the **gap d = j−i**, not on i,j themselves
  (translation invariance in the gap);
- **affine in d = j−i** with slope [n − n a_1 − a_1 + a_1² − 2a_2]/[n(n−1)(n−2)].

**The concrete summation that produces A_n, B_n via this source.**  Theorem 4.8
gives, for any weighted inversion statistic X = Σ_{i<j} wt(i,j) I_{i,j}, with
α_n(X)=Σ wt(i,j), β_n(X)=Σ (j−i−1)wt(i,j):

    E_λ[X] = (1/2 + a_2/(n(n−1)) − a_1(a_1−1)/(2n(n−1)))·α_n(X)
           + ([n − n a_1 − a_1 + a_1² − 2a_2]/[n(n−1)(n−2)])·β_n(X).

To get A_n, B_n one would: take wt(i,j) = indicator of a specific gap k (=1 per
pair at separation k), getting α and β counts; plug λ = cycle type of the
permutation whose powers are summed; and average over the conjugacy-class
distribution with class weights z_λ^{-1} = 1/∏(k^{a_k} a_k!) (Prop 2.2,
eq. (6.1)).  The class equation and Burnside identities (Lemma 6.1) are
exactly the tools that collapse Σ_{λ⊢n} z_λ^{-1} a_1 = 1, Σ z_λ^{-1} a_1² = 2,
Σ z_λ^{-1} a_2 = 1/2.  **But** this averages over a *single* permutation per
conjugacy class, not over the subgroup {π^i}; the run's f_n(k) needs
(n!/ord(π))-weighted sums over powers *inside* each cyclic subgroup, which no
weighted-inversion-statement here supplies.  So Source 1 gives the per-gap
mechanism and the summation calculus, not A_n, B_n.

### Source 2 — Pinsky & Schickentanz, "Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points", arXiv:2510.20654v2
Full text: `research/L0/pinsky_schickentanz_ewens_html.full.md`.
URL: https://arxiv.org/abs/2510.20654 (HTML: https://arxiv.org/html/2510.20654v2).
DOI: 10.48550/arXiv.2510.20654.

**Exact statement, Theorem 1a (eq. 1.1), unconditioned Ewens pair inversion
probability.**  Under P_θ^{(n)} (proportional to θ^{#cycles}; uniform is θ=1),

    P_θ^{(n)}((i,j) inverted) =
       n(n−2(j−i)+1)/[2(θ+n−1)] − (n−1)(n−2(j−i))/[2(θ+n−2)].

Depends on the pair only through the gap j−i, and is **affine in the gap**.
- θ=1 (uniform): reduces to 1/2.
- θ→0 (single n-cycle / rotation): 1/2 + (j−i−1)/[(n−1)(n−2)] — the pure
  cyclic-subgroup small-exponent inversion structure.

**Exact statement, Proposition 10a (eq. 3.2), fixed-point-conditioned.**
An exact finite-n closed form for P_θ^{(n)}((i,j) inverted | #fixed points = m),
a five-term combination of ratios
P_θ^{(n−2)}(#fixed = m−1,m,m+1,m+2) / P_θ^{(n)}(#fixed = m),
each term affine in the gap j−i.  Fixed-point count itself is Prop 4:
P_θ^{(n)}(#fixed=m) = [n! θ^m/(m! θ^{(n)})] Σ_{k=0}^{n−m} (−θ)^k θ^{(n−m−k)}/(k!(n−m−k)!),
θ^{(r)} rising factorial.

**Summation route to A_n, B_n (this source).**  Since the uniform permutation
has a Poisson(1) fixed-point count (see Source 4 / Ford), averaging the θ=1
fixed-point-conditioned per-gap probability over the fixed-point-count distribution
gives the per-gap inversion probability; combined with Source 3 this is a full
cycle-type summation machinery.  Same caveat: it is a per-single-permutation
probability, not a sum over the cyclic subgroup {π^i}.

### Source 3 — Pinsky, "The Inversion Statistic in Derangements and in other Permutations with a Prescribed Number of Fixed Points", Electron. J. Combin. 33(2), P2.36 (2026)
Library: `research/L1/pinsky_inversion_fixed_points.md`, full `research/L0/pinsky_inversion_fixed_points.full.md`.
URL: https://doi.org/10.37236/14250.  (arXiv companion 2505.02058.)

Exact finite-n formula for the per-pair inversion probability P_n^{(k)}
(σ_i^{-1} < σ_j^{-1}) conditioned on exactly k fixed points, and the expected
inversion number E P_n^{(k)}[inv].  Asymptotics: expected inversions in a random
derangement (k=0) = n(n−1)/4 + n/6 + 1/12 + o(1); for k≥2,
n(n−1)/4 − (k−1)n/6 − (k²−k−1)/12 + o(1).  This is the exact finite-n companion
to Source 2's Prop 10a and is the fixed-point-conditioned summation route to
A_n, B_n.

---

## (b) Summation producing A_n, B_n — where the AVERAGING must happen

The run's reduction (memory.md) is exact:
    Q(n) = (n!)^2 + A_n·S(n) + (B_n/2)·T(n),
    S(n) = Σ_{m=1}^{n−1} m·m! = n! − 1,   T(n) = Σ_{m=1}^{n−1} m(m−1)m!.
So only A_n and B_n (i.e. f_n(k)) are missing.  The route all sources open is:
f_n(k) counts inversions over {(π,i)} at gap k.  Writing each π's contribution as
(n!/ord(π))·[# of distinct powers τ∈⟨π⟩ with τ(k)<τ(0)], and using that within a
cyclic subgroup the cycle type is that of π (all powers share the conjugacy class),
one should be able to apply Source 1's Lemma 4.7/Tbl 1 with λ = cycle type of π
and average over cycle types with the extra n!/ord(π) weight.  **This extra
n!/ord(π) weighting over the cyclic subgroup is the part no source provides.**

### Source 4 — Ford, "Cycle type of random permutations: A toolkit", Discrete Analysis 2022:9, arXiv:2104.12019
Library: `research/L1/ford_cycle_type_toolkit.md`, full `research/L0/ford_cycle_type_toolkit.full.full.md`.
URL: https://ar5iv.labs.arxiv.org/html/2104.12019, DOI 10.19086/da.38090.
Provides the canonical calculus for the cycle-type sums: exact polynomial
factorial moment E[∏_k (C_k)_{r_k}] = ∏_k k^{−r_k} for Σ k r_k ≤ n, and
fixed-point count → Poisson(1) with rates.  The engine for evaluating the
Σ_{λ⊢n} z_λ^{-1}(…) sums over cycle types that A_n, B_n require.

---

## (c) Eulerian-polynomial closed forms for per-gap (k-step) inversion counts

### Source 5 — Sack & Úlfarsson, "Refined inversion statistics on permutations", arXiv:1106.1995v2
Full text: `research/L0/sack_ulfarsson_refined_inversion_pdf.full.md`.
URL: https://arxiv.org/pdf/1106.1995.  DOI: 10.48550/arXiv.1106.1995.

**Exact statement, Theorem 4.4** (§4.1, "The distribution of k-step inversions").
A *k-step inversion* of π is an inversion (a,b) with b−a = k (Def 4.1).
Let inv_k(π) = number of k-step inversions, H_{n,k}(x) = Σ_{π∈S_n} x^{inv_k(π)}.
For 1 ≤ k ≤ n, let s = ⌊n/k⌋+1 and t = rem(n/k).  Then

    H_{n,k}(x) = I(n,k,0) · A_s(x)^t · A_{s−1}(x)^{k−t},

where A_ℓ(x) = H_{ℓ,1}(x) is the ℓ-th Eulerian polynomial, and

    I(n,k,0) = ∏_{j=1}^{k−1} C(n − Σ_{i=0}^{j−1} λ_i, λ_j),

with λ_0 := 0 and λ_j the length of the j-th k-step run
(λ_j = ⌊(n−j)/k⌋+1; equivat., t runs of length s and k−t of length s−1).
So the *distribution of inversions at a single fixed gap k* (equivalently, over
S_n, the count of permutations with r inversions at gap k) is a closed product of
Eulerian polynomials.  This is the per-gap generating-function machinery that
matches the run's f_n(k) gaps, but — like the others — for a single permutation,
not for the cyclic subgroup {π^i}.

**Related exact results in the same paper:**
- Theorem 2.5: 1·π = n(n+1)(2n+1)/6 − invsum(π), with
  invsum(π) = Σ_{(a,b)∈INV(π)}(b−a).  So Σ_k k·inv_k(π) = invsum(π).
- Corollary 2.6: ninvsum(π∘ρ) = π·ρ^−1 − 1·1^c  (a trace-like identity for
  products/composed powers — relevant if one ever restricted inversions to powers).
- Theorem 3.7 (zone-crossing): Σ_{π∈S_n} q^{nzcv(π)_k} = k!(n−k)! [n; k]_q.
- Theorem 3.8: recursion for the non-inversion-sum distribution N_n(q).

---

### Conjugacy-class higher-moment polynomiality (potential route to B_n slope)
Source 1 also proves (Theorems 1.3/1.5, Prop 7.28, Cor 7.29): for λ with all
parts ≥ mk+1, E_λ[X^k] is independent of λ; for inv, E_λ[inv²] with all parts ≥5 is
(1/16)n^4 − (1/72)n^3 − (1/80)n^2 − (49/360)n; the inv^k mean has degree 2k and
leading coefficient 2^{−2k}.  These give the *k-gap-weighted* per-class moment
structure (via β_n = (n over 3) for inv) but again are single-permutation, not
cyclic-subgroup.

---

## Negative / delimiting findings (equally important)

- **Cambie & Yan, "Descents and inversions in powers of permutations",
  arXiv:2408.01211** (`research/L1/cambie_yan_html.md`, full `research/L0/cambie_yan_html.full.md`)
  is the *closest known match to the run's actual quantity* — it sums inversions
  of POWERS π^k — but only for fixed exponent k with n ≥ 2k+1:
    Thm 1.1 (descents): (1/n!)Σ_π des(π^k) = (n−1)/2 − [τ(k)²−τ(k)−τ_o(k)+σ(k)]/(2n).
    Thm 1.2 (inversions): (1/n!)Σ_π inv(π^k) = n(n−1)/4 − (τ(k)−1)n/6 − [τ(k)²−τ(k)−τ_o(k)+σ(k)]/12,
    τ(k)=#divisors, σ(k)=Σ_{d|k}d, τ_o(k)=#odd-divisors.
  It does NOT cover exponents t > (n−1)/2, which appear in the full i=1..n! sum;
  naive extrapolation of the per-exponent slopes FAILS (recorded in `cambie_yan_html.md`:
  n=3 gives slope-sum 32 but true B_3 = 1).  So it is a source for the
  small-exponent regime of the gap-affine per-pair counts, not a closed form for
  A_n, B_n.
- **No source computes Σ_{τ∈⟨π⟩} rank(τ) or the (π,i)-sum of Lehmer-weighted
  inversions over a cyclic subgroup.**  This is confirmed in `L2/reports_negatives.md`
  and `L1/report_literature_ranks_powers.md`.  OEIS lookups for A_n, Q(n), |B_n|/(n−1)!
  all returned "no results" (`oeis_Aseq.md`, `oeis_Qseq.md`, `oeis_Bdiv.md`).
- **Homomesy (Elder–Lafrenière–McNicholas–Striker–Welch, arXiv:2206.13409)** was
  noted as a possible structural tool (average of a statistic over a group action
  orbit is constant) but the library has only its abstract; no usable orbit-sum
  result is captured.

---

## What this means for the computation of Q(10^6)

To obtain closed forms for A_n and B_n (the only missing inputs to
Q(n) = (n!)^2 + A_n(n!−1) + (B_n/2)T(n)), the historically supported route is:
1. Express f_n(k) = Σ_{π} (n!/ord(π)) · #{τ∈⟨π⟩: τ(k)<τ(0)}.
2. For each cycle type λ (the common cycle type of all powers in ⟨π⟩), use
   Source 1's Lemma 4.7 affine per-gap pair-inversion probability on C_λ.
3. Evaluate the resulting double sum over λ ⊢ n (class weights z_λ^{-1}) with the
   exact factorial-moment calculus of Source 4, and over the order-domain weight
   n!/ord(π) governed by the average-order law (Source Stong, `L2/order_random_permutation.md`).
Steps 1–3 are the run's own derivation; the sources supply the per-gap mechanism
and the summation tools, not the answer.  The literature is clean-negative on a
closed form for Σ_{τ∈⟨π⟩} rank(τ).
