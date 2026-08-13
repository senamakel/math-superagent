```approach
idea: sofic-block-suffix-subshift
mechanism: |
  Studies the sequence of block patterns {B_k} as a formal language over the 
  alphabet of halved suffixes + intruder values. The conjecture "A_k(1) ∈ {0,2} 
  for all k" is exactly "the empty word is never in the language." If the 
  suffix+intruder process is a sofic system (factor of a subshift of finite type), 
  then Perron–Frobenius on the finite transfer matrix decides reachability of 
  the empty word — the conjecture reduces to a finite-automaton non-reachability 
  check.
status: refuted
precedent: |
  > Run's own event-rate sweep (code/out/event_rate_sweep_analysis.captured.txt, 
  1154 sequences): the step law, drain law, and {0,2}-closure — i.e., the 
  suffix+intruder state-transition mechanism — is IDENTICAL in dying and surviving 
  families. 852/1154 die, 302 survive; the mechanism that governs suffix transitions 
  is the same in both. What distinguishes them is the STARTING GAP SEQUENCE's 
  frequency profile, not any property of the suffix process itself. So the 
  suffix automaton captures the mechanism but NOT the distinguishing property.
  
  Additional structural problems: (1) the block length b_k grows to > 10^6 
  (code/out/block_constancy.json, max_b = 1,270,444), so the suffix set never 
  stabilizes at small L — any L capturing the boundary state must encode the 
  growing XOR-history of the block tail; (2) max_r0 = 29 in the live regime 
  (code/out/block_constancy.captured.txt), so even the "edge-0 run length" 
  state needs depth ≥ 30, making the suffix not small; (3) the intruder is 
  bounded (≤ 14 in live regime) but the SOURCE of intruders (prime gaps) is 
  unbounded — the finite alphabet property holds for the intruder value but 
  not for the process that generates it.
  
  Contrast with backward-extension-automaton: that was refuted because valid-extension 
  sets are GLOBAL (factorial-weighted); this proposal is FORWARD and CAN be sofic 
  even when backward is not. But the sweep data shows the sofic property, even if 
  it held, would encode the wrong thing — the mechanism, not the rate. The 
  distinguishing property is the gap-sequence frequency, which is not a finite-state 
  property of the suffix process.

killed-by: |
  The sweep data (1154 sequences) shows the suffix-process mechanism (step law, 
  drain law, XOR interior) is identical in dying and surviving families; the 
  distinguishing property is the gap-sequence frequency profile, not a suffix 
  state-transition property. Additionally: b_k grows unboundedly (> 10^6), the 
  suffix set does not stabilize at small L, max edge-0 run = 29 requires L ≥ 30, 
  and unbounded prime gaps mean the generating process is not finite-state. The 
  approach encodes the mechanism (which is universal) but not the rate (which is 
  the whole open question).
first-step: — (refuted)
```