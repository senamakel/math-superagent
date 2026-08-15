```thread
question: Why does the F₂ transfer die exactly on dyadic-periodic h, and what anti-dyadic property of the prime halved-gap bit string restores ν₂ ≥ c·n?
status: open — Directive 58 (stage-1 numbers measured host-side; prove the dichotomy, do not survey it)
rests-on: rule90-interior-xor, g-supply-transfer-universal-refuted, transfer-matrix-kernel-allones, g-supply-transfer-measured
blocked-by: none yet
next: |
  Directive 58. Stage-1 numbers are MEASURED HOST-SIDE — reproduce, do not
  re-explore. Periodic halved-gap bit string h, gap = 2 if bit else 4,
  nu2 = #2s in the maximal {0,2} suffix of the right diagonal, exact integers:
    period 1 (h=1)         nu2 = 1   at n = 200,400,800,1200
    period 2 (h=01)        nu2 = 2   at all four n
    period 4 (h=0001)      nu2 = 2   at all four n
    period 8 (h=00000001)  nu2 = 2   at all four n
    period 3 (h=001)       nu2 = 133, 264, 533, 798
    period 5 (h=00001)     nu2 = 104, 210, 424, 638
    period 6 (h=000001)    nu2 = 134, 264, 534, 796
    period 7 (h=0000001)   nu2 = 112, 112, 685, 684
  Dichotomy: nu2 = O(1) exactly on power-of-2 periods, nu2 ~ c*n otherwise
  (c in [0.53, 0.67]); period 6 = 2*3 grows, so the ODD FACTOR matters, not
  merely being non-dyadic.
  0. STEP 0 (Directive 59 — the falsifier is drafted and UNRUN, so this is one
     command, not another note): `timeout 600 python3 code/out/dyadic_periodic_check.py
     2>&1 | tee code/out/dyadic_periodic_check.captured.txt`. Report periods 1..8,
     nu2 over n=50..500, and say plainly whether the odd-factor periods grow.
     If they do NOT grow, close this thread — the dyadic story is dead, which is
     a good outcome, not a failure.
  1. tool_builder — confirm the eight rows above and extend to periods 9..16
     and to non-constant patterns of the SAME period (the claim is about the
     period, not the specific word).
     **Scholar note (library closed): reproduce with code/out/reproduce_dyadic_periodicity.py,
     and reconcile the period-2 value against the held alternating-2/4(=h=10)
     measurement nu2=1 (nu2-transfer-not-restored-by-nondegeneracy). By
     transfer-matrix-kernel-allones (complement-immaterial), h=01 and h=10 give
     the same tail, so stage-1 nu2=2 and directive-55 nu2=1 cannot both be right
     as stated — find the convention/off-by-one.**
  2. theorem_prover — prove from Lucas: h eventually periodic with period 2^k
     forces nu2 = O_k(1); and (harder) an odd factor in the period forces
     nu2 >> n.
     **Scholar note: the collapse leg is ALREADY the proved rule90-interior-xor
     (any period p bounds the folds by the period word, O_p(1)) — it needs no
     new source; BCZ Thm 5 is NOT the mechanism. The odd-factor growth leg is
     genuinely new and is the real open content — nothing held explains it.**
  3. State the dichotomy theorem, then say precisely what it does and does NOT
     give for the primes: aperiodicity alone is weaker than the quantitative
     anti-dyadic input the supply bound needs; the gap between them is the
     honest remaining statement. Do NOT claim it closes G-supply.
```
