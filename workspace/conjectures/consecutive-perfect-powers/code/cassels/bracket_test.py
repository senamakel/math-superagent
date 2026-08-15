"""Focused test of the BRACKET descent for the Cassels lemma.

From the reduction: if p | x-1 fails (p | y fails), then x-1 = a^q and
Phi_p(x) = b^q with x = a^q + 1, i.e.

    b^q = Phi_p(a^q + 1) = sum_{j=0}^{p-1} C(p, j+1) a^{q j}.

KEY OBSERVATION (candidate descent): the leading term of Phi_p(a^q+1) is
a^{q(p-1)}, so b is near a^{p-1}.  If we can prove

    (a^{p-1})^q  <  Phi_p(a^q+1)  <  (a^{p-1} + 1)^q            (*)

then b^q lies strictly between two CONSECUTIVE q-th powers, which is a
contradiction (no integer b has b^q strictly between consecutive q-th powers).
That proves the lemma (hence p | y / p | x-1) WITHOUT any descent to a smaller
solution — a clean contradiction.

We TEST:
  (A) whether (*) holds for all a >= 2, over a broad odd-prime grid (exact).
  (B) for which order of (p,q) it holds (p<q vs p>q).  The leading-term
      comparison suggested (*) holds only when p < q; we verify exactly.
  (C) the mirror:  Phi_q(-(c^p - 1)) = Phi_q(1 - c^p) vs (c^{q-1})^p and
      (c^{q-1}+1)^p,  holding when q < p.

Exact integer arithmetic throughout.  a = 1 (x = 2) is the separately-handled
small case (REDUCTION.md) and is excluded here.

The falsifier: the known solution 3^2 - 2^3 = 1 has p = 2 even, so it sits
outside every odd-prime hypothesis; it is EXCLUDED, never refuted, by (*).
"""
from math import gcd
import sys
sys.setrecursionlimit(100000)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_in(a, b):
    return [p for p in range(a, b + 1) if is_prime(p)]


def phi_p_at_ap1(a, q, p):
    """Phi_p(a^q + 1)."""
    return ((a ** q + 1) ** p - 1) // (a ** q)


