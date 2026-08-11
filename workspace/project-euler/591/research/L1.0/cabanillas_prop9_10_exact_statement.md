# Exact statement of Algorithm 3(ii), Prop. 9, Prop. 10 — Cabanillas

Source: Emmanuel Cabanillas, "A variant of Ostrowski numeration",
arXiv:1904.01874v2 [math.NT], 12 Sep 2019.
URL: https://arxiv.org/abs/1904.01874 ; PDF https://arxiv.org/pdf/1904.01874

All quotes below are transcribed from the local full text
`research/cabanillas_variant_pdf.full.md`.

## Setup and notation

- α ∈ [0,1[, CFE [a_k]_{k∈N} (a_0=0). (p_n/q_n) convergent, q_{-1}=0, q_0=1.
- δ_{-1}=1, δ_0=α, δ_k = -a_k δ_{k-1} + δ_{k-2}, so δ_k = |q_k α − p_k|
  strictly decreasing to 0 (α irrational case).
- **Algorithm 3(ii)** (§2.3, "the inverse function of Λα", α-numeration of a
  real β∈[0,1[): β_0 = β, and for k=1,2,… :
      b_k = min( a_k, ⌈ β_{k-1}/δ_{k-1} ⌉ )
      β_k = b_k δ_{k-1} − β_{k-1}
  Output (b_k)_{k∈N*} is the α-numeration of β.
- **Def. 6** (§4.3): {nα} is a *best α-approximation* of β iff
      ∀k ∈ {0..n−1}: ||nα−β|| < ||kα−β||
  where ||x|| = distance of x to Z. Remarks before Prop. 9: "a best
  α-approximation is also a best right or left α-approximation of β."
  Best right: {nα−β} < {kα−β} ∀k<n. Best left: {β−nα} < {β−kα} ∀k<n.

## Proposition 9 (§4.3) — best RIGHT positive α-approximations

Case 1: α rational (CFE [0,a_1,…,a_r,1]), β∈{{nα}, n∈N}, (b_1..b_r)=α-numeration
of β. Candidates:
- n = 0
- n = Σ_{i=1}^{r} b_i q_{i-1}
- n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1}, j∈{0..b_{2k}−1}, k∈{1..⌊r/2⌋}

Case 2: α IRRATIONAL (the relevant case: α={√d}, d non-square), β∈[0,1[,
(b_k)=α-numeration of β. Candidates:
- n = 0
- n = Σ_{i=1}^{s} b_i q_{i−1},  if b_k = 0 for all k > s  (terminal prefix)
- n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1},  j ∈ {0..b_{2k}−1},  k ∈ N*

## Proposition 10 (§4.3) — best LEFT positive α-approximations

Case 1: α rational as above. Candidates:
- n = Σ_{i=1}^{r} b_i q_{i−1}
- n = Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k},  j∈{0..b_{2k+1}−1},  k∈{0..⌊(r−1)/2⌋}

Case 2: α IRRATIONal, β∈[0,1[, (b_k)=α-numeration of β. Candidates:
- n = Σ_{i=1}^{s} b_i q_{i−1},  if b_k = 0 for all k > s   (terminal prefix)
- n = Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k},  j ∈ {0..b_{2k+1}−1},  k ∈ N

Note: in Prop. 10 Case 2 the summation Σ_{i=1}^{2k} has last included digit
b_{2k}·q_{2k−1}; j multiplies q_{2k}. Indices: k∈N means k≥0 in Prop.10.

## Why this is the O(log L) candidate set for PE591

For fixed d, set α = {√d} (irrational, since d non-square) and β = {π}∈[0,1[.
For integer b, ||b·√d − π||_Z = ||b·α − β||_Z (subtract the integer part of √d
and of π). The records of the sequence n ↦ ||nα−β|| (its "best
α-approximations") are, by Def. 6 and the remark, exactly the union of the
best right and best left α-approximations, which are parametrized in closed
form by Prop. 9 + Prop. 10 (Case 2, irrational-α — our situation). The global
minimum of ||nα−β|| over n ∈ [0,L] is attained at one of the records ≤ L, so it
is contained in the union of the two Prop. 9/10 lists restricted to n ≤ L.
Because q_k grows at least geometrically, only k = O(log L) indices survive the
bound n ≤ L, and each contributes ≤ b_{2k} (resp. b_{2k+1}) j-values — an
O(log L)-sized (in practice tiny) candidate set. 

Both signs of b in PE591 are handled by considering β AND 1−β (negative b
becomes positive-|b| approximation of −β ≡ 1−β; see §2.4 / Proposition 5,
symmetry β → 1−β), matching the run's both-sign solver.

## Hypotheses that must hold
1. α = {√d} irrational: holds for non-square d. (Fails if d is a square —
   excluded in PE591.)
2. β = {π} ∈ [0,1[: holds. β irrational not required by the propositions.
3. b = α-numeration of β must be computed by Algorithm 3(ii) (exact, using the
   δ_k and a_k), which is why high-precision arithmetic is needed.

## Agreement with `cabanillas_variant_pdf.md` (summary)
The summary (`research/cabanillas_variant_pdf.md`) states Prop. 9 as:
"n=0; terminal prefix n=Σ_{i=1}^{s} b_i q_{i−1} if expansion terminates; and
n=Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1}, j∈{0,…,b_{2k}−1}, k≥1" — matches.
Prop. 10 as: "terminal prefix n=Σ_{i=1}^{s} b_i q_{i−1}; and
n=Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k}, j∈{0,…,b_{2k+1}−1}, k≥0" — matches the
full text (k∈N ⟺ k≥0). Algorithm 3(ii) stated identically. The summary agrees
on all three statements; verified against the full text above.
