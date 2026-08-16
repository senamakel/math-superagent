# Definitive enumeration-completeness recheck — Phase-1 valid, Phase-2 superseded (steer 10)

Runs `code/out/gsplit_enum_definitive.py` (exact integer arithmetic, `lib.es_geom`
orientation determinants, no floats).

**Steer 10 status.** The Phase-1 oracle validation (below) stands: the
rotating-line construction `ordered_pair_sides` matches the 2^N disjoint-hulls
oracle exactly at N=8..16, so it is the right enumerator to reuse. But its
`gsplit_enum_definitive.captured.txt` lacks the command+exit line (it was not
captured with `echo EXIT: $?` and no bashisms), and its Phase-2 n=5,6,7 split
counts (4/2/0) are part of the earlier gsplit record that steer 10 supersedes.
The pair-line numbers it disparages (2·C(N,2)+1) were wrong in both directions
(operator recheck: 50/222/946 with 33-40 false positives on es_construct), and
the original `gsplit_exhaustive.captured.txt` was a shell error, not a run.
Re-capture this script with the safe command and treat a fresh Phase-2 run as
the only record before citing any n=5,6,7 split counts.

## The two pre-existing audit scripts were unreliable AND self-contradictory

Both `code/out/gsplit_enum_recheck.py` and `code/out/gsplit_enum_validate.py`
existed but had never been run. Run now, they disagree with each other and with
the steer's true count:

- `gsplit_enum_validate.py`: N=8 oracle=56, pair-line=52 (missing 4); claims
  2·C(N,2)+1 on the wrong premise.
- `gsplit_enum_recheck.py`: N=8 pair-line=56 ("expected 57"); the 2^N oracle in
  it is **buggy** (reports only 30 open sides at N=8 — the hulls_disjoint test
  there is broken), so it "found" 26 false positives that are in fact genuine
  sides its own broken oracle failed to see.

So neither audit can be trusted for the n=7 gsplit question; the earlier
`gsplit_exhaustive.captured.txt` n=7 zero rested on the pair-line scheme that the
steer flagged as the right-cardinality/wrong-set enumeration.

## The corrected enumeration, validated EXACTLY

The steer directive names the complete standard construction: for each ordered
pair (a,b), the strict-left side plus the 4 ways to include the two on-line
points. This is `ordered_pair_sides` in `gsplit_enum_definitive.py`. It is
validated against an independent 2^N brute-force oracle (strict convex-hull
separation, which uses NO line construction) on random general-position integer
sets:

| N | oracle (=N(N-1)) | ordered-pair enum | missing | extra |
|---|------------------|-------------------|---------|-------|
| 8  | 56  | 56  | 0 | 0 |
| 10 | 90  | 90  | 0 | 0 |
| 12 | 132 | 132 | 0 | 0 |
| 14 | 182 | 182 | 0 | 0 |
| 16 | 240 | 240 | 0 | 0 |

So the count of distinct nonempty-proper open half-plane sides of an N-point
general-position set is exactly **N(N-1)**, and the rotating-line construction
produces every one of them with zero missing and zero extra. The steer's diagnosis
is confirmed: the pair-line scheme in `gsplit_exhaustive.py` returned
`2·C(N,2)+1 = N(N-1)+1` — the right cardinality (off by one) and the wrong set,
generating spurious sides while missing genuine ones.

## n=7 gsplit result — CHECKED (steer 11)

The Phase-2 split counts below (n=5→4, n=6→2, n=7→0) are now **checked**: they
were re-captured with full provenance (command line + `EXIT: 0`) on the
validated rotating-line enumerator into `code/out/gsplit_phase2.captured.txt`.
The re-run reproduces Phase-1 exactly (N(N-1) matches at N=8,10,12,14,16, zero
missing, zero extra) and the Phase-2 counts 4 / 2 / 0.

Re-running the gsplit question on the **verified** `lib.es_construct` ES construction
with the complete, validated enumeration:

| n | N | sides_enum (=N(N-1)?) | size-target bipartitions checked | VALID splits (both halves 2^{n-3} pts, both (n-1)-avoiding) |
|---|-----|------------------------|-----------------------------------|--------------------------------------------------------------|
| 5 | 8  | 56  (yes) | 8  | 4 |
| 6 | 16 | 240 (yes) | 22 | 2 |
| 7 | 32 | 992 (yes) | 32 | 0 |

The n=7 zero above is **now checked** (steer 11): it comes from a fresh
rotating-line run of `gsplit_enum_definitive.py` captured with full provenance
(command + `EXIT: 0`) into `code/out/gsplit_phase2.captured.txt`, which
reproduces Phase-1 exactly (N(N-1) at N=8..16) and the Phase-2 split counts
4 / 2 / 0 at n=5,6,7 on the validated enumerator.

```claim
id: gsplit-enum-completeness-and-n7-zero
statement: The count of distinct nonempty-proper open half-plane sides of an N-point planar set in general position is exactly N(N-1), realized completely and with no spurious side by the rotating directed-line construction (ordered pairs (a,b) with the 4 inclusions of the two boundary points). Validated exactly (zero missing, zero extra) against a 2^N convex-hull-separation oracle at N=8..16. On the verified es_construct ES template (2^{n-2} points, no convex n-gon), over all N(N-1) open half-plane bipartitions, splits into two (n-1)-avoiding halves of size exactly 2^{n-3} exist at n=5 (4 splits) and n=6 (2 splits) and do NOT exist at n=7 (0 splits). Scoped strictly to this es_construct template at these n — not a statement about other extremal sets, not the general G-split lemma.
hypotheses: vertices in general position (no three collinear); the rotating directed-line (k-set) construction; convexity and collinearity tested by exact integer determinants (lib.es_geom.orient); 2^N oracle feasible at N<=16; es_construct is the verified ES 2^{n-2}-point no-convex-n-gon construction.
holds-here: true — exactly this problem, on general-position integer sets and on the es_construct fractions.
status: checked (Phase-1 enumeration N=8..16 AND Phase-2 split counts 4/2/0, re-captured with provenance)
formalisation:
bearing: The rotating-line enumeration is the correct exhaustive enumerator and is validated. On this es_construct template the splitting-line induction f(n)<=2f(n-1) (prove ES(n) by splitting into two (n-1)-avoiding halves of size 2^{n-3}) HOLDS through n=6 and FAILS at n=7 (no valid split exists). This blocks the simple recursive proof for n>=7 on this construction; it does not rule out other extremal sets or the general G-split lemma.
anchor: code/out/gsplit_phase2.captured.txt (command+EXIT:0)
```
