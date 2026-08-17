# Scholar verification pass — Baek–Balko split proof-status, Balko–Valtr, Károlyi–Tóth

Source-verification pass against the primary full texts. Everything here was
read from the `.full.md` sources cited, not from memory. Memory server is down
(`remember_memory` refused; recall graph half 409s), so this note is the stand-in
for Cognee and should be pushed to durable memory when the server recovers.

## What this pass verified, and the one genuinely new nuance

The library is phase-1 complete and heavily digested (109 claims, ~38 claim-bearing
summaries, ROOT.md meeting its GOAL-1 test). My value-add this cycle was to verify
the most load-bearing structural claim the current task queue rests on — the
Baek–Balko split threshold — against the primary full text, and to pin down exactly
which half of it is proved and which is asserted.

### (1) Baek–Balko SoCG 2025 — the split theorem is proved ONLY in the abstract half

Read `research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`
lines 471–650. Precise state:

- **Theorem 6 (abstract) is fully proved.** Upper bound via Lemma 10 (complete
  proof: injectivity of the down-set map v ↦ D(v), bounding-box r+s ≤ k−1, count
  via Lemma 9). Lower bound via Lemma 11 (complete proof: explicit δ-coloring
  χ on the down-set lattice). So
  Csplit(a,u,k) = 1 + Σ_{i=k−a+2}^{u} C(k−2, i−2) for all (a,u,k) ∈ T **holds**,
  over all 2-colorings of the ordered 3-uniform hypergraph.
- **Lemma 9** (number of down-sets in [a−2]×[u−2] with bounding box r×s, r+s ≤
  k−1, equals that binomial sum) is stated **proof-omitted**, but it is an
  elementary lattice count (the same line-partition / down-set count that
  Moshkovitz–Shapira and CFHMSV use, #down-sets in [m]×[n] = C(m+n,m)).
- **Theorem 4 (geometric) upper bound** = Theorem 6 upper bound + (3)
  ESsplit ≤ Csplit. Proved.
- **Theorem 4 (geometric) lower bound** ESsplit(a,u,k) ≥ 1 + Σ rests on
  **Lemma 12, whose proof is omitted** in the SoCG version (deferred to the JCTA
  2026 journal version, which this run does not hold). So the *general* (a,u,k)
  geometric tightness is **asserted-by-source**, not proved here.

Consequence for the run: the existing `baek-balko-split` claim "proved" (from the
SoCG digest) overstates the geometric half. The **abstract** threshold
Csplit(k)=2^{k-2}+1 is proved; the **geometric** ESsplit(k)=2^{k-2}+1 is proved
via the upper bound but the matching lower bound is asserted until Lemma 12 is
held. However, the a=u=k case the run actually uses (tightness witness =
es_construct) is machine-verified on disk: es_construct(n) contains no
paper-split-n-gon at n=5,6,7 (see scratch "split-gon spectrum disambiguation"),
so the *specific* tightness threshold ESsplit(n) ≥ 2^{n-2}+1 that the run leans on
is checked independently of Lemma 12.

The prior scholar cycle's discrepancy (baek-balko-decomposable "proved" vs
"asserted") is confirmed: **Theorem 8 (decomposable)** is verbatim "The proof of
Theorem 8 is omitted" (line ~330 of the full text). It stays load-bearing-but-
unverified until the JCTA 2026 full text is held. CONTEXT.md Established still
says "proved (SoCG 2025)" for the split/decomposable result — that line overstates
the evidence and should be corrected to "split upper bound + abstract threshold
proved; geometric lower bound and decomposable theorem asserted-by-source".

### (2) Balko–Valtr — the non-pseudolinearity of the refuting counterexamples is confirmed

