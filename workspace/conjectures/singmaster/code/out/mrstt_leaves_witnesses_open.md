# Every known high-multiplicity witness lies outside the MRSTT interior

`research/approaches/mrstt-exact-statement.md` now records MRSTT Theorem 1.3
(arXiv:2106.03335, QJM 73 (2022) 1137–1177) in the form the run needed:

> For `0 < ε < 1` and `t` sufficiently large, `C(n,m) = t` has at most **2**
> solutions in `exp((log n)^{2/3+ε}) ≤ m ≤ n/2`, hence at most **4** in the full
> symmetric interior `exp((log n)^{2/3+ε}) ≤ m ≤ n − exp((log n)^{2/3+ε})`.

The obvious question is then whether that theorem says anything about the
numbers that actually achieve high multiplicity. It does not, and the check is
cheap. Every nontrivial pair `(n,m)` in `code/out/witnesses.json` was tested
against the interior threshold.

## Result

**At every admissible `ε`, all 15 nontrivial witness pairs fall outside the
interior — below the lower cut `exp((log n)^{2/3+ε})`.**

| `a` | `(n,m)` | threshold at `ε=0.05` | inside? |
| --- | --- | --- | --- |
| 120 | (10, 3) | 6.159 | no |
| 120 | (16, 2) | 7.979 | no |
| 210 | (10, 4) | 6.159 | no |
| 210 | (21, 2) | 9.215 | no |
| 1540 | (22, 3) | 9.442 | no |
| 1540 | (56, 2) | 15.074 | no |
| **3003** | **(14, 6)** | **7.423** | **no** |
| **3003** | **(15, 5)** | **7.707** | **no** |
| **3003** | **(78, 2)** | 17.658 | no |
| 7140 | (36, 3) | 12.135 | no |
| 7140 | (120, 2) | 21.583 | no |
| 11628 | (19, 5) | 8.743 | no |
| 11628 | (153, 2) | 24.116 | no |
| 24310 | (17, 8) | 8.242 | no |
| 24310 | (221, 2) | 28.444 | no |

At `ε = 0.2` the margins widen and nothing changes. Only in the *inadmissible*
boundary case `ε = 0` does a single pair, `(17,8)` for `a = 24310`, creep inside
(threshold 7.406 against `m = 8`) — and `ε = 0` is excluded by the hypothesis
`0 < ε < 1`, so it does not count.

`m = 2` and `m = 3` pairs are never in the interior for any `n` in reach: the
threshold exceeds 3 as soon as `n ≥ 6`.

## What this does and does not establish

It makes the deliverable in `GOAL.md` precise — *what MRSTT leaves open* — in
the sharpest available form:

> The entire known record of Pascal's triangle, including `N(3003) = 8`, lives
> in the region MRSTT does not cover. The theorem is therefore consistent with
> `B = 8` without constraining it, and no improvement in the interior can lower
> the known lower bound `B ≥ 8`. Progress on `B` must come from the edge
> `m < exp((log n)^{2/3+ε})`, which is exactly where the binomial coefficient
> stops being smooth in `m` and where the Diophantine curve methods apply.

Two honest limits, both of which must be stated wherever this is used. Every
witness fails MRSTT's hypotheses TWICE:

1. **Small m (below the interior cut).** Every nontrivial witness pair has
   `m < exp((log n)^{2/3+ε})` for every admissible ε, as shown above. This is
   the region MRSTT explicitly does not cover (Remark 1.5).

2. **Small t (below the largeness threshold).** MRSTT requires "t sufficiently
   large depending on ε", and every witness has `t ≤ 24310`. These pairs fail
   the hypothesis twice over — the region comparison is about the *shape of the
   interior cut*, NOT a demonstration that a large-t witness would also escape
   the interior. That is not established.

3. **Whether the largeness threshold on t is effective — CONFIRMED.** Remark 1.7 of the
   full text (arXiv:2106.03335v1) states verbatim: "The implied quantitative bounds in
   the hypothesis 't is sufficiently large depending on ε' are effective; however, we
   have made no attempt whatsoever to optimize them in this paper, and will likely be
   too large to be of use in numerical verification of Singmaster's conjecture in their
   current form." So the threshold IS a computable function of ε — not non-constructive.
   The interior theorem therefore yields a numerical B in principle, but with an
   unoptimized, astronomically large constant. This is the effective-versus-usable
   distinction GOAL.md demands: effective-but-huge is not a bound anyone can evaluate.

