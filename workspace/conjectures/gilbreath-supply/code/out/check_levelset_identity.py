"""Verify the grouping identity behind candidate `level-set-explicit-formula-index-correlation`.

Claims under test:
(1) For g with 2^g <= some window,  A_g = sum_j chi(q_j) chi(q_{j+2^g})
    equals the level-set sum  sum_{p<p'} chi(p)chi(p') 1_{pi(p') - pi(p) = 2^g}.
    ("the same sum regrouped" -- the proposal calls this exact).
(2) The single-prime weighted sums collapse back to the index domain:
    M_+(z) := sum_{p<=x} chi(p) z^{pi(p)} == sum_{j<=pi(x)} chi(q_j) z^j  (as power series in z).
    This shows the "value-domain conversion" never leaves the index domain.
(3) Off-by-one: the proposal writes 1_{pi(p')-pi(p) = 2^g - 1}; test both 2^g and 2^g-1.
"""
import sympy

def primes_up_to(x):
    return list(sympy.primerange(2, x+1))

def chi(p):  # mod-4 quadratic character of the prime value: (-1)^{(p-1)/2}
    return 1 if p % 4 == 1 else -1

def run():
    x = 200
    qs = primes_up_to(x)          # qs[j-1] = j-th prime
    pi = {p: i for i, p in enumerate(qs, start=1)}  # pi(q_j) = j

    # --- claim (1) and (3): level-set regrouping ---
    print("g  sum_j chi(q_j)chi(q_{j+2^g})   levelset(2^g)   levelset(2^g-1)")
    for g in range(0, 4):
        D = 2**g
        left = 0
        for j in range(1, len(qs) - D + 1):
            left += chi(qs[j-1]) * chi(qs[j-1+D])
        rightD   = sum(chi(p)*chi(pp) for p in qs for pp in qs
                       if pi[pp]-pi[p] == D and p < pp)
        rightDm1 = sum(chi(p)*chi(pp) for p in qs for pp in qs
                       if pi[pp]-pi[p] == D-1 and p < pp)
        print(f"{g}   {left:6d}          {rightD:6d}         {rightDm1:6d}   match={left==rightD}")

    # --- claim (2): collapse to index domain (symbolic in formal z) ---
    z = sympy.symbols('z')
    M_plus = sum(chi(p) * z**pi[p] for p in qs)      # as a poly in z
    M_plus_index = sum(chi(p) * z**j for j, p in enumerate(qs, start=1))
    print("\nM_+(z) collapses to index-domain sum:", sympy.expand(M_plus - M_plus_index) == 0)

    # --- show that a single prime-valued character sum weighted by z^{pi(p)}
    #     is literally an index-domain character sum (no value conversion) ---
    M_minus = sum(chi(p) * z**-pi[p] for p in qs)
    # coefficient of z^0 in F(z) = sum_{p<p'} chi(p)chi(p') z^{pi(p')-pi(p)}:
    F = sum(chi(p)*chi(pp)*z**(pi[pp]-pi[p]) for p in qs for pp in qs if pp > p)
    Fpoly = sympy.expand(F)
    print("coeff_z0(F) = sum over adjacent (pi diff=0) pairs:", Fpoly.coeff(z,0))
    # F(z) is fully determined by M_+, M_- :  (M_+)(M_-) = F + flipped + diagonal
    print("(M_+)(M_-) - F has same coefficients as flipped+diagonal (rank-only object):",
          sympy.expand(sympy.expand(M_plus*M_minus) - Fpoly - sympy.expand(M_minus*M_plus) + 0*F) ,

          "--- symbolically: check M_plus*M_minus == F + F_rev + n")

if __name__ == "__main__":
    run()
