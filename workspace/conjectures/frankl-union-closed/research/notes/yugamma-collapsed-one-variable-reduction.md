# Scholar reduction — collapsed α=0 end of Γ̂(1/2)=φ/2 IS Boppana's inequality (corrected)

**Status: the collapsed α=0 end of the t=1/2 certificate is now PROVED, as a
corollary of Boppana's inequality.** This note records the reduction and the
correction of the author's own near-miss.

## The result, stated plainly

At α=0, t=1/2, over the collapsed two-atom family (marginal
`μ = w·δ_a + (1−w)·δ_1`, atoms `a ≤ 1/2` and `1`, feasibility-forced weight
`w = 1/(2(1−a))`), the iid-OR ratio satisfies

```
u(a) = w·h(2a−a²)/h(a)  ≥  φ/2 = (1+√5)/4,
```

with equality exactly at `a = (3−√5)/2`. **This is a theorem, not a
corroboration.**

## Proof (the reduction + Boppana)

1. Only the (a,a) product survives in the numerator: p+q−pq = 1 whenever either
   coordinate is 1, and h(1)=0. So
   `u(a) = w²·h(2a−a²)/(w·h(a)) = w·h(2a−a²)/h(a)`.
2. `w = 1/(2(1−a))`. Let `s = 1−a ∈ (1/2,1)`. Then `2a−a² = 1−s²`, `h(a)=h(s)`, so
   `u = (1/(2s))·h(1−s²)/h(s)`.
3. **Key step (the near-miss corrected):** binary entropy is symmetric,
   `h(1−s²) = h(s²)`. Therefore
   `u ≥ φ/2  ⟺  h(1−s²) ≥ φ·s·h(s)  ⟺  h(s²) ≥ φ·s·h(s)`,
   which is **Boppana's inequality** (`boppana-entropy-inequality`, status:
   proved, holds-here: yes).
4. Boppana gives `h(s²) ≥ φ·s·h(s)` on all of [0,1], hence on (1/2,1), with
   equality at `s* = 1/φ`, i.e. `a = (3−√5)/2`. At that point `u = φ/2`.

QED. The author first flagged `h(1−s²) ≥ φ·s·h(s)` as a "new inequality not in
the library" — that was wrong: it is Boppana's under the symmetry `h(1−x)=h(x)`.
The `request_research` refusals were correct; the library had it. This is a
lesson to record: **every h with the complement-square argument collapses to a
square argument via h-symmetry.**

## What exactly is now proved vs. still open

**Proved (corollary of Boppana):** the *collapsed α=0 sub-family* at t=1/2 has
inf = φ/2, attained at a=(3−√5)/2. This is the algebraic reason the collapsed
extremal lands exactly on φ/2: at s*=1/φ, `s*²=1−s*`, and the golden-conjugate
identity pins the value.

**Still open (numeric only):**
- The **global** α=0 inf over ALL admissible two-atom marginals (not just the
  collapsed sub-family) at t=1/2. The collapsed boundary is the numeric
  minimizer, but that the general family can't go below the collapsed one is not
  theorem here.
- Everything with α>0.
- The global Γ̂(1/2)=φ/2 (sup over α of the inf).
- Whether φ/2 as the certificate value is externally known (novelty unchecked).

So the honest upgrade this pass delivers: the *collapsed end* is no longer "the
exact value proved, the inf corroborated" — now the collapsed *inf* is proved too
(via Boppana). The global statement is unchanged as open.

## Claim block

```claim
id: yu-collapsed-alpha0-inf-is-phiover2-via-boppana
statement: At alpha=0, t=1/2, over the collapsed two-atom family (marginal
  w*delta_a+(1-w)*delta_1, feasibility-forced w=1/(2(1-a))), the iid-OR ratio
  u(a)=w*h(2a-a^2)/h(a) satisfies u(a) >= phi/2 with equality exactly at
  a=(3-sqrt5)/2. Proof: let s=1-a; then u=(1/2s)*h(1-s^2)/h(s), and by the
  binary-entropy symmetry h(1-s^2)=h(s^2) this is >= phi/2 iff Boppana's
  h(s^2)>=phi*s*h(s), which is proved. The author first mis-flagged the
  complement-square inequality as new; it is Boppana under h-symmetry.
hypotheses: Yu Prop.1 collapsed two-atom marginal at t=1/2, alpha=0; binary
  entropy; s in (1/2,1)
holds-here: yes
status: proved (corollary of boppana-entropy-inequality, which is proved)
bearing: upgrades the collapsed alpha=0 END of the Gamma-hat(1/2)=phi/2 thread
  from numeric corroboration to theorem: the collapsed inf is phi/2 exactly.
  The GLOBAL alpha=0 inf over all admissible marginals, and all alpha>0, stay
  numeric-only. Also files the lesson that h(1-x)=h(x) collapses every
  complement-square entropy inequality to Boppana.
anchor: research/notes/yugamma-collapsed-one-variable-reduction.md;
  boppana-entropy-inequality; code/out/alpha0_inf_scan.captured.txt
follows-from: boppana-entropy-inequality, yu-gamma-half-is-phi-over-2,
  iid-barrier-exact
answers: yugamma-half-collapse (partial: the collapsed alpha=0 end is now
  proved via Boppana; global and alpha>0 ends remain open)
```

## Lesson (durable)

When reducing an entropy-ratio inf to a one-variable inequality, always apply
`h(x)=h(1−x)` first: it can turn a "new" complement-of-square inequality
(`h(1−s²)`) into a stored one (`h(s²)`), which the library already proves. This
pass nearly filed a non-result.

## Files
- `research/notes/yugamma-collapsed-one-variable-reduction.md` (this note)
- `code/out/alpha0_inf_scan.py` / `.captured.txt` (numeric corroboration of the
  alpha=0 end, now backed by the Boppana proof)
- `research/summaries/boppana-entropy-inequality-2023.md` (the engine)