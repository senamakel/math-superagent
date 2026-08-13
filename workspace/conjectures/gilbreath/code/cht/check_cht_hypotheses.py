#!/usr/bin/env python3
"""CHT 2026 Theorem 1.6 hypothesis check against the real prime rows.

Task: decide whether the hypotheses of Theorem 1.6 of Chase-Hunter-Tao 2026
(arXiv:2607.08712, deterministic inverse theorem) hold for the actual prime
data at any depth the run can reach (1000 rows).

Normalized gaps (claim `cht-normalized-gap-definition`, OEIS A100820):
    a_n = (p_{n+2} - p_{n+1})/2 - 1,   n = 1, 2, ...

Quantities computed over the window of the first ~1.27e6 primes (sieve 2e7):
  (1) M  = smallest integer with max a_n <= 2^M   (reports max a_n as well)
  (2) L  = longest run of consecutive 0s in the a_n string, and where it sits
  (3) longest {0,d}-block over all d >= 1: max over d of the longest run of
      entries each lying in {0,d} (numpy vectorised, one pass per d value)
  (4) R_0 = 100 * L * 8^M, the smallest scale of the no-{0,d}-block axiom
      (iii); axiom (iii) must hold at depths <= 2 R_{m-1} and the theorem's
      condition (1.6) needs R_M < (N-N')/2, i.e. an array spanning depth
      > 2 R_0.

Verdict: if R_0 >> 1000 (the run's reachable depth), the theorem's constants
do not bite at any reachable depth -> holds-here: no, with exact numbers.
The answer is a comparison of R_0 to reachable depth, so the sieve is capped
at 2e7 by design: a deeper sieve only raises M by ~1 while R_0 grows by 8^M.

Cost: sieve O(LIMIT log log LIMIT) time / O(LIMIT) space (20 MB bytearray +
~1.27e6-int list); gaps pass O(G); numpy per-d scan O(G * #distinct values)
vectorised with arrays of a few MB.  G = 1,270,605, at most 90 distinct d.
Exact integer arithmetic throughout.
"""
import math
import os

import numpy as np

from lib.gilbreath import primes_up_to

LIMIT = 20_000_000
OUT_MD = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "out", "cht_hypotheses.md")


def longest_run(mask):
    """Length of the longest run of True in a boolean numpy array."""
    if mask.size == 0 or not mask.any():
        return 0
    b = np.concatenate(([0], mask.view(np.int8), [0]))
    d = np.diff(b)
    starts = np.flatnonzero(d == 1)
    ends = np.flatnonzero(d == -1)
    return int((ends - starts).max()) if starts.size else 0


