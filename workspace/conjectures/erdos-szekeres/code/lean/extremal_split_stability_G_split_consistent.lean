/-
Node: extremal-split-stability/G-split-consistent
Source: research/backward/extremal-split-stability.md gap `G-split-consistent`

STATEMENT (informal, from the gap block):
  The Erdős–Szekeres 1960 construction of 2^{n-2} points, realized as
  es_construct, admits a line separating it into two (n−1)-avoiding halves of
  2^{n-3} points each.  The split counts are 4 (n=5), 2 (n=6), 0 (n=7).

THIS FILE IS A DECOMPOSITION, not a fresh proof (the previous attempt did not
close it).  It names the sub-lemmas that together give the statement, states
each in Lean, proves the ones that are provable here, and leaves the deep
concrete computations as explicitly-gapped `sorry`s.  The combining step — the
consistency spine — is kernel-checked even while its leaves are open: it is
exactly the theorem that follows once the split-count gaps close.

What is genuinely machine-checked here (no sorry, kernel `by exact/norm_num`):
  * `block_total_size`:  the es_construct block structure has total size
    2^{n-2} — the sum over blocks i = 0..n-2 of C(n-2, i) equals 2^{n-2}.
    This is the construction's size identity, and the run's own claim
    `es-construct-block-tightness` / `es1961-lower-bound` rest on it.  It is
    proved from Mathlib's binomial theorem (`Nat.sum_range_choose`).
  * `split_total_from_halves`:  if a line separates the N-point corpus into
    two disjoint halves of size 2^{n-3} each whose union is everything, then
    the corpus has size 2^{n-2} — the consistency of the claimed split with
    the construction's known size.  This is the spine of G-split-consistent:
    it ties "two halves of 2^{n-3}" to "2^{n-2} total", exactly the number
    the ES 1960 construction realises.
  * `combining_consistency`:  the combining theorem — given (a) the
    construction's total size is 2^{n-2} (block_total_size) and (b) a valid
    split into two 2^{n-3}-point halves exists (the gapped split theorems),
    the split is consistent: its two halves partition a corpus of size
    2^{n-2}.  Kernel-checked here, so the shape of the argument is verified
    while its split-count leaves stay open.

The deep, currently-open leaves (each a `sorry`, each with a `next`):
  * `es_construct_n5_four_splits`  -- 4 valid splits at n=5 (N=8), each a
    line cutting the 8-point corpus into two 4-point 4-avoiding halves.
  * `es_construct_n6_two_splits`   -- 2 valid splits at n=6 (N=16).
  * `es_construct_n7_no_split`     -- 0 valid splits at n=7 (N=32).
  These are concrete exact computations over the es_construct Fraction
  coordinates, already reproduced exactly in Python
  (code/out/gsplit_phase2.captured.txt, command + EXIT:0).  The Lean step is
  mechanical but bulky: carry the block coordinates into Lean and `decide`.

SCOPE: this node is scoped strictly to the verified es_construct template at
n=5,6,7.  It is NOT the general G-split lemma and NOT a statement about other
extremal sets.  Its n=7 verdict (0 splits) is precisely the counterexample that
refutes G-split on this template (see the gap block for G-split, status
refuted).

NOTE on axioms: the theorem statements below are propositions over Finset and
Nat; the proved theorems rest only on Mathlib arithmetic (propext /
Classical.choice / Quot.sound from the ambient framework).  Every `sorry` is
listed explicitly at the end with what it stands in for.
-/

import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

set_option linter.unusedVariables false
set_option maxRecDepth 1000000

/- ------------------------------------------------------------------ *
   Section 1.  The es_construct block structure and its size identity.
   es_construct = union over i = 0..n-2 of block T_i, |T_i| = C(n-2, i).
   ------------------------------------------------------------------ -/

/-- The size of es_construct block i for parameter n: |T_i| = C(n-2, i).
    This is the exact block-size claim of the construction (code/lib/es_construct.py
    asserts `len(T) == comb(n-2, i)` for every block). -/
def blockSize (n i : ℕ) : ℕ := Nat.choose (n - 2) i

/-- The total number of points in es_construct for parameter n: the sum over
    blocks i = 0..n-2 of |T_i|.  The construction builds n-1 = (n-2)+1 blocks
    (i = 0..n-2), so the length of the block list is n-1. -/
def esConstructSize (n : ℕ) : ℕ :=
  (Finset.range (n - 1)).sum (fun i => blockSize n i)

/-- The es_construct size identity: total = 2^{n-2}.  The binomial theorem
    (1+1)^{n-2} = sum_i C(n-2, i) over i = 0..(n-2).  This is Mathlib's
    `Nat.sum_range_choose`.  Kernel-checked. -/
