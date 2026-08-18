```ladder
goal: compute Psi(10^18) mod 101001001, where S_0="0", S_1="01", S_n=S_{n-1}S_{n-2} (concatenation), a Fibonacci subword of length k is a distinct contiguous factor of some S_n, val(x) reads the binary word x as a decimal number (leading zeros ignored), and Psi(k) = sum_{x in F_k} val(x)^2
difficulties: k=10^18-scale, k+1-intercepts, square-second-moment, non-toeplitz-correlation, decimal-phi-independence, leading-zero-boundary, modular-mod-M
status: open
```

```rung
id: R0-one-worked-case
statement: establish the single worked case Psi(3)=20302 by explicitly generating S_5=0100101001001, extracting the four distinct length-3 factors 001, 010, 100, 101, interpreting them as 1, 10, 100, 101, and summing their squares.
off: k=10^18-scale, k+1-intercepts, square-second-moment, non-toeplitz-correlation, decimal-phi-independence, leading-zero-boundary, modular-mod-M
stance: settled
established-by: g1-oracle-length3
merge: turn on scale to a finite but general range — enumerate factors for any small k by brute force.
```

```rung
id: R1-brute-oracle
statement: compute Psi(k) exactly for small k (1 <= k <= 30) by exhaustive substring enumeration over a sufficiently long finite Fibonacci word, retaining decimal interpretation, leading-zero handling, squares, modulus, and the k+1 factor count; reproduce Psi(3)=20302 and Psi(10) mod 101001001 = 10699667.
off: k=10^18-scale, k+1-intercepts, decimal-phi-independence
stance: settled
established-by: understand-brute
merge: turn on the structural difficulty of identifying the factor set without enumeration — replace brute substring extraction by the Sturmian complexity theorem.
```

```rung
id: R2-sturmian-factor-structure
statement: prove and verify that the infinite Fibonacci word is the characteristic Sturmian word of slope 1/phi^2 with exactly k+1 distinct length-k factors for every k; this identifies the summation domain as the k+1 factors of the infinite word but does not evaluate decimal values or moments.
off: k=10^18-scale, k+1-intercepts, square-second-moment, non-toeplitz-correlation, decimal-phi-independence, leading-zero-boundary, modular-mod-M
stance: settled
established-by: fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity
merge: turn on the mechanical-word digit representation — encode each factor's bits by floor differences of an irrational rotation, enabling decimal evaluation without enumerating the word.
```

```rung
id: R3-mechanical-direct
statement: for k <= 400, compute the actual Psi(k) using the exact mechanical-word representation: slope alpha = 1/phi^2, k+1 intercepts x_m = -m*alpha mod 1, digits by floor differences, decimal value by telescoping sum v(x) = floor(x + k*alpha) - 10^{k-1}*floor(x) + 9*sum_{j=1}^{k-1} 10^{k-1-j}*floor(x + j*alpha), square v(x)^2, sum over m=0..k, and agree with the brute oracle wherever it reaches. This is the direct O(k^2) method — correct but does not scale.
off: k=10^18-scale, decimal-phi-independence
stance: settled
established-by: g3-telescoped-second-moment
merge: turn on moderate scale — push the same direct O(k^2) method to k=10^4 and k=10^6, obtaining anchors that any efficient method must reproduce.
```

```rung
id: R4-moderate-scale-anchors
statement: compute Psi(10^4) mod M = 34432237 and Psi(10^6) mod M = 20938836 by the valid direct mechanical/window method, with exactly 10001 and 1000001 factors respectively. These are the verified anchors at scale — they gate every candidate efficient method.
off: k=10^18-scale
stance: settled
established-by: directive6-anchors-verified-incontainer
merge: turn on the O(log) per-intercept primitive — the universal-Euclidean monoid must correctly reproduce a single intercept's decimal value (S1) and its square (S2) before anyone attempts to aggregate over all intercepts.
```

```rung
id: R5-per-intercept-ueuclid-validation
statement: for a single mechanical intercept x_m (any m in 0..k), compute its factor's decimal value val(w_m) and its square val(w_m)^2 through the universal-Euclidean second-moment monoid (ueuclid with geometric weight z = 10^{-1} mod M), and verify against mech_psi's per-factor decomposition for k=1..400. This confirms that the O(log k) primitive correctly handles the problem's actual floor-difference digit sequences — decimal telescoping, leading zeros, geometric weights, and modular arithmetic — for one intercept at a time. (Currently validated only at k=1,2,3 by verify_z_index.py; the range extension to k=1..400 is the open part.)
off: k=10^18-scale, k+1-intercepts, non-toeplitz-correlation, decimal-phi-independence
stance: open
merge: turn on the k+1-intercept difficulty — sum the per-intercept contributions over all m=0..k, but for the first moment only (no squares), to isolate the aggregation problem from the correlation problem.
```