def main():
    ODD = primes_in(3, 60)   # 3..59
    print("ODD primes:", ODD)

    print("=" * 80)
    print("(A) BRACKET LEMMA: is  (a^(p-1))^q < Phi_p(a^q+1) < (a^(p-1)+1)^q"
          "  for a in [2,Amax]?")
    Amax = 2000
    fail_low = []
    fail_high = []
    by_order = {('<', 0): 0, ('>', 0): 0}  # count of checks by p vs q
    fail_by_order = {('<', 0): 0, ('>', 0): 0}
    for p in ODD:
        for q in ODD:
            if p == q:
                continue
            key = ('>', 0) if p > q else ('<', 0)
            for a in range(2, Amax + 1):
                by_order[key] += 1
                val = phi_p_at_ap1(a, q, p)          # b^q
                low = (a ** (p - 1)) ** q
                high = (a ** (p - 1) + 1) ** q
                if not (low < val):
                    fail_low.append((p, q, a))
                if not (val < high):
                    fail_high.append((p, q, a))
                    fail_by_order[key] += 1
    print(f"   (p<q) checks: {by_order[('<',0)]},  high-bracket failures: "
          f"{fail_by_order[('<',0)]}")
    print(f"   (p>q) checks: {by_order[('>',0)]},  high-bracket failures: "
          f"{fail_by_order[('>',0)]}")
    print(f"   low-bracket failures (val <= low): {len(fail_low)}")
    print(f"   high-bracket failures total: {len(fail_high)}; "
          f"first 10: {fail_high[:10]}")
    # how many distinct (p,q) pairs fail for p>q ?
    pairs_fail = sorted(set((p, q) for (p, q, a) in fail_high))
    print(f"   distinct (p,q) pairs failing the high bound (all a<=Amax): "
          f"{len(pairs_fail)}")
    print(f"   sample failing pairs: {pairs_fail[:30]}")
    print()

    print("=" * 80)
    print("(B) Smaller bound for p>q: does Phi lie between (a^(p-1))^q and a "
          "DIFFERENT consecutive q-th power?")
    # Try: find floor(b) = largest integer with floor^q <= val; see if it is
    # always < val and (floor+1)^q > val. i.e. always non-integer root.
    # Report min gap to next power for p>q.
    def floor_root(val, q):
        lo, hi = 0, 1
        while hi ** q <= val:
            hi *= 2
        while lo <= hi:
            mid = (lo + hi) // 2
            pw = mid ** q
            if pw == val:
                return mid, 0
            if pw < val:
                lo = mid + 1
            else:
                hi = mid - 1
        nxt = (hi + 1) ** q
        return hi, nxt - val
    print("   For p>q pairs, is Phi_p(a^q+1) ALWAYS a strict non-qth-power?")
    never = 0
    for p in ODD:
        for q in ODD:
            if p <= q:
                continue
            for a in range(2, Amax + 1):
                val = phi_p_at_ap1(a, q, p)
                fl, gap = floor_root(val, q)
                if fl ** q == val or gap == 0:
                    never += 1
                    print(f"      PERFECT: p={p} q={q} a={a}")
    print(f"   perfect q-th powers found (p>q, a in [2,{Amax}]): {never}")
    print()

    print("=" * 80)
    print("(C) MIRROR bracket:  Phi_q(1 - c^p) vs (c^(q-1))^p , (c^(q-1)+1)^p")
    # mirror: y+1 = c^p, Phi_q(-y) = d^p,  -y = 1 - c^p
    def phi_q_mirror(c, p, q):
        """Phi_q(-y) with y = c^p - 1  =>  Phi_q(1 - c^p).
           Phi_q(t) = (t^q - 1)/(t - 1);  t = 1 - c^p.  (t-1) = -c^p."""
        t = 1 - c ** p
        return (t ** q - 1) // (t - 1)
    m_fail = []
    for q in ODD:
        for p in ODD:
            if p == q:
                continue
            for c in range(2, 400 + 1):
                val = phi_q_mirror(c, p, q)
                # leading term magnitude: Phi_q(1-c^p) ~ (c^p)^(q-1) = c^{p(q-1)}
                low = (c ** (q - 1)) ** p
                high = (c ** (q - 1) + 1) ** p
                if not (low < val < high):
                    m_fail.append((q, p, c))
    print(f"   mirror checks c in [2,400]: failures of bracket = {len(m_fail)}")
    pfails = sorted(set((a, b) for (a, b, c) in m_fail))
    print(f"   distinct (q,p) pairs failing mirror bracket: {pfails[:30]}")
    print()

    print("=" * 80)
    print("(D) which ORDER does each bracket handle?")
    # x-side bracket (Phi_p(a^q+1), p first, q second) holds for p<q
    # mirror bracket (Phi_q(1-c^p), q first, p second) holds for q<p
    print("   x-side:  Phi_p(a^q+1) < (a^{p-1}+1)^q  holds iff p < q (A)")
    print("   mirror:  Phi_q(1-c^p) < (c^{q-1}+1)^p  holds iff q < p (C)")
    print("   => x-side gives p|y for p<q; mirror gives q|x for p>q")
    print()

    print("=" * 80)
    print("(E) FAILSAFE: every lemma evaluated against known solution")
    x, p, y, q = 3, 2, 2, 3
    print(f"   known solution 3^2 - 2^3 = 1: p={p}, q={q}")
    print(f"   is (p,q) both odd primes? {p>=3 and q>=3}  -> NO (p=2): every\n"
          f"      odd-prime lemma is EXCLUDED-by-hypothesis here, not refuted.")
    print(f"   concluded divisibilities at known solution: p|y -> {y%p==0}, "
          f"q|x -> {x%q==0}, p|x-1 -> {(x-1)%p==0}, q|y+1 -> {(y+1)%q==0}")


if __name__ == "__main__":
    main()
