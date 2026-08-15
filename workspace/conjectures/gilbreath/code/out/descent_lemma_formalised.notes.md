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

## Scope (Directive 50 — do not let it grow in the retelling)

This claim is **strictly the abstract combinatorial core in halved units**:
an arbitrary `{0,1}^L` pattern and arbitrary starting `w`. It does **NOT**
cover: Link A (`v ≤ g*_n`, still unverified after the Directive 45 vacuity);
the composition `g*_n ≤ 2ν₂+2 ⟹ success`; the reduction from real column
dynamics to the `(pattern, v)` model (the Directive 48 item 1 proof, still to
be written); or the supply side. **It does not upgrade `lemma54-re-derived-proof`
to proved** — that claim asserts the full lemma on the even domain, strictly
more. The honest path to a Lean-proved full Lemma 5.4 is to formalise Link A
and the composition too.
