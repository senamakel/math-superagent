# van Lint, "A survey of perfect codes" (Rocky Mountain J. Math. 5(2), 1975; doi 10.1216/rmj-1975-5-2-199)

A general survey of perfect codes. Its relevance here is narrow but load-bearing:

## What it establishes for this problem

1. **The five-member list.** For the family of graphs/parameters in the Conway problem (λ=1, μ=2 strong regular context), the members are `9, 99, 243, 6273, 494019`. This is the classic Berlekamp–van Lint–Seidel / Makhnev–Minakova list. It matches the run's independent integrality computation (claim `integrality-five-members`, status: checked): k = u²+u+2, u ∈ {1,3,4,10,31}.

2. **The Berlekamp–van Lint–Seidel construction (243,22,1,2).** The BvLS graph is the coset graph of the perfect ternary Golay code. Construction recipe (verified independently against Wikipedia; used by the oracle):
   - take the 5×11 parity-check matrix H of the ternary Golay [11,6,5] code (kernel = the code);
   - vertices are the 3⁵ = 243 cosets (each = one syndrome, i.e. the 243 cosets of the code in F₃¹¹);
   - two vertices are adjacent iff they differ by a weight-1 vector (± one coordinate), i.e. iff their syndromes differ by ± one column of H;
   - the graph is srg(243,22,1,2), spectrum 4¹³² (−5)¹¹⁰.

The survey's own statement of the five-member list is definitive (Rocky Mountain J. Math., peer-reviewed 1975).

## Does not settle

The construction detail (which cosets, exact H) is standard and confirmed by Wikipedia; the survey itself frames BvLS in the perfect-code context. It does not bear on (99,14,1,2) directly except as the source of the five-member classification and the 243 construction the oracle must reproduce.

```claim
id: five-member-list-vanlint1975
statement: The parameters of the family converge to exactly the five members (9,4),(99,14),(243,22),(6273,112),(494019,994), equivalently k=u^2+u+2 with u in {1,3,4,10,31}; the BvLS graph on 243 vertices exists via the coset graph of the ternary Golay code.
hypotheses: srg(v,k,1,2); standard ternary-Golay machinery.
holds-here: yes.
status: sourced (van Lint 1975, Rocky Mountain J. Math.; cross-checked by exact integrality arithmetic, status: checked)
bearing: fixes the family; supplies the explicit 243 construction the oracle needs as a positive control.
anchor: research/sources/van-lint-perfect-codes-survey-1975.full.md
```

[[van-lint-perfect-codes-survey-1975.full]]
