"""Test whether the PE1006 state vector evolves under a constant-coefficient
linear recurrence mod M = 101001001 (prime).

State u(k) is a vector over F_M. For order d we ask whether a fixed matrix C
(m x m*d) exists with

    u(k) = C * [u(k-1); u(k-2); ... ; u(k-d)]      (mod M)

for ALL k in a window k = d+1 .. K. This is deciding, over the field F_M,
whether the output component is in the column space of the stacked-past
feature matrix -- a consistency check solved by modular Gaussian elimination.
No floats; everything is exact integer arithmetic mod the prime M.

Also tested:
  - individual components (P1, vR) against their own past d values,
  - an affine variant u(k) = C*[past states] + c (extra constant feature).
"""
import os

MOD = 101001001

# ---- modular linear algebra over F_p -------------------------------------
def mat_inv_mod(a, p):
    return pow(a, p - 2, p)

def gauss_consistent(A, b, p):
    """Decide if A x = b (mod p) is consistent and return one solution.

    A: list of rows, each length ncols. b: length nrows target.
    Returns (consistent: bool, solution: list|None) over F_p.
    Uses Gaussian elimination on the augmented matrix with partial pivoting.
    """
    nrows = len(A)
    ncols = len(A[0]) if nrows else 0
    # build augmented [A | b]
    aug = [A[i][:] + [b[i] % p] for i in range(nrows)]
    r = 0
    col = 0
    pivots = []
    while r < nrows and col < ncols:
        # find pivot
        piv = None
        for i in range(r, nrows):
            if aug[i][col] % p != 0:
                piv = i
                break
        if piv is None:
            col += 1
            continue
        aug[r], aug[piv] = aug[piv], aug[r]
        inv = mat_inv_mod(aug[r][col] % p, p)
        aug[r] = [(x * inv) % p for x in aug[r]]
        for i in range(nrows):
            if i != r and aug[i][col] % p != 0:
                f = aug[i][col] % p
                aug[i] = [(aug[i][c] - f * aug[r][c]) % p for c in range(ncols + 1)]
        pivots.append(col)
        r += 1
        col += 1
    # consistency: any row with all-zero coefficients must have zero RHS
    for i in range(r, nrows):
        if all(aug[i][c] % p == 0 for c in range(ncols)) and aug[i][ncols] % p != 0:
            return (False, None)
    # one solution: x[col]=aug value for pivot columns, 0 for free
    sol = [0] * ncols
    for rr, cc in enumerate(pivots):
        sol[cc] = aug[rr][ncols] % p
    return (True, sol)

# ---- state data -----------------------------------------------------------
def read_states(path):
    """Return list of state dicts in order k=1..K.

    Columns: k,P_mod,S_mod,N1,N0,P1_mod,vR_mod. Values already mod M.
    """
    states = []
    with open(path) as f:
        f.readline()  # header
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = line.split(',')
            states.append({
                "k": int(p[0]),
                "P": int(p[1]) % MOD,
                "S": int(p[2]) % MOD,
                "N1": int(p[3]) % MOD,
                "N0": int(p[4]) % MOD,
                "P1": int(p[5]) % MOD,
                "vR": int(p[6]) % MOD,
            })
    return states

def vector_of(states, cols):
    """Return list of u(k) vectors (length len(cols)) over F_M, in k order."""
    return [[s[c] for c in cols] for s in states]

# ---- the test --------------------------------------------------------------
def build_system(uvecs, d, affine=False):
    """For each k with uvecs[k] defined and k>=d, one feature row (stacked past
    d states, optionally +constant) and one target row uvecs[k].

    Fits using ALL k from d .. K (K = len(uvecs)-1, 0-indexed), i.e. the full
    window past the first d states.
    """
    m = len(uvecs[0])
    K = len(uvecs) - 1  # last index (0-based), states 0..K = k=1..K+1
    rows = []
    targets = []
    for k in range(d, K + 1):
        feat = []
        for j in range(1, d + 1):
            feat.extend(uvecs[k - j])
        if affine:
            feat.append(1)
        rows.append(feat)
        targets.append(uvecs[k])
    return rows, targets

