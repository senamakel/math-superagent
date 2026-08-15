```thread
question: What is the weakest gap-variety / non-degeneracy hypothesis — satisfied by the primes, violated by constant gaps — under which the F₂ transfer ν₂ ≥ c·w holds, restoring G-supply as prime-free?
status: open — Directives 55+56
rests-on: g-supply-transfer-universal-refuted, transfer-matrix-kernel-allones, rule90-interior-xor, g-supply-transfer-measured
blocked-by: none yet
next: |
  1. STOP SWEEPING (Directive 56). The refutation gave a question, not a library
     gap: what do the primes have that constant-gap sequences lack, so switches
     survive into the {0,2} suffix? Library CLOSED (39/46); no search — this is
     tool_builder + theorem_prover, not librarian.
  2. Check the four candidates cheapest-first, each stated prime-free:
     (a) gap variety — the gap sequence takes >=2 values infinitely often;
     (b) non-eventual-periodicity of the halved-gap bit vector h;
     (c) positive density of j with h_j != h_{j+1} — switches one level up;
     (d) the F_2 kernel condition, stated directly as the hypothesis.
  3. For each: check it FAILS on consecutive odds and HOLDS on real primes to
     N=30000, then keep the weakest survivor. Do not re-assert the dead
     universal bound; do not run another sweep.
```
