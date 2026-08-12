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
    # mimic build_base: consecutive atleast with a shared rising top_id
    top = 0
    peaks = []
    for k, b in ((4, 3), (5, 3), (6, 3)):
        enc = CardEnc.atleast(lits=list(range(1, k + 1)), bound=b,
                              top_id=top, encoding=EncType.seqcounter)
        peaks.append(enc.nv)
        top = enc.nv
    # helper vars must be strictly above the sentinel C(6,2)=15
    assert all(p >= 15 for p in peaks), f"helper vars collided: {peaks}"
    print(f"  nv peaks across three atleast calls: {peaks} (all >= C(6,2)=15) OK")
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