def test_configuration(states, cols, orders, affine=False,
                       k0_offset=0, K=-1):
    """Return results dict for each order."""
    uvecs = vector_of(states, cols)
    m = len(cols)
    if K == -1:
        K = len(uvecs) - 1
    results = {}
    for d in orders:
        # rows for all k in [d+k0_offset, K]
        rows, targets = [], []
        for k in range(d + k0_offset, K + 1):
            feat = []
            for j in range(1, d + 1):
                feat.extend(uvecs[k - j])
            if affine:
                feat.append(1)
            rows.append(feat)
            targets.append(uvecs[k])
        # solve per output column; consistent iff every column solvable
        nfeat = m * d + (1 if affine else 0)
        all_ok = True
        solution = []
        for j in range(m):
            A = [r[:] for r in rows]
            b = [t[j] for t in targets]
            ok, sol = gauss_consistent(A, b, MOD)
            if not ok:
                all_ok = False
                break
            solution.append(sol)
        results[d] = {"cols": list(cols), "affine": affine,
                      "consistent": all_ok,
                      "n_rows": len(rows), "nfeat": nfeat}
        if all_ok:
            results[d]["solution"] = solution
    return results

def verify_solution(states, cols, d, solution, affine, k0_offset=0):
    """Check found coefficients reproduce every state on the WHOLE window."""
    uvecs = vector_of(states, cols)
    m = len(cols)
    K = len(uvecs) - 1
    first_bad = None
    nb = 0
    for k in range(d + k0_offset, K + 1):
        feat = []
        for j in range(1, d + 1):
            feat.extend(uvecs[k - j])
        if affine:
            feat.append(1)
        for j in range(m):
            pred = 0
            for c, cf in zip(feat, solution[j]):
                pred = (pred + c * cf) % MOD
            if pred != uvecs[k][j]:
                nb += 1
                if first_bad is None:
                    first_bad = (k, j, pred, uvecs[k][j])
    return nb, first_bad

def main():
    here = os.path.dirname(__file__)
    state_path = os.path.join(here, "..", "out", "psi_state_1_200.txt")
    states = read_states(state_path)
    print(f"loaded {len(states)} states (k=1..{len(states)}), M={MOD}")

    COL_PSS = ["P", "S", "N1", "P1", "vR"]         # task's 5-dim state
    COL_ALL = ["P", "S", "N1", "N0", "P1", "vR"]   # with extra combinatoric N0

    orders = list(range(1, 7))

    def report(tag, cols, affine, k0_offset, verify=True):
        print(f"\n=== {tag}  (affine={affine}, skip first {k0_offset}) ===")
        res = test_configuration(states, cols, orders, affine=affine,
                                 k0_offset=k0_offset)
        for d in orders:
            r = res[d]
            if r["consistent"]:
                nb, bad = verify_solution(states, cols, d, r["solution"],
                                          affine, k0_offset)
                msg = (f"order {d}: CONSISTENT on fitted window; "
                       f"verify-errors on whole window = {nb}")
                if bad is not None:
                    msg += f" first_bad k={bad[0]+1} comp={bad[1]}"
                print(msg)
            else:
                print(f"order {d}: INCONSISTENT (no fixed C fits fitted window)")
        return res

    # main 5-dim, linear, no skip
    report("5-dim state [P,S,N1,P1,vR]", COL_PSS, False, 0)
    # 5-dim affine
    report("5-dim affine", COL_PSS, True, 0)
    # 6-dim with N0
    report("6-dim state [P,S,N1,N0,P1,vR]", COL_ALL, False, 0)
    # 6-dim affine
    report("6-dim affine", COL_ALL, True, 0)

    # individual components: P1 and vR
    for comp in ["P1", "vR", "N1", "P"]:
        print(f"\n=== single component {comp} (linear, order fits own past) ===")
        res = test_configuration(states, [comp], orders, affine=False, k0_offset=0)
        for d in orders:
            r = res[d]
            if r["consistent"]:
                nb, bad = verify_solution(states, [comp], d, r["solution"], False)
                print(f"order {d}: CONSISTENT; verify-errors={nb}")
            else:
                print(f"order {d}: INCONSISTENT")

    # eventual: skip first 30 states (allow early-part anomalies)
    report("5-dim, skip first 30", COL_PSS, False, 30)
    report("5-dim affine, skip first 30", COL_PSS, True, 30)

if __name__ == "__main__":
    main()
