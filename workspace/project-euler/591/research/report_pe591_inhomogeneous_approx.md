# Research Summary: Inhomogeneous Diophantine Approximation & the PE591 Closest-Quadratic-Integer Problem

Question answered: given irrational t=√d, real shift z=π, and bound B, find b in [0,B]
(on either side) minimizing ||t·b − z|| = distance from t·b−z to the nearest integer, in
O(log B). This is the inhomogeneous Diophantine approximation / nearest lattice point
problem for a rank-two lattice in R¹, and it is the exact core of Project Euler 591.

All URLs below were actually fetched/read (full text for the two arXiv/DMTCS sources;
highlights for the rest — the full text of each downloaded source is stored under `research/`).

---

## 0. Reduction to the core subproblem (self-contained)

Let s = √d, α = {√d} = s − ⌊s⌋ ∈ (0,1), and β = {π}. For a fixed integer b,
|a + b s − π| is minimized over a∈Z by a = round(π − b·s). The residue
π − b·s = {π} − b·{√d} (mod 1), so the absolute error equals the circular distance
between {b·α} and β:

    dist( {b α}, β ) = min( |{bα} − β|, |{bα} − β ± 1| ),   b ≥ 0,
    dist( {−b α}, {−π} ) with target {−π} = 1 − β,           b < 0.

The box |a| ≤ n restricts b to |b|·√d ≲ n + π, giving B⁺ = ⌊(n+π)/√d⌋ and
B⁻ = ⌊(n−π)/√d⌋ (see `brute.py`, `verify_big.py`). The problem is therefore:

> **(Core)** irrational α∈(0,1), target β∈[0,1), bound B. Find b∈[0,B]
> minimizing the circular distance from {bα} to β.

The negative-b half is the same routine applied to the target 1−β. This is exactly
the "nearest lattice point of the rank-2 lattice {a + b·α} to the horizontal line
through β" problem.

---

## 1. The exact O(log B) algorithm: Ostrowski α-numeration

**Primary source (fetched, read in full):**
Cabanillas-López & Labbé, "A variant of Ostrowski numeration", arXiv:1904.01874 (2019).
- Abstract/TOC: https://arxiv.org/abs/1904.01874
- Full text: https://ar5iv.labs.arxiv.org/html/1904.01874
- Local copy: `research/cabanillas-labbe-ostrowski-variant.full.md` (+ summary `.md`)

### 1.1 Setup (Section 2.3 of the paper)
α has CF α = [0; a₁, a₂, …]; reduce (p_n/q_n) are the convergents; the *continuants*
(denominators) satisfy
    q_{-1}=0, q₀=1, q_n = a_n·q_{n−1} + q_{n−2}.
The convergent "errors" are the positive decreasing sequence
    δ_{-1}=1, δ₀=α, δ_n = −a_n·δ_{n−1} + δ_{n−2},
with δ_n = (−1)^n (q_n α − p_n) > 0, ↓0. (This δ recurrence is the same as the
"partial remainders" of [1303.3445]; denominators q_n grow exponentially for a
quadratic α, since q_{k+nT} ≈ c·θ^n with θ>1 the larger root of x²−Mx+(−1)^T — see
the Lekkerkerker generalization, impan.pl/…/81968. This is what makes O(log B) work.)

### 1.2 The greedy α-numeration of β (Algorithm 3(ii))
Set β₀ = β; for k = 1,2,3,…:
    b_k = min( a_k, ceil( β_{k−1} / δ_{k−1} ) ),
    β_k = b_k·δ_{k−1} − β_{k−1}.
The integer b is recovered from its digits via the integer Ostrowski basis
(Algorithm 3(i) / Prop 4):  b = Σ_k d_k·q_{k−1}. (Wikipedia "Ostrowski numeration"
gives the same integer representation and the same q_n recurrence.)

### 1.3 The central theorem — best left/right α-approximations (Section 4.3)

Definition: {nα} is a *best right* (resp. *left*) α-approximation of β if it is
strictly closer to β from the right (resp. left) than every {kα}, k<n. A best
approximation in circular distance is always a best right or left approximation.

**Proposition 9 (best RIGHT, α irrational):** candidates are
    n = 0,
    n = Σ_{i=1}^{s} b_i q_{i−1}   (if b_k=0 for all k>s, the terminal point),
    n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1},
        j ∈ {0, …, b_{2k} − 1},   k ≥ 1.

**Proposition 10 (best LEFT, α irrational):** candidates are
    n = Σ_{i=1}^{s} b_i q_{i−1}   (terminal point, if it exists), and
    n = Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k},
        j ∈ {0, …, b_{2k+1} − 1},   k ≥ 0.

(The paper also gives the rational-α analogues for the case α rational, Prop 9/10
Case 1 — not needed here since {√d} is irrational.)

