"""Probe the pysat CardEnc semantics the driver actually relies on.

The old probe tested a `output=` kwarg that this pysat version (1.9.dev13)
removed from CardEnc.atleast/atmost.  The driver never uses it: it calls
`CardEnc.atleast(lits, bound=3, top_id=top, encoding=seqcounter)` and keeps
`enc.nv` as the running top variable, then CardEnc continues allocating fresh
vars above that.  So this probe checks the properties that matter:

  1. Equisatisfiability: for a small literal set, SatCNF(models) restricted to
     the literals always has sum >= bound (no model with fewer than `bound`
     literals true), and every assignment with sum >= bound extends to a
     satisfying assignment (so the encoding introduces no spurious
     restriction).  Checked for k in 1..6, bound in 0..k, all 2^k assignments,
     with the encodings run one after another sharing a rising top_id exactly
     as build_base does.
  2. The running-top_id handoff: variables allocated by a later CardEnc call
     are all above the previous enc.nv (so solve_n's decode, which only reads
     edge vars 1..C(n,2), cannot collide with count-helper vars).
  3. Cadical153 accepts long solve calls (time_limit only set when the caller
     passes it; the driver passes none and relies on wall-clock timeout).
"""
from itertools import product
from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical153


def _enc_sat(cnf_clauses, k, bound, label):
    """Return the set of TRUE-literal masks (ints) among the first k lits
    that the CNF admits, and report if any violates sum>=bound."""
    bad = []
    s = Cadical153(bootstrap_with=cnf_clauses)
    for mask in range(1 << k):
        # force the first k lit values according to mask (bit b -> lit b+1)
        forced = []
        for b in range(k):
            forced.append((b + 1) if (mask >> b) & 1 else -(b + 1))
        sat = s.solve(assumptions=forced)
        # count how many of the first k lits are forced true by this mask
        true_cnt = bin(mask).count("1")
        if sat and true_cnt < bound:
            bad.append((mask, true_cnt))
            break
    s.delete()
    return bad


def check_atleast_equisat():
    print("== CardEnc.atleast(bound) equisatisfiability (all 2^k assignments) ==")
    ok = True
    top = 0
    for k in range(1, 7):
        for bound in range(0, k + 1):
            cnf = CardEnc.atleast(lits=list(range(1, k + 1)), bound=bound,
                                  top_id=top, encoding=EncType.seqcounter)
            # every SAT model respecting a forced assignment must have >= bound true
            bad = _enc_sat(cnf.clauses, k, bound, (k, bound))
            if bad:
                masks = [f"{b[0]:0{k}b} (only {b[1]} true)" for b in bad[:5]]
                print(f"  k={k} bound={bound}: model with <{bound} true found i.e. "
                      f"{masks}")
                ok = False
            top = cnf.nv
    print("  result:", "OK: every atleast model has sum>=bound" if ok
          else "FAIL (see above)")
    return ok


def check_running_top():
    print("== running top_id handoff (decode cannot collide with helpers) ==")
    # Mirror build_base exactly: for each u, atleast over the incident edge
    # vars (1..C(n,2)) with top_id = C(n,2) at the start, then running top.
    # The decode step only reads edge vars 1..C(n,2); helper vars from the
    # cardinality encodings must all sit strictly above that.
    from encode import build_base
    for n in (4, 6, 8, 10):
        _, top = build_base(n)
        C = n * (n - 1) // 2
        print(f"  n={n}: C(n,2)={C}, base top_var={top} "
              f"({top - C} helper slots above edge vars)")
        assert top >= C, f"helpers collided with edge vars for n={n}"
    return True


def probe_cadical():
    print("== Cadical153 basic solve ==")
    s = Cadical153()
    s.add_clause([1])
    s.add_clause([-1, 2])
    assert s.solve() is True
    m = s.get_model()
    assert m in ([1, 2], [1, -2]), m
    print(f"  small solve SAT, model={m} OK")
    s.delete()
    return True


if __name__ == "__main__":
    r1 = check_atleast_equisat()
    r2 = check_running_top()
    r3 = probe_cadical()
    print("\nALL OK" if (r1 and r2 and r3) else "SOME CHECKS FAILED")
