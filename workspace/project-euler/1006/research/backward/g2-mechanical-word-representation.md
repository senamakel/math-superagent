# g2-mechanical-word-representation

```skeleton
evidence: code/refute/G2-slope-refutation.md, code/out/check_slope.captured.txt, research/notes/mechanical-slope-correction.md.
goal: The k+1 length-k factors of F are produced exactly by the rotation/mechanical construction with slope a=F(n-2)/F(n) (= fib(n)/fib(n+2), the continued-fraction convergents to 1/phi^2), F(n)>k.
implies: This is what rewrites the factor set (which is what Psi is over) into a sum over m=0..k of v(x_m), the object Lemmas 3-4 can handle.
rests-on: mechanical-word-digit-rule, g2-mech-shell-exact-binary, governing-sturmian, conjugate-christoffel-factor-sturmian
status: discharged — mechanical-word-digit-rule + g2-mech-shell-exact-binary + in-container machine check mech_psi == brute k=1..50 (code/out/mech_psi.captured.txt): the set {v(x_m)} equals the factor-set decimal values at every k tested. The deep identity mech_reproduces_factors is executed, not yet stated as a lemma; formalisation nicety, not a numerical gap.
```
