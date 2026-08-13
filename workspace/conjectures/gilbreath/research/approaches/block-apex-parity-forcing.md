```approach
idea: block-apex-parity-forcing
mechanism: |
  Within the {0,2} regime, the block lemma's apex formula says the block's
  interior evolves by XOR (Rule 90), and the apex value
  A_{k+b_k-1}(1) = 2 · XOR_{j=0}^{b_k-1} [C(b_k-1, j) mod 2 · (A_k(j+1)/2)]
  is exactly 0 or 2 depending on the block's bit pattern.

  Now focus on the boundary: the value A_k(b_k+1) — the "intruder" — meets the
  last block entry A_k(b_k) ∈ {0,2}. After one difference:
    - If A_k(b_k)=0: A_{k+1}(b_k) = intruder (passes through unreduced)
    - If A_k(b_k)=2: A_{k+1}(b_k) = intruder − 2 (reduced by 2)
  So whether the intruder gets reduced depends on the PARITY OF THE LAST BLOCK
  ENTRY.

  The block's apex formula lets us trace the last block entry back through the
  block's evolution. The pattern of 0s and 2s in the block determines, via XOR,
  whether the last entry is 0 or 2 at every depth. In particular, the "erosion
  front" — the value that meets the intruder — is determined by the pattern of
  the original block.

  The new question: can we prove that for the PRIME triangle, the block patterns
  that occur are NOT the worst-case ones? Specifically, the constant block
  (0,0,...,0) and the constant block (2,2,...,2) both have apex 0 (XOR of equal
  bits). If the prime triangle NEVER produces these worst-case blocks beyond
  some small size, then every block has an internal 0↔2 transition, which forces
  the last entry to be 2 at some descendant row, which forces the intruder to
  reduce.

  This reduces regeneration to a DIFFERENT question: classify which {0,2} block
  patterns are realizable from the prime gap sequence under the absolute-difference
  operator. The constant blocks might be ruled out by the mod-4 linearization
  constraint on how blocks form from below.

  Why it's different from mod4-pascal: we don't need mod-8 or higher. We only
  need to show that constant-0 and constant-2 blocks of sufficient length cannot
  form in the prime triangle. This is a statement about the MOD-4 CONSTRAINTS on
  the entries that feed into block formation, not about lifting to higher moduli.

  Why it's different from rule90-absorption: we're not claiming uniform absorption.
  We're claiming that the SPECIFIC worst-case block patterns that would prevent
  absorption cannot arise from the prime gap structure.
status: proposed
first-step: |
  Extract all block patterns (the bit-sequence of 0s and 2s in each {0,2} block)
  from the depth-1000 data. Classify them by length and by whether they are
  constant (all 0s or all 2s) or mixed. Check if constant blocks of length ≥ 3
  ever occur. Then attempt to prove, using the mod-4 linearization backwards,
  that a constant {0,2} block of length ≥ L cannot arise from the prime gap
  sequence — encoding as an SMT query: "does there exist a 2-then-odds start
  whose triangle develops a constant {0,2} block of length L?"
```