# Suffix-fold vs prefix-fold — the window error that made the fold look wrong

**Decision:** the converging round found a window error in this run's own
identification of the supply quantity, and the correct object is the suffix
Pascal-mod-2 fold Φ_n. This note records the resolution and the claim.

## The tension, resolved

Two held claims contradict each other about the central identity:

- `linearization_verify.captured.txt` (suffix fold): ν₂(q_n) == wt(Φ_n h),
  0 violations over 8,001,999 real-prime cells, all sparse {50..3999} and
  dense [50,3000] samples.
- `thue-morse-sublinear-supply-witness` (prefix fold): ζ(h)[d] = Σ_{j⊆d} h[j]
  gives 7 ones ≤ 100, while measured true ν₂(100) = 27; the note calls this a
  "parity vs membership" gap.

Both are correct about what each computed. The contradiction is a **window
error**: the right-diagonal tail cell at depth k folds over the SUFFIX window
[n−k, n−1] (`code/lib/rule90fold.py` `fold_cell_bit`: `hcol[n−k+i]`), while
the prefix subset-zeta ζ(h)[d] = Σ_{j⊆d} h[j] folds over [0, d]. The prefix
subset-zeta is the BCZ left-edge involution (bcz-2023-left-edge-stabilization),
not the right-diagonal supply object.

For gap ∈ {2,4} words the halved triangle is exactly {0,1}-valued
(|0−0|=0, |0−1|=1, |1−1|=0), so XOR is exact: parity = value. There is no
"parity vs membership" gap for these words — the Thue–Morse note's diagnosis of
its own mismatch is wrong. The correct diagnosis is prefix-vs-suffix window.
The true right-diagonal ν₂ is the suffix fold weight, which is exact.

## Claim

```claim
id: suffix-fold-equals-nu2-prefix-does-not
statement: |
  The right-diagonal {0,2}-suffix count satisfies nu2(q_n) = wt(Phi_n h)
  EXACTLY, where Phi_n is the anti-diagonal Pascal-mod-2 matrix folding the
  halved-gap bit string h over the SUFFIX window: cell (k, n-k) has value
  XOR_{i subset (k-1)} h[n-k+i] (Pascal-row-(k-1) coefficients). This is the
  operator in code/lib/rule90fold.py (fold_cell_bit / fold_weight_h). The
  PREFIX subset-zeta zeta(h)[d] = XOR_{j subset d} h[j] is a DIFFERENT
  operator and is NOT equal to nu2 in general: for Thue-Morse h the prefix
  fold gives 7 ones <= 100 while the true suffix nu2(100) = 27. The mismatch
  is a window error, not a "parity vs {0,2}-membership" error: for gap-{2,4}
  words the halved triangle is {0,1}-valued so XOR is exact (parity = value).
hypotheses: |
  rule90-interior-xor (proved: halved {0,2}-block cells evolve by XOR); for
  gap-{2,4} words the halved triangle stays in {0,1} so the fold is exact;
  the suffix-fold per-cell identity is additionally machine-verified on the
  REAL prime triangle (all gaps incl. 6,10,...) as the mod-4 linearization.
holds-here: yes
status: checked
evidence: |
  suffix fold == nu2: code/out/linearization_verify.captured.txt (0 violations,
  8,001,999 cells, sparse+ dense n); prefix fold != nu2: the Thue-Morse note's
  own 7 vs 27 (research/notes/thue-morse-sublinear-supply-witness.md), now
  re-diagnosed as a window error. A one-shot check (code/out/resolve_fold_vs_nu2.py)
  is written but not yet executed; the two captures above are independent and
  suffice for the diagnosis, and the script settles it in one code path.
bearing: |
  Corrects the object for the supply question. The fold IS the right
  observable, in suffix form; the refutation of the Gowers/tree-martingale
  candidates' "nu2 = fold density" identification was valid only against the
  PREFIX fold. Their refutations stand anyway on the independent ground that
  no named theorem transfers to a deterministic suffix fold. The open supply
  bound for the primes remains abgs-2011-s9-mod4-switch-limit-open.
anchor: research/approaches/suffix-fold-pascal-linear-operator.md
contradicts: (resolves the contradiction between
  thue-morse-sublinear-supply-witness and dyadic-separating-invariant-three-strings /
  linearization_verify — the former used the prefix fold, the latter the suffix)
```

## Status of the surrounding claims

- `dyadic-collapse-proved` (suffix fold, cyclic σ): unaffected, still proved.
- `spad-nondegenerate-linear-refuted` (suffix fold, `fold_weight_h`):
  unaffected, still refuted — the half-step witness is on the correct operator.
- `thue-morse-sublinear-supply-witness`: the prefix-fold "proved O(log n)" is
  dead (wrong operator); the qualitative sublinear conclusion survives as
  measurement (true ν₂ density 0.27→0.011 over n=100..4000).
