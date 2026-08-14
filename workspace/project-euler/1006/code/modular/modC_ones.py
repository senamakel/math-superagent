"""Exact structure of the ones distribution in the k+1 Fibonacci factors.

From the balanced-factor theorem each factor w of length k has floor(k a) or
ceil(k a) ones (a=1/phi^2). So T(k) = sum over factors of #ones = (k+1) floor(ka)
+ r_k, where r_k = number of factors carrying the extra (ceil) count. We compute
r_k exactly from the data and look for its pattern; also inspect where the
column counts N(i;k) take the high value (a rotation structure check).

Exact integer arithmetic throughout (only the irrational a used for the
floor--ceil split; r_k itself is an exact integer count).
"""

import json
import os
from decimal import Decimal, getcontext, ROUND_FLOOR

getcontext().prec = 60
A = (Decimal(3) - Decimal(5).sqrt()) / Decimal(2)


def floor_dec(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def load(data):
    pos_counts = {}
    for k in range(1, 41):
        factors = data[str(k)]
        pc = [0] * k
        for s in factors:
            for i, ch in enumerate(s):
                if ch == "1":
                    pc[i] += 1
        pos_counts[k] = pc
    return pos_counts


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
    data = json.load(open(base))
    pc = load(data)

    out = []
    out.append("ONES DISTRIBUTION ANALYSIS\n")
    out.append("For each k: T(k)=sum_i N(i;k)=total ones over all (k+1) factors;\n"
               "floor(ka)=ones per 'light' factor; r_k = number of factors with ceil(ka) ones.")
    out.append(" k   : T(k)   : (k+1)*floor(ka) : r_k : T(k)/(k+1)*[a] : F-index")
    rows = []
    for k in range(1, 41):
        T = sum(pc[k])
        f = floor_dec(Decimal(k) * A)
        base_r = (k + 1) * f
        r = T - base_r
        # quick check each factor really has f or f+1 ones
        facs = data[str(k)]
        ones = [s.count("1") for s in facs]
        ok = all(o in (f, f + 1) for o in ones)
        rows.append((k, T, base_r, r, ok))
        out.append(f" {k:2d}   : {T:6d} : {base_r:6d} : {r:3d} : ok={ok}")
    out.append("")
    out.append("r_k table (excess count = # of 1-heavy factors):")
    rvals = [r for (k, T, b, r, ok) in rows]
    out.append("  " + " ".join(f"{r}" for r in rvals))
    # positions where r_k seems special (Fibonacci-adjacent)
    out.append("")
    out.append("r_k vs Fibonacci structure:")
    fibs = [1, 2, 3, 5, 8, 13, 21, 34]
    for k in range(1, 41):
        _, _, _, r, _ = rows[k - 1]
        tag = ""
        for F in fibs:
            if k == F:
                tag = f"k=F={F}"
        if tag:
            out.append(f"  k={k:2d} r_k={r}  ({tag})")
    out.append("")
    out.append("Check T(k) = sum_i N(i;k) equals sum over factors of #ones:",
               )
    # also report the high-value positions rotationally: count how many columns
    # take the high value, i.e. max-N(i) - min-N(i).
    out.append("")
    out.append("Per column: min/max and count of high columns:")
    for k in [6, 8, 11, 13, 16, 20]:
        vals = pc[k]
        lo, hi = min(vals), max(vals)
        nhigh = vals.count(hi)
        out.append(f"  k={k:2d}: min={lo} max={hi} #high={nhigh}/{k}")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_C_ones.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
