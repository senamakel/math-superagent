# Will Sawin, "An improved lower bound for the union-closed sets conjecture" — arXiv:2211.11504v3

**Note — replaces the structural digest.** Wikilink to full text:
[[sawin-improved-lower-bound-2022.html.full]]

Full text: `research/sources/sawin-improved-lower-bound-2022.html.full.md`.
Preprint (unpublished in a journal).

## What it establishes (precise statements)

**Theorem 2 (the sharp iid inequality).** `A,B` independent samples from a
distribution over subsets of `[n]` with `Pr[i∈A] ≤ u` for all `i`. Then
`H(A∪B) ≥ H(A)·{ H(2u−u²)/H(u) if u ≤ (3−√5)/2;  (1−u)·2/(√5−1) if u ≥ (3−√5)/2 }`.
This is Liu's Prop 1 verbatim; AHS/Chase–Lovett also proved it. **Theorem 1**:
any nonempty union-closed `ℱ⊆2^[n]` has an element in `≥ (3−√5)/2` of its sets
— the `(3−√5)/2` barrier, proved (with AHS).

**Lemma 3 (the engine, sharp).** For `p,q` iid `[0,1]`-valued with `Ep ≤ u`:
`E[H(p+q−pq)] ≥ E[H(p)]·{same two-branch factor}`. **Sharpness:**
- `u ≤ (3−√5)/2`: sharp at `p ≡ u` (Gilmer's independent-events example).
- `u ≥ (3−√5)/2`: sharp at `p = (3−√5)/2` w.p. `(1−u)·2/(√5−1)`, else `p=1`.
So the ratio `inf_{Ep≤u} E[H(p+q−pq)]/E[H(p)]` equals exactly the two-branch
factor; hence the `(3−√5)/2` bound is the **ceiling of the iid coupling class**
(confirms the thread: barrier to iid, not to the method).

**Theorem 2 / Lemma 3 sharpness ⟹ negative answers to two Gilmer questions.**
The `u ≥ (3−√5)/2` sharp example answers **negatively** Gilmer's first bulleted
question (whether the ratio stays `H(2u−u²)/H(u)` for all `u`) for
`u > (3−√5)/2`; the positivity side for `u ≤ (3−√5)/2`.

**Proposition 6 (disproves Gilmer's Conjecture 1 = KL-divergence escape).**
For any `u < 1` and `d > H(2u−u²)/H(u)`, for all large `n` there is a random
`A ⊆ [n]` containing each element w.p. `≤ u` with `H(A∪B) ≤ d H(A)` yet
`D(A∪B‖A) = O(1)` while `H(A) = O(n)`. **This is the dead end recorded in the
library**: adding a KL-divergence penalty does not let the iid argument escape
`(3−√5)/2`. (The same-day independent counterexample, `[4]`, is for `n=2`
instead of fixed `n`.)

**Dependent-coupling improvement (§2 proof sketch).** Consider `A,B` iid
uniform from `ℱ` *and* `A,C` uniform but **correlated** (coupling chosen greedily
to maximize the entropy increase at each inductive step). For distributions close
to Lemma 3's optimizer the gain beats the loss, so a suitable *convex
combination* of the two entropies gives lower bound `(3−√5)/2 + δ` for some
`δ > 0`. **This is the origin of the dependent-coupling escape** that Yu/Cambie
evaluate to `0.38234`, and the engine of all post-barrier constants. It is a
**proof sketch** in Sawin (stated as sketch, not fully formalised with an
effective `δ`); the rigorous, computable form is Yu's `Γ̂`/Proposition 1.

## Hypotheses and holds-here

- Theorem 1/2/Lemma 3: `ℱ` finite, union-closed, nonempty; element densities are
  exact marginals. **Holds-here: yes** — exactly this problem's setting.
- The two-branch factor is **proved**; its sharpness (the Examples) is **proved**.
- The dependent-coupling `(3−√5)/2+δ` claim is **sketched**, not a formalised
  theorem with a numeric `δ`; the computable rigorous form is Yu's Proposition 1.
- Proposition 6's counterexample is **proved** in-paper.

## What this lets the run do

- **Bears directly on `G-coupling-half`.** Sawin is the pivot: it proves the
  iid class is capped at `(3−√5)/2` (rigorously, with the two sharp examples),
  then *escapes* that cap by the dependent coupling. Any proof of UC through the
  coupling-entropy reduction MUST use a dependent coupling — the iid route is
  closed (recorded as `G-iid-half` refuted). The rigorous computable dependent
  bound is Yu's `Γ̂`, not Sawin's sketch.
- The **KL-divergence dead end** (Prop 6) is a specific obstruction the run
  should not re-attempt: penalising the bound by `D(A∪B‖A)` does not improve
  the constant.
- The **sharp examples** (Gilmer's `p≡u`; and `p=(3−√5)/2` w.p.
  `(1−u)·2/(√5−1)` else `1`) are the candidate extremal distributions any
  claimed better constant must beat at every `u`.

## What it does not settle

Sawin gives no numeric `δ` and no fully formal proof of the dependent-coupling
improvement (it is a sketch). It does not address whether the dependent class
reaches `1/2` — it is the origin of the record `0.38234` but nothing more.
It disproves Gilmer's *iid-with-KL* conjecture but not UC itself.

```claim
id: sawin-iid-ceiling
statement: For p,q iid [0,1]-valued with Ep≤u, the ratio
  E[h(p+q−pq)]/E[h(p)] is exactly the two-branch factor
  {h(2u−u²)/h(u) if u≤(3−√5)/2; (1−u)·2/(√5−1) if u≥(3−√5)/2}; both branches
  attained, so (3−√5)/2 is the exact ceiling of the iid coupling class for UC.
hypotheses: p,q iid, Ep≤u; finite union-closed family (for the UC implication)
holds-here: yes
status: proved
bearing: proves G-iid-half refuted: no iid-coupling entropy argument can certify
  density > (3−√5)/2; any UC proof via this reduction needs a dependent coupling
anchor: research/sources/sawin-improved-lower-bound-2022.html.full.md
follows-from: (Gilmer's method restated); sharp examples in-paper
answers: (supports ROOT's 'what (3−√5)/2 is a barrier FOR' = iid class only)
```

```claim
id: sawin-kl-dead-end
statement: Adding a KL-divergence penalty (Gilmer's Conjecture 1) does not help:
  for any u<1 and d>h(2u−u²)/h(u), for all large n there is A⊆[n] with
  Pr[i∈A]≤u, H(A∪B)≤d·H(A), and D(A∪B‖A)=O(1) while H(A)=Θ(n). Hence UC cannot
  follow from any iid argument relying on the KL-divergence term.
hypotheses: finite A, iid A,B, element densities ≤u
holds-here: yes
status: proved
bearing: a specific recorded dead end — do not re-attempt KL-penalised iid bounds. (Disproves Gilmer's first Conjecture 1; that conjecture is not filed as a claim block, so the contradiction is recorded here in prose rather than as an edge.)
anchor: research/sources/sawin-improved-lower-bound-2022.html.full.md
```

```claim
id: sawin-dependent-coupling
statement: Considering A,B iid uniform from a family F together with A,C
  uniform but greedily-correlated, a convex combination of the two OR-entropy
  bounds strictly exceeds (3−√5)/2 (sketch: gain beats loss near Lemma 3's
  optimizer); the origin of the dependent-coupling record 0.38234.
hypotheses: finite union-closed family; coupling chosen greedily to maximise
  per-step entropy increase
holds-here: yes (sketched in Sawin; rigorous computable form is Yu Prop 1)
status: asserted (proof sketch, no effective δ in Sawin; formalised by Yu/Cambie)
bearing: the escape route from the iid cap that motivates the live G-coupling-half
  attack and all record constants beyond (3−√5)/2
anchor: research/sources/sawin-improved-lower-bound-2022.html.full.md
follows-from: sawin-iid-ceiling
```
