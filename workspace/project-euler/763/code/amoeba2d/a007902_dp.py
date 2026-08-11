"""Exact DP for OEIS A007902 (2D amoeba / pebble-spreading counts).

G(k, m) counts the 2D reachable configurations with k pebbles whose "extra"
/top structure sits at level m (a structural auxiliary from the OEIS entry,
Alois P. Heinz).  a(n) = number of reachable configs with n pebbles, offset 1
with a(1) = 1, a(n) = G(n, 0) for n >= 2.

Verified recurrence (works for all base cases / boundary k this DP reaches):
    G(k, m):
        k < 1          -> 0
        m = 0          -> 2*G(k-1, 0) + G(k, 1) + (1 if k == 2 else 0)
        m = 1          -> G(k-3, 0) + 2*G(k-2, 1) + G(k-1, 2) + G(k-4, 1)
        m >= 2         -> G(k-m-2, m-1) + 2*G(k-m-1, m) + G(k-m, m+1)
    a(1) = 1;  a(n) = G(n, 0) for n >= 2

Indexing care:
  - The k < 1 guard is essential: many terms call G with negative indices
    (e.g. G(k-1, 0), G(k-4, 1), G(k-m-2, m-1)) and those must read as 0.
  - m can exceed k+1; then the m>=2 branch's indices are all negative/zero and
    return 0 (with the guard), so the table naturally dies off.
  - The [k==2] term in the m=0 line is the only explicit base constant.

Run:  python code/amoeba2d/a007902_dp.py  [max_n]  [--table k]
"""

import sys
from functools import lru_cache

# Reference values from OEIS A007902 (offset 1).
A007902_FIRST_22 = [
    1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668,
    87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805,
]


@lru_cache(maxsize=None)
def G(k, m):
    """A007902 auxiliary G(k, m).  Returns 0 for k < 1."""
    if k < 1:
        return 0
    if m == 0:
        return 2 * G(k - 1, 0) + G(k, 1) + (1 if k == 2 else 0)
    if m == 1:
        return G(k - 3, 0) + 2 * G(k - 2, 1) + G(k - 1, 2) + G(k - 4, 1)
    # m >= 2
    return G(k - m - 2, m - 1) + 2 * G(k - m - 1, m) + G(k - m, m + 1)


def a(n):
    """Number of reachable 2D pea-configs with n pebbles, offset 1."""
    if n == 1:
        return 1
    return G(n, 0)


def a_seq(max_n):
    return [a(n) for n in range(1, max_n + 1)]


def g_table(k_max):
    """Print the full G(k, m) table for 1 <= k <= k_max, m >= 1 (column m=1..)."""
    lines = []
    header = "k \\ m | " + " ".join(f"{m:>10}" for m in range(0, k_max + 1))
    lines.append(header)
    lines.append("-" * len(header))
    for k in range(1, k_max + 1):
        row = [f"{k:>4}   "]
        for m in range(0, k_max + 1):
            row.append(f"{G(k, m):>10}")
        lines.append(" | ".join(row))
    return "\n".join(lines)


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    table_k = int(sys.argv[sys.argv.index("--table") + 1]) if "--table" in sys.argv else 10

    seq = a_seq(max_n)
    print(f"a(1..{max_n}) =")
    print(seq)

    # Check against OEIS reference up to a(22).
    ref = A007902_FIRST_22[:max_n]
    match = seq == ref
    print(f"\nmatches OEIS A007902 first {max_n} terms: {match}")

    print(f"\ntarget check: a(22) = {seq[21]} (OEIS says 13686805): "
          f"{'OK' if seq[21] == 13686805 else 'FAIL'}")

    print("\n" + "=" * 60)
    print(f"G(k, m) table for k = 1..{table_k}")
    print(g_table(table_k))


if __name__ == "__main__":
    main()
