# Operator-filed claims: Yu coupling verification and barrier details

<!-- regenerator-trigger -->

Three results verified this pass and filed so the write-up can cite them. All three
were reproduced by tool_builder (`code/out/operator_verify.captured.txt`, every
program exit 0). The exact oracle is `lib.uc` for the enumeration claims.

```claim
id: yu-certified-point-crosscheck
statement: Yu's certified point is faithfully reproduced: the objective ratio
g/Eh(p) at (alpha=0.035, a=0.3300622, b1=a, b2=1, t=0.38234) evaluates to
1.00000889294, matching the paper's 1.00000889 to 2.937e-9. This was confirmed by
an INDEPENDENT code path from yu_optimization.py (yu_crosscheck.py): explicit
math.fsum over the 4 marginal-atom pairs and the 3 Q-atoms, explicit 3-sort for
phi(1,p,q), no numpy -- a genuinely separate implementation of the same formula.
hypotheses: Yu Entropy 2023 Prop 1 objective; the paper's stated certified point.
holds-here: yes
status: verified computationally (checked), two independent implementations agree
to 2.9e-9
bearing: the 0.38234 record reproduction (yu-record-0-38234) now has a second,
independent route to the same value; the reproduction is not single-route.
anchor: code/out/operator_verify.captured.txt, code/out/yu_crosscheck.py (last
line: Cross-check value 1.00000889, Abs diff 2.937e-09)
```

```claim
id: yu-gamma-hat-nonincreasing
statement: Gamma_hat(t) = sup_alpha inf_{P_pq in F_t} g(P_pq,alpha)/E h(p) is
non-increasing in t. Proof: the feasible set F_t = {symmetric two-atom couplings:
a=(a1+a2)/2 <= t < b=(b1+b2)/2 <= 1, beta=(t-a)/(b-a)} satisfies F_t subset F_{t'}
for t <= t' (raising the ceiling t only adds admissible couplings), so the
infimum over the larger set is no larger; the sup over alpha and non-negativity
of g/Eh preserve monotonicity. Hence Gamma_hat(t) <= 1 for every t beyond the
crossing point t_hat_max.
hypotheses: Yu Prop 1 two-atom symmetric coupling family; t <= t' in (0,1/2).
holds-here: yes
status: proved (set-inclusion argument)
bearing: with Gamma_hat(0.38234)=1.00000889 > 1 and Gamma_hat non-increasing,
Gamma_hat(1/2) < 1: the Yu/Sawin finite-dimensional relaxation certifies nothing
above t_hat_max ~ 0.38235 and in particular does not reach density 1/2. It is the
set-inclusion half of the quantitative barrier; paired with
yu-gamma-half-is-phi-over-2 it puts the number phi/2 on the barrier at t=1/2.
anchor: code/out/yu_optimization_verbatim.md (Claim monotone in t, proof)
```

```claim
id: yu-gamma-hat-scan-values
statement: Scanning the collapsed/high-t region of Yu's Gamma_hat(t) gives the
following values (t : Gamma_hat, alpha*, a1=a2): 0.382: 1.00056231, alpha* 0.0375,
a1 0.32772; 0.454: 0.88344656, alpha* 0.0000, a1 0.381966; 0.48: 0.84137767,
alpha* 0.0000, a1 0.381966; 0.50: 0.80901699, alpha* 0.0000, a1 0.381966.
Between t=0.30 (Gamma_hat ~ 1.13443) and t=0.38 (Gamma_hat ~ 1.00521) the value
drops from above 1 toward the crossing; past the certified max the optimizer
collapses to alpha*=0 with a1=a2=(3-sqrt5)/2, and Gamma_hat(1/2)=phi/2.
hypotheses: Yu Prop 1 objective, full / collapsed coupling optimization as t varies.
holds-here: yes
status: verified-numerically (scan data; the t=0.30..0.38 endpoints 1.13443 /
1.00521 are read off -- see anchor comment); collapse corroborated by
yu-gamma-half-is-phi-over-2 exact value at 1/2.
bearing: numerically confirms Gamma_hat is non-increasing and crosses 1 near
0.382; the extremal a=(3-sqrt5)/2 ties the collapse to the iid-OR barrier constant.
anchor: code/out/yu_optimization_verbatim.md, code/out/yugamma_structure.py
scan values, code/out/yugamma_phi2_claim.md
```

<!-- claim blocks above feed research/CLAIMS.md; command.log scan endpoint
     1.13443 @ 0.30 and 1.00521 @ 0.38 are the run's own recorded scan values -->
