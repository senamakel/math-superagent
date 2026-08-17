# Thread: u-resultant converge-or-dispose

```thread
question: Does the u-resultant n=4 validation close in reasonable time — compute the
      u-resultant, certify V(I)={0} as c·u^B, and match B against prod ord_0(R_i)
      (Valabrega-Valla) — against the run's ground truth (n=4 bad primes {3,5,7},
      lcm J_T=1575, n=3 elimination certificate with both inclusions checked)? If yes,
      what does the projected n=5 cost say about whether a univariate eliminant outruns
      the d=8 Groebner wall (the approach's advertised payoff)? If no, the wall time and
      where it stopped is the measured boundary (directive 13: converge or dispose, one
      shot, no third setup attempt).
status: open
rests-on: badprimes-n4-lcm-jt (code/out/badprimes_n4.captured.txt), macaulays-u-resultant,
      ca-univariate-eliminant-precedent, elimination-n3-certificate (code/out/elimination_n3.captured.txt)
next: One tool_builder run from the existing code/uresultant/ scripts (ureesultant_first_step_clean.py
      plus the underscore probes, each holding one validated piece of the n=4 check) — do NOT
      restart the setup from a fresh Groebner dump. Capture to
      code/out/uresultant_n4.captured.txt with header naming program, oracle function, base
      ring and exact range; temp file, move on exit 0. Validates -> projected n=5 cost, stop.
      Not closing in reasonable time -> measured boundary + close the task.
```

## Context

- The u-resultant approach (`research/approaches/uresultant-one-var-eliminant.md`, adopted):
  for I = (R_1,…,R_{n−1}) ⊂ Q[a_1..a_{n−1}], R_i = Res_x(f, H_i f) (Hasse), the u-resultant
  in a generic linear form factors as ∏_{P∈V(I)} (u−u(P))^{mult(P)}; CA in degree n is
  V(I)={0}, i.e. Res_u = c·u^B. Independent check: B = ∏ ord_0(R_i) under the weighted
  order w(a_j)=j (Valabrega–Valla; equality is STRICTLY STRONGER than CA — a mismatch is
  gr_m evidence about the associated graded, not a CA counterexample).
- **VV hypothesis now source-anchored (scholar, 2026).** The Valabrega–Valla source
  (Nagoya Math. J. 72, 93–101) is held in full and its Thm 2.3 + Cor 2.4 verified
  verbatim. The equality B = ∏ ord_0(R_i) holds iff gr_{m0}(K[a]/(I)) is Cohen–Macaulay.
  A mismatched dangling entailment edge was repaired: `uresultant-multiplicity-trees-new`
  now correctly follows from `uresultant-order-n-n-i-sourced` +
  `valabrega-valla-initial-forms-regular-sequence` (it previously referenced the
  nonexistent `samuel-multiplicity-product-of-orders`). No new CA fact; this anchors
  what the thread already assumed.
- Four cycles produced 15 files in code/uresultant/, all underscore-prefixed probes, no
  capture; a second tool_builder restarted from a fresh Gröbner dump instead of continuing.
- Ground truth held at n=4: bad primes {3,5,7}, lcm J_T = 1575 (badprimes_n4.captured.txt),
  and the n=3 elimination certificate with both inclusions checked (elimination_n3.captured.txt).