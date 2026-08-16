# Index — code/badprimes

Bad-prime verification over GF(p) by the S_n scheme, a second route distinct
from the minors-criterion computation.

| File | Purpose |
| --- | --- |
| `verify_badprimes_sn.py` | For n = 3, 4 and every prime p < 60, decides CA_{n,p} over GF(p) by checking rad(I_n) = rad(P_n): direction 1 = P_n ⊆ rad(I_n) via Rabinowitsch radical membership (sympy groebner, modulus=p, from lib.casasalvero); direction 2 = I_n vanishes on the pure-power locus. CA HOLDS iff both pass. Second independent route: bounded F_p enumeration (p ∈ {2,3,5,7}, ≤ 2401 polys) through lib.casas_alvero counting explicit counterexamples. Entry guards (pure powers pass, generic fails, char-p witness is a counterexample). Validated against the published lists {2} and {3,5,7} (Castryck et al. 2012 Thm 4 / De Jong–Draisma); capture in code/out/badprimes_sn.captured.txt; exit 0 iff all checks pass. |
