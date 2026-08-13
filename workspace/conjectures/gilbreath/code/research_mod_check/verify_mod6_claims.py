#!/usr/bin/env python3
"""Verify the factual claims of research/approaches/prime-gap-mod6-structure.md
against the oracle rows and elementary algebra.

Claim A: halved gaps h_n mod 3 == 1 implies h_{n+1} mod 3 != 1 (gap 2 mod 6
         must be followed by gap 0 or 4 mod 6). Checked on real gaps.
Claim B: in the real rows, H_k(1) mod 3 == 2 never occurs (k <= depth).
         Note: since H_k(1) in {0,1} in the verified range (conjecture), the
         residue is trivially 0 or 1; residue 2 occurs at other positions.
Claim C: |a-b| mod 3 is NOT a function of (a mod 3, b mod 3), so the approach's
         "finite-state machine modulo 3" is not well-defined; also tested is
         whether the mod-3 reduction of the operator is even well-defined on
         residues (it is not).
"""
import sys
from lib.gilbreath import primes_up_to, rows_generator


def claim_c():
    """Show |a-b| mod 3 is not a function of (a,b) mod 3."""
    examples = []
    for r in range(3):
        for s in range(3):
            outs = set()
            for a in (r, r + 3, r + 6, r + 9):
                for b in (s, s + 3, s + 6, s + 9):
                    outs.add(abs(a - b) % 3)
            if len(outs) > 1:
                examples.append((f"a={r} mod 3, b={s} mod 3", sorted(outs)))
    print("Claim C: |a-b| mod 3 is NOT determined by (a mod 3, b mod 3):")
    for ex in examples[:6]:
        print("   ", ex)
    print("    => the operator has no well-defined reduction mod 3; residues",
          "evolve with multiplicity (a 'finite-state machine mod 3' needs",
          "the full values, not just residues).")


def claim_b(depth=700, N=400_000):
    primes = primes_up_to(N)
    gen = rows_generator(primes, depth)
    A0 = next(gen)
    h = [(A0[i + 1] - A0[i]) // 2 for i in range(len(A0) - 1)]

    # Claim A adjacency
    bad_adj = 0
    for n in range(len(h) - 1):
        if h[n] % 3 == 1 and h[n + 1] % 3 == 1:
            bad_adj += 1
        if h[n] % 3 == 2 and h[n + 1] % 3 == 2:
            bad_adj += 1
    print(f"Claim A: h_n mod 3 == 1 followed by 1 (gap 2 then 2): {bad_adj}")
    # more precisely per-residue transitions
    trans = {(a, b): 0 for a in range(3) for b in range(3)}
    for n in range(len(h) - 1):
        trans[(h[n] % 3, h[n + 1] % 3)] += 1
    print("   transition counts (h_n mod 3 -> h_{n+1} mod 3):", dict(trans))

    # Claim B
    H = h
    pos1 = []
    other_2 = 0
    for k in range(1, depth + 1):
        H = [abs(H[i] - H[i + 1]) for i in range(len(H) - 1)]
        pos1.append((k, H[1]))
        for i in range(2, min(200, len(H))):
            if H[i] % 3 == 2:
                other_2 += 1
    vals = {v for _, v in pos1}
    print(f"Claim B: H_k(1) values over k=1..{depth}: min={min(v for _,v in pos1)},"
          f" max={max(v for _,v in pos1)}, distinct={sorted(vals)}")
    print("   H_k(1) mod 3 == 2 any k?", any(v % 3 == 2 for _, v in pos1))
    print(f"   entries at positions i>=2 with residue 2 mod 3: {other_2} "
          f"(sample count up to position 200 per row)")

    # Show how few rows still have non-{0,1} halved second entry vs the full
    # halved triangle (distribution of H_k(1) over the first rows)
    from collections import Counter
    print("   distribution of H_k(1) values (first 80 rows):",
          dict(Counter(v for k, v in pos1 if k <= 80)))


if __name__ == "__main__":
    claim_c()
    print()
    claim_b()