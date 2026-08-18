id: g2-mechanical-word-representation
status: conditional
formalisation: code/lean/g2_mechanical_word_representation-d47418d3.lean
statement: For factor length k and convergent index n, if k < fib(n+2), the mechanical/rotation factor set with slope fib(n)/fib(n+2) and intercepts -m*slope for m ≤ k equals the length-k factor set of the Fibonacci word.
source: Berstel, Recent Results on Sturmian Words, rotational-factor theorem (represented by Cited.mechanical_factors in the Lean file).
notes: k is the length, n is the approximant index, and h is the denominator-exceeds-length hypothesis. The result is conditional because the deep Sturmian theorem is cited as an axiom; the Lean implication itself is kernel-checked with no sorry.
