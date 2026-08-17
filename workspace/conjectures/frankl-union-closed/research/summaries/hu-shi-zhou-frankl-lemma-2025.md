# Hu–Shi–Zhou, "A lemma on a finite union-closed family of finite sets and its applications" (arXiv:2507.11008)

Source: https://arxiv.org/abs/2507.11008 ; full text:
`research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md`
(v1, 15 Jul 2025). Zechun Hu, Yun Q. Shi, Qianqian Zhou. Status: arXiv preprint.

## The main lemma (Lemma 1.1)

`F ⊆ 2^[n]` union-closed, `∪F = [n]`, `n ≥ 2`. Fix `i ∈ [n]`,
`G = {A∖{i} : A ∈ F}`. For `j ≠ i`, write `G_j = {A ∈ G : j ∈ A}`,
`F_j = {A ∈ F : j ∈ A}`. Then:

**`|G_j|/|G| ≥ c` (c ∈ (0,1]) ⟹ `|F_j|/|F| ≥ 1/(1 + 2(1−c)/c)`.**

Sharp: when `|G_j|/|G| = c`, `x = 0`, `y = |G_{/j}|`, equality holds
(Remark 2.2). Proof is a two-page elementary counting argument (Lemma 2.1:
a weighed-median inequality `b/a, d/c ≥ k ⟹ (b+d)/(a+c) ≥ k`), no entropy.

## Application 1 (Prop 3.1): Frankl ⟺ Nagel

Nagel's conjecture = "the kth-most frequent element is in ≥ |F|/(2^{k−1}+1)
sets". The authors prove **Frankl's conjecture is EQUIVALENT to Nagel's
conjecture**. Proof: assuming Frankl, element 1 has density ≥ 1/2; apply
Lemma 1.1 to `G = {A∖{1}}` (union-closed on `[n]∖{1}`, has an abundant
element `i` of density ≥ 1/2 in G) to get element `i` at density
`1/(1+2(1/2)/(1/2)) = 1/3 = 1/(2^2−1+1)` in F; the density ordering then gives
the k=2 case, and the reduction iterates for k = 3..n (using the exact identity
`1/(1 + 2(1−1/(2^{k−1}+1))/(1/(2^{k−1}+1))) = 1/(2^k+1)`). Nagel gives Frankl
trivially (k=1... k=1 is the `1/(2^0+1)=1/2` case), so the two are equivalent.

## Application 2 (Prop 3.3): complement to Nagel's Lemma 2.4

Nagel's Lemma 2.4: for any `A ∈ F` with `|A| ≥ 1` and `x ∈ A`,
`|F_x| ≥ |F|/(2^{|A|−1}+1)`. The authors prove **for any `A ∈ F` with
`|A| ≥ 2`, SOME `y ∈ A` has `|F_y| ≥ |F|/(2^{|A|−2}+1)`** — i.e. one element
of any non-singleton set has the density the next level of Nagel would
guarantee.

## Application 3 (Remark 3.4 on S-Frankl)

S-Frankl (Cui–Hu): `T(F) = min set size ≥ 2 ⟹ ≥ 2 elements at density ≥ 1/2`.
- (i) Conjectured best two-element version: `c1 = 1/2, c2 = 1/3`
  ("by virtue of Subsection 3.1").
- (ii) If `T(F) = 2` (a 2-element set exists), then `c1 = 1/2, c2 = 1/3`
  is attained (Prop 3.3 / Lemma 1.1).
- (iii) S-Frankl ⟺ taking `c1 = c2 = 1/2` in Question 1.
- (iv) From **Liu's c ≈ 0.38234**, Lemma 1.1 gives
  `c2 ≥ 1/(1 + 2(1−0.38234)/0.38234) ≈ 0.23635` for a second element.

## Why this source was added

Surfaced by a 2025 search (category research-paper); not in the library; not a
derivative. It is a new structural lemma aimed exactly at the run's
`abundance-profile` thread and the S₂/Cui–Hu question (KPT Proposition 7:
Conj 4 = "smallest set ≥ 2 ⟹ ≥2 abundant" stands strictly between Frankl and
Poonen). Two reprocessing notes for the library:

