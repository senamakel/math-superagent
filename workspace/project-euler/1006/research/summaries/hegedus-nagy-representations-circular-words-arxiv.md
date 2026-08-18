# Hegedüs & Nagy, "Representations of Circular Words"

**Source:** https://arxiv.org/html/1405.5607v1 (arXiv:1405.5607; EPTCS 151 (2014)
261–270, DOI 10.4204/EPTCS.151.18)

Full text: research/sources/hegedus-nagy-representations-circular-words-arxiv.full.md
Claims from this source: research/notes/wen-wen-and-circular-words-claims.md
(id hegedus-nagy-circular-words-fibonacci-trees)

(Note: the .2014 file is the arXiv *landing page* only; the .arxiv file is the
paper proper.)

## What it establishes

Studies two representations of **circular words** (conjugate classes of finite
words), with the second (tree/trie representation) applied to finite Fibonacci
words.

- **Circular word:** w° = {v | v conjugate of w} = {σ^ℓ(w) | 0 ≤ ℓ < |w|}, the set
  of all cyclic shifts.
- **Lemma 2 (after Séébold):** if u² is a factor of the infinite Fibonacci
  word, then u is a conjugate of some finite Fibonacci word. (Second,
  independent statement of the square-conjugate identification, previously
  anchored by Du–Mousavi–Schaeffer–Shallit.)
- **Theorem 3:** the tree φ_i of the circular Fibonacci word (f_i)° has exactly
  one branching node on every level except the last two. Proof uses the
  Sturmian fact that the number of distinct length-k factors of the Fibonacci
  word is k+1.
- **Corollary 1:** φ_i is a subtree of φ_j whenever j > i (self-similar
  nesting of the factor trees).
- **Theorem 4:** the difference in level of two consecutive branching nodes on
  one path of φ_i is a Fibonacci number (uses Lemma 2).

## Relevance to PE1006

- Second, independent source (an EPTCS workshop paper, open access, not the
  same lineage as the run's other factor-complexity citations) for the k+1
  factor count.
- Independent restatement of Séébold's lemma: u² a factor ⇒ u conjugate to a
  finite Fibonacci word — corroborates `fibonacci-squares-conjugate-finite-word`.
- The Fibonacci-number branching-gap structure (Thm 4) and the subtree-nesting
  (Cor 1) connect to the run's Fibonacci-block renormalisation structure on
  the factor sets.

## Obtained

Open-access full text (arXiv HTML). The `.2014` landing-page download is
redundant and kept only as provenance metadata; use the `.arxiv` file.