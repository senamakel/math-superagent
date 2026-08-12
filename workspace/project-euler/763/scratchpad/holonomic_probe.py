"""Rigorous holonomic/P-recursive extrapolation probe for PE763 D(N).

For each K in {11,12,13,14} and each (order m, degree d) in a small sweep,
fit a P-recursive recurrence sum_j p_j(N) D[N+j] = 0 on the first K points
via lib.holonomic.fit, and check whether ANY independent nullspace solution
reproduces ALL held-out points D(K..14) EXACTLY.

If a recurrence passes (reproduces every held-out point), extrapolate it to
predict D(20) and D(100) mod 1e9 and compare to the statement's falsifiers
(D(20)=9204559704, last-9 of D(100)=780166455).

Exact rational arithmetic throughout (sympy).  P-recursive recurrence uses
p_j(N)=sum_t a[j][t] N^t and solves for the highest-index term.
"""
import sys
import sympy
from lib.amoeba import D
from lib.holonomic import fit

SEQ = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
       514419, 1749267, 5949063]  # D(0..14)


def extend(vec, m, d, D0, n_targets):
    """Extend sequence known to len(D0) up to length n_targets using the
    recurrence.  Returns (full_list, err) or (None, err)."""
    D_ = list(D0)
    while len(D_) < n_targets:
        k = len(D_)
        i = k - m            # base index; recurrence ties D[i..i+m], i+m=k
        p_m = sum(vec[m * (d + 1) + t] * (i ** t) for t in range(d + 1))
        if p_m == 0:
            return None, f"p_m(N={i})=0: recurrence ill-posed"
        rhs = 0
        for j in range(m):
            p_j = sum(vec[j * (d + 1) + t] * (i ** t) for t in range(d + 1))
            rhs -= p_j * D_[i + j]
        term = sympy.Rational(rhs) / sympy.Rational(p_m)
        D_.append(term)
    return D_, None


def run():
    out = []
    log = out.append

    log("=== Step 1: canonical BFS oracle (lib.amoeba.D) ===")
    for n in (2, 10):
        v = D(n, d=3)
        log(f"D({n}) = {v}  (expected {3 if n==2 else 44499})")
    log("")

    log("=== Step 2: P-recursive fit sweep, held-out exactness ===")
    log("Known D(0..14): " + " ".join(map(str, SEQ)))
    log("")

    ks = [11, 12, 13, 14]
    sweep = [(m, d) for m in (1, 2, 3, 4, 5) for d in (1, 2, 3)]
    any_pass = []   # (K, m, d, vec) that reproduced all held-out points

    for K in ks:
        log(f"--- Fit on first K={K} points D(0..{K-1}); "
            f"held-out D({K}..14) ---")
        fit_D = SEQ[:K]
        for (m, d) in sweep:
            ncols = (m + 1) * (d + 1)
            rows = len(fit_D) - m
            if rows < 1:
                continue
            basis = fit(m, d, fit_D)
            if not basis:
                continue
            # find any basis vector reproducing all held-out points
            good = None
            tested = 0
            for vec in basis:
                ext, err = extend(vec, m, d, fit_D, len(SEQ))
                tested += 1
                if err:
                    continue
                held = SEQ[K:]
                pred = ext[K:]
                if all(a == b for a, b in zip(pred, held)):
                    good = vec
                    break
            if good is None:
                log(f"  (m={m},d={d}): #solutions={len(basis)}; "
                    f"NONE reproduces all held-out points")
            else:
                log(f"  (m={m},d={d}): #solutions={len(basis)}; "
                    f"solution #{tested} reproduces ALL held-out points "
                    f"D({K}..14) exactly")
                any_pass.append((K, m, d, good))
        log("")

    # ---- Step 3: extrapolate passing recurrences to D(20), D(100)----
    log("=== Step 3: extrapolate any recurrence passing held-out check ===")
    if any_pass:
        # dedupe by (m,d) keeping the largest K for the most data
        seen = {}
        for K, m, d, vec in any_pass:
            if (m, d) not in seen or K > seen[(m, d)][0]:
                seen[(m, d)] = (K, vec)
        for (m, d), (K, vec) in seen.items():
            # extend from full SEQ (use fitted data; refit not needed since
            # the recurrence is fully determined)
            ext20, e1 = extend(vec, m, d, SEQ, 21)
            ext100, e2 = extend(vec, m, d, SEQ, 101)
            d20 = ext20[20] if e1 is None else None
            d100 = ext100[100] if e2 is None else None
            mod100 = int(d100) % 10 ** 9 if d100 is not None else None
            log(f"K={K} (m={m},d={d}) [passed held-out check]:")
            log(f"   predicted D(20) = {d20}")
            log(f"      statement D(20)=9204559704, "
                f"match={d20 == 9204559704 if d20 is not None else None}")
            log(f"   predicted D(100) mod 1e9 = {mod100}")
            log(f"      statement last9=780166455, "
                f"match={mod100 == 780166455 if mod100 is not None else None}")
    else:
        log("No (m,d,K) produced a recurrence reproducing ALL held-out points;")
        log("nothing passes to extrapolation.")
    log("")

    log("=== VERDICT on extrapolation viability ===")
    if any_pass:
        log("WARNING: {len(any_pass)} candidate recurrences passed the held-out")
        log("check on D(13)/D(14); see D(20)/D(100) falsifier comparison above.")
    else:
        log("Extrapolation is NOT viable: no low-order P-recursive recurrence")
        log("fitted on the first K points (K=11..14) reproduces every held-out")
        log("point. The fitted recurrences are overfits (any finite window of")
        log("an arbitrary sequence admits a P-recursive interpolation of high")
        log("enough order), and they break immediately out of sample. They")
        log("cannot reach N=10000.")

    return "\n".join(out)


if __name__ == "__main__":
    text = run()
    sys.stdout.write(text + "\n")
    with open("/workspace/scratchpad/holonomic_probe.txt", "w") as f:
        f.write(text + "\n")
    print("[wrote /workspace/scratchpad/holonomic_probe.txt]")