def main():
    print(f"sieve limit: {LIMIT} (fixed; a deeper sieve only raises M by ~1 "
          f"while R_0 grows by 8^M, and the verdict is R_0 vs reachable "
          f"depth 1000)")
    primes = primes_up_to(LIMIT)
    num = len(primes)
    print(f"primes <= {LIMIT}: {num}")

    # normalized gaps a_n for n = 1..num-2 (window the depth-1000 triangle spans)
    gaps = [(primes[i + 1] - primes[i]) // 2 - 1 for i in range(1, num - 1)]
    G = len(gaps)
    print(f"num normalized gaps a_n: {G}")

    # oracle check: first nine gaps must equal OEIS A100820
    expected = [0, 0, 1, 0, 1, 0, 1, 2, 0]
    print(f"first nine a_n: {gaps[:9]}  (OEIS A100820 check: "
          f"{'PASS' if gaps[:9] == expected else 'FAIL'})")
    assert gaps[:9] == expected

    max_a = max(gaps)
    max_idx = gaps.index(max_a) + 1  # 1-based first occurrence n
    M = math.ceil(math.log2(max_a))
    print(f"max a_n = {max_a}  (prime gap {2 * (max_a + 1)}; first at n = "
          f"{max_idx})")
    print(f"M = smallest integer with a_n <= 2^M: {M}  (2^{M - 1} = "
          f"{2 ** (M - 1)} < {max_a} <= {2 ** M} = 2^{M})")
    assert 2 ** (M - 1) < max_a <= 2 ** M

    # longest run of consecutive 0s and where it occurs (1-based)
    L = 0
    L_start = -1
    cur = 0
    cur_start = -1
    for idx, v in enumerate(gaps):
        if v == 0:
            if cur == 0:
                cur_start = idx
            cur += 1
            if cur > L:
                L, L_start = cur, cur_start
        else:
            cur = 0
    print(f"L = longest run of consecutive 0s = {L}  (a_n = 0 for n = "
          f"{L_start + 1}..{L_start + L})")
    # NB p, p+2, p+4 cannot all be prime (one is divisible by 3), so three
    # consecutive a_n = 0 is impossible; L = 2 (from 3,5,7) is exact for all n.

    # longest {0,d}-block over all d >= 1
    arr = np.array(gaps, dtype=np.int64)
    d_vals = np.unique(arr[arr > 0])
    best_len, best_d = 0, None
    per_d = {}
    for d in d_vals:
        rl = longest_run((arr == 0) | (arr == d))
        per_d[int(d)] = rl
        if rl > best_len:
            best_len, best_d = rl, int(d)
    print(f"longest {{0,d}}-block over all d >= 1: length {best_len} "
          f"(attained by d = {best_d})")
    top = sorted(per_d.items(), key=lambda kv: -kv[1])[:5]
    print(f"top (d, longest {{0,d}}-block): {top}")

    R0 = 100 * L * (8 ** M)
    print(f"R_0 = 100 * L * 8^M = 100 * {L} * 8^{M} = {R0}")
    print(f"log10(R_0) = {math.log10(R0):.2f};  R_0 / 1000 = {R0 / 1000:,.1f}")
    reachable = 1000
    print(f"run's reachable depth: {reachable};  R_0 > 1000: {R0 > 1000}")

    verdict = "no" if R0 > 1000 else "yes"

    md = f"""# CHT Theorem 1.6 hypothesis check against the real prime rows

Computed by `code/cht/check_cht_hypotheses.py` (sieve to 2e7, exact integer
arithmetic), output captured in `code/out/cht_hypotheses.captured.txt`.

Theorem 1.6 (Chase–Hunter–Tao 2026, arXiv:2607.08712, deterministic inverse
theorem) concludes `a(N-1,1) in {{0,1}}` from three axioms:

- (i)   `a_n <= 2^M` for all n in the window;
- (ii)  no 0-block of length L anywhere in the array;
- (iii) no {{0,d}}-block (`2^{{M-m}} < d <= 2^{{M-m+1}}`) of length
  `>= R_m - 3 R_{{m-1}}` at depth `<= 2 R_{{m-1}}`, with `R_m >= 4 R_{{m-1}}`
  and `R_0 >= 100 L 8^M`.

## Numbers (window: primes <= 2e7, primes = {num:,}, normalized gaps = {G:,})

- **max a_n = {max_a}** (prime gap {2 * (max_a + 1)}, first at n = {max_idx})
  → **M = {M}** (smallest M with `a_n <= 2^M`:
  `2^{{M-1}} = {2 ** (M - 1)} < {max_a} <= {2 ** M} = 2^{M}`)
- **L = {L}** = longest run of consecutive 0s in the a_n string (occurs at
  n = {L_start + 1}..{L_start + L}).  Note: three consecutive zeroes are
  provably impossible (p, p+2, p+4 cannot all be prime, one is divisible by
  3), so L = 2 is exact for all time.
- **longest {{0,d}}-block over all d >= 1: length {best_len}** (attained by
  d = {best_d})
- **R_0 = 100 * L * 8^M = 100 * {L} * 8^{M} = {R0}**
  (log10(R_0) = {math.log10(R0):.2f})

Axiom (iii) must hold with no {{0,d}}-block at depths up to `2 R_{{m-1}}`,
the smallest scale being R_0, and condition (1.6) of the theorem needs
`R_M < (N - N')/2`, i.e. the array itself must span depth ≳ 2 R_0 ≈
{2 * R0:,} rows.  R_0 = {R0:,} is {R0 / 1000:,.1f} times the run's reachable
depth (1000), so the theorem's hypotheses are **not satisfiable at any depth
this run can reach**: the two obstruction families the theorem names (long
zero-blocks, long shallow {{0,d}}-blocks) live at scales ~{R0:,} and are not
surveyable within 1000 rows.

**Verdict: holds-here = no** — the theorem's constants do not bite at
reachable depths; the inverse theorem gives no information about the prime
rows at depth <= 1000.

```claim
id: cht-inverse-theorem
statement: If a_n <= 2^M, no length-L 0-block, and no {{0,d}}-block (2^{{M-m}} < d <= 2^{{M-m+1}}) of length >= R_m - 3 R_{{m-1}} at depth <= 2 R_{{m-1}} (R_m >= 4 R_{{m-1}}, R_0 >= 100 L 8^M), then a(N-1,1) in {{0,1}}; long zero-blocks and long shallow {{0,d}}-blocks are the only obstructions to decay.
hypotheses: nonneg-integer initial data with a_n <= 2^M; R-tower hierarchy with R_0 >= 100 L 8^M; axioms (ii) no-L-zero-block and (iii) no-shallow-{{0,d}}-block verified at depths up to order R_0, with the array spanning depth > 2 R_0.
holds-here: no (R_0 = {R0:} ≫ 1000: the theorem's no-{{0,d}}-block protection threshold is ~4.2e8 rows, so the hypothesis is not satisfiable at any depth <= 1000 — the theorem does not bite at reachable depths)
status: checked — computed from the real prime rows (sieve 2e7, {num:,} primes, {G:,} normalized gaps a_n = (p_{{n+2}} - p_{{n+1}})/2 - 1): max a_n = {max_a} -> M = {M}, longest 0-run L = {L} (provably exact: p, p+2, p+4 cannot all be prime), longest {{0,d}}-block = {best_len} (d = {best_d}), so R_0 = 100*L*8^M = {R0:,} = {R0 / 1000:,.0f}x the run's max reachable depth (1000). First nine gaps match OEIS A100820.
bearing: the CHT inverse-theorem route cannot be applied to the reachable prime rows; the attack must either rule out long zero-blocks and long shallow {{0,d}}-blocks for the primes (needs analytic hypotheses) or find an invariant bypassing the dichotomy.
anchor: code/out/cht_hypotheses.captured.txt, code/cht/check_cht_hypotheses.py, research/sources/chase-hunter-tao-2026-full-html.full.md (Theorem 1.6)
```
"""
    with open(OUT_MD, "w") as f:
        f.write(md)
    print(f"\nwrote {OUT_MD}")
    print(f"\nVERDICT: holds-here = {verdict}  (R_0 = {R0:,} "
          f"{'>>' if R0 > 1000 else '<='} 1000)")


if __name__ == "__main__":
    main()