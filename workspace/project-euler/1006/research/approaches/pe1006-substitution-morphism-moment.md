# Approach: morphic / substitution transfer-matrix recursion for Ψ(k)

```approach
idea: The infinite Fibonacci word F is built by the substitution
      0 -> 01, 1 -> 0 (S_n = S_{n-1} S_{n-2} is exactly the n-th iterate).
      Carry the *set-valued* quantity Ψ(k) (or rather the vector of the k+1
      factor values) through the substitution using the concatenation identity
      value(ab) = value(a)·10^{|b|} + value(b). Because the factor set of a
      Sturmian word is substitution-recursive (standard-word / Berstel
      factor-structure), Ψ over factors of one length maps to Ψ over factors
      of a stretched length by a matrix (transfer) built from Kronecker
      products of the base-10 position weights with the substitution matrix.
      The intended result: an O(log k) recursion for Ψ, orthogonal to the
      floor-sum machinery, from the morphism itself.

mechanism: Substitution 0->01, 1->0 sends each letter to a word, and extends
      linearly over concatenation. Concatenation in base 10 is
      val(ab)=val(a)10^|b|+val(b), so val^2 and the positional weights form a
      quadratic form closed under the letter map. The factors of the Fibonacci
      word of length k, ordered by first occurrence, shift by one letter under
      windowing; the set is deterministic by the substitution. The second
      moment then satisfies a recursion whose step cost is a bounded matrix
      product (Kronecker structure), not k. This is the *combinatorics on
      words / substitution dynamics* representation, distinct from the
      mechanical-floor-sum representation the run currently uses.

status: refuted

killed-by: The substitution does NOT push the factor set of length k onto a
      single length-(~φk) factor set, so the commuting square that a
      transfer-matrix recursion needs does not exist. A length-k factor w with
      c ones is mapped by 0->01,1->0 to a word of length k+c. A Sturmian word
      is balanced, so the number of ones in its length-k factors takes at most
      two consecutive values {m, m+1} (Perrin-Restivo, A note on Sturmian
      words, TCS 2011; Sturmian balance). Hence the images of the k+1 factors
      have TWO different lengths (k+m and k+m+1), not one, and there is no
      single factor-set of one length they all land in — the morphism does not
      close Ψ at one length. The substitution/Christoffel machinery (Fici,
      arXiv:1508.06754; Perrin-Restivo) is real and standard, but it governs
      counting and factor *structure*, not a sum of the decimal values of the
      factors of one fixed length; no source applies a transfer matrix to that
      sum, and the reason is the variable image length above. The method is
      wrong in cost the moment one tries to force a single length.

precedent:
      - Perrin & Restivo, "A note on Sturmian words", Theoretical Computer
        Science 2011, doi:10.1016/j.tcs.2011.12.047 (Sturmian = balanced
        factor structure; factors are conjugates of standard words).
      - Fici, "Factorizations of the Fibonacci infinite word", arXiv:1508.06754
        (Christoffel/singular-word factorisations of F — the substitution
        structure at the *factor* level, length-changing).
      - Decision algorithms for Fibonacci-automatic words (Du, Mousavi,
        Schaeffer, Shallit, arXiv:1406.0670) — the standard way substitution
        structure is turned *computational*; it is automata, not a value-sum
        transfer matrix.
      No source applies a morphic transfer matrix to a sum of decimal factor
      values; the length-changing obstruction is structural, not a search gap.

first-step: None — closed. If this idea is ever revisited, it must first find a
      way to make the image lengths coincide (e.g. padding), which changes the
      decimal value and breaks the very identity it wants. Not pursued.
```

## Assessment for the run

This idea fails on a **structural** ground, not on absence of literature: the
Fibonacci substitution stretches a length-`k` factor by one letter per `1` it
contains, and Sturmian balance leaves that count two-valued, so the substituted
factor set does not have one common length. The transfer-matrix/commuting-square
picture the method needs cannot be drawn. Rejected on that basis.
