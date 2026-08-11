<!-- source: https://arxiv.org/abs/1904.01874 ; full text at https://ar5iv.labs.arxiv.org/html/1904.01874 | converted from HTML -->

## Summary

Cabanillas-López & Labbé, "A variant of Ostrowski numeration", arXiv:1904.01874 (2019).

This is the PRIMARY algorithm behind PE591. It builds an Ostrowski-style numeration (α-numeration) based on the continued fraction of an irrational α∈[0,1) that codes every integer n and every fractional part {nα} by the SAME finite digit sequence, and uses it to analyze order properties of Kronecker sequences ({nα−β}).

**Notation / setup (Section 2.3):** α has CF [0; a_1,a_2,…], convergents p_n/q_n, and the error sequence
  δ_{-1}=1, δ_0=α, δ_n = −a_n·δ_{n−1} + δ_{n−2}   (so δ_n = (−1)^n(q_n α − p_n) > 0).
(δ_n is positive and decreases to 0.)

**α-numeration of β∈[0,1) (Algorithm 3(ii), the greedy rule):** set β_0=β; for k=1,2,…:
  b_k = min(a_k, ⌈ β_{k−1}/δ_{k−1} ⌉)
  β_k = b_k·δ_{k−1} − β_{k−1}
These digits b_k are the "α-numeration" of β; integer n has α-numeration digits d_k with n = Σ d_k q_{k−1} (Algorithm 3(i)).

**Central theorem — best left/right α-approximations (Section 4.3):**
{nα} is a *best right (resp. left) α-approximation* of β if it is closer from the right (resp. left) than every {kα}, k<n. A best α-approximation (in circular distance ‖·‖=min({·},{−·})) is always a best right or left approximation.

Prop 9 (best RIGHT, α irrational — Case 2): the best right candidates are n=0, n=Σ_{i=1}^{s} b_i q_{i−1} (terminal, if b_k=0 ∀k>s), and
  n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1},   j ∈ {0,…,b_{2k}−1},  k≥1.

Prop 10 (best LEFT, α irrational — Case 2): the best left candidates are n=Σ_{i=1}^{s} b_i q_{i−1} (if b_k=0 ∀k>s) and
  n = Σ_{i=1}^{2k} b_i q_{i−1} + j·q_{2k},   j ∈ {0,…,b_{2k+1}−1},  k≥0.

The proof derives these from the order isomorphism Λ_α between the α-admissible sequences (with alternate lexicographic order) and [0,1), identifying best sided approximations as minimal points of the sequences ({nα−β}, n) in the product order.

**Why O(log B):** for b limited by B, the CF denominators q_k grow like q_k ~ const^φk (exponentially), so only O(log B) digits/levels k are needed; the candidate enumeration is O(log B). This is the core subproblem: find b∈[0,B] minimizing the circular distance from {bα} to β. Negative b in PE591 is handled by running the same routine with target {−π}=1−{π}.

Related results in the paper: Section 4.1 gives a one-page proof of the **three-distance theorem** (points {kα}, k=1..N−1 divide [0,1] into at most 3 interval lengths, largest = sum of others; explicit lengths in terms of δ_s, δ_{s−1}). Section 2.4 gives the CFE-complement for α-numeration of negative integers.

Full text: `research/cabanillas-labbe-ostrowski-variant.full.md`.

[1904.01874] Contents

A variant of Ostrowski numeration

Emmanuel Cabanillas

ABSTRACT :

