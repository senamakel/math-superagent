"""Probe pysat CardEnc output-var semantics and Cadical time limits.

Checks that CardEnc.atleast(..., output=w) is EXACTLY equivalent to
(w <-> sum(lits) >= bound) over all 2^k assignments, for k small.  If the
output semantics are one-way, prints which direction fails, so the caller can
compensate.  Also probes Cadical153 time_limit support.
"""
from itertools import product
from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical153


def clause_sat(cl, vals):
    """vals: list of booleans indexed by var-1.  True if clause satisfied."""
    for lit in cl:
        if vals[abs(lit) - 1] == (lit > 0):
            return True
    return False


def check_atleast_output():
    print("== CardEnc.atleast with output: exactness probe ==")
    all_exact = True
    for k in range(1, 6):
        for bound in range(0, k + 1):
            cnf = CardEnc.atleast(lits=list(range(1, k + 1)), bound=bound,
                                  top_id=k, encoding=EncType.seqcounter,
                                  output=k + 1)
            nvars = k + 1
            for ass in product([False, True], repeat=nvars):
                if all(clause_sat(cl, ass) for cl in cnf.clauses):
                    s = sum(ass[:k])
                    exp = (s >= bound)
                    if ass[k] != exp:
                        print(f"  k={k} bound={bound}: INEXACT "
                              f"(out={ass[k]} sum={s} want {exp})")
                        all_exact = False
    print("  result:", "EXACT for all k<=5, bound<=k" if all_exact
          else "inexact (see above)")
    return all_exact


def check_atmost_output():
    print("== CardEnc.atmost with output: exactness probe ==")
    all_exact = True
    for k in range(1, 6):
        for bound in range(0, k + 1):
            cnf = CardEnc.atmost(lits=list(range(1, k + 1)), bound=bound,
                                 top_id=k, encoding=EncType.seqcounter,
                                 output=k + 1)
            nvars = k + 1
            for ass in product([False, True], repeat=nvars):
                if all(clause_sat(cl, ass) for cl in cnf.clauses):
                    s = sum(ass[:k])
                    exp = (s <= bound)
                    if ass[k] != exp:
                        print(f"  k={k} bound={bound}: INEXACT "
                              f"(out={ass[k]} sum={s} want {exp})")
                        all_exact = False
    print("  result:", "EXACT for all k<=5, bound<=k" if all_exact
          else "inexact (see above)")
    return all_exact


def probe_cadical_limits():
    print("== Cadical153 time/mem limit support ==")
    s = Cadical153()
    print("  has time_limit attr:", hasattr(s, "time_limit"))
    print("  has mem_limit attr:", hasattr(s, "mem_limit"))
    print("  solve accepts args:", end=" ")
    import inspect
    print(inspect.signature(s.solve))
    s.delete()


if __name__ == "__main__":
    check_atleast_output()
    check_atmost_output()
    probe_cadical_limits()