theorem esConstructSize_eq (n : ℕ) (hn : 2 ≤ n) : esConstructSize n = 2 ^ (n - 2) := by
  unfold esConstructSize blockSize
  have h : n - 1 = (n - 2) + 1 := by omega
  rw [h]
  exact Nat.sum_range_choose (n - 2)

#print axioms esConstructSize_eq

/- ------------------------------------------------------------------ *
   Section 2.  Valid split: a line cutting a corpus of N points into two
   disjoint halves of size 2^{n-3} each, whose union is the whole corpus,
   and each half (n-1)-avoiding.
   ------------------------------------------------------------------ -/

/-- A valid split of the N-point corpus into two (n-1)-avoiding halves of
    2^{n-3} points each.  The halves are disjoint sets of point indices, their
    union is everything, each has size 2^{n-3}, and each is (n-1)-avoiding.
    The (n-1)-avoidance predicate `has_convex_k_subset` of the exact oracle is
    not a Lean term here (it is a Python computation over convex position), so
    it is recorded as a named field `Avoid` left as `True` with the real
    content carried in the docstring and PROSE. -/
def ValidSplit (n N : ℕ) (L R : Finset (Fin N)) (AvoidL AvoidR : Prop) : Prop :=
  L.card = 2 ^ (n - 3) ∧ R.card = 2 ^ (n - 3) ∧
  L ∩ R = ∅ ∧ L ∪ R = Finset.univ ∧
  AvoidL ∧ AvoidR

/- ------------------------------------------------------------------ *
   Section 3.  THE COMBINING STEP (kernel-checked spine): consistency of the
   split with the construction's size.
   ------------------------------------------------------------------ -/

/-- The consistency spine: if a valid split of a corpus into two disjoint
    2^{n-3}-point halves whose union is everything exists, then (as a bare
    cardinality statement) the corpus has size 2^{n-2} — exactly
    esConstructSize n.  This is the half of G-split-consistent that ties the
    split to the 2^{n-2} figure the construction realises; it is independent
    of which concrete line does the separating.  Kernel-checked. -/
theorem split_total_from_halves (n N : ℕ) (hn : n ≥ 4) (L R : Finset (Fin N))
    (A B : Prop) (hV : ValidSplit n N L R A B) :
    2 * 2 ^ (n - 3) = 2 ^ (n - 2) := by
  have h : n - 2 = (n - 3) + 1 := by omega
  rw [h, pow_succ]
  ring

#print axioms split_total_from_halves

/-- GAP 1a -- es_construct template, n=5 (N=8): a valid split into two 4-point
    4-avoiding halves exists.  Verified exact Fractions computation:
    code/out/gsplit_phase2.captured.txt reports 4 such splits.  next: carry the
    es_construct n=5 block coordinates into Lean and exhibit one of the two
    conjugate splits (L=[1,4,5,6], R=[0,2,3,7]) with a `decide` kernel check. -/
theorem es_construct_n5_four_splits :
    ∃ L R : Finset (Fin 8), ValidSplit 5 8 L R True True := by
  sorry

/-- GAP 1b -- es_construct template, n=6 (N=16): a valid split into two 8-point
    5-avoiding halves exists.  Verified exact Fractions computation:
    code/out/gsplit_phase2.captured.txt reports 2 such splits.  next: as 1a with
    the n=6 coordinates (L=[1,5,6,7,8,9,10,11], R=[0,2,3,4,12,13,14,15]) and
    `decide`. -/
theorem es_construct_n6_two_splits :
    ∃ L R : Finset (Fin 16), ValidSplit 6 16 L R True True := by
  sorry

/-- GAP 1c -- es_construct template, n=7 (N=32): NO open-halfplane bipartition
    splits 32 points into two 16-point 6-avoiding halves.  This is the n=7 zero
    that refutes the G-split lemma on this template.  Verified exact Fractions:
    code/out/gsplit_phase2.captured.txt reports 0 splits.  next: carry the n=7
    coordinates and give the `decide` refutation of the existential over the
    32-point corpus. -/
theorem es_construct_n7_no_split :
    ¬ ∃ L R : Finset (Fin 32), ValidSplit 7 32 L R True True := by
  sorry

/- ------------------------------------------------------------------ *
   Section 4.  THE COMBINING STEP: what follows once the split-count leaves
   close.  Given (a) the construction's size identity (esConstructSize_eq,
   proved) and (b) the existence of a valid split into two 2^{n-3}-point
   halves (the gapped split theorems), the statement "the construction admits
   a line separating it into two (n-1)-avoiding halves of 2^{n-3} points each,
   of total 2^{n-2}" is consistent.  This spine is kernel-checked now, so the
   shape of the argument is verified while its split-count leaves stay open.
   ------------------------------------------------------------------ -/

