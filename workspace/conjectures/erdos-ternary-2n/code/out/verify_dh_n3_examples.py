"""Verify the two worked n=3 examples in Dimitrov-Howe (arxiv 2105.06440).

Equation (1), n=3: 3^x = 2^{a1}+2^{a2}+2^{a3} mod M.

Operational definitions from the paper:
  - A power 2^i is DETERMINATE mod M iff the only b>=0 with 2^b == 2^i (mod M)
    is b=i.  Equivalently, 2^i is on the "tail" of the powers-of-2 diagram.
  - A residue-class solution 3^x == sum 2^{a_j} (mod M) is "bad"/extraneous
    (in the Section 3 sense) iff at least one summand power 2^{a_j}, or the
    power 3^x, is indeterminate.

Paper claims:
  M1 = 5440 = 2^6 * 5 * 17  : has extraneous solutions (solution (6) involves
        indeterminate 2^6 mod M1).
  M2 = 2^7 * 5 * 17 * 257   : is CLEAN — the only solution is
        3^4 = 2^0+2^4+2^6 mod M2, with 2^0,2^4,2^6 all determinate (on tail).
"""
import itertools

def pow2_tail_loop(M):
    """Return (tail_set, loop_set) of distinct residues 2^i mod M, as sets of
    exponents that are determinate (tail) vs indeterminate (loop).
    A residue is on the tail iff its exponent is the unique preimage; because
    powers of 2 mod M stabilize once i >= v2(M), the tail is exactly the set of
    exponents i for which 2^i appears only once in {2^0,2^1,...}."""
    seen = {}
    seq = []
    i = 0
    r = 1 % M
    while r not in seen:
        seen[r] = i
        seq.append(r)
        r = (r * 2) % M
        i += 1
    # loop starts at index seen[r]; everything before is the tail.
    loop_start = seen[r]
    tail_exps = list(range(loop_start))
    loop_len = i - loop_start
    # determinate exponent i  <==>  i is a tail exponent
    return tail_exps, loop_len

def pow3_cycle(M):
    """Cycle (period) of the powers of 3 mod M, and set of residues."""
    seen = {}
    i = 0
    r = 1 % M
    while r not in seen:
        seen[r] = i
        r = (r * 3) % M
        i += 1
    return i - seen[r], set(seen.keys())

def determinate_pow2_exps(M):
    tail, _ = pow2_tail_loop(M)
    return set(tail)

def enum_solutions(M):
    """Enumerate all residue-class solutions to 3^x == 2^a+2^b+2^c mod M,
    with 0<=a<=b<=c, and return list of (x_resclass, a,b,c, has_indeterminate).
    A solution is flagged has_indeterminate if any summand 2^a_j is an
    indeterminate (loop) power of 2 mod M."""
    # distinct powers of 2 as residues with their exponent set
    res2 = {}
    seen = {}
    i = 0; r = 1 % M
    while r not in seen:
        seen[r] = i
        i += 1
        r = (r*2) % M
    loop_start = seen[r]
    # exponents that hit each residue
    exps_of = {}
    for i in range(loop_start + (i - loop_start)):  # tail + one full loop
        rr = pow(2, i, M)
        exps_of.setdefault(rr, []).append(i)
    # distinct residue values for powers of 2
    pow2_res = sorted(set(pow(2, i, M) for i in range(loop_start + (i-loop_start))))
    # residues that are powers of 3
    pow3_res = set()
    r = 1 % M
    for _ in range(10000):
        pow3_res.add(r)
        r = (r*3) % M
        if r == 1 % M:
            break
    solutions = []
    for a in pow2_res:
        for b in pow2_res:
            if b < a: continue
            for c in pow2_res:
                if c < b: continue
                s = (a + b + c) % M
                if s in pow3_res:
                    # exponents for each residue (min)
                    ea = min(exps_of[a]); eb = min(exps_of[b]); ec = min(exps_of[c])
                    # indeterminate iff exponent is on loop
                    indet = not (ea < loop_start and eb < loop_start and ec < loop_start)
                    solutions.append((s, ea, eb, ec, indet))
    return solutions, loop_start

for M in [5440, 2**7*5*17*257]:
    print("="*70)
    m = M
    fac = []
    p = 2
    while p*p <= m:
        e=0
        while m%p==0: m//=p; e+=1
        if e: fac.append(f"{p}^{e}")
        p += 1 if p==2 else 2
    if m>1: fac.append(f"{m}^1")
    print(f"M = {M} = {'*'.join(fac) if fac else '1'}")
    tail, looplen = pow2_tail_loop(M)
    print(f"  powers of 2: tail length {len(tail)}, loop length {looplen}")
    print(f"  determinate (tail) powers of 2: 2^{tail[0]}..2^{tail[-1] if tail else '?'}")
    per3, _ = pow3_cycle(M)
    print(f"  powers of 3: cycle length {per3}")
    sols, loop_start = enum_solutions(M)
    print(f"  {len(sols)} residue-class solutions to 3^x = 2^a+2^b+2^c mod M")
    for (s,ea,eb,ec,indet) in sorted(sols, key=lambda t:(t[1],t[2],t[3])):
        tag = "  [INVOLVES INDETERMINATE 2]" if indet else "  [all summands determinate]"
        print(f"    3^? == 2^{ea}+2^{eb}+2^{ec} mod M{tag}")
    any_ind = any(t[4] for t in sols)
    print(f"  -> M has a solution involving an indeterminate power of 2: {any_ind}")
    print()
