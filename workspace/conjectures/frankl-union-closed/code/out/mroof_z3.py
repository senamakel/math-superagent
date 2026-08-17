"""Exact M♮-concavity certificate feasibility checker, over the reals via Z3.

is_feasible_mroof(F_masks, n, x) -> bool
  Does there exist w : 2^[n] -> R with
    (i)  w(A) = 0 for every A not in F_masks,
    (ii) w(A) >= 0 for all A and sum_{A in F_masks} w(A) = 1,
    (iii) abundance at x: sum_{A in F_masks, x in A} w(A) >= 1/2,
    (iv) w is M♮-concave on the Boolean lattice 2^[n] (gross-substitutes
         exchange): for every X, Y subseteq [n] and u in X\\Y, at least one
         branch holds -- either (B1) w(X)+w(Y) <= w(X-u)+w(Y+u), or (B2) there
         exists v in Y\\X with w(X)+w(Y) <= w(X-u+v)+w(Y+u-v).

The M♮-condition is a conjunction over every (X, Y, u) triple of a disjunction
of linear inequalities in the w-values, so it is a finite union of (closed)
polyhedra and Z3 decides satisfiability exactly over QF_LRA / QF_NRA (the
inequalities are linear; QF_LRA).

A family F is a set of integer bitmasks over [n]: element i (0-indexed) is in
mask s iff bit i of s is 1. All arithmetic is exact: constants enter as
z3 Real(Q(1,2)) rationals, never floats.

THE SUPPORT-RESTRICTION GAP (why case (a) below is subtle):
The *whole-lattice* constant w == 1/|F| is M♮-concave trivially (branch B1 is
equality). But constraint (i) replaces it by the support-restricted function
w(A) = 1/|F| for A in F and w(A) = 0 otherwise, and THAT function is NOT
generally M♮-concave. Concrete counterexample: n=2, F = {empty, {x,y}} (the
two masks 00 and 11). Restricted constant is 1/2 on {00,11}, 0 on {01,10}.
At (X={x,y}, Y=empty, u=x): B1 reads 1/2+1/2 <= 0+0, false; Y\\X is empty so
there is no v for branch B2; no branch holds. Hence the restricted constant
fails M♮-concavity, and the constant-weight proof does NOT by itself certify
case (a). Whether a genuinely-abundant element is still feasible follows from
the existence of SOME M♮-concave w, which is what is_feasible_mroof computes.
"""
from z3 import Real, And, Or, Solver, sat, unsat, Q


def _masks(n):
    return list(range(1 << n))


def _wvars(n):
    return {a: Real("w_%d" % a) for a in _masks(n)}


def _inb(mask, i):
    return (mask >> i) & 1


def is_feasible_mroof(F_masks, n, x):
    """Return True iff an exact-real M♮-concave w satisfying (i)-(iv) exists."""
    F = set(F_masks)
    w = _wvars(n)
    cons = []

    # (i) supported on F: w(A) == 0 for A not in F
    for a in _masks(n):
        if a not in F:
            cons.append(w[a] == 0)

    # (ii) nonnegativity and total mass 1
    for a in _masks(n):
        cons.append(w[a] >= 0)
    cons.append(sum(w[a] for a in F) == 1)

    # (iii) abundance at x
    cons.append(sum(w[a] for a in F if _inb(a, x)) >= Q(1, 2))

    # (iv) M♮-concavity: for every X, Y, u in X\Y, at least one branch holds.
    mroof_conds = []
    for X in _masks(n):
        for Y in _masks(n):
            for u in range(n):
                if not _inb(X, u) or _inb(Y, u):
                    continue
                branches = []
                # B1
                branches.append(w[X] + w[Y] <= w[X & ~(1 << u)] + w[Y | (1 << u)])
                # B2
                for v in range(n):
                    if _inb(Y, v) and not _inb(X, v):
                        newX = (X & ~(1 << u)) | (1 << v)
                        newY = (Y | (1 << u)) & ~(1 << v)
                        branches.append(w[X] + w[Y] <= w[newX] + w[newY])
                mroof_conds.append(Or(*branches))
    cons.append(And(*mroof_conds))

    s = Solver()
    s.add(*cons)
    r = s.check()
    if r == sat:
        return True
    if r == unsat:
        return False
    raise RuntimeError("Z3 returned unknown (nonlinear real arithmetic); "
                       "expected QF_LRA with linear inequalities only.")


