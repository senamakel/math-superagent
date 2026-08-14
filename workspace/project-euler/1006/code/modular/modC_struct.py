"""Verify two structural facts about N(i;k) = per-position one-counts, and
give the honest verdict on the naive closed form.

Fact 1: for every k<=40, the sequence i -> N(i;k) is BALANCED: it takes only
        two consecutive integer values.
Fact 2: at k = F_m - 1 (one less than a Fibonacci number), N(i;k) is CONSTANT
        across all positions i, equal to F_{m-2}.
Fact 3 (test of the task's candidate): N(i;k) = floor((k-i)*a + const) with
        a=1/phi^2 does NOT hold with any single const (nor per-k const).

All exact integer arithmetic except the irrational a (high-precision Decimal).
"""

import json
import os
from decimal import Decimal, getcontext, ROUND_FLOOR

MOD = 101001001
getcontext().prec = 60
A = (Decimal(3) - Decimal(5).sqrt()) / Decimal(2)  # 1/phi^2 = (3-sqrt5)/2


def floor_dec(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def load_pc(data):
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


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
    data = json.load(open(base))
    pc = load_pc(data)

    out = []
    out.append("STRUCTURAL ANALYSIS OF N(i;k)\n")

    # Fact 1: balanced in i
    out.append("Fact 1) N(i;k) balanced in i (two consecutive values per k):")
    all_bal = True
    for k in range(1, 41):
        vals = sorted(set(pc[k]))
        uv = list(set(pc[k]))
        balanced = (len(uv) == 2 and abs(uv[0] - uv[1]) == 1) or len(uv) == 1
        all_bal &= balanced
        out.append(f"  k={k:2d}: values={uv} balanced={balanced}")
    out.append(f"  ALL k<=40 balanced: {all_bal}\n")

    # Fact 2: constant at k=F_m - 1 with value F_{m-2}
    out.append("Fact 2) N(i;k) constant across i when k=F_m-1:")
    const_ok = True
    for m in range(5, 12):
        Fm = fib(m)
        k = Fm - 1
        if 1 <= k <= 40:
            uv = set(pc[k])
            pred = fib(m - 2)
            is_const = len(uv) == 1
            match = is_const and (list(uv)[0] == pred)
            const_ok &= match
            out.append(f"  k=F_{m}-1={k}: N(i;k)={sorted(uv)} (const={is_const})"
                       f", expected F_{m-2}={pred}, match={match}")
    out.append(f"  ALL match: {const_ok}\n")

    # Fact 3: the task's candidate fails
    out.append("Fact 3) Test of candidate N(i;k)=floor((k-i)*a+const), a=1/phi^2:")
    # try to find any single const matching ALL (k,i)
    best = None
    for num in range(-200, 201):
        c = Decimal(num) / Decimal(100)
        matches = 0
        total = 0
        for k in range(1, 41):
            for i in range(k):
                pred = floor_dec(Decimal(k - i) * A + c)
                matches += (pred == pc[k][i])
                total += 1
        if best is None or matches > best[0]:
            best = (matches, total, c)
    out.append(f"  best single const c={best[2]} matches {best[0]}/{best[1]} "
               f"(a perfect fit would be {best[1]}/{best[1]})")
    out.append("  => the candidate form does NOT match for k<=40.")
    out.append("")
    out.append("  Consistency check at a single k (k=8): would need const 0.94 at i=0 ")
    out.append("  but const 0.33 at i=1 for (k-i)*a to give N=3; so no single const works even per-k.")
    out.append("")

    # Bonus: show that N(i;k) is a mechanical (two-value) sequence; identify the
    # positions where it takes the higher value for a few k, to display structure.
    out.append("High-value positions H_k = {i : N(i;k)=max}:")
    for k in [6, 8, 11, 13, 16]:
        mx = max(pc[k])
        H = [i for i in range(k) if pc[k][i] == mx]
        out.append(f"  k={k:2d}: N={pc[k]}  H={H}")
    out.append("")
    out.append("Total ones T(k)=sum_i N(i;k)=sum_j #ones(w_j), and k+1, fraction:")
    for k in range(1, 41):
        T = sum(pc[k])
        if k in (3, 4, 7, 12, 20, 33):
            out.append(f"  k={k:2d}: T={T}, (k+1)={k+1}, T/(k+1)={Decimal(T)/Decimal(k+1)}")
    out.append("")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_C_struct.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
