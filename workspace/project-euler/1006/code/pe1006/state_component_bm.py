"""Independent cross-check: Berlekamp–Massey minimal linear-recurrence order
over F_M for each state component, verified on the second half of the data.

BM run on the first half of each component's sequence gives the minimal LFSR
order + coefficients over F_M for that prefix. If the component genuinely
satisfied a low-order constant linear recurrence mod M, BM on a long-enough
prefix would return that small order and the coefficients would reproduce the
untrained second half. This is a completely different route than the
Gaussian-elimination consistency test (state_recurrence_test.py).

Exact arithmetic mod the prime M; no floats.
"""
import os

MOD = 101001001

from state_recurrence_test import read_states
from lib.recurrences import berlekamp_massey, verify_recurrence


def main():
    here = os.path.dirname(__file__)
    state_path = os.path.join(here, "..", "out", "psi_state_1_200.txt")
    states = read_states(state_path)
    ks = [s["k"] for s in states]
    n = len(states)
    half = n // 2  # train on states 0..half-1 (k=1..half)

    components = ["P", "S", "N1", "N0", "P1", "vR"]
    print(f"M={MOD}, n={n} states, train on first {half} terms, verify on rest")
    for comp in components:
        seq = [s[comp] % MOD for s in states]
        train = seq[:half]
        order, coeffs = berlekamp_massey(train, MOD)
        if order == 0:
            # constant? then everything equals seq[0]
            ok = all(x == seq[0] for x in seq)
            print(f"{comp}: order 0 (constant) -> all-constant={ok}")
            continue
        ok, first_bad = verify_recurrence(seq, coeffs, p=MOD)
        # verify_recurrence checks from k>=order on the WHOLE seq
        print(f"{comp}: BM order on first half = {order}; "
              f"reproduces whole 200-term sequence mod M = {ok}"
              + ("" if ok else f" (first_bad k={first_bad+1})"))


if __name__ == "__main__":
    main()
