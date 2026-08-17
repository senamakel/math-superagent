# Extremal splitting: the stability reduction for ES(n) ≤ 2^{n−2}+1

**Status of this decomposition: BROKEN at n = 7.** The crux lemma G-split is
refuted by the run's own checked computation (see `killed-by` and the discharge
notes). This is a result, not a dead file: the naive splitting-line induction
*f(n) ≤ 2 f(n−1)* cannot prove the conjecture, because its one structural lemma
fails already at n = 7 on the canonical construction. A proof of ES(n) needs a
different mechanism than "every extremal set splits into two (n−1)-avoiding
halves" — the Baek–Balko split-*k*-gon theorem (`baek-balko-split`, asserted-by-source)
is a candidate for a correct reformulation of that split, and it is where the
reduction should be rebuilt from.

```skeleton
goal: For every n ≥ 3, ES(n) ≤ 2^{n-2}+1 — i.e. every set of 2^{n-2}+1 points in general position in the plane contains n points in convex position. (The matching lower bound ES(n) ≥ 2^{n-2}+1 is settled; only the upper bound is the open claim.)
implies: Let f(n) be the maximum size of a set in general position with no convex n-gon; then ES(n) = f(n)+1, so the goal is equivalent to f(n) ≤ 2^{n-2} for all n ≥ 3. Induction on n. Base (n = 3): f(3) = 2 = 2^{1}. Step (n ≥ 4): let X be an extremal n-avoiding set, |X| = f(n). By the splitting lemma (G-split) there is a line ℓ meeting no point of X such that the two open half-planes' parts X⁺, X⁻ each contain no convex (n-1)-gon. Then |X| = |X⁺| + |X⁻| ≤ 2·f(n-1) ≤ 2·2^{n-3} = 2^{n-2}. THIS INFERENCE IS REFUTED AT n = 7. G-split is false as stated: the verified 32-point 7-avoiding set es_construct(7) does not split into two 6-avoiding halves (checked), yet if G-split held at n=7 the induction would force f(7) = 32, making es_construct(7) extremal, whereupon G-split would apply to it and give the split that the checked data says is absent. See killed-by for the full chain. The decomposition therefore proves nothing beyond n = 6. The cup–cap characterization (G-cupcap) is DISCHARGED — it is the run's own checked claim g-cupcap-verified (and the classical 1935 cups-caps / four-point criterion). It was the dictionary that rewrites "no convex (n-1)-gon in a half-plane" as a cups-and-caps condition; that dictionary is still available, but the lemma is no longer open.
killed-by: G-split refuted at n=7 by the run's own checked data. Chain: (1) es_construct(7) verified 32-point 7-avoiding => f(7)>=32; (2) f(6)=16 (es-exact-values); (3) G-split at n=7 would give f(7)<=2*f(6)=32, so f(7)=32 and es_construct(7) is extremal; (4) G-split must then split es_construct(7), but gsplit-enum-completeness-and-n7-zero reports 0 splits (all 992 half-planes; a 32-pt split into two 6-avoiding halves forces both =16). Contradiction. G-cupcap discharged by g-cupcap-verified; G-split-consistent discharged by gsplit-enum-completeness-and-n7-zero. The naive splitting-line induction f(n)<=2f(n-1) cannot prove ES(n); a replacement structural step is needed (Baek-Balko split-k-gon theorem is the constructive candidate).
rests-on: f(3) = 2 (elementary: any three points in general position form a convex triangle). The settled lower bound es-lower (f(n) ≥ 2^{n-2}), the exact base values es-exact-values (ES(3..6) = 3,5,9,17, so f(6) = 16), and the checked template facts es-construct-layer-extremality and gsplit-enum-completeness-and-n7-zero. All are recorded in the claims ledger.
status: broken
```

```gap
id: G-cupcap
lemma: (Cup–cap characterization, Erdős–Szekeres 1935.) After a rotation
      making all x-coordinates distinct: a set X in general position contains
      n points in convex position iff for some k ∈ {2,…,n} it contains a k-cup
      C and an (n+2−k)-cap D whose leftmost and rightmost points coincide
      (equivalently, C ∪ D is exactly n points in convex position).
status: discharged
discharged-by: g-cupcap-verified (checked) — the run's own oracle split a set
      into cups/caps and confirmed the iff on 624 sets, 1220 (set,n) cases,
      1220 agreement, 0 mismatch; plus the classical es35-cups-caps-bound and
      four-point-criterion. No longer a gap.
next: none — already established. Do not restate as open.
```

```gap
id: G-split
lemma: (Extremal splitting / stability.) For every n ≥ 4, every extremal
      n-avoiding set X (|X| = f(n), no convex n-gon, general position) admits
      a line ℓ containing no point of X such that each of the two open
      half-planes' parts of X contains no convex (n−1)-gon.
status: refuted (at n = 7)
discharged-by: the contradiction in killed-by, built from the checked claims
      gsplit-enum-completeness-and-n7-zero (0 splits on the 32-point
      7-avoiding es_construct(7)), es-construct-layer-extremality (it is a
      verified 32-point 7-avoiding set), es-lower (f(7) ≥ 32), and
      es-exact-values (f(6) = 16). Those four force: if G-split held at n=7,
      then f(7) = 32 and es_construct(7) is extremal, so G-split must apply to
      it — contradicting the checked zero. The general lemma is false for
      n ≥ 7.
next: none for this statement — it is dead. The constructive replacement, if
      the induction is to be revived, is the Baek–Balko split-*k*-gon theorem
      (baek-balko-split, asserted-by-source — held doc is the LIPIcs abstract
        page: ES_split(k) = 2^{k-2}+1, tight for split
      k-gons), which redefines "split" as a convex (k−1)-gon plus two special
      points rather than a half-plane cut of the whole set. The open question
      that would re-attach to the goal is whether every set of 2^{n-2}
      no-convex-n-gon points is in fact a split configuration in the
      Baek–Balko sense — that is a different, genuinely open structural lemma.
```

```gap
id: G-split-consistent
lemma: (Consistency on the extremal template.) The Erdős–Szekeres 1960
      construction of 2^{n-2} points, realized as es_construct, admits a line
      separating it into two (n−1)-avoiding halves of 2^{n-3} points each.
      The split counts are 4 (n=5), 2 (n=6), 0 (n=7).
status: discharged
discharged-by: gsplit-enum-completeness-and-n7-zero (checked) — the rotating-
      line enumerator, validated exactly (zero missing / zero extra, count
      N(N−1)) against the 2^N oracle at N=8..16, re-captured with provenance
      (command + EXIT:0), gives 4 splits at n=5, 2 at n=6, 0 at n=7. This
      supersedes all earlier counts (6/4/2/0 and 57/241/993 / 50/222/946, which
      came from the dead pair-line enumerator). The n=7 zero is precisely the
      counterexample that refutes G-split (see G-split).
next: none — established. Its n=7 verdict is now a refutation of the crux
      lemma, so its role flipped from "consistency check" to "kills the
      decomposition"; record that in the thread.
```
