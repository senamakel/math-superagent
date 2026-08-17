# Baek & Balko, "The Erdős–Szekeres Conjecture Revisited" — **full text held**

Source: LIPIcs SoCG 2025 PDF, https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf
Full text: [[baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full]]

> This digest **replaces the abstract-only digest** (`baek-balko - ... 2025 correct.md`),
> which correctly flagged the two Baek–Balko claims as asserted-by-source because only the
> LIPIcs landing page was held. The paper body is now on disk; the split-gon results are
> proved here, while the decomposable-set proof is **omitted in the SoCG version** (deferred
> to the journal version, JCTA 2026). Exact statements below.

## Exact definitions (Section 2–4)

- **Split k-gon** in a point set P: an a-cap and a u-cup that share the **rightmost** point,
  with a + u = k + 2. It has k or k+1 points; if they also share the leftmost point, the k
  points are in convex position.
- **ESsplit(a,u,k)** = least N such that every N-point general-position set contains an
  a-cap, a u-cup, or a split k-gon. T = {(a,u,k): a,u ≥ 2, max{a,u} ≤ k ≤ a+u−2}.
- **Csplit(a,u,k)** = same over **all** 2-colorings of the ordered K³_N (abstract analogue:
  red monotone path = cap, blue = cup, split k-gon = red P³_a + blue P³_u sharing rightmost
  vertex). Point-set colorings χ_P are a subclass, so ESsplit ≤ Csplit.
- **Weak k-gon**: red P³_a + blue P³_u sharing **both** end-vertices; **strong** k-gon:
  sharing only the end-vertices. For point-set colorings every weak k-gon is strong and is
  exactly k points in convex position.
- **Decomposable set**: |P| = 1, or P splits into two decomposable sets A, B with **A deep
  below B** (all of B above every line through two points of A, and all of A below every line
  through two points of B). The ES tightness sets P(a,u) are decomposable; **every non-empty
  subset of a decomposable set is decomposable**.
- **Valtr's construction** (described, credited to Valtr via private comm.): S(a,u,k) points
  arranged as clusters Q_i of C(k−2,i−1) points at positions q_i of a (a+u−k−1)-point set,
  deep below each other, each Q_i free of (k−i+2)-caps and i-cups. **P(a,u,k)** (Erdős–
  Szekeres construction) is the special case where the q_i form a cup and Q_j = P(k+1−j, j+1);
  for a=u=k it is the class of the run's verified `es_construct`.

## Theorems and their evidence in the held text

```claim
id: baek-balko-split
statement: ESsplit(k) = 2^{k-2}+1 for every k ≥ 2 (Theorem 3), from the exact formula ESsplit(a,u,k) = 1 + Σ_{i=k-a+2}^{u} C(k-2, i-2) for all (a,u,k) ∈ T (Theorem 4). Same formula holds for the abstract Csplit(a,u,k) over all 2-colorings of ordered K³_N (Theorem 6).
hypotheses: (a,u,k) ∈ T; planar general position (geometric case); arbitrary red/blue colorings of ordered 3-uniform hypergraphs (abstract case).
holds-here: yes — the geometric statement is exactly the relaxed-threshold claim the run treats as the strongest partial evidence for the 2^{k-2}+1 constant.
status: proved-in-source (upper bound Lemma 10 has a complete proof: down-set injectivity v ↦ D(v) into down-sets of [a−2]×[u−2] with bounding box r×s, r+s ≤ k−1; lower bound Lemma 11 complete via linear-extension/delta-colorings. Lemma 12 (geometric lower bound) says "proof omitted", and Lemma 9 (combinatorial count) says "proof omitted" — both deferred; the framework and both hypergraph + upper bounds are fully written).
bearing: the 2^{k-2}+1 threshold is now proved exactly for the split relaxation, and for the fully abstract hypergraph analogue; the run's `es_construct` at a=u=k is the tightness witness (no split k-gon) and can be machine-checked for split-k-gon-freeness with the oracle (longest cap/cup sharing a rightmost point).
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

```claim
id: baek-balko-decomposable
statement: For a,u ≤ k, every decomposable set of more than S(a,u,k) = Σ_{i=k-a+2}^{u} C(k-2, i-2) points contains an a-cap, a u-cup, or k points in convex position (Theorem 8). In particular every set of more than 2^{k-2} points from a decomposable set contains k in convex position — the ES conjecture holds on decomposable sets.
hypotheses: decomposable point set (A deep below B recursively); a,u ≤ k.
holds-here: yes — a restricted class where the full ES conjecture holds, exactly as the run's threads record.
status: asserted-by-source — the SoCG version states the theorem and says "The proof of Theorem 8 is omitted" (deferred to the full version). NOT proved on disk. Do not upgrade to proved until the JCTA 2026 version is held.
bearing: the run's extremal-structure thread leans on this as the strongest restricted-class result; it remains author-asserted, and the definition of decomposable (deep-below partition) is now held precisely — the run can test candidates for decomposability and verify the theorem's instances computationally.
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

