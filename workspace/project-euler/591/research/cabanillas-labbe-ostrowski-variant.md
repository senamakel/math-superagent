> **Excerpt only — read this first.** The complete text is beside it at `research/cabanillas-labbe-ostrowski-variant.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://ar5iv.labs.arxiv.org/html/1904.01874 | converted from HTML -->

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
