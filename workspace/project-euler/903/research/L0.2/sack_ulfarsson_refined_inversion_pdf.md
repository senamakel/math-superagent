# Summary — Sack & Úlfarsson, *Refined inversion statistics on permutations*

Source: https://arxiv.org/abs/1106.1995 (arXiv:1106.1995, math.CO, 2012), full text in
[[sack_ulfarsson_refined_inversion_pdf.full]].

This is the gap-resolved inversion literature for permutations: k-step inversions
(inversions (a,b) with b−a=k) and non-inversion sums. Key results:
- **Thm 4.4** (k-step inversion distribution): H_{n,k}(x)=I(n,k,0)·A_s^t·A_{s-1}^{k-t}
  with Eulerian polynomials A and binomial-product I. Closed form for inversions at a
  single fixed gap k.
- **Thm 2.5** dot-product identity: 1·π = 1·1^c + ninvsum(π) = n(n+1)(2n+1)/6 − invsum(π).
  Cor 2.6: ninvsum(π∘ρ)=π·ρ^{-1}−1·1^c.
- **Zone-crossing vectors** (Def 3.1, Prop 3.3, Lemma 3.4) uniquely encode π and the
  non-inversion sum; **Thm 3.8** recurrence for the ninvsum distribution N_n(q).

Relevance: gives exact per-gap inversion machinery for f_n(k)=A_n+(k−1)B_n. It treats
only the single permutation π, NOT the cyclic subgroup {π^i} that PE 903 sums ranks
over — so it is a route to A_n,B_n, not the Q(10^6) answer.
