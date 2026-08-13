# Sharp asymptotics of the 3-Higgs semigroup as a Burris–Yeats fragment process

```approach
idea: Treat the 3-Higgs primes P_3 and their cubefree semigroup S_3^{(≤3)} as a
  self-referential "prime fragment" process in the sense of Burris–Yeats (the
  paper's own citation [16]), and derive *sharp local* asymptotics of
  S_3^{(≤3)} from the fixed-point functional equation of its generating
  Dirichlet series, to turn the paper's too-strong Theorem 27 hypothesis into a
  checkable statement about the joint distribution {4pk+1 prime, k ∈ S_3^{(≤3)}}.
mechanism: The pair (P_3, S_3^{(≤3)}) satisfies the coupled fixed point
  P_3 = {p prime : p−1 ∈ S_3^{(≤3)}} and S_3^{(≤3)} = the monoid on P_3 with each
  exponent ≤ 3. Hence the Dirichlet series
  Z(s) = Σ_{k ∈ S_3^{(≤3)}} k^{−s} = ∏_{p ∈ P_3} (1 + p^{−s} + p^{−2s} + p^{−3s})
  satisfies a functional equation whose coefficients are the primes of P_3, which
  are in turn defined by the values of Z's coefficients — a genuine
  self-referential "fragment" structure of the kind Burris–Yeats formalise for
  subprime (Higgs) sequences. Singularity analysis (Flajolet–Odlyzko transfer)
  of Z(s) at its abscissa of convergence σ_3 recovers the thinness exponent η,
  and — the new part — the *local* (short-interval, friable-number-like)
  distribution of S_3^{(≤3)}. Conjecture 23 is precisely a statement about that
  local distribution: no prime r with ord_r(2) = 4k has (r−1)/4k ∈ S_3^{(≤3)}.
  Expressing the admissible log-mass (C24) or the C23 obstruction as a Mellin
  transform / contour integral of Z(s) turns the δ in C24, or the finiteness in
  C23, into a statement about the *singularity and residue* of Z(s), attackable
  by transfer-operator or saddle-point methods — a change of representation away
  from both enumeration and Chebotarev. Named machinery: Burris–Yeats prime
  fragments, formal Dirichlet series with a fixed-point equation, and
  singularity analysis (Flajolet–Odlyzko).
status: proposed
first-step: (1) Write down the exact fixed-point equation satisfied by the
  counting function Π_3(x) = #{p ≤ x : p ∈ P_3} in terms of the cubefree
  semigroup S_3^{(≤3)}, and the matching functional equation for Z(s). (2)
  Numerically compute σ_3 and the thinness exponent η from the first ~10^6
  elements of P_3 (recomputed independently), and test whether the singularity
  of Z(s) is algebraic or logarithmic — that classification decides whether the
  local distribution is accessible by transfer operators. (3) Identify what
  local smoothness of S_3^{(≤3)} would make the paper's Theorem 27 hypothesis
  (currently "too strong") checkable.
```

## Notes for the research check

- **Distinct from everything on the list**: no approach so far has used
  generating functions / analytic combinatorics of the semigroup. The paper's
  Theorem 27 is the *qualitative* "semigroup-growth route" whose hypothesis the
  paper itself calls too strong; this proposal aims for *sharp* (residue-level)
  asymptotics, which is a different and finer claim, and targets C23/C24 through
  the local distribution rather than through global thinness.
- **Falsifier**: if the singularity of Z(s) at σ_3 turns out to be of a type
  (e.g. essential) that yields no short-interval control of S_3^{(≤3)}, the
  transfer to C23 fails and this route gives only a re-derivation of thinness.
- **Cost**: enumeration only to ~10^6 for the exponent/numerical check; the real
  work is the fixed-point analysis.
- Speculative level: high — the Burris–Yeats theory is qualitative about fragment
  counts, and it is not established that it delivers local (not just global)
  asymptotics of this particular capped semigroup; research should check whether
  anyone has done singularity analysis on a Higgs-type semigroup.
