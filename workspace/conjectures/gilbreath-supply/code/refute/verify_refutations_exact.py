#!/usr/bin/env python3
"""Definitive exact check of the two refutations in
code/out/refuter_live_structural_claims.md.  Literal fold cell, no reliance on
any library reduction.  Prints the verdict for each claimed identity."""

def t(n, d, h):
    """T(n,d) = XOR_{o subseteq d} h[n-1-d+o], literal definition."""
    x = 0
    for o in range(d + 1):
        if (o & d) == o:
            x ^= h[n - 1 - d + o]
    return x

print("=== Refutation A: abel boundary recurrence  T(n,d)==T(n-1,d)^T(n-1,d-1) ===")
h = (0, 0, 0, 1)
n, d = 4, 2
lhs = t(n, d, h)
rhs = t(n-1, d, h[:n-1]) ^ t(n-1, d-1, h[:n-1])
print(f"  h={h} n={n} d={d}: T(4,2)={lhs}  T(3,2)={t(3,2,h[:3])}  T(3,1)={t(3,1,h[:3])}")
print(f"  LHS={lhs} RHS={rhs}  -> CLAIM {'HOLDS' if lhs==rhs else 'REFUTED'}")
# general: scan small n,d for any more violations and its exact residual formula
print("  scanning n=3..8, all h: violations?")
viol = 0
for nn in range(3, 9):
    for dd in range(2, nn):
        for mask in range(1 << nn):
            hh = [(mask >> i) & 1 for i in range(nn)]
            if dd <= nn-2:
                if t(nn, dd, hh) != t(nn-1, dd, hh[:nn-1]) ^ t(nn-1, dd-1, hh[:nn-1]):
                    viol += 1
print(f"  total violations over n=3..8, all h: {viol}  (nonzero -> relation false)")

print()
print("=== Refutation B: substitution rules ===")
# rule (i) T(2n,2d)=T(n,d)
h = (0, 0, 0, 1); n, d = 2, 1
a = t(2*n, 2*d, h); b = t(n, d, h)
print(f"  (i) T(2n,2d)=T(n,d): h={h} n=2 d=1: T(4,2)={a} T(2,1)={b} -> {'HOLDS' if a==b else 'REFUTED'}")
# rule (ii) T(2n,2d+1)=0
h = (1, 0, 0); n, d = 1, 0
a = t(2*n, 2*d+1, h)
print(f"  (ii) T(2n,2d+1)=0: h={h} n=1 d=0: T(2,1)={a} -> {'HOLDS' if a==0 else 'REFUTED'}")

print()
print("=== brute: over how many (h,n,d) do the substitution rules fail? ===")
for rule, fn in [
    ("T(2n,2d)==T(n,d)", lambda nn, dd, hh: t(2*nn, 2*dd, hh) == t(nn, dd, hh)),
    ("T(2n+1,2d)==T(n,d)", lambda nn, dd, hh: t(2*nn+1, 2*dd, hh) == t(nn, dd, hh)),
    ("T(2n+1,2d+1)==T(n,d)", lambda nn, dd, hh: t(2*nn+1, 2*dd+1, hh) == t(nn, dd, hh)),
]:
    total = ok = 0
    for nn in range(2, 5):
        # h length 2n+2
        L = 2*nn + 2
        for dd in range(1, nn):
            for mask in range(1 << L):
                hh = [(mask >> i) & 1 for i in range(L)]
                total += 1
                if fn(nn, dd, hh):
                    ok += 1
    print(f"  {rule}: {ok}/{total} hold -> {'REFUTED' if ok < total else 'holds exhaustively'}")
