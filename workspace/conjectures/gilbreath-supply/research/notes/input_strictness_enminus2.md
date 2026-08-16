# Switch density is not necessary for linear supply: the h = e_{n-2} witness

Directive 38 asks for the precise statement of what `code/out/input_strictness_capture.txt`
exhibited, with the scope kept scrupulous: this is a fact about the fold as a
property of *strings*, and it says nothing about the primes.

```claim
id: enminus2-linear-supply-switch-density-not-necessary
statement: The per-window family h^(n) = e_{n-2} (a single 1 at index n-2, zeros
  elsewhere in a length-n window) has switch density 1/n -> 0, yet
  nu2(n) = wt(Phi_n h^(n)) = ceil((n-2)/2) ~ n/2 = Theta(n) — linear supply.
  Mechanism: the fold cell T(n,d) = XOR_{o subseteq d} h[n-1-d+o] reads position
  n-2 exactly when the offset o = d-1 is a submask of d, which holds exactly when
  d is odd (for even d the low bit of d-1 is set while d's is clear); hence
  nu2(n) = #{odd d in [2, n-1]} = ceil((n-2)/2).
hypotheses: floor convention at index 2, d-range [2, n-1]; fold cell
  T(n,d) = XOR_{o subseteq d} h[n-1-d+o]; h inspected per window (a fresh string
  of length n for each n), NOT fixed across n.
holds-here: yes — the odd-depth count is an exact all-n formula, and the capture
  reproduces it at every n in [8, 4000] (spot values n=8: S=0, nu2=3; n=53:
  S=1, nu2=25; n=4000: S=0, nu2=1999), cross-checked s_sos == s_direct; the
  canonical prime guard nu2(53)=18, nu2(64)=27 passes first.
status: proved (the mechanism is a hand derivation valid for all n; the capture
  is the confirming check to n=4000, not the evidence) — per-window family, NOT
  a fixed string.
bearing: Positive mod-4 switch density is NOT necessary for linear supply: the
  property "nu2(n) >= c n for all large n" does not imply positive switch
  density as a property of strings, so supply is strictly weaker than switch
  density and the first pass's "equivalence to switch density indicated" is
  refuted from the other side too (complementing the collapse refutation in
  research/REOPENED.md). This gives NO arithmetic input controlling the PRIMES:
  SUPPLY for the prime gap-parity string stays open in full. It bears on
  problem.md result type 4 (an input strictly weaker than switch density), NOT
  result type 1 (unconditional SUPPLY). A FIXED single 1 gives nu2(n) = O(1)
  (claim fixed-single-1-fold-weight-bounded-by-j); the witness is the
  per-window family, and its support must be read as the single index n-2 in
  the length-n window.
anchor: code/order_k/input_strictness.py; code/out/input_strictness_capture.txt;
  this note.
```