```claim
id: baek-balko-weak7-fails
statement: Cweak(7) > 33 (Theorem 7): there is a 2-coloring of K³_{33} with no weak 7-gon; and Cstrong(7) > 33 was already shown by Balko–Valtr. Hence the abstract (all-colorings) analogue of the ES conjecture fails for weak k-gons already at k=7.
hypotheses: arbitrary 2-colorings of the ordered complete 3-uniform hypergraph; weak/strong k-gon as defined.
holds-here: no — it is a ruling-out statement: any upper bound over arbitrary hypergraph colorings is provably false; the pseudolinear/signotope constraint is essential.
status: proved-in-source (SAT-solver proof reported; the run's balko-valtr-refutes-PS claim is the Cstrong half).
bearing: confirms the run's standing warning — only realizable/pseudolinear (signotope) colorings are admissible; an abstract-order-type upper bound is refuted on arrival.
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

```claim
id: baek-balko-signotope-analogue-open
statement: The signotope analogue of the ES conjecture — every signotope on ≥ 2^{k-2}+1 vertices contains a weak k-gon — is open and equivalent to a conjecture of Goodman–Pollack; with a SAT-based search the authors found NO signotope without a weak k-gon at these sizes (Section 3, last two paragraphs). For signotopes every weak k-gon is a strong k-gon.
hypotheses: signotopes on K³_N (the 1-change-per-4-tuple condition; = pseudoline arrangements by Felsner–Weil).
holds-here: yes — this is exactly the object class of the run's SAT/signotope arm (SMQH, Dumitru, Balko–Valtr encodings), and the target that no abstract-coloring result refutes.
status: asserted-by-source (author-reported experiment; the equivalence to the Goodman–Pollack conjecture is cited/claimed).
bearing: sharpens the computational target: an UNSAT over all signotopes for some N ≥ 2^{n-2}+1 would PROVE the signotope analogue, not refute ES — the correct strengthening to aim the run's encoder test at after reproducing ES(5)=9, ES(6)=17.
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

```claim
id: baek-balko-blowup-new-constructions
statement: Lemma 14 (abstract): for any S and sequences X,Y with x_i+y_i ≤ k−1 and x_i+y_j ≤ k−1−s_{i,j}, the (X,Y)-blow-up b_{X,Y,k}(S) has no k points in convex position and size Σ_l C(k−2,l) over endpoint clusters + Σ C(x_i+y_i, x_i) middle. Theorem 19: for m = k−2x ≥ 3, the x-blow-up of the explicit 2^{m-2}-point set M (Definition 17) has exactly 2^{k-2} points and no k in convex position — a genuinely NEW family of extremal-sized no-convex-k-gon sets generalizing the ES and Valtr constructions. Genetic-algorithm search over all (X,Y) never exceeded 2^{k-2} points (k ≤ 20).
hypotheses: general position; cluster copies P'(y_i+2, x_i+2) / P'(k, x_1+2, k) / P'(y_N+2, k, k) placed almost-vertically in small neighborhoods.
holds-here: yes — concrete extremal constructions the run's oracle can instantiate and test (the M set and its blow-ups are new test beds beyond es_construct for the scored search).
status: proved-in-source (Lemma 14 proof omitted; Theorem 19 has a complete proof with the binomial identity).
bearing: (a) new extremal-shaped sets for the es-nogon scored search (a plateau at 32 on these too would strengthen the structural picture); (b) the blow-up size identity is a checkable constraint for candidate near-extremal sets.
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

## Direct consequences for this run

1. **`baek-balko-split` is now proved on disk** for the split threshold and for the abstract
   hypergraph formula; only the geometric lower-bound Lemma 12 count and Lemma 9 are
   deferred ("proof omitted"). The tightness witness at a=u=k **is the run's `es_construct`**;
   a machine check "es_construct(n) contains no split n-gon" (no a-cap + (n+2−a)-cup sharing
   a rightmost point, for any a) would verify the geometric lower-bound instance at n=5,6,7 —
   a cheap, exact-arithmetic task for the oracle (longest cap/cup per rightmost point are
   already computed by lib.es_geom).
2. **`baek-balko-decomposable` stays asserted-by-source**: "The proof of Theorem 8 is
   omitted" in the held SoCG version. ROOT.md §5.1, the weakened doc, and the threads must
   keep the honest label; the upgrade to proved requires the JCTA 2026 full version.
3. **The signotope analogue is open and is the right target** for the SAT arm (stronger than
   ES, not refuted by any abstract result, still unverified). This is a new, well-posed
   intermediate goal: after the encoder reproduces ES(5)=9 and ES(6)=17, decide the
   signotope analogue at k=7 (N=33).
4. **New extremal families** (M-blown-up constructions, Theorem 19) are concrete inputs the
   es-nogon scorer has not seen; scoring them 32/32 with no 33 is data, and any 33 would be
   the required independent re-verification challenge.

## What this source does NOT help with

It does not settle ES(k) — the paper's own experiments never exceed 2^{k-2}, the weak-k-gon
abstract analogue fails at k=7, and no signotope suppression was found. The gap ROOT.md §7
records (ES(7)=33 open; structural route needed) is unchanged.