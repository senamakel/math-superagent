# Wen & Wen, "Some properties of the singular words of the Fibonacci word"

**Source:** https://www.mat.univie.ac.at/~slc/opapers/s30wen.pdf
(Séminaire Lotharingien de Combinatoire, preprint of W.-F. Wen & Z.-Y. Wen,
published in European J. Combin. 15 (1994) 587–598, DOI 10.1006/eujc.1994.1060)

Full text: research/sources/wen-wen-singular-words-fibonacci-word-1994.full.md
Claims from this source: research/notes/wen-wen-and-circular-words-claims.md (id wen-wen-singular-words-structure)

## What it establishes

Introduces the **singular words** w_n of the Fibonacci infinite word F_∞ and
studies their structure — the factor-structure side of the factor set the run
sums over.

- **Definition:** the singular word w_n is the word obtained by complementing
  the first letter in a left rotation of the finite Fibonacci word F_n
  (equivalently the unique word that differs from the conjugates of F_n).
- **Two decompositions (Theorems 1 & 2):** F_∞ = ∏ (singular words) in two
  canonical ways — the singular-word concatenation factorization of the
  Fibonacci word.
- **Structural properties:**
  - w_n is a **palindrome** for n ≥ 1 and **primitive** for n ≥ 2 (Lemma 1/2).
  - w_n appears only once in F_{n−1}F_n (Lemma 2).
  - Recursive structure: w_n = w_{n−2} w_{n−3} w_{n−2} (singular-word
    self-similarity), linking adjacent singular words.
  - Adjacent singular words of the same order are positively separated
    (Cor 2); w_n has no overlap (Cor 4).
- **Powers of factors (Theorem 3):**
  - w_n² never occurs as a factor of F_∞;
  - (C_k(F_n))² does occur for 0 ≤ k ≤ f_n − 1;
  - u⁴ never occurs for any factor u of F_∞.
- **Special words (Theorem 5):** a factor w is a special word iff w is a
  prefix of some F_n — the one right-special-factor-per-length structure.
- **Overlaps (Theorem 6, Cor 6):** for f_n < |u| ≤ f_{n+1}, u ≠ w_{n+1}, u is
  an overlapping factor iff w_n is not a factor of u; the overlap of u is then
  unique, of length |u| − f_n.

## Relevance to PE1006

The singular words and the prefix-characterization of special factors are the
structural backbone of the factor set { length-k factors of the Fibonacci
word }. The theorem that special factors are exactly the prefixes of finite
Fibonacci words corroborates the run's claim
`fibonacci-unique-special-factor-reverse` (one right-special factor of length
n, the reverse of the length-n prefix) from a second, primary source. The
power-facts (Theorem 3) are the source-level basis for the run's observation
that no factor is square-heavy, which bounds the Lmin/window-prefix length.

## Obtained

Free full text (Séminaire Lotharingien de Combinatoire). This is the *primary*
statement of the singular-word construction (later also treated in Fici's
factorizations survey on disk).