"""
Verify the Lacasa mod-6 -> parity projection claim (the crux of whether the
one unconditional K>1 input survives to the fold's parity string h).

Claim under test (research/notes/lacasa_parity_projection_transfer.md, recorded
as a *conjecture* at the general m):
  For every m, every binary parity block (b_1..b_m) is realisable as
  h_j = (g_j/2) mod 2 from actual gaps g_j, so the parity string carries NO
  forbidden-block constraint from the mod-6 enumeration at any order. Equivalently
  the projection map (mod-6 classes + free gap-parity) is surjective onto all
  binary blocks from BOTH the admissible and the forbidden mod-6 classes.

Two checks:
  (A) ABSTRACT: given a mod-6 class c_j in {0,2,4}, the parity bit is
      h_j = (a_j mod 2) ^ (c_j/2 mod 2) where g_j = 6 a_j + c_j.  Since a_j is a
      free parameter (any even gap >= 2 in class c is realisable), for ANY fixed
      class vector c the map p -> (p_j ^ (c_j/2 mod 2)) is a bijection on
      {0,1}^m.  Hence every binary block is realisable from every fixed class
      vector c, in particular from both an admissible and a forbidden one.
      This is checked by enumerating all c-vectors and all binary targets.
  (B) DATA: against the REAL prime gap sequence, confirm that every binary
      block of length m appears in the parity string h for m up to a bound —
      i.e. the real prime parity string carries no forbidden block at small order.
"""
import sympy

def parity_string(N):
    """h[j] = ((p_{j+1}-p_j)/2) mod 2 for the first N primes."""
    primes = list(sympy.primerange(2, sympy.nextprime(N * 20)))  # enough primes
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    return [ (g//2) % 2 for g in gaps ]

def check_abstract(m):
    """For every mod-6 class vector c in {0,2,4}^m and every binary target b,
    there is a free parity p (a_j mod 2) solving b_j = p_j ^ (c_j/2 mod 2).
    Since p is free this is a tautology; we enumerate to confirm."""
    classes = [0, 2, 4]
    from itertools import product
    ok = True
    for cvec in product(classes, repeat=m):
        contrib = [(cj // 2) % 2 for cj in cvec]
        free_parities = [b ^ k for b, k in [(0,0),(1,1)]]  # per bit
        # for each bit j, both values of b_j achievable by choosing p_j
        for j in range(m):
            achievable = {p ^ contrib[j] for p in (0,1)}
            if achievable != {0,1}:
                ok = False
    return ok

def check_data(N, m, needed):
    """Every binary block of length m appears in h over the first N primes?"""
    h = parity_string(N)
    from itertools import product
    seen = set()
    for i in range(len(h) - m + 1):
        seen.add(tuple(h[i:i+m]))
    missing = [b for b in product([0,1], repeat=m) if tuple(b) not in seen]
    return seen, missing

if __name__ == "__main__":
    print("(A) ABSTRACT projection surjectivity")
    for m in range(1, 7):
        print(f"  m={m}: every mod-6 class vector, every target bit reachable -> {check_abstract(m)}")

    print("(B) REAL prime parity string  -- all blocks present?")
    N = 200000
    for m in range(1, 7):
        seen, missing = check_data(N, m, 2**m)
        print(f"  m={m}: seen {len(seen)}/{2**m} blocks, missing {len(missing)}")
        if missing:
            print("        missing:", missing[:8])