In this article, we propose a variant of the usual Ostrowski α \alpha -numeration ( where α \alpha is a real in [0, 1 [[0,1[) that codes integers ( positive as well as negative) and reals of [0, 1 [[0,1[( instead of [− α, 1 − α [[-\alpha,1-\alpha[), so that for every integer n n, n n and { n ​ α } \{n\alpha\} have the same coding sequence. These coding sequences respect natural lexicographic orders and will be used to prove well known results on order properties of Kronecker sequences ( { n ​ α − β }) n (\{n\alpha-\beta\})_{n}.

## 1 Introduction

### 1.1 overview

Ostrowski’s numeration system is based on convergents ( q n) n ∈ ℕ (q_{n})_{n\in\mathbb{N}} of a real α ∈ [0, 1 [\alpha\in[0,1[and code, with a sequence of digits non negative integers as well as reals in [− α, 1 − α [[-\alpha,1-\alpha[( see [6] for the original article and [1] for a survey). Definitions are mentioned in 2.1
In 2.2 and 2.3, we propose a variant of this system : it is still based on ( q n) n (q_{n})_{n}, but the ” markovian condition” is changed and we will be able to code any integer n n and any real { n ​ α } \{n\alpha\} with the same finite sequence ( { x } \{x\} denotes the fractional part of a real x x). We study separately the cases α \alpha irrational and α \alpha rational. This last case could appear uninteresting, but it is useful for applications to numerical semigroups for example ( see [3]).
In 3, we give some dynamical aspects of this α \alpha -numeration.
In 4, we use it to explore some order properties of Kronecker sequences ( { n ​ α + β }) n (\{n\alpha+\beta\})_{n}, as the famous ” three distance theorem”. These sequences have been widely studied with various points of view and we refer to [1] for an exhaustive bibliography.

### 1.2 notations

All along this paper, we will denote : ℤ \mathbb{Z} the set of integers, ℕ ∗ \mathbb{N}^{*} the set of positive integers and ℕ \mathbb{N} the set of non negative integers.
For all reals x x, ⌊ x ⌋ \lfloor x\rfloor denotes its floor , ⌈ x ⌉ \lceil x\rceil its ceiling and { x } \{x\} its fractional part.
For a sequence d = ( d k) k ∈ ℕ ∗ d=(d_{k})_{k\in\mathbb{N}^{*}}, we use the following notations for slices of d d: for all integers r, s r,s such that 0 < r ⩽ s 0<r\leqslant s:

 | d [r, s] = ( d r, d r + 1, ⋯, d s); d [r, ∞] = ( d r, d r + 1, ⋯) d_{[r,s]}=(d_{r},d_{r+1},\cdots,d_{s})\hskip 8.5359pt;\hskip 8.5359ptd_{[r,\infty]}=(d_{r},d_{r+1},\cdots) |  |

We will also use concatenation of sequences and intuitive notations as ( 3, 5, 0 4, 1, 6, 0 ∞) (3,5,0^{4},1,6,0^{\infty}) to denote ( 3, 5, 0, 0, 0, 0, 1, 6, 0, 0, 0, ⋯) (3,5,0,0,0,0,1,6,0,0,0,\cdots). Moreover, if ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} is a sequence of positive integers and if we restrict ourself to sequences in ∏ k { 0 ⋯ a k } \prod_{k}\{0\cdots a_{k}\}, then max \max at the index k k will denote a k a_{k}: for example, ( max, 1, 0, max, 3, ⋯,) (\max,1,0,\max,3,\cdots,) means ( a 1, 1, 0, a 4, 3, …) (a_{1},1,0,a_{4},3,...). So, the notation max r \max^{r} or ( max, 0) r (\max,0)^{r}, where r ∈ ℕ ∪ { ∞ } r\in\mathbb{N}\cup\{\infty\} will often be used. For example : ( 0 2, max 3, 0 4, ( max, 0) ∞) (0^{2},\max^{3},0^{4},(\max,0)^{\infty}) denotes the sequence ( 0, 0, a 3, a 4, a 5, 0, 0, 0, 0, a 10, 0, a 12, 0, a 14, 0, ⋯) (0,0,a_{3},a_{4},a_{5},0,0,0,0,a_{10},0,a_{12},0,a_{14},0,\cdots).

For α \alpha -numeration, we will often use two lexicographic orders on sequences of ℝ ℕ ∗ \mathbb{R}^{\mathbb{N}^{*}}:
▶ \blacktriangleright the reversed lexicographic order ( RLO) denoted ⩽ 𝑅 \underset{R}{\leqslant}:


*[excerpt ends; 153295 characters not shown — see `research/cabanillas-labbe-ostrowski-variant.full.md`]*