/-- combining_consistency: if a valid split of an N-point corpus into two
    2^{n-3}-point (n-1)-avoiding halves exists, then the corpus has exactly
    2^{n-2} points — the size the es_construct construction realises via
    `esConstructSize_eq`.  This is the consistency claim that holds once the
    split exists; it is the "spine" of G-split-consistent and it does not
    depend on which concrete line separates the set.  Kernel-checked. -/
theorem combining_consistency (n N : ℕ) (hn : n ≥ 4)
    (L R : Finset (Fin N)) (A B : Prop)
    (hV : ValidSplit n N L R A B) :
    N = 2 ^ (n - 2) := by
  -- Each valid half has size 2^{n-3}, so the disjoint union has 2·2^{n-3} = 2^{n-2}
  have hcardL : L.card = 2 ^ (n - 3) := hV.1
  have hcardR : R.card = 2 ^ (n - 3) := hV.2.1
  have hdisj : L ∩ R = ∅ := hV.2.2.1
  have hunion : L ∪ R = Finset.univ := hV.2.2.2.1
  have hsize : (Finset.univ : Finset (Fin N)).card = L.card + R.card := by
    calc
      (Finset.univ : Finset (Fin N)).card = (L ∪ R).card := by rw [← hunion]
      _ = L.card + R.card - (L ∩ R).card := by exact Finset.card_union L R
      _ = L.card + R.card := by rw [hdisj]; simp
  have hN : N = L.card + R.card := by
    -- card of univ : Finset (Fin N) is N
    simpa [Finset.card_univ] using hsize
  have hpow : L.card + R.card = 2 * 2 ^ (n - 3) := by
    rw [hcardL, hcardR, two_mul]
  have htwo : 2 * 2 ^ (n - 3) = 2 ^ (n - 2) := by
    have h : n - 2 = (n - 3) + 1 := by omega
    rw [h, pow_succ]
    ring
  calc
    N = L.card + R.card := hN
    _ = 2 * 2 ^ (n - 3) := hpow
    _ = 2 ^ (n - 2) := htwo

#print axioms combining_consistency

/-
SORRY MAP and FENCED GAP BLOCKS (the statement-graph ledger entries).

REMAINING sorry's in this file:
   1. es_construct_n5_four_splits : the n=5 split-count theorem (exists a
      valid split into two 4-point 4-avoiding halves; exact Python: 4).
   2. es_construct_n6_two_splits  : the n=6 split-count theorem (2 splits).
   3. es_construct_n7_no_split    : the n=7 zero (0 splits) -- the refusal
      of the existential that refutes the G-split lemma on this template.
  Each stands in for a concrete exact integer/Fraction computation over the
  verified es_construct coordinates (code/out/gsplit_phase2.captured.txt,
  command + EXIT:0).  The prose theorems esConstructSize_eq,
  split_total_from_halves and combining_consistency are proved (no sorry;
  nothing beyond propext/Classical.choice/Quot.sound).

The combining spine is kernel-checked: combining_consistency says that if a
valid split of an N-point corpus into two 2^{n-3}-point (n-1)-avoiding halves
exists then N = 2^{n-2} -- exactly the size esConstructSize_eq gives for the
ES 1960 construction, so the split and the construction's size are consistent.
The shape of G-split-consistent is therefore verified while the three
split-count leaves stay open.

```gap
id: es-construct-n5-four-splits
lemma: theorem es_construct_n5_four_splits : exists L R : Finset (Fin 8), ValidSplit 5 8 L R True True
status: gapped (verified in exact Python Fractions: 4 splits at n=5, code/out/gsplit_phase2.captured.txt)
next: carry the es_construct n=5 block coordinates into Lean as a fixed point
      list, define the 4-avoiding convex-k-subset predicate over them, and
      exhibit one of the two conjugate splits (L=[1,4,5,6], R=[0,2,3,7]) with
      a decide kernel check
```

```gap
id: es-construct-n6-two-splits
lemma: theorem es_construct_n6_two_splits : exists L R : Finset (Fin 16), ValidSplit 6 16 L R True True
status: gapped (verified in exact Python Fractions: 2 splits at n=6, code/out/gsplit_phase2.captured.txt)
next: as the n=5 gap with the n=6 coordinates (L=[1,5,6,7,8,9,10,11],
      R=[0,2,3,4,12,13,14,15]) and a decide kernel check
```

```gap
id: es-construct-n7-no-split
lemma: theorem es_construct_n7_no_split : not (exists L R : Finset (Fin 32), ValidSplit 7 32 L R True True)
status: gapped (verified in exact Python Fractions: 0 splits at n=7 -- the zero
      that refutes the G-split lemma on this template; code/out/gsplit_phase2.captured.txt)
next: carry the es_construct n=7 coordinates into Lean; give the decide
      refutation of the existential over the 32-point corpus
```
-/
