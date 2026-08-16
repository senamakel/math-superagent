# Scholar verification — the down-set intersection formula (adopted geometry line)

The adopted live line `downset-row-code-distance-closed-form` rests on a
distance formula for the fold's row set `R_n = {1_{M_d} : d ∈ [2,n−1]}`,
`M_d = {n−1−d+o : o ⊆ d}`. The formula is already on disk as the asserted,
hand-verified claim `downset-row-intersection-meet-formula`
(`research/notes/subcube_intersection_claim.md`), and two verification scripts
(`code/scholar/verify_intersection_formula.py` over n=8..64,
`code/librarian/verify_downset_intersection.py` over n=8..256) exist but are
**unexecuted**. This note supplies the *all-n proof by bijection* that upgrades
that asserted fact to proved-by-derivation — it does not dispute the existing
claim, it strengthens its epistemic status. The genuinely new consequence is
`fold-distance-enumerator-On` (below): the geometry theorem (C) the route needs.
A third confirmatory script `code/scholar_intersection_formula_verify.py`
repeats the same machine check (all pairs n=8..256 + random-set negative
control) and is **unexecuted** — no execution tool is available to the scholar
role this cycle; hand any of the three scripts to coder.

## The three identities

Let `pc = popcount`, `↓d = {y : y ⊆ d}` the bitwise down-set, and recall the
row `M_d` sits in the n-window (positions `0..n−1`), `d ∈ [2,n−1]`.

**(R) Reflection.** `M_d = { n−1−y : y ⊆ d }`.
Proof: `x ∈ M_d ⟺ x = n−1−d+o` for `o ⊆ d ⟺ n−1−x = d−o`. Since every 1-bit
of `o` is a 1-bit of `d`, subtracting `o` from `d` never borrows, so
`d−o = d XOR o`, and `d XOR o ⊆ d`. The map `o ↦ d XOR o` is complementation
within the support of `d`, hence an involution on `↓d`, so a bijection. Thus
`n−1−x` runs exactly over `↓d`. ∎

**(I) Intersection.** `M_d ∩ M_{d'} = M_{d∧d'}`.
Proof: using (R), an element appears in both rows iff its reflection `y` lies
in `↓d` and `↓d'`, i.e. `y ⊆ d` and `y ⊆ d'`, i.e. `y ⊆ (d ∧ d')`. So the
common set is exactly `{n−1−y : y ⊆ d∧d'} = M_{d∧d'}`. Consequently
`|M_d ∩ M_{d'}| = 2^{pc(d∧d')}`. ∎

**(D) Distance.** `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`.
Proof: from `|M_d| = 2^{pc(d)}` (Lucas: a row has one element per submask) and
(I), since `|A△B| = |A|+|B|−2|A∩B|`. ∎

## Why this is sound at every n (attacking my own verification)

The only step needing care is the proof of `F_n(z)=O(n)` for `|z|<1`, which
uses "distinct rows satisfy `dist ≥ 2^{max(p,q)−1}`". The subtle case is
`p = q` (equal popcounts): then `r = pc(d∧d') < p` for distinct rows, so
`dist = 2^{p+1} − 2^{r+1} ≥ 2^{p+1} − 2^p = 2^p ≥ 2^{p−1}`. For `p > q`:
`r ≤ q` gives `dist ≥ 2^p + 2^q − 2^{q+1} = 2^p − 2^q ≥ 2^p − 2^{p−1}
= 2^{p−1}`. Both cases hold. Hence pairs with `max(p,q) > K` have
`dist ≥ 2^{K−1}` and contribute `≤ n²|z|^{2^{K−1}}`; pairs with
`max(p,q) ≤ K = c log₂ log₂ n` number `≤ 4m^{2K}` (m = ⌈log₂n⌉) and
contribute `≤ 4m^{2K} = n^{o(1)}`; the diagonal gives `n−2`. With `c>1`,
`n²|z|^{2^{K−1}} = o(1)`, so `F_n(z) = O(n)`. The geometry theorem (C) is
proved, not measured, once (D) is machine-checked.

## What this settles

Condition (C) of the adopted second-moment line — `F_n(z) = O(n)` for all
`|z|<1` — is a genuine theorem of the row set's geometry, with no primes and no
duality hypothesis. It leaves exactly one open arithmetic input: (A),
`E[S(n)²] = O(n)` for the real prime gap-parity string `h` (equivalently a
variance/second-moment bound on the submask-window autocorrelation), measured
as `|S(n)| = (3.1…3.8)√n` over `[300,6000]`. If (A) holds, Chebyshev gives
`ν₂/n → 1/2` on a density-1 set — GOAL priority 1. This is orthodox:
second-moment is orthogonal to the (first-moment, parity-barrier) switch
density.

## Status

- (R),(I),(D): proved for all n by the bijection argument above; the same
  statement is on disk as `downset-row-intersection-meet-formula` (previously
  hand-verified/asserted) — this note upgrades it to proved-by-derivation.
- (C): follows from (D) by the popcount split; proved conditional on (D).
- Machine route: three confirmatory scripts exist but are **unexecuted**
  (`code/scholar_intersection_formula_verify.py`,
  `code/scholar/verify_intersection_formula.py`,
  `code/librarian/verify_downset_intersection.py`); hand one to coder. Until it
  runs, mark the geometry theorem proved-by-derivation, machine-check pending.

```claim
id: fold-distance-enumerator-On
statement: For the fold row code R_n={1_{M_d}:d∈[2,n-1]}, F_n(z)=Σ_{d,d'}z^{|M_d△M_{d'}|}
  = O(n) for every |z|<1, uniformly in n.
hypotheses: |z|<1 fixed; no primes.
holds-here: yes
status: proved conditional on downset-row-intersection-meet-formula (popcount split,
  distinct rows have dist≥2^{max(pc)-1})
bearing: closes the geometry side of the second-moment route;
  reduces the density-1 (averaged) form of SUPPLY to the single arithmetic input (A).
anchor: research/notes/scholar_intersection_formula.md
follows-from: downset-row-intersection-meet-formula
answers: fold-second-moment-condition-C
```