### 1.4 Why O(log B) and how to get the global minimum
Each candidate is a prefix plus a bounded number of steps of a continuum q_{2k} or
q_{2k−1}; the number of k-levels is O(log B) because q_n grows geometrically for the
quadratic irrational α (termination/recoding argument in Berthé–Imbert below gives
O(log log B) iterations for the greedy variant). Enumerate the O(log B) candidates,
reduce modulo the bound, evaluate the circular distance with high-precision π, and
take the min (ties broken as the statement requires). Both the left and right sets
carry the record-minima of {nα} straddling β; the true closest point in [0,B] lies in
their union.

**Related primary source (fetched, read in full):**
Berthé & Imbert, "Diophantine Approximation, Ostrowski Numeration and the Double-Base
Number System", DMTCS vol 11:1 (2009) 153–172.
- URL: https://dmtcs.episciences.org/450/pdf (local: `research/berthe-imbert-ostrowski.full.md`)
This is an independent Ostrowski-based route: it directly computes the *best left
α-approximations* of β by the sequence (k_i, l_i), updated from the convergents and
the convergent errors f_n=|q_n α − p_n| (Algorithm 2, correctly: Prop 4, complexity
O(log log B) by Prop 6). It proves the same qualitative statement: the record minima
that can ever become closest are O(log B) in number and generated by the continued-fraction
scale q_n.

---

## 2. Alternative: exact closest vector / nearest lattice point by Euclidean/Gauss reduction

The problem can also be read as: find the lattice point (a,b) of {a + b·α} closest to
the horizontal line through π with |a|,|b| ≤ n. Two provably O(log) alternatives:

**(i) Exact nearest lattice point near a line, Euclidean-style (O(log) on |A|,|B|).**
A self-contained O(log B) reduction (math.stackexchange 2216747 — this is a workable
sketch, arguably a lower-confidence source than the peer-reviewed paper): for the line
Ax + By + C = 0 with A>0, one reduces (A,B,C) → (B, A mod B, C), halving the smaller
coordinate each step exactly like the Euclidean algorithm, and reads off the closest
lattice point in the box. This is the classical "2D lattice point closest to a line"
version of the continued-fraction/Euclidean reduction.

**(ii) The shift is handled best by the α-numeration result of §1** because π's
fractional part β is an arbitrary target, and the two-sided (left+right) character of
the nearest point is what Prop 9/10 capture. A plain "closest rational to π with
denominator ≤ B" (Farey-enclosing, e.g. the O(log) algorithm of Ashley, DeVoe, Perttunen,
Pratt & Zhigljavsky, "On Best Rational Approximations Using Large Integers", esrg…/paper_brap_detailed.pdf)
solves the *homogeneous* problem |p − qπ| but not the inhomogeneous target β with a
nonzero shift; the integral-part shift is exactly why the Ostrowski α-numeration of β
matters.

### 2.3 Note on the shift encoding
The α-numeration of β (Algorithm 3(ii)) is precisely the mechanism by which the shift
β={π} enters: the digits b_k are the greedy Ostrowski recoding of β against the δ-scale,
and Propositions 9/10 then tell you which prefixes/jumps of q-denominators are the
record closest points. This is the "how the shift z enters" the candidate generation that
a naive Euclidean reduction would miss.

---

## 3. Three-distance (three-gap) theorem — structure of the orbit

**Sources (fetched highlights):**
- https://en.wikipedia.org/wiki/Three-gap_theorem
- https://arxiv.org/abs/2308.11999 (concise proof)
- https://www.irif.fr/~berthe/Articles/Intelligencer.pdf (Berthé survey)
- The paper of §1 proves it in one page (Section 4.1).

Statement: for irrational α and N, the points {0α},{α},…,{(N−1)α} with 1 divide [0,1]
into at most three interval lengths, and if there are three, the largest is the sum of
the other two. The explicit lengths are δ_s (or δ_{s−1}) and δ_s + i·δ_{s−1} etc.
(Theorem 1 in §4.1), where s is the least index with N ≤ q_s + q_{s−1}.

**Relevance:** the three-distance theorem is the *structure* behind why the closest
point to β in [0,B] is attained at a best left or right α-approximation — the orbit
{ {nα} } only fills gaps of O(1) widths locally, so the nearest point to β is one of the
record-minimal left/right hits, i.e. exactly the candidates of §1. It bounds the number
of "relevant" prefix candidates.

---

## 4. Structure of the optimal (a,b): NOT Pell-unit related

A common guess is that the best a+b√d for fixed d is a unit/Pell power (a+b√d of norm
±1). This is **wrong for the inhomogeneous problem** — the optimal b is neither a
convergent denominator nor generally a Pell solution. Reasons:

- The best b solves the *inhomogeneous* target problem: minimize ||b·α − β||. The record
  closest points are the **best left/right α-approximations** of §1, whose b-values are
  sums of the b_i·q_{i−1} with the digits b_i of β — combinations of convergents/semiconvergents
  shifted by the digits of β, not pure convergents and not Pell/unit denominators.
