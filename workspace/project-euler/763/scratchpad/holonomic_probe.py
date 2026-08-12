"""Probe: confirm D(2)=3, D(10)=44499 via lib.amoeba.D, and test whether a
low-order P-recursive recurrence fit via lib.holonomic.fit predicts held-out
D points correctly.

Report, for each (order m, degree d) in a small sweep, whether a nullspace
solution exists, its polynomial coefficients, and whether the fitted
recurrence reproduces held-out points exactly (fit on first K points, predict
the rest; check D(13)=1749267 and D(14)=5949063).  If a recurrence fits, use
it to predict D(20) and D(100) mod 10^9 and compare to the statement's
falsifiers D(20)=9204559704, last9(D(100))=780166455.
"""
import sys
import sympy
from lib.amoeba import D
from lib.holonomic import fit, D_DEFAULT

SEQ = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
       514419, 1749267, 5949063]


def predict_from_recurrence(vec, m, d, D0, n_targets):
    """Given nullspace vector a[j][t] (order m, degree d) and initial D0,
    compute subsequent terms by solving the recurrence
        sum_j p_j(N) D[N+j] = 0,  p_j(N)=sum_t a[j][t] N^t
    for D[N+m] (highest index), requiring p_m != 0 at the needed N.
    Returns list of predicted terms after those already known, plus the
    extrapolated derived sequence (index-aligned list of full length).
    """
    D_ = list(D0)
    for N in range(0, len(D_) - m):
        # already known whenever N+m < len(D_)
        pass
    # We grow the sequence term by term: at each new index k = len(D_),
    # use the recurrence valid for base index i = k - m, with D[i..i+m] where
    # i+m = k (the new term has the highest index).  Then
    #   p_m(i) * D[k] = - sum_{j=0}^{m-1} p_j(i) * D[i+j]
    while len(D_) < n_targets:
        k = len(D_)
        i = k - m
        p_m = sum(vec[(m) * (d + 1) + t] * (i ** t) for t in range(d + 1))
        if p_m == 0:
            return None, f"p_m at N={i} is zero (recurrence ill-posed)"
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

    # ---- Step 1: BFS oracle confirmation ----
    log("=== Step 1: canonical BFS oracle (lib.amoeba.D) ===")
    for n in [2, 10]:
        v = D(n, d=3)
        log(f"D({n}) = {v}  (expected D(2)=3, D(10)=44499)")
        if n == 2:
            log(f"  -> match: {v == 3}")
        else:
            log(f"  -> match: {v == 44499}")
    log("")

    # ---- Step 2: holonomic fit sweep, predict held-out points ----
    log("=== Step 2: P-recursive fit sweep (fit on first K, predict rest) ===")
    known = SEQ  # D(0..14)
    # sweep orders/degrees that are not so large that the nullspace is trivial
    # (nullspace must have non-negative dimension given K points)
    ks = [11, 12, 13, 14]
    sweep = []
    for m in [1, 2, 3, 4, 5]:
        for d in [1, 2, 3]:
            sweep.append((m, d))

    log("Known D(0..14): " + " ".join(str(x) for x in known))
    log("")
    predictions_d20_d100 = []
    for K in ks:
        log(f"--- Fit on first K={K} points D(0..{K-1}), predict D(K..14), "
            f"check held-out D(13), D(14) ---")
        fit_D = known[:K]
        for (m, d) in sweep:
            # number of unknowns (m+1)(d+1); rows = K - m
            ncols = (m + 1) * (d + 1)
            rows = len(fit_D) - m
            if rows < 1:
                continue
            basis = fit(m, d, fit_D)
            if not basis:
                log(f"  (m={m},d={d}): no nullspace solution (rank full)")
                continue
            # try each independent solution that can be extended
            reproduced = []
            for vec in basis:
                ext, err = predict_from_recurrence(vec, m, d, fit_D,
                                                   len(known))
                if err:
                    continue
                ok13 = (ext[13] == SEQ[13]) if len(ext) > 13 else None
                ok14 = (ext[14] == SEQ[14]) if len(ext) > 14 else None
                reproduced.append((vec, ext, ok13, ok14))
            if not reproduced:
                log(f"  (m={m},d={d}): nullspace nonempty but none extendable")
                continue
            # report the first solution's coefficients and match status
            vec, ext, ok13, ok14 = reproduced[0]
            coeffs = ", ".join(str(sympy.simplify(c)) for c in vec)
            log(f"  (m={m},d={d}): #solutions={len(basis)}, first sol coeffs=[{coeffs}]")
            log(f"      predicts D(13)={ext[13] if len(ext)>13 else 'n/a'} "
                f"(match={ok13}), D(14)={ext[14] if len(ext)>14 else 'n/a'} "
                f"(match={ok14})")
            # if a solution reproduces both held-out points, remember it for
            # extrapolation
            if ok13 and ok14:
                predictions_d20_d100.append((K, m, d, vec))
        log("")

    # ---- Step 3: extrapolation of any fully-fitted recurrence ----
    log("=== Step 3: extrapolate any recurrence that reproduced D(13), D(14) ===")
    if predictions_d20_d100:
        for (K, m, d, vec) in predictions_d20_d100:
            D20, err = predict_from_recurrence(vec, m, d, SEQ, 21)
            D100plus, err2 = predict_from_recurrence(vec, m, d, SEQ, 101)
            d20 = D20[20] if D20 and len(D20) > 20 else "n/a"
            d100 = D100plus[100] if D100plus and len(D100plus) > 100 else "n/a"
            mod100 = None
            if d100 != "n/a":
                mod100 = int(d100) % (10 ** 9)
            log(f"K={K}, m={m}, d={d}:")
            log(f"   predicted D(20) = {d20}  (statement: 9204559704, "
                f"match={d20 == 9204559704 if d20!='n/a' else 'n/a'})")
            log(f"   predicted D(100) mod 1e9 = {mod100}  "
                f"(statement: 780166455, "
                f"match={mod100 == 780166455 if mod100 is not None else 'n/a'})")
    else:
        log("No fitted recurrence reproduced both held-out points D(13) and D(14);")
        log("no extrapolation attempted.")
    log("")
    log("=== VERDICT on extrapolation viability ===")
    log(verdict(predictions_d20_d100))
    return "\n".join(out)


def verdict(preds):
    if not preds:
        return ("Extrapolation is NOT viable: no low-order P-recursive "
                "recurrence fitted on the first K points reproduces both "
                "held-out points D(13) and D(14). P-recursive extrapolation "
                "does not reach D(10000).")
    return (f"NOTE: {len(preds)} fitted recurrences reproduced held-out "
            "points -- see their D(20)/D(100) predictions above.")


if __name__ == "__main__":
    text = run()
    sys.stdout.write(text + "\n")
    with open("/workspace/scratchpad/holonomic_probe.txt", "w") as f:
        f.write(text + "\n")
    print("\n[wrote /workspace/scratchpad/holonomic_probe.txt]")
