# SUPPLY — the fold has no generic weight obstruction

Backs the bottom rung `R-random-expectation` of `research/weakened/supply.md`.
The claim is a one-line consequence of an imported fact; it is *stated*, not
machine-checked here.

```claim
id: C-fold-generic-expectation
statement: If h is uniform on the domain of the F₂ fold matrix Φ_n and rank Φ_n = r, then E_h[wt(Φ_n h)] = r/2. With the corrected rank r = n−2 this gives E_h[wt(Φ_n h)] = (n−2)/2, hence ≥ n/3 for all n ≥ 6. In words: the fold imposes no weight obstruction on generic input; a linear lower bound on wt(Φ_n h) is the generic behaviour, so the whole difficulty of SUPPLY is carried by the specific prime input h.
hypotheses: rank Φ_n = n−2 over F₂ (corrected rank; full row rank of the operative (n−2)×n matrix, rows d = 2..n−1 — see fold-rank-is-n-2-nullity-2-alternating); h uniform on the domain F₂^n of Φ_n.
holds-here: yes — the rank fact is machine-verified n = 2..20 (code/fold_rank/rank_of_fold.py). The identity E[wt] = (number of nonzero coordinate projections of Im(Φ_n))/2 holds because Φ_n h is uniform on Im(Φ_n), an r-dimensional subspace, and a nonzero coordinate projection is 1 with probability 1/2 at every one of its r independent coordinates. Every coordinate projection of Im(Φ_n) is nonzero (no coordinate is identically 0 on the image, since full row rank has no zero rows), so E[wt] = (n−2)/2 exactly.
status: checked (exact linear-algebra identity; rank from the corrected rank computation)
bearing: Settles ladder rung R-random-expectation; is the bottom of the weakened ladder and the statement that says the primes carry the difficulty, not Φ. The earlier statement's hypothesis "rank = n−3" is superseded; the conclusion only strengthens ((n−2)/2 ≥ (n−3)/2).
anchor: code/fold_rank/rank_of_fold.py (rank verify n=2..20); code/lib/supply_fold.py
```

## Adversarial flag (not part of the claim)

problem.md fact (3) reads "rank Φ_n = n−3, nullity 1, ker Φ_n = span(all-ones)".
For a map with domain F₂^d, rank + nullity = d, so this forces d = n−2. The
expectation bound above uses *only* rank, so it is insensitive to the
domain/nullity convention; but any later rung that needs the domain dimension
must fix it against the run's floor convention (problem.md, "Convention note").
Also: the expectation bound does **not** by itself give concentration. A
rank-2 subspace W = span{e_1, (0,1,…,1)} has E[wt] = n/2 yet only half its
vectors have wt ≥ n/4 (weights are 0, 1, n−1, n, each with prob 1/4). So
`R-random-pointwise` needs Φ_n-specific (Lucas) structure, not the bare rank.