```rung
id: R5b-fibonacci-minus-one-first-moment
statement: at the restricted lengths k = F_n - 1 (k = 1,2,4,7,12,20,33,54,88,143,...), establish the conjectured first-moment balance Psi_1(k) = c_1(k)*(10^k-1)/9, where c_1(k) = 1 + floor(k/phi^2) = F_{n-2}, rather than claiming it for general k.
off: k=10^18-scale, k+1-intercepts, square-second-moment, non-toeplitz-correlation, decimal-phi-independence
stance: failed
failed-by: the first-moment balance was verified only at k = F_n - 1 (mech_psi and brute agree there) and is computationally observed to fail at every other k, with the deviation matching no catalogued sequence; no combinatorial proof of even the restricted symmetry exists, so it supplies no route to the general-k first moment and is not a climbable rung.
merge: the identity describes the special Toeplitz domain but has no proof and no extension; keep it as a diagnostic waypoint, not a rung toward the target. Do not re-propose without a proof of the restricted combinatorial symmetry.
```

```rung
id: R6-first-moment-intercept-aggregation
statement: compute the first moment Psi_1(k) = sum_{m=0}^{k} val(w_m) — the sum of decimal values of the k+1 factors, without squares — by a fixed-dimensional aggregation over all k+1 mechanical intercepts, at cost O(log k) rather than O(k log k). Verify against the direct mechanical oracle at k=1..400 and at k=10^4. This isolates the intercept-aggregation structure from the square-moment correlation problem.
off: k=10^18-scale, square-second-moment, non-toeplitz-correlation
stance: open
merge: turn on the square-second-moment in the Toeplitz domain — at k=F_n-1 the pair-correlation C(j,ell)=A(ell-j) collapses to one variable, so the second moment becomes a single weighted floor-sum rather than a joint observable; evaluate it and verify against the brute/mech_psi oracle at the special lengths.
```

```rung
id: R6b-toeplitz-domain-second-moment
statement: at the restricted lengths k = F_n - 1 (k = 1,2,4,7,12,20,33,54,88,143,...), compute the full second moment Psi(k) = sum_{m=0}^{k} val(w_m)^2 by exploiting the Toeplitz pair-correlation collapse C(j,ell) = A(ell-j) (verified against brute for n=3..12 by claim-three-gap-autocorrelation-home). The Toeplitz structure reduces the digit-pair double sum to a single weighted floor-sum over the lag d, which the universal-Euclidean monoid evaluates in O(log k). Verify against mech_psi at every k=F_n-1 up to k=143 and against the brute oracle where it reaches. This is the full second moment — squares, decimal weights, modular reduction, leading zeros — but only where the non-Toeplitz correlation difficulty is provably off.
off: k=10^18-scale, non-toeplitz-correlation
stance: open
merge: turn on the non-Toeplitz difficulty — extend from k=F_n-1 to general k, where the pair-correlation residual R(j,ell) = C(j,ell) - A(ell-j) is nonzero and the joint intercept aggregation must handle the full two-variable correlation structure.
```

```rung
id: R7-second-moment-intercept-aggregation
statement: compute the full Psi(k) = sum_{m=0}^{k} val(w_m)^2 — the sum of squares, with decimal weights, modular reduction, and all boundary conventions — by a fixed-dimensional O(log k) aggregation over all k+1 mechanical intercepts at general k, matching the verified anchors at k=10^4 (34432237) and k=10^6 (20938836). This is precisely goal G4 — joint-intercept-evaluation, the run's single open goal.
off: k=10^18-scale
stance: open
merge: turn on the astronomical scale — apply the established fixed-dimensional recurrence at k = 10^18, independently verify the residue by a second derivation or route, and check that Psi(10^18) mod 100 = 52 (the pattern-hunt cross-check).
```

```rung
id: R8-full-target
statement: compute Psi(10^18) mod 101001001 exactly under the original problem definition.
off: —
stance: open
merge: none; this is the original target, reached only after the intercept-aggregation and square-moment difficulties are both settled at logarithmic cost.
```
