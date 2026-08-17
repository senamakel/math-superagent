# Currie & Saari — *Least Periods of Factors of Infinite Words* (RAIRO-ITA 43, 2009)

Source: https://www.numdam.org/item/ITA_2009__43_1_165_0.pdf
(full text: [[currie-saari-least-periods-factors.full]])

## What this source establishes

This paper initiates the study of the **period set** of an infinite word — the
set of positive integers occurring as the least period of some factor.

**Main results.**

- Theorem 2: every positive integer occurs as the least period of some factor
  of the **Thue–Morse** word.
- For **Sturmian words**, the period set is characterized (Corollary 3); in the
  **Fibonacci** case (Corollary 4): **the least period of any factor of the
  Fibonacci word is a Fibonacci number** — and conversely every Fibonacci
  number occurs as a least period. This is the primary peer-reviewed anchor for
  the fact the run previously only had from Wikipedia.

**Structural lemmas relevant to PE1006.**

- Lemma 8 (de Luca–De Luca): the least period of a factor w equals the length
  of a longest unbordered factor of w.
- Theorem 3: the fractional root of a factor of the Fibonacci word x is a
  conjugate of some standard word t_m (m ≥ −1); Corollary 6: a finite word is a
  factor of a Sturmian word **iff** its fractional root is a conjugate of a
  standard word — the finite↔infinite bridge also present in
  Bugeaud–Reutenauer (on disk).
- Corollary 8: for n ≥ 2 the least period of the standard word s_n is q_{n−1}.

**Fibonacci conventions.** The paper's Fibonacci word x has standard words
s_n = s_{n−1}^{d_n} s_{n−2}, directive sequence (1,1,1,…) — the same object as
the problem's S_n limit, in the standard-word construction.

## What it implies for PE1006

1. Replaces the Wikipedia-carried "least period of a subword is a Fibonacci
   number" with a primary source (Cor 4).
2. Corollary 6 is a second bridge for the k = F_n − 1 factor-set statement:
   the k+1 factors at length F_n − 1 are the truncated rotations of the
   standard word q_n, and fractional roots/conjugates of standard words are
   exactly the objects whose factors are Sturmian — supporting directive 1's
   autocorrelation counting.
3. Least periods being Fibonacci constrains what repeated structure length-k
   factors can have (no small non-Fibonacci periods), which is relevant for the
   leading-zero / duplicate handling in the sum.

## Claims anchored here

`fibonacci-least-period-set` (research/notes/sourced-claims-least-periods-standard-factors.md).

## What it does NOT establish

- Nothing about reading factors as decimals or summing squares.
- Nothing about the mechanical-word / floor-sum primitive.
- The period-set statement is the Fibonacci-word side; the general Sturmian
  period-set characterization is Corollary 3 (not needed here beyond
  confirming the Fibonacci special case).