# Refutation note: I^1_6b ECT shortcut

```claim
id: i6b-ect-four-passage-closure-refuted
statement: Four passage contributions that are individually ECT can be summed and remain ECT.
status: checked
counterexample: Over Q[x], p=(1,x), q=(-1,-x). Their two-function Wronskians are W(p)=1 and W(q)=1, but p+q=(0,0), so W(p+q)=0. The family (a, ax) has W=a^2 and loses rank at a=0.
search-frame: exact polynomial representatives degree <=1; algebraic fragment, not a faithful I^1_6b model.
evidence: code/refute/i6b_ect_obstruction_exact.py; code/out/i6b_ect_obstruction_exact.captured.txt
falsifier: A structural sign/separation condition on the actual four Dulac leading coefficients excluding cancellation uniformly on every parameter stratum.
```

The smallest obstruction is cancellation/rank loss, not a verified zero of the actual I^1_6b displacement. It refutes the inference “each of four second-type pieces is ECT, therefore their total is ECT.”

Roussarie–Shan–Zhu (2015), Theorem 1.1 discussion, states that some I^1_6b limit-periodic sets involve four second-type Dulac maps and cannot be reduced to one equation; in the center case they require two equations in `(r1,rho1,r2,rho2)` with `r_i rho_i=nu_i`. Their Theorem 2.3 gives a first-type resonant expansion with property-J remainder, not the needed four-map uniform composition. Therefore this is a checked obstruction to the shortcut, while the full dynamical claim remains undecided.

Uniformity also fails in the toy at the leading-coefficient-zero stratum: `W=a^2` for `a != 0`, but vanishes at `a=0`. A real proof must stratify slow-divergence/leading-coefficient zeros and control the next nonzero term; compactness alone does not give a uniform ECT bound.