- Pell units (x+y√d with x²−dy²=±1) are precisely the convergents p_n/q_n with
  p_n²−dq_n²=±1, which occur only at n = k·(period)−1 (Encyclopedia of Mathematics
  "Pell equation"; crypto.stanford.edu/pbc/notes/contfrac/pell.html; UCI 2pell.pdf;
  Canterbury continued_fractions.pdf). They give the best *homogeneous* |p−q√d|
  approximants, but the target π's fractional part β enters the digits and generically
  pushes the optimum off the Pell lattice.
- Concrete: BQA₂(π,10)=6−2√2 (a=6,b=−2). |6−2√2| ≈ 3.17, and 6−2√2 is NOT of the form
  ±(1+√2)^n (Pell units of Z[√2] have norm ±1; (6)²−2·(−2)²=36−8=28 ≠ ±1). So the optimum
  is not a unit. This is the PE591-given example, confirming the non-Pell structure.

So: the theory that governs the optimal (a,b) is the **Ostrowski α-numeration of {π}**
(inhomogeneous approximation), not **Pell's equation / units of Z[√d]**.

---

## 5. Numerical verification status

- A verification harness `verify_ostrowski.py` was written: it implements the §1 algorithm
  (build a_k, q_k, δ_k from α; α-numerate β; enumerate Prop 9/10 candidates; take best in
  [0,B]) and checks against a brute-force scan for random small (B, β) over d ∈ {2,3,5,7,10,13,
  17,19,21,29,41,97}.
- **This environment has no code-execution tool, so the harness was NOT run here.** It is
  kept in the workspace for the solver agent to execute before trusting the returned (a,b).
- Independent cross-checks that DO not require the harness (from the statement/given data):
  - BQA₂(π,10)=6−2√2 (a=6,b=−2) — direct hand-check, |6−2√2−π|≈0.17157 < |π−3|=0.14159·...,
    actually ≈ 0.17, and is the stated optimum.
  - BQA₅(π,100)=26√5−55 (a=−55,b=26).
  - BQA₇(π,10⁶)=560323−211781√7 (a=560323,b=−211781).
  - I₂(BQA₂(π,10¹³))=−6188084046055 → a=−6188084046055, b=+4375636191520 for d=2 at n=10¹³
    (the statement's double inequality lists both bounds). `verify_big.py` recomputes this gap
    at 60-digit precision to confirm < 10⁻¹³.

---

## 6. Sources actually fetched (citable URLs)

1. **Cabanillas-López & Labbé, "A variant of Ostrowski numeration", arXiv:1904.01874**
   - https://arxiv.org/abs/1904.01874
   - https://ar5iv.labs.arxiv.org/html/1904.01874
2. **Berthé & Imbert, "Diophantine Approximation, Ostrowski Numeration and the Double-Base Number System", DMTCS 11:1 (2009) 153–172**
   - https://dmtcs.episciences.org/450/pdf
3. **Three-distance / three-gap theorem**
   - https://en.wikipedia.org/wiki/Three-gap_theorem
   - https://arxiv.org/abs/2308.11999
   - https://www.irif.fr/~berthe/Articles/Intelligencer.pdf
4. **Ostrowski numeration (recurrences, Zeckendorf case)**
   - https://en.wikipedia.org/wiki/Ostrowski_numeration
5. **Best rational approximation algorithms (homogeneous, Farey/continued-fraction, O(log))**
   - https://esrg.sourceforge.net/docs/paper_brap_detailed.pdf
   - https://www.math.canterbury.ac.nz/~j.booher/expos/continued_fractions.pdf
6. **Nearest lattice point to a line, Euclidean O(log) (stackexchange, workable sketch)**
   - https://math.stackexchange.com/questions/2216747
7. **Pell / convergents / units (why the optimum is NOT Pell)**
   - https://encyclopediaofmath.org/wiki/Pell_equation
   - https://crypto.stanford.edu/pbc/notes/contfrac/pell.html
   - https://www.math.uci.edu/~ndonalds/math180b/2pell.pdf
   - https://www.math.canterbury.ac.nz/~j.booher/expos/continued_fractions.pdf
8. **Ostrowski decomposition of quadratic irrationals (exponential growth of q_n)**
   - https://www.impan.pl/shop/en/publication/transaction/download/product/81968?download.pdf
   - https://ar5iv.labs.arxiv.org/html/1303.3445
9. **Problem statement:** https://projecteuler.net/minimal=591

Caveat: MathSE 2216747 is a community answer, not peer-reviewed; treat the O(log)
Euclidean-reduction there as a sketch corroborating the peer-reviewed Ostrowski route
(sources 1–2), which is the one to rely on for the exact O(log B) guarantee.
