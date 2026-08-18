```skeleton
goal: Collapse the contiguous-window prefix sum of decimal squares over Fibonacci blocks to O(log k): Ψ(k)=Σ_{r=N-k-1}^{N-1}V_r² for a doubled standard word of length N>k.
implies: CW1+CW2 express Ψ as a terminal window block with a rolling affine update; CW3 gives exact summary composition; CW4 is the decisive renormalisation theorem that summaries of Fibonacci blocks form a fixed-dimensional closed monoid under Fibonacci concatenation and evaluate in O(log k); CW5 equates the computed summary with Ψ(k). CW1-CW3 alone are O(k) and do not imply CW4.
killed-by: CW4 (fixed-dimensional base-10 Fibonacci-block renormalisation) is refuted by the literature audit: no source establishes closure of the base-10 affine decimal-window observable, and pe1006-contiguous-window-cyclic-minus-prefix.md records the route closing back onto the universal-Euclidean floor-sum primitive. The finite transfer checks (k=1..150, k=10^4 anchor) are oracle evidence only.
rests-on: fibonacci-position-theorem-contiguous-windows, monoid-composition-formulas-verified
status: broken
```

```gap
id: CW1-terminal-window-set
lemma: For every k≥1 and every Fibonacci length N=F_t>k (with q_t the corresponding standard word and q_tq_t its double), the k+1 distinct length-k Fibonacci factors are exactly the windows q_tq_t[r:r+k] for r=N-k-1,...,N-1, each once.
status: discharged
discharged-by: fibonacci-position-theorem-contiguous-windows plus finite verification in code/out/directive9_transfer.captured.txt (k=1..150; k=3 and 10 reproduce Ψ). The exact q_tq_t indexing is solver-checked rather than stated verbatim by the source.
thread: research/threads/directive9-contiguous-window-prefix.md
next: If a formal proof is required, derive the stated terminal range from the sourced first-occurrence position theorem and the standard-word conjugacy convention, then formalise the index translation.
```

```gap
id: CW2-rolling-window-recurrence
lemma: If y is the doubled Fibonacci digit word and V_r=Σ_{j=0}^{k-1}y_{r+j}10^{k-1-j}, then V_{r+1}=10V_r-y_r10^k+y_{r+k}; consequently V_{r+1}² is a quadratic polynomial in (V_r,y_r,y_{r+k}) with coefficients depending only on k and powers of 10.
status: discharged
discharged-by: elementary algebra and the exact implementation in code/directive9_transfer.py; code/out/directive9_transfer.captured.txt reports the recurrence method agrees with mech_psi for k=1..150.
thread: research/threads/directive9-contiguous-window-prefix.md
next: State the induced affine update on the augmented state (V, V², V, 1) explicitly and verify the four possible endpoint pairs (y_r,y_{r+k}) by a small independent script.
```

```gap
id: CW3-summary-composition
lemma: For any adjacent window ranges A and B, their summaries T=(count,ΣV,ΣV²) compose by T(A∪B)=T(A)+T(B); equivalently the additive second-moment summary is an associative monoid, and any boundary-aware transfer summary must compose by affine block substitution.
status: discharged
discharged-by: elementary distributivity; code/directive9_transfer.py check_composition passes for every k=1..150, captured in code/out/directive9_transfer.captured.txt. The analogous floor-moment boundary-shift monoid is independently proved by monoid-composition-formulas-verified.
thread: research/threads/directive9-contiguous-window-prefix.md
next: For a proposed non-additive block summary, write its exact compose law and test associativity against direct concatenation on all Fibonacci blocks through a small bound.
```

```gap
id: CW4-fixed-dimensional-fibonacci-renormalisation
lemma: There exists a fixed dimension d independent of k and a computable summary σ_k(B) of every Fibonacci block B, containing enough information to evaluate the terminal prefix sum of V_r² for the k-shifted pair sequence (y_r,y_{r+k}), such that σ_k(B_{i+1})=Compose_k(σ_k(B_i),σ_k(B_{i-1})) (with finitely many boundary states), Compose_k is O(1) modular arithmetic, and σ_k for a prefix of length k is obtained in O(log k) block compositions.
status: refuted
killed-by: No proof or source establishes closure of the base-10 affine observable under a fixed-dimensional Fibonacci-block monoid. The approach audit explicitly refutes this as an independent O(log) method: the claimed ~87-block renormalisation is unsupported and the construction closes back onto the universal-Euclidean/floor-sum primitive. A finite O(k) transfer experiment cannot discharge this asymptotic lemma.
next: Do not scale the finite transfer search. A new theorem would be needed: either prove fixed-dimensional closure symbolically (including the k-shift boundary word) or replace the route with the established universal-Euclidean reduction.
```

```gap
id: CW5-terminal-correction
lemma: Given CW1 and an exact evaluator for the full cyclic sum and the initial prefix, the identity Ψ(k)=Σ_{r=N-k-1}^{N-1}V_r²=Σ_{r=0}^{N-1}V_r²−Σ_{r=0}^{N-k-2}V_r² holds with the same indexing and no multiplicity or wraparound error.
status: discharged
discharged-by: finite arithmetic identity; k=3 terminal windows in code/out/directive9_transfer.captured.txt give 20302, and k=10 gives 10699667. The general cyclic/prefix decomposition is algebraically immediate once CW1 fixes the range.
thread: research/threads/directive9-contiguous-window-prefix.md
next: Formalise the range partition for 0≤k<N and test the wraparound endpoint at k=1, k=N−1, and a non-Fibonacci k.
```