# G-split exhaustive line test — exact state of the question (steering item 3)

## The question

For the **verified** ES lower-bound construction `lib.es_construct` (N = 2^{n-2}
points, no convex n-gon), does **ANY** line (containing no point of the set)
split the set into two halves each free of a convex (n-1)-gon?

Because |S| = 2^{n-2} and an (n-1)-avoiding half has at most 2^{n-3} points, a
valid split forces each half to have **exactly** 2^{n-3} points (the halves sum
to 2^{n-2}). The effective question is:

> Is there a side of size exactly 2^{n-3} whose complement is also (n-1)-avoiding?

## The standard fact that makes it exhaustive

Every combinatorially distinct half-plane bipartition of a finite planar point
set is realized by a line through a pair of its points (the usual k-set fact:
as a line rotates, its "side" changes only when it passes a point, and the
bipartition on either side of a pair collapses onto the pair-line). So it
suffices to enumerate, for each of the C(N,2) pairs of points, the line through
the pair and the small perturbations off it (assigning the two on-line points
to each side in all ways). This is implemented in
`code/out/gsplit_exhaustive.py`.

## What is already established (captured in commands.log)

- **`gsplit_consistent.py`** (the dead guess the directive named): the single
  candidate **even-index vs odd-index block split** satisfies "each half is
  2^{n-3} points and is (n-1)-avoiding" at n=5,6,7 (both halves no-convex-4/5/6).
  ```
  n=5: even 4pts no-4 True, odd 4pts no-4 True
  n=6: even 8pts no-5 True, odd 8pts no-5 True
  n=7: even16pts no-6 True, odd16pts no-6 True
  ```
- **`gsplit_line.py`**: that same even/odd split is NOT strictly line-separable
  at n=5,6,7 (no member of that one candidate family is a separating line).
  ```
  Line-separability of even vs odd block halves (strict line):
    n=5 False, n=6 False, n=7 False
  ```

So the even/odd candidate *fails to be line-realizable* even though both sides
are (n-1)-avoiding. That is exactly why the directive called it a dead guess: an
actual line must separate the two halves, and no line separates even from odd
blocks in this radial placement.

The exhaustive test (`gsplit_exhaustive.py`) enumerates ALL C(N,2) pair-lines ×
perturbations, i.e. every combinatorially distinct bipartition, and checks each
size-2^{n-3} side against has_convex_k_subset(n-1). **Its result is NOT yet
captured in commands.log** — the file exists but no run output for it is on disk.

## What an empty result would rule out

If gsplit_exhaustive finds **no** line splitting the es_construct set into two
(n-1)-avoiding halves at n=5,6,7, then:

- The split reduction `f(n) <= 2 f(n-1)` (prove ES(n) by splitting an extremal
  set into two (n-1)-avoiding halves) **fails on this specific construction**.
- **Scope strictly**: this rules out a line-split for THIS template (the ES
  radial construction) at THESE n. It does NOT rule out other extremal sets or
  the general split lemma — other hypothetical extremal sets at the same size
  might (in principle) be splittable, and the split reduction needs the split to
  hold for *every* extremal set, which empty-result-on-one-template does not touch.

## Status — SUPERSEDED (steer 10); steer 11 accepts Phase 1 done

- The captured `gsplit_exhaustive.captured.txt` was a **shell error, not a run**:
  its command used `${PIPESTATUS[0]}` (a bash array) under `/bin/sh` (dash) and
  died `exit: 2 ... Bad substitution`, so the script never re-ran.
- The operator's recheck of the pair-line scheme on `es_construct` gives
  50/222/946 distinct bipartitions at n=5,6,7 — not the 57/241/993 the old
  capture reported — with 33-40 false positives per set. The pair-line
  enumeration is wrong in both directions, so the 6,4,2,0 valid-split decay and
  the n=7 zero are NOT established.
- **Steer 11:** Phase 1 of the rotating-line enumerator is ACCEPTED DONE — it
  matches the 2^N disjoint-hulls oracle exactly at N=8,10,12,14,16 (zero
  missing/zero extra, count N(N-1)). The remaining work is one provenance
  re-capture (task `gsplit-enumeration-recheck`): re-run n=5,6,7 into
  `code/out/gsplit_phase2.captured.txt` with the command and exit code, then read
  it back. If it reproduces 4 splits at n=5, 2 at n=6, 0 at n=7, promote
  `gsplit-enum-completeness-and-n7-zero` to checked for the split counts and
  retire `gsplit-exhaustive-esconstruct` pointing at the new anchor. If not,
  report the new numbers plainly. Do not start another enumerator.

The stale statements below are kept for history only; do not cite them.

```claim
id: gsplit-even-odd-not-line-separable
statement: For the verified es_construct ES construction at n=5,6,7, the even-index vs odd-index block halves each have exactly 2^{n-3} points and are (n-1)-avoiding, but NO straight line strictly separates those even-blocks from the odd-blocks in this radial placement.
hypotheses: the es_construct construction (2^{n-2} no-convex-n-gon), the even/odd block-index bipartition, n in {5,6,7}
holds-here: yes
status: checked (captured in commands.log: gsplit_consistent + gsplit_line)
bearing: the naive 'split by parity of block index' candidate for the f(n)<=2f(n-1) reduction is NOT line-realizable, so it is a dead guess; the exhaustive all-lines question remains open.
anchor: code/out/gsplit_consistent.py, code/out/gsplit_line.py
```

`gsplit-exhaustive-pending` CLOSED (steer 8): it was a duplicate of
`gsplit-exhaustive-esconstruct` whose "result not yet captured" text went stale once
`code/out/gsplit_exhaustive.captured.txt` landed, and it contradicted
`gsplit-exhaustive-esconstruct` beside it. The single live claim is
`gsplit-exhaustive-esconstruct` in `code/out/gsplit_exhaustive_claim.md` (n=7 zero
still provisional pending `gsplit-enumeration-recheck`).
