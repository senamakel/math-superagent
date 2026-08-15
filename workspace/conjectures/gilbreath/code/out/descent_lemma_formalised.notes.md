# Descent lemma (Granville 5.4 combinatorial core) — formalised

```claim
id: descent-lemma-halved-formalised
statement: For a {0,1} pattern el (every entry 0 or 1) and start w : Nat, with
trajectory d_0 = w, d_{k+1} = |d_k - e_k| (runAbs) and ν₁ = countOnes el:
  (1) w ≤ ν₁ + 1 ⟹ runAbs w el ∈ {0,1};
  (2) w > ν₁ + 1 ⟹ runAbs w el = w - ν₁ exactly;
  (3) {0,1} is absorbing under |x - e| for e ∈ {0,1}.
hypotheses: el : List Nat with ∀ e ∈ el, e = 0 ∨ e = 1; w any Nat.
holds-here: yes
status: formalised
formalisation: code/lean/descent_lemma.lean
anchor: code/lean/descent_lemma.lean (lean_check)
bearing: This is the sharpened descent lemma at the combinatorial core of
  Granville's Lemma 5.4, in halved units, with the δ=0 (absorption) case
  Granville discards handled as a normal closure case. It establishes the
  {0,1} ↔ {0,2} (halved / unhalved) final-value criterion for an arbitrary
  {0,1} pattern L, with L arbitrary — exactly the absorption claim route B
  needs from a 2-then-odds descent.
```

`lean_check` on `code/lean/descent_lemma.lean`: compiled=true, verified=true,
zero `sorry` warnings. `#print axioms` for every lemma (`absorbing`,
`run_absorb`, `run_high`, `run_inv`, `descent_claim1`, `descent_claim2`) lists
only the accepted kernel builtins `propext`, `Classical.choice`, `Quot.sound`;
no `sorryAx` anywhere. `descent_claim1` and `descent_claim2` are `theorem`s in
the file with `#print axioms` in-file.
