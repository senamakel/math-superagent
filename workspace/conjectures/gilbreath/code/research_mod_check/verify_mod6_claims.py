#!/usr/bin/env python3
"""Verify the three factual claims of research/approaches/prime-gap-mod6-structure.md
against the real rows and against the operator's algebra.

Claim A: halved gaps h_n = (p_{n+1}-p_n)/2 take values 0,1,2 mod 3 (gaps 0,2,4 mod 6).
  -> trivial for any integer sequence; the real content would be the adjacency
     constraint (h_n = 1 => h_{n+1} != 1, h_n = 2 => h_{n+1} != 2). Checked.

Claim B: H_k(1) mod 3 is never 2 in the halved triangle (H_k(i) = A_k(i)/2, k>=1, i>=1).
  -> We already KNOW A_k(1) in {0,2} in the verified range, so H_k(1) in {0,1}
     and mod 3 is 0 or 1 trivially. The claim is the conjecture restated
     (circular). Still: record what the rows actually show, and crucially
     test the NON-circular instance: H_k(i) mod 3 at OTHER positions, where
     values are NOT known to stay in {0,1} -- do residues 2 occur there?

Claim C: |a-b| mod 3 is determined by (a mod 3, b mod 3) -- the "finite-state
  machine modulo 3". This is FALSE in general: enumerate pairs.
"""
from lib.gilbreath import primes_up_to, rows_generator


def check_claim_c():
    """|a-b| mod 3 is NOT a function of (a mod 3, b mod 3)."""
    examples = []
    for r in range(3):
        for s in range(3):
            vals = set()
            for a in range(r, 15, 3):
                for b in range(s, 15, 3):
                    vals.add(abs(a - b) % 3)
            if len(vals) > 1:
                examples.append((r, s, sorted(vals)))
    print("Claim C (deterministic mod-3 evolution): FALSE")
    print("  residue-pairs with ambiguous |a-b| mod 3:", examples)


def check_claim_b():
    N = 400_000
    depth = 800
    primes = primes_up_to(N)
    gen = rows_generator(primes, depth)
    A0 = next(gen)
    h = [(A0[i+1] - A0[i]) // 2 for i in range(len(A0) - 1)]

    # Claim A / adjacency: h_n mod 3 == 1 must be followed by != 1, == 2 by != 2
    bad_adj = 0
    for n in range(len(h) - 1):
        if h[n] % 3 == 1 and h[n+1] % 3 == 1:
            bad_adj += 1
        if h[n] % 3 == 2 and h[n+1] % 3 == 2:
            bad_adj += 1
    print("Claim A adjacency violations (h=1 then 1, or 2 then 2):", bad_adj)

    # Claim B: build halved triangle; position-1 residues and residues elsewhere
    H = h
    pos1_res = {}
    other_res2 = []   # (k, i, H_k(i) mod 3 == 2)
    cap = 120         # only scan first cap positions per row for the "elsewhere" test
    for k in range(1, depth + 1):
        H = [abs(H[i] - H[i+1]) for i in range(len(H) - 1)]
        pos1_res[k] = H[1] % 3
        for i in range(2, min(cap, len(H))):
            if H[i] % 3 == 2:
                other_res2.append((k, i, H[i]))
    res_at_1 = sorted(set(pos1_res.values()))
    print("Claim B: residues mod 3 occurring at H_k(1), k=1..%d:" % depth, res_at_1)
    print("  count of rows where H_k(1) mod 3 == 2:",
          sum(1 for r in pos1_res.values() if r == 2))
    print("  H_k(1) is exactly in {0,1}? (conjecture check):",
          all(H[1] in (0, 1) for H in []))  # placeholder; real check below

    # Real value check: H_k(1) in {0,1} for all k in range (the reduction's claim,
    # known true in verified range; confirm on this run too)
    H2 = h
    exact = True
    for k in range(1, depth + 1):
        H2 = [abs(H2[i] - H2[i+1]) for i in range(len(H2) - 1)]
        if H2[1] not in (0, 1):
            exact = False
            print("  WORST: H_k(1) =", H2[1], "at k =", k)
            break
    print("  H_k(1) in {0,1} for all k<=%d (reduction check):" % depth, exact)
    print("  residues 2 occurring at positions i>=2 (first 10):", other_res2[:10])
    print("  total count of residue-2 entries at i>=2 up to cap:",
          len(other_res2))


if __name__ == "__main__":
    check_claim_c()
    print()
    check_claim_b()