- The authors' "Frankl ⟺ Nagel" (Prop 3.1) is **not new**: Das–Wu Observation
  1.3 already proves Frankl ⟹ Nagel by a different route (`π_{k−1}` projection
  plus 2^{k−1}-to-1 preimage counting, `research/sources/das-wu-frequent-elements-2024.full.md`
  lines 99–137), with a weaker bound `1/(1+2^{k−1})`. So the equivalence is
  already in the library via Das–Wu (and Nagel's remark); Hu–Shi–Zhou's
  contribution is the sharp Lemma 1.1 and the `1/(2^{|A|−2}+1)` complement.
- The authors cite Das–Wu as "Nagel's conjecture is true for k ≥ 3 and k = 2
  under an additional condition" but their own Proposition 3.1 (Frankl ⟺ Nagel)
  supersedes/bypasses that reading; the equivalence direction is the same as
  Das–Wu Observation 1.3.

## Claims

```claim
id: hsz-frankl-lemma-density-transfer
statement: Let F ⊆ 2^[n] be union-closed with ∪F=[n], fix i∈[n], and let
  G = {A∖{i} : A ∈ F}. If for some j≠i, |G_j|/|G| ≥ c, then
  |F_j|/|F| ≥ 1/(1 + 2(1−c)/c). The bound is sharp: equality is attained with
  x=0, y=|G_{/j}| when |G_j|/|G| = c.
hypotheses: F finite union-closed, ∪F=[n], n ≥ 2, i∈[n], j≠i.
holds-here: yes
status: proved (in source; elementary counting proof on disk, arXiv preprint)
bearing: transfers densities across removing an element; the engine behind the
  Frankl⟺Nagel equivalence and the T(F)=2 ⟹ (1/2, 1/3) two-abundance result.
  Load-bearing for the abundance-profile thread: it gives the sharpest known
  transfer rule between the family and the family with one element deleted.
anchor: research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md (Lemma 1.1)
ceiling: bound is sharp as stated (author's Remark 2.2), so no improvement
  within this statement; a different statement (e.g. using union-closure of G
  itself rather than a single density) could do better.
```

```claim
id: hsz-nagel-equivalent-frankl
statement: Frankl's conjecture is equivalent to Nagel's conjecture (kth-most
  frequent element has density ≥ 1/(2^{k−1}+1)). This is a reproof of the
  equivalence already in the library via Das–Wu Observation 1.3 (Frankl ⟹
  Nagel) and Nagel's triviality (Nagel ⟹ Frankl); the new content is the sharp
  Lemma 1.1 producing the exact densities 1/(2^k+1) inductively.
hypotheses: F finite union-closed.
holds-here: yes
status: proved (in source; and already established in library via daswu-nagel
  provenance — Das–Wu Observation 1.3)
bearing: the run can rely on Frankl ⟺ Nagel with two independent proofs on
  disk; no need to re-derive. Confirms the daswu-nagel claim's equivalence
  half.
anchor: research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md
  (Prop 3.1); research/sources/das-wu-frequent-elements-2024.full.md (Obs 1.3)
ceiling: equivalence claim, no numeric ceiling; a counterexample family to
  one side would refute it (there is none — both conjectures are open, so the
  equivalence is conditional on their truth).
```

```claim
id: hsz-one-element-of-any-2set-dense
statement: For any A ∈ F with |A| ≥ 2 there exists y ∈ A with
  |F_y| ≥ |F|/(2^{|A|−2}+1). In particular, if F contains a 2-element set,
  some element of it has density ≥ 1/2 (recovering Sarvate–Renaud), and if F
  contains a 3-element set, some element of it has density ≥ 1/3 (well-known),
  with the general bound one Nagel-level stronger than Nagel's Lemma 2.4.
hypotheses: F finite union-closed, A ∈ F, |A| ≥ 2.
holds-here: yes
status: proved (in source; Prop 3.3, elementary)
bearing: the "small sets force SOME element abundance" line: for any set of
  size k in F, one of its elements is in ≥ |F|/(2^{k−2}+1) sets. Tightens the
  folklore singleton/2-set cases to all k and gives the density transfer that
  the abundance-profile thread can use.
anchor: research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md (Prop 3.3)
ceiling: the bound 1/(2^{k−2}+1) is not claimed sharp by the authors for
  k ≥ 4; sharpness only shown for the cases used.
```

```claim
id: hsz-two-element-density-from-record
statement: From any element-density constant c1 for Frankl (currently
  c1 ≈ 0.38234 by Liu/Yu), Lemma 1.1 yields a second element with density
  ≥ 1/(1 + 2(1−c1)/c1) ≈ 0.23635. If T(F)=2 (F contains a 2-element set),
  then (c1, c2) = (1/2, 1/3) is attained among two elements. The conjectured
  best two-element pair is (1/2, 1/3) (Open, Remark 3.4(i)).
hypotheses: F finite union-closed.
holds-here: yes
status: proved (in source; Remark 3.4(iv),(ii)); the (1/2,1/3) conjecture is
  asserted-by-source, open
bearing: gives a concrete numerical target for the abundance-profile thread:
  family with ALL elements of density < 1/3 except one at ~0.38234? The lemma
  says the second-most-frequent element has density ≥ 0.23635 unconditionally
  from the current record. Note KPT Theorem 6(3) constructs exactly-two-
  abundant families with n ≥ 5k−4, so the two-element profile is real.
anchor: research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md (Remark 3.4)
ceiling: the 0.23635 value moves if the record c1 moves; the (1/2,1/3)
  conjecture is open.
```

```claim
id: hsz-published-status
statement: Hu–Shi–Zhou, "A lemma on a finite union-closed family..." is an
  arXiv preprint (v1, 15 Jul 2025); no journal appearance verified as of this
  run.
hypotheses: none.
holds-here: yes
status: asserted-by-source (arXiv listing)
bearing: citation honesty — this is a 2025 preprint, not a published record.
anchor: https://arxiv.org/abs/2507.11008
ceiling: a journal version supersedes.
```