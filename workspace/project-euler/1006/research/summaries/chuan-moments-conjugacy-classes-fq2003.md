# Chuan — Characterizations of α-Words, Moments, and Determinants

Source: Wai-Fong Chuan, "Characterizations of α-Words, Moments, and
Determinants", The Fibonacci Quarterly 41.3 (2003) 194–208. Librarian-
downloaded this cycle as `research/sources/chuan-moments-conjugacy-classes-fq2003.full.md`
(30.7 KB converted text). URL in file: https://fq.math.ca/Scanned/41-3/chuan.pdf
(free from the Fibonacci Quarterly archive).

> **OCR caveat.** The source PDF scanned from the journal converts with heavy
> OCR noise (fragmentary proofs, formulas garbled). The *definitions* and the
> *statement-level* facts below are readable and reliable; individual displayed
> equations should be read in the original PDF before being quoted.

## What it establishes (relevant to PE1006)

This paper studies statistics ("**moments**") over **conjugate classes** of
binary words — the cyclic rotations of a word. These are exactly the objects
Ψ sums over at k = F_n − 1 under directive 1 (the k+1 factors are the F_n
truncated rotations of the standard word). It also characterizes α-words and,
via them, **standard Sturmian words** and the PER set.

Definitions it gives (clean, usable):
- Rotation operator T, conjugate class [w] = {T^j(w)}.
- **Moment** M(w) = Σ_{i=1}^{q} (q+1−i)·c_i for w = c_1…c_q — a weighted
  position-sum of the 1s. M([w]) = set of moments over the class;
  s(w) = max difference of moments within the class.
- α-words defined via the continued fraction of p/q and the word recursion
  w_{−1}=1, w_0=0, w_{k+1}=w_k^{a_{k+1}}·w_{k−1} (the standard-word / PER
  recursion — the same one directive 1's standard word q_n uses).

Key results (statement level):
- **Theorem 4.4** (characterization): if w is an α-word of length q, then
  M([w]) is a set of q **consecutive positive integers** and s(w) = q−1; each
  of these properties conversely characterizes α-words.
- **Corollary 3.2 and Section 3**: characterizations of elements of the PER set
  and of **standard Sturmian words** via these moment conditions.
- Lemma 2.1 (another α-word characterization) used to prove Theorem 4.4.
- The τ ↦ w(τ) map is increasing in lexicographic order from reduced fractions
  in [0,1] onto the Lyndon α-words.

## Relation to PE1006

This gives a **primary combinatorial anchor for the conjugate/rotation
structure** the run sums over at k = F_n−1, complementary to the standard-word
sources (de Luca 1997, Richomme–Saari–Zamboni, cmb-1993 characteristic
sequence) already held. It does **not** give the decimal-value-squared sum Ψ
directly (that combines moments with powers of 10), but the M([w]) = q
consecutive integers fact is a structural statement about how the set of
rotations is distributed — useful cross-check material when the solver handles
the k = F_n−1 case.

Not the adopted general-k route (directive 2's mechanical-word floor-sum for all
k); it supports the k = F_n−1 subcase that directive 1 covers.
