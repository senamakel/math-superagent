"""Corroboration (numerical) for two CRT-based erasure conclusions, both proved
rigorously by hand; these checks confirm the accounting but are not the proof.

(A) Lacasa forbidden-block erasure:  the fold's input h[j] = ((q_{j+1}-q_j)/2) mod 2
    is the PARITY of the half-gap.  Lacasa's forbidden mod-6 gap-residue blocks are
    indexed by the half-gap MOD 3.  gcd(2,3)=1 (CRT) => parity independent of symbol,
    so the forbidden-block rule imposes no constraint on the parity string h.  We
    confirm: every parity string in F2^m is realizable by an ALLOWED (non-forbidden)
    6-block, i.e. the forbidden structure leaves NO trace in parity space.

(B) LOS oriented-pair erasure:  the fold bit h[j] = [q_{j+1} != q_j mod 4] is the
    UNORIENTED switch indicator: it merges the oriented pairs (1,3) and (3,1) into a
    single bit.  LOS's secondary K>=2 term C(k) is ODD (C(k) = -C(-k)), i.e. it
    distinguishes (a,b) from (b,a).  We confirm the merge: count how many distinct
    oriented mod-4 residue-pair types map to each fold bit, showing h[j] cannot see
    orientation.
"""

import itertools


def is_forbidden_mod6(tuple_halfgap_mod3):
    """Lacasa: block of half-gaps (mod 3) is forbidden iff some odd prime r is ticked
    by all partial sums (each a distinct residue of 1..r-1 mod r).  Actual gap = 2g,
    partial sum of gaps accumulates, residues mod r."""
    partials = []
    acc = 0
    for g in tuple_halfgap_mod3:
        acc += 2 * g          # actual gap whose residue mod 6 is 2g
        partials.append(acc)
    S = acc
    for r in range(3, S + 3):
        if r % 2 == 0:
            continue
        if not all(r % d != 0 for d in range(2, int(r ** 0.5) + 1)):
            continue
        counts = {}
        ok = True
        for p in partials:
            res = p % r
            if res == 0:
                ok = False
                break
            counts[res] = counts.get(res, 0) + 1
        if not ok:
            continue
        if len(counts) == r - 1 and all(v == 1 for v in counts.values()):
            return True
    return False


def partA():
    print("=== (A) Lacasa forbidden-block erasure under parity projection ===")
    for m in range(1, 6):
        allblocks = list(itertools.product([0, 1, 2], repeat=m))
        adm = [b for b in allblocks if not is_forbidden_mod6(list(b))]
        forb = [b for b in allblocks if is_forbidden_mod6(list(b))]
        # parity projection of a half-gap-mod-3 block: g mod 2.
        adm_parity = set(tuple(g % 2 for g in b) for b in adm)
        full = set(itertools.product([0, 1], repeat=m))
        missing = full - adm_parity
        nf = 3 ** m - 2 ** (m + 1)
        status = ("ERASED (no parity string is killed by the forbidden rule)"
                  if not missing else f"survives: {len(missing)} parity strings killed")
        print(f"  m={m}: |adm|={len(adm)} |forb|={len(forb)} (Lacasa {nf}) | "
              f"parity strings realizable by admissible blocks|={len(adm_parity)}/{2**m} "
              f"-> {status}")
    return


def partB():
    print("\n=== (B) LOS oriented-pair erasure (mod-4 switch, unoriented) ===")
    # residues a,b in {1,3} (reduced residues mod 4); oriented pairs counted.
    residues = [1, 3]
    # fold bit h[j] = [a != b mod 4]
    from collections import defaultdict
    by_bit = defaultdict(list)
    for a, b in itertools.product(residues, repeat=2):
        bit = 1 if a != b else 0
        by_bit[bit].append((a, b))
    for bit in sorted(by_bit):
        pairs = by_bit[bit]
        # how many oriented pairs collapse to this bit, and how much orientation info lost
        switched = sum(1 for (a, b) in pairs if a != b)
        print(f"  h[j]={bit} <- {len(pairs)} oriented pairs {pairs}; "
              f"{len(pairs)} distinct orientations merged into one bit")
    print("  => the fold bit cannot distinguish (1,3) from (3,1); any input that is odd "
          "in the orientation (LOS C(k)=-C(-k)) is invisible to h.")
    return


if __name__ == "__main__":
    partA()
    partB()
