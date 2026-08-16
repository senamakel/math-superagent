"""Verify the two worked n=3 examples in Dimitrov & Howe, "Powers of 3 with few
nonzero bits and a conjecture of Erdős" (arXiv:2105.06440, Rocky Mountain J.
Math 2021).

Equation under study (Introduction): (1) 3^x = 2^{a1}+2^{a2}+2^{a3}  in Z/MZ,
with n=3 distinct-summand restriction set aside (the modulus enumeration ignores
distinctness, exactly as DH do for the illustration).

Operational definitions (read from the held full text):
  - A power 2^i is DETERMINATE mod M iff the only b>=0 with 2^b == 2^i (mod M)
    is b=i. Equivalently the residue 2^i lies on the TAIL of the powers-of-2
    cycle-and-tail diagram. (DH Definition 2.2, lines 294-306; the tail length
    is v2(M), DH lines 327-329.)
  - A residue-class solution is called extraneous/indeterminate here if at least
    one summand power 2^{a_j} is an indeterminate (loop) power of 2. DH Section 3
    associates "extraneous solutions: not a reduction of a solution in the
    integers" with solutions involving indeterminate powers of 2 or 3.

Paper's two examples:
   M1 = 5440 = 2^6 * 5 * 17            -> three residue-class solutions, and the
        one that matters ((6): 3^4 = 2^0+2^4+2^6) involves an INDETERMINATE 2^6
        (since the loop starts at exponent 6). So M1 has extraneous solutions.
   M2 = 2^7 * 5 * 17 * 257             -> the ONLY residue-class solution is
        3^4 = 2^0+2^4+2^6, and 2^0,2^4,2^6 are all DETERMINATE (tail length 7, so
        exponents 0..6 are on the tail). So M2 is CLEAN (no extraneous solutions).
        The 257 prime contributes ord_257(3) = 256, a multiple of 2^5, defeating
        Lemma 3.1's condition for forcing an extraneous sibling.
"""
import itertools
from collections import Counter

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def power_graph(M, base):
    """Return (tail_length, loop_length) of the diagram of powers of `base`
    modulo M: 1, base, base^2, ... stabilises once exponent >= v_p(M) where p is
    the prime dividing base (here base=2, p=2); the part before stabilisation is
    the tail, the periodic part the loop."""
    seen = {}
    i = 0; r = 1 % M
    while r not in seen:
        seen[r] = i
        i += 1
        r = (r * base) % M
    loop_start = seen[r]
    return loop_start, i - loop_start

def is_determinate_2exp(M, i):
    """2^i determinate mod M iff i < v2(M) (on the tail)."""
    tail, _ = power_graph(M, 2)
    return i < tail

def distinct_2_residues(M):
    """Distinct residue values reached by 2^i mod M, plus their min exponents
    and whether each exponent is on the tail."""
    tail, loop = power_graph(M, 2)
    exp = {}
    r = 1 % M
    for i in range(tail + loop):
        rr = pow(2, i, M)
        exp.setdefault(rr, i)
    return exp  # residue -> min exponent

def enum_solutions(M):
    """All residue-class solutions 3^x == 2^a+2^b+2^c (mod M), 0<=a<=b<=c,
    returning (x_lowest, a, b, c, any_summand_indeterminate)."""
    exp2 = distinct_2_residues(M)
    res2 = sorted(exp2)
    # powers of 3 residues
    tail3, loop3 = power_graph(M, 3)
    pow3 = set(pow(3, i, M) for i in range(tail3 + loop3))
    tail2len, _ = power_graph(M, 2)
    sols = []
    for a in res2:
        for b in res2:
            if b < a: continue
            for c in res2:
                if c < b: continue
                if (a + b + c) % M in pow3:
                    ea, eb, ec = exp2[a], exp2[b], exp2[c]
                    indet = (ea >= tail2len) or (eb >= tail2len) or (ec >= tail2len)
                    sols.append((ea, eb, ec, indet))
    return sols, tail2len

def ord_mod(base, n):
    if n == 1: return 1
    k = 1; r = base % n
    while r != 1:
        r = (r * base) % n
        k += 1
        if k > 10**7:
            raise RuntimeError("no order found")
    return k

def odd_coprime6(M):
    while M % 2 == 0: M //= 2
    while M % 3 == 0: M //= 3
    return M

for M in [5440, 2**7*5*17*257]:
    print("="*72)
    print(f"M = {M}")
    # factor
    m = M; fac = {}; p = 2
    while p*p <= m:
        e = 0
        while m % p == 0: m //= p; e += 1
        if e: fac[p] = e
        p += 1 if p == 2 else 2
    if m > 1: fac[m] = fac.get(m, 0) + 1
    print("  factorization:", " * ".join(f"{p}^{e}" for p,e in sorted(fac.items())))
    tail2, loop2 = power_graph(M, 2)
    tail3, loop3 = power_graph(M, 3)
    print(f"  powers of 2: tail={tail2}  loop={loop2}   (total distinct = {tail2+loop2})")
    print(f"  powers of 3: tail={tail3}  loop={loop3}   (total distinct = {tail3+loop3})")
    sols, tail2len = enum_solutions(M)
    print(f"  residue-class solutions to 3^x = 2^a+2^b+2^c mod M: {len(sols)}")
    for (ea, eb, ec, indet) in sorted(sols, key=lambda t: (t[0],t[1],t[2])):
        tag = "  [indeterminate summand present -- extraneous-type]" if indet else "  [all determinate]"
        print(f"     3^? == 2^{ea}+2^{eb}+2^{ec} mod M{tag}")
    any_ext = any(t[3] for t in sols)
    print(f"  -> M has an extraneous-type solution: {any_ext}")
    # exact n=3 solution check
    sol3 = 3**4; rsum = 2**0+2**4+2**6
    print(f"  exact check 3^4 = {sol3} ; 2^0+2^4+2^6 = {rsum} ; equal in Z: {sol3==rsum}; "
          f"3^4 mod M == sum mod M: {sol3 % M == rsum % M}")
    print()

# Lemma 3.1 hypothesis check: O'_2 and O'_3 (Notation 2.3) for both moduli
print("="*72)
print("Notation 2.3 cross-orders: O'2(M)=ord of 2 mod M', O'3(M)=ord of 3 mod M', M'=M/(2^u 3^v)")
for M in [5440, 2**7*5*17*257]:
    Mp = odd_coprime6(M)
    o2 = ord_mod(2, Mp)
    o3 = ord_mod(3, Mp)
    print(f"  M={M}: M'={Mp}  O'2={o2} (div by 3^4=81? {o2 % 81 == 0})  "
          f"O'3={o3} (div by 2^5=32? {o3 % 32 == 0})")
print("\nExpectation: for M1 both cross-orders are modest (extraneous solutions present);")
print("for M2, O'3 = ord of 3 mod 5*17*257 is a multiple of 2^5 (via ord_257(3)=256),")
print("so the Lemma-3.1 extraneous-forcing condition fails -> M2 clean.")
