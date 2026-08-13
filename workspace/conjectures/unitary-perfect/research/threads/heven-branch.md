# Thread: closing the H_even branch (finiteness of Subbarao–Warren reduction)

```thread
question: Is H_even = { even m : every prime factor of 2^m+1 is 3-Higgs }
  finite? (Equiv by arXiv:2605.20475 Thm 7 to the prime branch {2p : 2p∈H_even}.)
status: open — the paper proves thinness, a finite frontier, and the structural
  reduction, but explicitly does not prove finiteness
rests-on: hb-prop4-structural (Higgs-cubefree structure), heven-prime-case-reduction,
  heven-thinness-not-finiteness, hb-thm30-conditional, heven-two-mod-four
blocked-by: the divisor-level gap on Phi_{4p}(2) — primitive divisors r of
  Phi_{4p}(2) need ord_r(2)=4p, r≡1 mod 4p, (r-1)/4p∈S_3^{(≤3)}; log-mass forces
  mass ≫p while Ford-type thinness gives only reciprocal mass O(1/p), an
  exponential 2^{2p}/p gap. GRH/Chebotarev are the wrong scale (finite divisor
  set, not a prime range). Conjectures 24 (log-mass) and 29 (mod-16
  equidistribution) are the recommended targets; Thm 30 needs both H1 and H2
  conjectural. The 2-adic line is exhausted once m=2p (all surviving candidates
  are 2 mod 4).
next: divisor-transference / divisor-level equidistribution for prime divisors
  of Phi_{4p}(2) — the paper states no such theorem exists in the literature.
  Establishing (or refuting) Conj 29's c·ω(Phi_{4p}(2)) mod-16 lower bound, or
  a log-mass statement, is the open move.
```

## Key facts

- Every prime divisor of a UPN is 3-Higgs; `p` is 3-Higgs iff each prime factor
  `q` of `p−1` is 3-Higgs and `v_q(p−1) ≤ 3`. Smallest omitted prime is 17.
- Prop 4: members of H_even are doubled Higgs-cubefree values (factors 3-Higgs,
  exponent ≤3, closed under odd divisors).
- Thm 7: `|H_even| ≤ 4^N` where N = size of the 2p prime branch.
- Thm 21: power-saving thinness but not finiteness (exponential at height
  x = 2^{2k}).
- The impostor-branch within box ℬ (p≤2000, e≤6, at max a=10000) is closed
  rigorously by the three-filter certificate (Z/N/O); the whole UPN question is
  reduced to H_even finiteness.

## Claims this thread relies on

`hb-prop4-structural`, `heven-prime-case-reduction`, `heven-thinness-not-finiteness`,
`heven-verified-members`, `heven-two-mod-four`, `hb-lemma20-closures`,
`hb-thm30-conditional`, `hb-no-v2ge4-witness-1e11`.
