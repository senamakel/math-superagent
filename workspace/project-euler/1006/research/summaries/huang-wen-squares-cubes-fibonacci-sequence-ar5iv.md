# Huang & Wen — Number of distinct and repeated squares and cubes in the Fibonacci sequence

Source: Yuke Huang, Zhi-Ying Wen, "The number of distinct and repeated squares
and cubes in the Fibonacci sequence", arXiv:1603.04211 (2016).
Full text: `research/sources/huang-wen-squares-cubes-fibonacci-sequence-ar5iv.full.md`
(URL recorded in file: https://ar5iv.labs.arxiv.org/html/1603.04211).

## What it establishes

- Studies the Fibonacci sequence F, fixed point of σ(a,b) = (ab, a), with
  prefix F[1,n] of length n.
- Gives **explicit expressions for all squares and all cubes** in F, via the
  recursive structure of squares and cubes (return-word analysis).
- Determines the **number of distinct squares** A(n) and cubes C(n) in F[1,n]
  for all n, and gives algorithms counting repeated squares B(n) and repeated
  cubes D(n); for special n = f_m (Fibonacci numbers) it recovers known results
  (Fraenkel–Simpson, Shallit et al.).
- Key structural tools: return words, the recursive square/cube structure
  (positions Γ_{1,m,p}[i], Γ_{2,m,p}[i]), and the exact criteria for when
  ω_p ω_{p+1} is a square factor / ω_p ω_{p+1} ω_{p+2} is a cube factor.
- Generalises Iliopoulos–Moore–Smyth's square characterization to explicit
  counting formulas for arbitrary prefixes, not just Fibonacci-number lengths.

## Relevance to PE1006

This is the primary treatment of the **repetition (square/cube) structure of
the Fibonacci word**, the object the run's "squares are cyclic rotations of
Fibonacci words" claim (fibonacci-squares-conjugate-finite-word, from
Du–Mousavi–Schaeffer–Shallit) is about. It gives the recursive structure that
any Fibonacci-block renormalisation of Ψ must respect, and provides exact
counting formulas usable as bounded cross-checks. It does not give the
decimal-valued second moment Ψ — that remains the run's own construction.

## Claim block

```claim
id: huang-wen-squares-cubes-fibonacci-recursive-structure
statement: All squares and all cubes of the Fibonacci sequence (fixed point of
a→ab, b→a) admit explicit expressions built from return words; the numbers of
distinct squares/cubes in any prefix F[1,n] are computable for all n, with
closed forms at Fibonacci-number lengths recovering Fraenkel–Simpson and Shallit
results; repeated-square/cube counts have linear-time algorithms.
hypotheses: F the infinite Fibonacci sequence, σ(a,b)=(ab,a); F[1,n] its length-n prefix.
holds-here: true — PE1006's S_n limit is the same word (0→01, 1→0 is the letter-renamed σ).
status: sourced
bearing: Primary recursive-structure source for squares/cubes in the Fibonacci
word — the shape any Fibonacci-block renormalisation of Ψ must respect; supplies
exact bounded cross-checks. Not the G4 decimal second-moment collapse.
anchor: research/sources/huang-wen-squares-cubes-fibonacci-sequence-ar5iv.full.md
(https://ar5iv.labs.arxiv.org/html/1603.04211)
answers: frontier-square-structure-cluster
```
