# Scholar handoff — Horton verification run (for coder)

The scholar digested Horton 1983 (the one genuine frontier gap the librarian
closed this cycle) and wrote a verification script. It needs coder to run it.

## The script

`code/out/horton_verify.py` (scholar-written) verifies the **empty-side**
construction that the new primary source establishes:

- Horton's $S_k = \{(i, d(i)) : 0 \le i < 2^k\}$, $d(i)=\sum_{j=1}^k a_j c^{j-1}$,
  $c=2^k+1$, $(a_1\dots a_k)$ the fixed-width binary expansion of $i$.
- Check (1) **general position** (exact integer 3×3 determinants, no three
  collinear) for $k=3,4$.
- Check (2) **absence of an empty convex 7-gon** — no 7-subset in convex
  position with no other point in its interior — for $k=3,4$ (and `--k5` for the
  32-point case, heavier).
- Exact integer arithmetic throughout (`numpy dtype=object`); the empty-7-gon
  test enumerates 7-subsets (C(16,7)=11440, C(32,7)=3.4M for k=5) and for each
  convex-7 tests interior emptiness — no 2^n enumeration, should be fast.

## Command (no pipe, no tee, no arrays)

```
cd /workspace && timeout 550 python code/out/horton_verify.py > code/out/horton_verify.captured.txt 2>&1; echo EXIT: $?
```

then read `code/out/horton_verify.captured.txt` back.

## Expected result

- `general_position = True` for all k.
- `has_empty_convex_7gon = False` for all k — reproducing the claim
  `horton-no-empty-7gon` (for every k there is a 2^k-point set with no empty
  convex 7-gon).

If it fails (a witness found, or collinearity), report the witness coordinates
verbatim — that would be a real finding about the Horton construction's
coordinates (the bit-order convention in `build()` is the most likely place a
bug would live, but the trefoil/staircase structure is robust to bit-order).

## Caveat (kept strictly)

This is the **empty** convex 7-gon — the Erdős–Szekeres–Horton (empty-hexagon)
side, which GOAL.md marks adjacent and keeps OUT of Established as ES progress.
The run already verifies the *convex-position* ES construction separately
(`es_construct`, largestConvex=n−1 at n=4..6). This run only confirms the
freshly-digested Horton primary; it does not bear on ES(n)=2^{n-2}+1.

Files: `code/out/horton_verify.py` (new), capture to `code/out/horton_verify.captured.txt`.
