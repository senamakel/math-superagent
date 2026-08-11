# Sack–Úlfarsson: refined inversion statistics on permutations

**Source:** arXiv:1106.1995 (math.CO), DOI 10.48550/arXiv.1106.1995. Full text at
[[sack_ulfarsson_refined_inversion_pdf.full]] (PDF, 28.7 KB source under L0).
Journals/stats baked into the file.

## What it establishes, relevant to PE 903

This run's core is the **gap decomposition of pair-inversion counts**:
f_n(k) = A_n+(k−1)B_n counts (over π and its powers) pairs at separation gap k.
This paper is exactly the literature on gap-refined inversion statistics.

- **k-step inversion** = inversion (a,b) with b−a = k (Def 4.1); inv(π)=Σ_k inv_k(π).
  The k-step count **H_{n,k}(x)** has a closed distribution (Thm 4.4):
  H_{n,k}(x)=I(n,k,0)·A_s(x)^t·A_{s−1}(x)^{k−t}, where A are Eulerian polynomials,
  s=⌊n/k⌋+1, t=rem(n/k), and I is a product of binomials. This is the distribution
  of inversions at a *single fixed gap k* — the direct analytic handle on the gap
  function f_n(k) the reduction needs. It does **not** include the powers {π^i},
  only the base permutation.
- **Non-inversion sum** ninvsum(π)=Σ_{(a,b)∈NINV}(b−a) relates to the dot product
  (Thm 2.5): 1·π = 1·1^c + ninvsum(π) = n(n+1)(2n+1)/6 − invsum(π). Cor 2.6:
  ninvsum(π∘ρ)=π·ρ^{−1}−1·1^c — a trace-like identity for products/composed powers.
- **Zone-crossing vector** (Def 3.1): z_k = # pairs (a,b) with a≤k<b; uniquely
  determines π (Prop 3.3), and ninvsum = Σ of its coordinates (Lemma 3.4). Recurrence
  for the ninvsum distribution N_n(q) (Thm 3.8) via inserting n+1 (Lemma 3.6).
- (k1,k2)-step inversions (fix both gap and value separation) — Prop 4.6/4.8 give
  leading-coefficient and recurrence results.

## Why it matters here / what's still missing

The k-step inversion distribution **is** the gap-resolved inversion structure the
run's f_n(k)=A_n+(k−1)B_n arithmetic form encodes — it supplies the generating
function machinery (Eulerian connections, zone-crossing recurrence) for the per-gap
counts. Open negatively: it treats only the single permutation π, never the cyclic
subgroup {π^i} over which PE 903 sums ranks, so it does **not** close the A_n,B_n
closed-form hunt by itself. Mechanism/route, not the Q(10^6) answer.
