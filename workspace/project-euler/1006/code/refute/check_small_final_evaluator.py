"""Refuter for the current efficient reduction's indexing and final evaluator.

This is deliberately bounded: it compares brute.py, mech_psi, and the existing
ue0 primitive at k=1,2,3, while also testing the tempting single-intercept
final evaluator.  Complexity: exponential only for the declared oracle at
these tiny inputs; ue0 itself is O(log(max(p,q,r,n))).
"""
from brute import psi, fibonacci_word
from mech.mech_psi import mech_psi, slope_for
from lib.ueuclid import M, ue0


def single_intercept(k):
    a, q, p = slope_for(k, 1)
    z = pow(10, -1, M)
    # The disputed reduction: one intercept only, with formulation-B's
    # floor-square moment and z^0,...,z^k indexing.
    return ue0(p, 0, q, k + 1, z).S2 % M


def main():
    rows = []
    for k in (1, 2, 3):
        brute_value = psi(k)
        mech_value = mech_psi(k)[0]
        mech_b = mech_psi(k)[1]
        a, q, p = slope_for(k, 1)
        # Directly attack the indexing convention against the primitive.
        z = pow(10, -1, M)
        primitive = ue0(p, 0, q, k + 1, z)
        direct_s0 = sum(pow(z, i, M) for i in range(k + 1)) % M
        direct_s1 = sum(pow(z, i, M) * ((p*i)//q) for i in range(k + 1)) % M
        direct_s2 = sum(pow(z, i, M) * ((p*i)//q)**2 for i in range(k + 1)) % M
        indexing_ok = (primitive.S0, primitive.S1, primitive.S2) == (direct_s0, direct_s1, direct_s2)
        row = {
            "k": k, "brute": brute_value, "mech_A": mech_value,
            "mech_B": mech_b, "primitive_indexing": indexing_ok,
            "single_intercept": single_intercept(k),
        }
        rows.append(row)
        print(row)
    assert all(r["brute"] == r["mech_A"] == r["mech_B"] for r in rows)
    assert all(r["primitive_indexing"] for r in rows)
    # This assertion is expected: it identifies the current reduction gap,
    # rather than silently treating a failed final evaluator as correct.
    assert any(r["single_intercept"] != r["mech_A"] % M for r in rows)
    print("RESULT: indexing gate passes k=1,2,3; single-intercept final evaluator is refuted.")


if __name__ == "__main__":
    main()