`balko-valtr-refutes-PS` (cES(7)>32, cES(8)>64) refutes the Peters–Szekeres
strengthened conjecture over ALL 2-colorings of K³_N. The full text's
pseudolinear discussion (lines 225–242) confirms: a coloring is pseudolinear iff
every 4-tuple induces a realizable coloring; over pseudolinear colorings they
verify the ETV-Conjecture-3.1 values N(4,7,7)=16, N(4,8,8)=22, matching the
conjecture. Since the non-geometric counterexamples are FOUND by SAT on the
unrestricted (non-pseudolinear) hypergraph, they do NOT realize as planar point
sets — so this is a true theorem about a weaker abstraction, and it does not touch
the geometric ES conjecture. `holds-here: no` is the correct stance (as recorded).
The open request `balko-valtr-attack-baa4` and `open-access-full-1e6e` are both
answered by the held ENDM 2015 full text (its encoding is the triple-orientation /
red-blue K³_N formulation the run's SAT arm should reproduce).

### (3) Károlyi–Tóth twin construction — the second family the task queue needs exists and is explicit

The current task queue (directive 23) requires a "second family" beyond
es_construct to test lifting. `karolyi-toth-twin-construction` — the recursive
twin set T_n with |T_n|=2^n, no 2^n+1 convex points — is confirmed against the
primary (lines 112–132): each point of T_{k−1} is replaced by a near-twin pair
along a line ℓ in general position (Lemma 2 proves no 2^n+1 convex points via the
"twins are consecutive on the hull ⇒ at most two twin pairs ⇒ m−2 parents in
T_{n−1} convex" induction), and the separation property (Lemma 3) makes it avoid
every separation-property order type. This is a genuine alternative near-extremal
family, realizable, with structure explicit enough to run the cone-capacity and
supersaturation DPs on. (Note the twin size is 2^n with no 2^n+1 convex points —
near-extremal but NOT at the 2^{n-2} scale; the run must scale/adjust to compare
at the same N as es_construct.)

## Sources that do not help (confirmed, so nobody reads them again)

- **Aichholzer order-type DB** — only up to n≤10; ES(7)=33 is far beyond its
  range. Usable as small-n enumeration source and for the second-family lifts at
  n≤10, not for ES(7) full.
- **CFHMSV "big line or big convex polygon"**, **Holmsen–Mojarrad–Pach–Tardos**,
  **Suk** — asymptotic 2^{n+o(n)} bounds, recorded as context only; cannot settle
  the exact constant 2^{n-2}+1.
- **k-convex IWOCA** — log-type bounds on a relaxation; encyclopedic only.
- **MIS-DOWNLOAD stubs** — nothing; never cite.

## Durables for memory (push to Cognee when the server recovers)

**D1 — Baek–Balko split proof-status split.** Abstract Csplit(k)=2^{k-2}+1 proved
(Lemmas 10, 11 complete; Lemma 9 omitted but elementary); geometric ESsplit lower
bound rests on omitted Lemma 12 (asserted until JCTA 2026); the a=u=k tightness
witness (es_construct) is machine-verified independently. Decomposable Theorem 8
is asserted ("proof omitted"). Correct the CONTEXT.md Established line.

**D2 — PointSAT/Dumitru/Koshelev–Koshka frontier.** ES(7)=33 open; all 32-point
no-7-gon candidates found in abstract order-type space are unrealizable (200k
sampled), none refutes. An upper-bound proof must enforce realizability.

**D3 — Balko–Valtr + Baek–Balko-Theorem-7 double confirmation that the abstract
(unrestricted) analogue fails.** Any proof over all 2-colorings / all abstract
chirotopes is trying to prove something false; pseudolinearity (4-tuple
realizability) is essential.

## Claim blocks (entering derived/CLAIMS.md)

```claim
id: baek-balko-split-proof-status
statement: In Baek–Balko (SoCG 2025), the abstract split threshold is fully proved — Csplit(a,u,k) = 1 + Σ_{i=k−a+2}^{u} C(k−2,i−2) for all (a,u,k) ∈ T (Theorem 6), via Lemma 10 (upper bound: injective down-set map, complete) and Lemma 11 (lower bound: δ-coloring, complete), Lemma 9 (down-set count) stated proof-omitted but elementary; the geometric upper bound ESsplit ≤ Csplit is proved; but the geometric lower bound ESsplit(a,u,k) ≥ 1 + Σ (Theorem 4) rests on Lemma 12 whose proof is omitted in the SoCG version (deferred to JCTA 2026), so the general geometric tightness is asserted-by-source. The a=u=k case (ESsplit(k) = 2^{k-2}+1) is nevertheless machine-verified in this run at n=5,6,7 via the paper-witness es_construct (no paper-split-n-gon), independently of Lemma 12.
hypotheses: (a,u,k) ∈ T; split k-gon = a-cap + u-cup sharing rightmost vertex, a+u = k+2; ordered 3-uniform hypergraph colorings for the abstract half; planar general position for the geometric half.
holds-here: yes — the run leans on ESsplit(n) ≥ 2^{n-2}+1 only at a=u=k, machine-checked.
status: verified against primary full text (lines 471–650); the a=u=k tightness witness is checked (scratch split-gon spectrum).
bearing: narrows which of the two Baek–Balko claims may be cited as proved: the abstract Csplit threshold (proved) and the geometric upper bound (proved) yes; the general geometric lower bound no (asserted until Lemma 12/JCTA 2026). Consistent with baek-balko-split, whose status field already records the Lemma 12/9 omissions.
follows-from: baek-balko-split
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
```

```claim
id: karolyi-toth-twin-explicit
statement: The Károlyi–Tóth twin construction T_n is explicit and realizable: T_0 is one point; T_k replaces each p ∈ T_{k−1} by a near-twin pair p′,p″ along a line ℓ in general position; |T_n| = 2^n; Lemma 2 proves T_n contains no 2^n+1 points in convex position (twins consecutive on the hull ⇒ at most two twin pairs ⇒ m−2 parents in T_{n−1}); Lemma 3 (separation property) shows T_n avoids every order type with the separation property. Used as the second (non-es_construct) near-extremal family.
hypotheses: line ℓ not parallel to any line determined by T_{k−1}; twin segments short enough to preserve order type.
holds-here: yes — a realizable alternative near-extremal family, though at scale 2^n (no 2^n+1 convex) rather than 2^{n-2}, so it must be scaled/adjusted to compare with es_construct at equal N.
status: verified against primary full text (lines 112–132).
bearing: supplies the "second family" directive 23 requires for the cone-capacity and supersaturation lifts.
anchor: research/sources/karolyi-toth-2012-ES-forbidden-subconfigurations-springer.full.md
```

## What the run still lacks (unchanged)

- ES(7)=33 open; no exact value or counterexample beyond n=6.
- JCTA 2026 (deferred proofs of Lemma 12 and Theorem 8).
- Machine check of the PointSAT 23-point h(6,7) witness and Koshelev–Koshka
  17/18-point coordinate sets against `lib.es_geom`.
- Cognee storage of the durable findings in this note (server down).
