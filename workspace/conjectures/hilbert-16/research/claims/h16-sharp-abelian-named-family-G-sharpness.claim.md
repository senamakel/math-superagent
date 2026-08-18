```claim
id: h16-sharp-abelian-named-family-G-sharpness
statement: Given SharpnessData carrying a rational named family of degree <= n, h₀>0, rank μ, N=μ−1, N disjoint subintervals of (0,h₀) with certified simple Abelian-integral zeros, and the lower/upper cyclicity inequalities N≤cycl≤N, the cyclicity equals N.
status: formalised
formalisation: code/lean/h16_sharp_abelian_named_family_G_sharpness-a2083575.lean
```

Binder correspondence: `n`, `degree_le`, and `parameters` carry the degree and rational-parameter hypotheses; `μ`, `N`, and `N_eq` carry N=μ−1; `h₀` and `h₀_pos` carry the interval endpoint hypothesis; `I`, `intervals`, `disjoint`, `inside`, and `simple_zero` carry the zero-certificate data; `sturm_certified` records the alternative exact certificate interface; `cyclLower` carries the Abelian/Melnikov lower-bound implication and `upper` carries the independently established upper bound. The file proves only equality from these supplied hypotheses/data; it does not establish existence of a SharpnessData witness, nor does it formalise interval arithmetic, Sturm theory, or the dynamical reduction.