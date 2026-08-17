"""Ground the 5/6-dim linear-state negative result by testing the state the
extension formula actually needs.

The exact (verified) extension recurrence is
    P(k+1) = 100*P(k) + 100*vR(k)^2 + 20*P1(k) + N1(k).
The right-hand side needs vR(k)^2, a QUADRATIC in the state. So a state that
is closed under a constant linear map must carry vR^2 (or make it recoverable
linearly). We test:

  A) enriched nonlinear-enabling state  [P, S, vR, vR2, P1, N1, N0]  (linear map),
     where vR2(k) = vR(k)^2 mod M is itself kept as a state component.
     If the full dynamics, including how vR and vR2 evolve, were linear, this
     would be consistent. It is the maximal "honest" linear closure of the
     extension formula's RHS.
  B) the affine variants of A.
  C) single component vR2 (vR^2) against its own past (low order).

All exact modular arithmetic over the prime M. No floats.
"""
import os

MOD = 101001001

from state_recurrence_test import (read_states, test_configuration,
                                   verify_solution, vector_of)


def build_enriched(states, with_vr2=True, include_S=True, include_N0=True):
    """Return list of dicts with keys:
       P,S,N1,N0,P1,vR, and optionally V2=vR^2 mod M."""
    out = []
    for s in states:
        d = dict(s)
        if with_vr2:
            d["V2"] = (s["vR"] * s["vR"]) % MOD
        out.append(d)
    return out


def main():
    here = os.path.dirname(__file__)
    state_path = os.path.join(here, "..", "out", "psi_state_1_200.txt")
    states = read_states(state_path)
    est = build_enriched(states, with_vr2=True, include_S=True, include_N0=True)

    orders = list(range(1, 7))

    def report(tag, cols, est_states, affine, skip):
        print(f"\n=== {tag} (skip first {skip}) ===")
        res = test_configuration(est_states, cols, orders, affine=affine,
                                 k0_offset=skip)
        for d in orders:
            r = res[d]
            if r["consistent"]:
                nb, bad = verify_solution(est_states, cols, d, r["solution"],
                                          affine, skip)
                print(f"order {d}: CONSISTENT; verify-errors={nb}")
            else:
                print(f"order {d}: INCONSISTENT")
        return res

    # maximal honest state incl vR^2
    report("enriched [P,S,vR,V2,P1,N1,N0]", ["P", "S", "vR", "V2", "P1", "N1", "N0"],
           est, False, 0)
    report("enriched affine", ["P", "S", "vR", "V2", "P1", "N1", "N0"],
           est, True, 0)
    # without S and N0 (purest extension-formula state)
    report("enriched [P,vR,V2,P1,N1]", ["P", "vR", "V2", "P1", "N1"],
           est, False, 0)

    # individual vR^2
    print("\n=== single component V2 = vR^2 (own past, linear) ===")
    res = test_configuration(est, ["V2"], orders, affine=False, k0_offset=0)
    for d in orders:
        r = res[d]
        if r["consistent"]:
            nb, bad = verify_solution(est, ["V2"], d, r["solution"], False)
            print(f"order {d}: CONSISTENT; verify-errors={nb}")
        else:
            print(f"order {d}: INCONSISTENT")

    # skip-first-30 versions
    report("enriched [P,S,vR,V2,P1,N1,N0] skip30", ["P", "S", "vR", "V2", "P1", "N1", "N0"],
           est, False, 30)
    report("enriched affine skip30", ["P", "S", "vR", "V2", "P1", "N1", "N0"],
           est, True, 30)


if __name__ == "__main__":
    main()