# ----------------------------------------------------------------------------
# Constant weight is M♮-concave (whole lattice) -- the fact case (a) invokes.
# ----------------------------------------------------------------------------
def prove_constant_mroof_note():
    """Prove: the constant set-function w ≡ c on all of 2^[n] is M♮-concave.

    Take any X, Y and u in X\\Y. Branch B1 reads
        w(X) + w(Y) <= w(X-u) + w(Y+u)   i.e.   2c <= 2c,
    which is equality. Since B1 alone always holds, the disjunction is
    satisfied and w is M♮-concave for every n. This uses no support
    restriction (all four sets are evaluated, which they are: w is defined
    on all of 2^[n] regardless of F).
    """
    return ("Proof: for constant w == c, branch B1 is 2c <= 2c (equality) for "
            "every X, Y, u in X\\Y, so the M♮-disjunction is always satisfied. "
            "Note this is the WHOLE-LATTICE constant; the support-restricted "
            "constant (zero outside F) is not generally M♮-concave, see the "
            "module docstring counterexample.")


def _density(F, n, x):
    """Exact decimal density of element x in F (pure Python, no z3)."""
    cnt = sum(1 for a in F if _inb(a, x))
    return cnt, len(F)


def main():
    from lib.uc import decide_union_closed, abundant_elements

    print("=" * 78)
    print("M♮-concavity certificate feasibility via Z3 (QF_LRA, exact reals)")
    print("=" * 78)
    print("Encoding of (i)-(iv):")
    print("  (i)   w[A] == 0 for every mask A not in F       [support]")
    print("  (ii)  w[A] >= 0 all A;  sum_{A in F} w[A] == 1  [prob mass]")
    print("  (iii) sum_{A in F, A contains x} w[A] >= 1/2    [abundance@x]")
    print("  (iv)  M♮: for each X,Y,u in X\\Y:  Or(B1, B2_1..B2_k)")
    print("        B1    : wX+wY <= w[X-u]+w[Y+u]")
    print("        B2_v  : wX+wY <= w[X-u+v]+w[Y+u-v]  (v in Y\\X)")
    print("Logic: QF_LRA (all inequalities linear in Real vars). Z3 "
          + __import__("z3").get_version_string())
    print()

    print(prove_constant_mroof_note())
    print()

    # ---- Case (b): n=1, F = {empty, {x}} --------------------------------
    print("-" * 78)
    print("Case (b): n=1, F = {empty, {x}}")
    n = 1
    F = {0, 1}
    cnt, m = _density(F, n, 0)
    print("  density of x: %d/%d (abundant, >= 1/2)" % (cnt, m))
    r = is_feasible_mroof(F, n, 0)
    print("  is_feasible_mroof(F, x) = %s  (expected True)" % r)
    assert r is True, "n=1 F={empty,{x}} must be feasible for x"
    # Control: element not present in any set -> abundance sum is 0 < 1/2.
    print("  CONTROL: n=2, F={empty,{y}}, ask about x (present in no set):")
    F2 = {0, 2}  # masks over [2]: 0=empty, 2={y} (bit1)
    rc = is_feasible_mroof(F2, 2, 0)
    print("    is_feasible_mroof = %s  (expected False: x in no set)" % rc)
    assert rc is False

    # ---- Case (a): a genuinely union-closed family, abundant element -----
    print("-" * 78)
    print("Case (a): truly-abundant element of a UC family must be feasible")
    # UC family: F = {empty, {x}, {x,y}} over [2]; x abundant (2/3), y not (1/3).
    n = 2
    F = {0, 1, 3}  # 0=empty, 1={x}, 3={x,y}
    print("  family masks {0,1,3} = {empty, {x}, {x,y}}; UC = %s"
          % decide_union_closed(F))
    for x in range(n):
        cnt, m = _density(F, n, x)
        ab = (2 * cnt >= m)
        r = is_feasible_mroof(F, n, x)
        print("  element %s: density %d/%d, truly-abundant=%s, feasible=%s"
              % (x, cnt, m, ab, r))
    print("  -> check: truly-abundant x=0 must be feasible.")
    assert is_feasible_mroof(F, n, 0) is True

    # Case (a) at a larger UC family (near-cube n=3) for a sanity sweep.
    print("  SANITY SWEEP over UC families n=3 (abundant-elements all feasible?):")
    from itertools import combinations
    # enumerate a handful of UC families by taking closures of small generators
    def fam_from_gens(gens, n):
        return __import__("lib.uc", fromlist=["closure"]).closure(gens)
    all_sets = list(range(1 << 3))
    checked = 0
    mismatches = []
    # generators: pick 3 elements present -> try the near-cube and a few
    # specific families, plus several random-closure families.
    import random
    random.seed(7)
    fams = []
    for trial in range(40):
        k = random.randint(2, 4)
        gens = random.sample(all_sets[1:], k)  # include at least one non-empty
        Ff = fam_from_gens(gens, 3)
        if not Ff:
            continue
        fams.append(Ff)
    fams.append(set(all_sets))          # full power set (UC)
    # near-n-cube n=3: all sets of size >= 2 plus {0,1} (mask 3)
    fams.append(set(range(1 << 3)) - {1, 2, 4} | {3})  # heavy-ish UC? verify below
    seen = set()
    for Ff in fams:
        key = tuple(sorted(Ff))
        if key in seen:
            continue
        seen.add(key)
        if not decide_union_closed(Ff):
            continue
        for x in range(3):
            cnt, m = _density(Ff, 3, x)
            truly_ab = (2 * cnt >= m)
            if not truly_ab:
                continue  # only sanity-check the truly-abundant elements
            r = is_feasible_mroof(Ff, 3, x)
            checked += 1
            if r is not True:
                mismatches.append((Ff, x, r))
    print("  tried %d UC families; %d (family,abundant-element) checks; "
          "infeasible-abundant mismatches: %s"
          % (len(seen), checked, mismatches if mismatches else "NONE"))
    if mismatches:
        print("  *** UNDER-CERTIFICATION: some truly-abundant element is NOT "
              "M♮-certifiable under support restriction.")

    # ---- Case (c): antichain / non-abundant unreachable element ----------
    print("-" * 78)
    print("Case (c): can a NON-abundant element be CERTIFIED by M♮-w (over-"
          "certification) or is it unreachable?")
    # Candidate over-certification: F = {empty,{x,y}} (masks {0,3}), x has
    # density 1/2 (abundant) - not a good over-cert test. Try an antichain.
    # Antichain F = {{x}, {y}} (masks {1,2}): each density 1/2 (abundant).
    F = {1, 2}  # {x} and {y}, an antichain on [2], NOT union-closed
    n = 2
    for x in range(n):
        cnt, m = _density(F, n, x)
        truly_ab = (2 * cnt >= m)
        r = is_feasible_mroof(F, n, x)
        print("  antichain {x},{y}: element %s density %d/%d truly-ab=%s "
              "feasible=%s" % (x, cnt, m, truly_ab, r))
        print("    (expectation: element IS certifiable only if it can carry "
              "weight; M♮ may or may not block it)")
    print("  CONTROL (unreachable structural case): n=2 family {empty,{x,y}} "
          "= masks {0,3}, element x has density 1/2 but the restricted "
          "constant is NOT M♮ - does a non-constant M♮-w still certify?")
    F = {0, 3}
    for x in range(n):
        r = is_feasible_mroof(F, n, x)
        print("    element %s density 1/2, feasible=%s" % (x, r))

    # Control: element present in only one set and that branch is the only
    # carrier - over-certification probe: F={empty,{x,y},{z}} on n=3.
    print("  OVER-CERT probe: find a non-abundant element made abundant by "
          "some M♮-w, or show all are blocked.")
    # F = {empty, {x,y}} (masks {0,3}) n=2: element x density 1/2. n=3 richer:
    for x in range(2, 3):
        pass
    n3 = 3
    Fcand = {0, 3, 4}  # empty, {x,y}, {z}  -- z density 1/3 non-abundant
    print("  family {empty,{x,y},{z}} (masks {0,3,4}), n=3:")
    for x in range(n3):
        cnt, m = _density(Fcand, n3, x)
        truly_ab = (2 * cnt >= m)
        r = is_feasible_mroof(Fcand, n3, x)
        print("    element %s density %d/%d truly-ab=%s feasible=%s"
              % (x, cnt, m, truly_ab, r))
        if not truly_ab:
            print("      non-abundant element: over-certified? " +
                  ("YES (reached 1/2)" if r else "NO (blocked, under-cert)"))

    print()
    print("Validation complete. See captured output for every True/False.")


if __name__ == "__main__":
    main()
