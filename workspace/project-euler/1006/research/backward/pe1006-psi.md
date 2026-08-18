```skeleton
goal: Compute Ψ(10^18) mod 101001001 for the Fibonacci subword second moment defined in GOAL.md.
implies: G1 identifies F_k with the k+1 length-k factors of the infinite Fibonacci word; G2 parametrises those factors by mechanical-word intercepts x_m=-m·a for an admissible Fibonacci convergent a; G3 rewrites each factor's decimal value as the telescoped quantity v_a(m), so Ψ(k)=Σ_{m=0}^k v_a(m)^2. G4 evaluates this coupled sum modulo 101001001 in fixed dimension and O(log k), and proves the result is independent of the admissible convergent. Applying the evaluator at k=10^18 yields the goal.
status: live
rests-on: pe1006-psi/G1-finite-subword-limit-identification, pe1006-psi/G2-mechanical-factor-parametrisation, pe1006-psi/G3-telescoped-decimal-second-moment
```

```gap
id: pe1006-psi/G4-joint-intercept-evaluation
lemma: There exists an explicitly defined fixed-dimensional state σ(a,k), with associative composition whose evaluation costs O(log k), that computes Σ_{m=0}^k v_a(m)^2 modulo 101001001 for every admissible Fibonacci convergent a with denominator exceeding k+2; the computed residue is independent of the chosen admissible convergent and therefore equals Ψ(k) modulo 101001001.
status: open
next: Formalise and kernel-check a proposed joint state over the intercept-position grid for k≤150, explicitly accounting for the moving boundary h∈[-m,k-m] and the known non-Toeplitz defect.
```