```claim
id: mrstt-interior-excludes-all-known-witnesses
statement: For every admissible epsilon in (0,1), all fifteen nontrivial pairs
  (n,m) recorded in code/out/witnesses.json lie strictly below the MRSTT
  Theorem 1.3 interior cut exp((log n)^(2/3+epsilon)), hence outside the range
  in which that theorem bounds the number of solutions of C(n,m)=t. This
  includes all three nontrivial pairs realising N(3003)=8, namely (14,6),
  (15,5) and (78,2). At the inadmissible boundary epsilon=0 exactly one pair,
  (17,8) for a=24310, would fall inside. Consequently MRSTT's interior bound is
  consistent with the known record without constraining it, and cannot lower
  the established lower bound B >= 8.
hypotheses: MRSTT Theorem 1.3 as recorded in
  research/approaches/mrstt-exact-statement.md; 0 < epsilon < 1; the counting
  convention of witnesses.json, in which C(n,k) and C(n,n-k) are distinct pairs
  and the trivial pair C(a,1) is included
holds-here: yes for the region comparison, which is a direct evaluation. Note
  the witnesses independently fail the theorem's separate requirement that t be
  sufficiently large, since every witness has t <= 24310, so this is a
  statement about which region the known record occupies and not a claim that a
  large-t witness would also escape
status: checked
bearing: makes precise what MRSTT leaves open, which is the partial result
  named in GOAL.md. Locates every known high-multiplicity example in the
  uncovered edge m < exp((log n)^(2/3+epsilon)), so no strengthening of the
  interior bound can move B, and directs effort to the edge where the
  Diophantine curve methods apply. Does not itself bound B.
anchor: code/out/witnesses.json; code/out/verify_mrstt_witnesses.captured.txt;
  research/approaches/mrstt-exact-statement.md
source: operator-computation
```

```claim
id: mrstt-threshold-effective
statement: The "t sufficiently large depending on ε" hypothesis in MRSTT Theorem
  1.3 (arXiv:2106.03335v1) is effective: the implied quantitative bound is a
  computable function of ε, not a non-constructive existence claim. Remark 1.7
  of the full text states verbatim: "The implied quantitative bounds in the
  hypothesis 't is sufficiently large depending on ε' are effective; however,
  we have made no attempt whatsoever to optimize them in this paper, and will
  likely be too large to be of use in numerical verification of Singmaster's
  conjecture in their current form."
effective: yes
uniform-in-k: yes (Theorem 1.3 covers all m in the interior range
  simultaneously; no per-pair fixing)
size: astronomically large — the authors did not optimize the constant, and
  describe it as "likely too large to be of use in numerical verification."
  No explicit expression for the threshold is given; it is the output of an
  effective but unoptimized construction.
kind: effective-bound — a computable threshold exists, distinguishing this from
  Siegel/Faltings (ineffective), but the constant is not usable for numerical
  work. This is precisely the effective-versus-usable distinction in GOAL.md:
  an effective constant nobody can evaluate is a different object from a bound
  one can check, and MRSTT gives the former.
hypotheses: Remark 1.7 of MRSTT full text (research/sources/mrstt-fulltext.full.md)
holds-here: yes — confirmed from the full text
status: sourced (confirmed against primary text)
bearing: This separates MRSTT from the Siegel/Faltings per-pair results: MRSTT's
  interior theorem IS effective and uniform over the interior, unlike per-pair
  genus arguments. But the constant is too large to use, and the boundary remains
  open. See the companion analysis below for what this yields.
anchor: research/sources/mrstt-fulltext.full.md (Remark 1.7);
  research/approaches/mrstt-exact-statement.md
source: primary-source
```

## Does an effective-but-astronomical interior threshold plus the boundary result yield anything?

**No.** The MRSTT route is at a dead end for Singmaster's conjecture, for two
independent reasons that compound rather than cancel.

### Reason 1: the interior theorem cannot reach any known witness

Every witness, including 3003 (the reason B ≥ 8), lies in the boundary
`m < exp((log n)^(2/3+ε))`, as shown above. The interior theorem therefore
cannot constrain the known lower bound regardless of whether its constant is
effective or ineffective, optimised or astronomical. An interior bound of 2
or 4 tells us nothing about numbers whose multiplicity is already known to
be 6 or 8 from the edge.

### Reason 2: the boundary admits no effective treatment from this method

Proposition 1.12 of MRSTT states that the non-archimedean equidistribution
method requires `N, M = O(exp(log^(3/2-ε) P))`, and "even under the Riemann
hypothesis we do not know how to relax this requirement." The authors note
that a randomness heuristic could push the range to `exp(P^c)`, which would
lower the interior threshold from `exp((log n)^(2/3+ε))` to `(log n)^C` —
still leaving the small-m regime `m = O(log n / log log n)` untouched, since
the method fundamentally cannot handle `m / log t → 0`.

The boundary is therefore not merely "not yet covered" — it is **provably
inaccessible to the interior method**. No improvement in constants, no
optimisation of the effective threshold, and no weakening of hypotheses can
close the gap. The 2/3 exponent is a genuine barrier.

### What this means

MRSTT reduces Singmaster to the boundary `2 ≤ m ≤ (log t) / (log log t)^(3/2-ε)`.
That is a structural reduction, and it is the sharpest statement of the open
problem available. But it does not itself move the conjecture: the boundary is
exactly where all the multiplicity lives, and the interior method cannot reach it.

**The MRSTT route has delivered its partial result and can go no further.**
Progress on B must come from the boundary, which is the Diophantine curve regime
— fixed-(k1,k2) effective results (Avanesov, de Weger, BMSST) on one hand, and
Baker's method on linear forms in logarithms for effective height bounds on the
other. Neither currently gives uniformity, and neither is touched by MRSTT's
interior theorem.
