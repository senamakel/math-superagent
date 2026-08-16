# Generator: produce a complete, correct TPTP encoding of the n=8 fold
# (cells T(8,d), d=2..7, over h0..h7) as parity DNF minterms, and generate the
# two conjectures we check. Matches lib.supply_fold's definition:
#   T(n,d) = XOR over submasks o of d of h[n-1-d+o].
def cells(n=8):
    out = {}
    for d in range(2, n):
        idx = [n-1-d+o for o in range(d+1) if (o & d) == o]
        out[d] = idx
    return out

print("library cell definitions:")
for d, idx in cells().items():
    print(f"  T(8,{d}) = XOR of h{idx}")

# Parity minterms: for a set of k variables that must be summed to 1 mod 2,
# the DNF is the union of all minterms with odd parity.
def parity_dnf(vars_, want=1):
    k = len(vars_)
    md = []
    for mask in range(1 << k):
        if bin(mask).count('1') % 2 == want:
            lit = []
            for i, v in enumerate(vars_):
                lit.append(v if (mask >> i) & 1 else f"~{v}")
            md.append("(" + " & ".join(lit) + ")")
    return " | ".join(md)

def dnf_clause(name, vars_, tp):
    body = parity_dnf(vars_)
    return f"fof(def_{name}, axiom, ( {name} <=> ( {body} ) ))."

# generate clauses for each cell
print("\nTPTP clauses:")
for d, idx in cells().items():
    print(dnf_clause(f"t{d}", [f"h{j}" for j in idx], 1))

# weight-2 constraint: exactly two of h0..h7 are 1.
# exactly-2 among 8: for each pair, that pair is 1 and all others 0.
pairs = []
for a in range(8):
    for b in range(a+1, 8):
        lits = [f"h{a}", f"h{b}"] + [f"~h{j}" for j in range(8) if j != a and j != b]
        pairs.append("(" + " & ".join(lits) + ")")
wt2 = " | ".join(pairs)
print(f"\nfof(wt2, axiom, ( wt2 <=> ( {wt2} ) )).")

# nu2 >= 4: wt = sum of t-cells >= 4, i.e. at least 4 of t2..t7.
# at-least-4-of-6: 4-of-6, 5-of-6, 6-of-6.
from itertools import combinations
ts = [f"t{d}" for d in range(2, 8)]
choices = []
for r in range(4, 7):
    for comb in combinations(ts, r):
        choices.append("(" + " & ".join(comb) + ")")
ge4 = " | ".join(choices)
print(f"\nfof(ge4, axiom, ( ge4 <=> ( {ge4} ) )).")

print("\nConjecture (to refute): no weight-2 h has nu2>=4.")
print("fof(goal, conjecture, ( ~( wt2 & ge4 ) )).")
